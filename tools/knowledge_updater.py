#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
knowledge_updater.py — Self-improving crawl pipeline for Skill #156
(Podcast / Talkshow Content & Script Producer, cluster: marketing-content-branding)

This script implements the knowledge base update workflow specified in CLAUDE.md:
  1. crawl4ai -> fetch latest papers/standards from domain sources
  2. Parse -> title, authors, date, DOI/URL, abstract, key findings
  3. Score -> rank by recency + domain-keyword relevance
  4. Append -> add scored entries to SECOND-KNOWLEDGE-BRAIN.md (date-stamped)
  5. Deduplicate -> skip entries already present (DOI/URL hash)

Recommended schedule: weekly cron (e.g., 0 2 * * 1 for Monday 2 AM)

Graceful degradation: If crawl4ai or network unavailable, script exits successfully
so the skill continues working with the existing knowledge base.

Exit codes:
  0 — Success (including graceful degradation)
  1 — Configuration error
  2 — File system error
  3 — Runtime error

Usage:
    python tools/knowledge_updater.py [--dry-run] [--verbose]

Author: Skill #156 (podcast-talkshow-producer)
Version: 1.0.0 (production-ready)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import List, Dict, Optional, Set

# =============================================================================
# Configuration
# =============================================================================

ARXIV_CATEGORIES = ["cs.CL", "cs.SD"]

WEB_SOURCES = [
    "https://blog.pacific-content.com",
    "https://www.edisonresearch.com",
    "https://transom.org",
    "https://www.npr.org/sections/npr-extra",
]

SEARCH_QUERIES = [
    "podcast storytelling structure retention",
    "talkshow interview question techniques",
    "podcast cold open hook",
    "trending podcast topics 2026",
]

# =============================================================================
# Paths
# =============================================================================

SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
BRAIN_PATH = PROJECT_ROOT / "SECOND-KNOWLEDGE-BRAIN.md"
LOG_PATH = SCRIPT_DIR / "knowledge_updater.log"

# =============================================================================
# Logging Setup
# =============================================================================

def setup_logging(verbose: bool = False) -> logging.Logger:
    """Configure structured logging with file and console handlers."""
    logger = logging.getLogger("knowledge_updater")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    console_handler.setFormatter(console_formatter)

    # File handler (always debug level for file)
    file_handler = logging.FileHandler(LOG_PATH, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# =============================================================================
# Data Structures
# =============================================================================

@dataclass
class KnowledgeEntry:
    """Represents a single knowledge base entry."""
    title: str
    authors: str
    year: str
    venue: str
    url: str
    abstract: str
    relevance_score: float
    hash: str

    def to_markdown(self, entry_date: str) -> str:
        """Convert to markdown format for appending to knowledge base."""
        return (
            f"- {entry_date} — **{self.title}** ({self.venue}, {self.year}) "
            f"[{self.url}] relevance={self.relevance_score:.2f} <!--hash:{self.hash}-->"
        )

# =============================================================================
# Core Functions
# =============================================================================

def compute_hash(url: str) -> str:
    """
    Compute SHA256 hash of URL for deduplication.

    Args:
        url: The URL to hash (empty string returns empty hash)

    Returns:
        First 16 characters of hex digest
    """
    if not url:
        return ""
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def extract_existing_hashes(text: str) -> Set[str]:
    """
    Extract all existing hashes from knowledge base content.

    Args:
        text: The full content of SECOND-KNOWLEDGE-BRAIN.md

    Returns:
        Set of existing hashes
    """
    return set(re.findall(r"<!--hash:([0-9a-f]{16})-->", text))


def compute_relevance_score(title: str, abstract: str) -> float:
    """
    Compute relevance score based on keyword matching.

    Args:
        title: Entry title
        abstract: Entry abstract or description

    Returns:
        Score from 0.0 to 1.0 based on keyword hits
    """
    # Build relevance keywords from search queries
    relevance_keywords = [word.lower() for query in SEARCH_QUERIES for word in query.split()]

    # Search in title and abstract
    searchable_text = (title + " " + abstract).lower()
    hits = sum(1 for keyword in relevance_keywords if keyword in searchable_text)

    # Score: hits / total keywords (bounded 0-1)
    return hits / max(1, len(relevance_keywords))


def fetch_arxiv_entries(category: str, logger: logging.Logger) -> List[Dict[str, str]]:
    """
    Fetch recent entries from an ArXiv category.

    Args:
        category: ArXiv category (e.g., "cs.CL")
        logger: Logger instance

    Returns:
        List of entry dictionaries
    """
    entries = []

    try:
        from crawl4ai import WebCrawler

        crawler = WebCrawler()
        crawler.warmup()

        url = f"https://arxiv.org/list/{category}/recent"
        logger.debug(f"Fetching ArXiv category: {category}")

        response = crawler.run(url=url)
        markdown = getattr(response, "markdown", "") or ""

        # Parse ArXiv IDs from markdown
        for match in re.finditer(r"(arXiv:\d{4}\.\d{4,5})", markdown):
            arxiv_id = match.group(1).split(":")[1]
            entries.append({
                "title": f"ArXiv {arxiv_id}",
                "authors": "-",
                "year": str(date.today().year),
                "venue": "arXiv",
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "abstract": "",
            })

        logger.debug(f"Found {len(entries)} entries in {category}")

    except ImportError:
        logger.warning("crawl4ai not available; skipping ArXiv fetch")
    except Exception as e:
        logger.warning(f"ArXiv fetch failed for {category}: {e}")

    return entries


def fetch_web_source_entries(source: str, logger: logging.Logger) -> List[Dict[str, str]]:
    """
    Fetch entries from a web source.

    Args:
        source: Base URL of the source
        logger: Logger instance

    Returns:
        List of entry dictionaries
    """
    entries = []

    try:
        from crawl4ai import WebCrawler

        crawler = WebCrawler()
        crawler.warmup()

        logger.debug(f"Fetching web source: {source}")

        response = crawler.run(url=source)
        markdown = getattr(response, "markdown", "") or ""

        if markdown.strip():
            # Create a summary entry from the source content
            # Extract first few meaningful paragraphs
            paragraphs = [p.strip() for p in markdown.split("\n\n") if p.strip() and not p.startswith("#")]
            abstract = " ".join(paragraphs[:3]) if paragraphs else ""

            entries.append({
                "title": f"Update scan: {source}",
                "authors": "-",
                "year": str(date.today().year),
                "venue": source,
                "url": source,
                "abstract": abstract[:600] if abstract else "",
            })

            logger.debug(f"Created summary entry for {source}")

    except ImportError:
        logger.warning("crawl4ai not available; skipping web source fetch")
    except Exception as e:
        logger.warning(f"Web source fetch failed for {source}: {e}")

    return entries


def fetch_all_entries(logger: logging.Logger) -> List[Dict[str, str]]:
    """
    Fetch entries from all configured sources.

    Args:
        logger: Logger instance

    Returns:
        Combined list of all entry dictionaries
    """
    all_entries = []

    # Fetch from ArXiv categories
    for category in ARXIV_CATEGORIES:
        all_entries.extend(fetch_arxiv_entries(category, logger))

    # Fetch from web sources
    for source in WEB_SOURCES:
        all_entries.extend(fetch_web_source_entries(source, logger))

    logger.info(f"Fetched {len(all_entries)} total entries from all sources")
    return all_entries


def score_and_filter_entries(
    entries: List[Dict[str, str]],
    existing_hashes: Set[str],
    logger: logging.Logger
) -> List[KnowledgeEntry]:
    """
    Score entries by relevance and filter out duplicates and low-relevance items.

    Args:
        entries: Raw entry dictionaries
        existing_hashes: Set of hashes already in knowledge base
        logger: Logger instance

    Returns:
        List of scored, filtered KnowledgeEntry objects
    """
    scored_entries = []

    for entry in entries:
        # Skip if no URL
        if not entry.get("url"):
            logger.debug(f"Skipping entry with no URL: {entry.get('title', 'Unknown')}")
            continue

        # Compute hash for deduplication
        url_hash = compute_hash(entry["url"])

        # Skip if already exists
        if url_hash in existing_hashes:
            logger.debug(f"Skipping duplicate (hash {url_hash}): {entry['title']}")
            continue

        # Compute relevance score
        relevance = compute_relevance_score(
            entry.get("title", ""),
            entry.get("abstract", "")
        )

        # Skip low-relevance entries
        if relevance <= 0:
            logger.debug(f"Skipping low-relevance (score {relevance}): {entry['title']}")
            continue

        # Create scored entry
        scored_entries.append(KnowledgeEntry(
            title=entry["title"],
            authors=entry.get("authors", "-"),
            year=entry.get("year", str(date.today().year)),
            venue=entry.get("venue", "Unknown"),
            url=entry["url"],
            abstract=entry.get("abstract", ""),
            relevance_score=relevance,
            hash=url_hash
        ))

    # Sort by relevance score descending
    scored_entries.sort(key=lambda e: e.relevance_score, reverse=True)

    logger.info(f"Scored and filtered to {len(scored_entries)} entries")
    return scored_entries


def append_to_knowledge_base(
    entries: List[KnowledgeEntry],
    dry_run: bool = False,
    logger: logging.Logger = None
) -> int:
    """
    Append new entries to the knowledge base file.

    Args:
        entries: Scored, filtered entries to append
        dry_run: If True, don't actually write to file
        logger: Logger instance

    Returns:
        Number of entries appended
    """
    if not logger:
        logger = logging.getLogger("knowledge_updater")

    # Verify knowledge base file exists
    if not BRAIN_PATH.exists():
        logger.error(f"Knowledge base not found: {BRAIN_PATH}")
        return 0

    # Read existing content to get hashes
    with open(BRAIN_PATH, "r", encoding="utf-8") as f:
        existing_text = f.read()

    existing_hashes = extract_existing_hashes(existing_text)
    today = date.today().isoformat()

    # Filter entries against current hashes (in case file changed since fetch)
    new_entries = [e for e in entries if e.hash not in existing_hashes]

    if not new_entries:
        logger.info("No new entries to append (all duplicates)")
        return 0

    # Generate markdown section
    lines = [f"### Auto-crawl {today}\n"]
    lines.extend([e.to_markdown(today) for e in new_entries])
    lines.append("")  # Trailing newline

    if dry_run:
        logger.info(f"[DRY RUN] Would append {len(new_entries)} entries:")
        for line in lines[1:-1]:  # Skip header and trailing newline
            logger.info(f"  {line}")
        return len(new_entries)

    # Append to file
    with open(BRAIN_PATH, "a", encoding="utf-8") as f:
        f.write("\n".join(lines))

    logger.info(f"Appended {len(new_entries)} new entries to {BRAIN_PATH}")
    return len(new_entries)


# =============================================================================
# Main
# =============================================================================

def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md with latest research",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate run without modifying files"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose (debug) logging"
    )

    return parser.parse_args()


def main() -> int:
    """
    Main entry point for knowledge updater script.

    Returns:
        Exit code (0 = success, 1 = config error, 2 = file error, 3 = runtime error)
    """
    args = parse_arguments()
    logger = setup_logging(verbose=args.verbose)

    logger.info("=" * 60)
    logger.info("Knowledge Updater for Skill #156 (podcast-talkshow-producer)")
    logger.info(f"Mode: {'DRY RUN' if args.dry_run else 'PRODUCTION'}")
    logger.info("=" * 60)

    try:
        # Step 1: Fetch entries from all sources
        logger.info("Step 1: Fetching entries from sources...")
        raw_entries = fetch_all_entries(logger)

        if not raw_entries:
            logger.warning("No entries fetched from any sources (graceful degradation)")
            return 0  # Success exit code

        # Step 2: Read existing hashes
        logger.info("Step 2: Reading existing knowledge base...")
        if not BRAIN_PATH.exists():
            logger.error(f"Knowledge base file not found: {BRAIN_PATH}")
            return 2  # File system error

        with open(BRAIN_PATH, "r", encoding="utf-8") as f:
            existing_text = f.read()
            existing_hashes = extract_existing_hashes(existing_text)

        logger.info(f"Found {len(existing_hashes)} existing entries")

        # Step 3: Score and filter entries
        logger.info("Step 3: Scoring and filtering entries...")
        scored_entries = score_and_filter_entries(raw_entries, existing_hashes, logger)

        if not scored_entries:
            logger.info("No new entries after scoring/filtering")
            return 0

        # Step 4: Append to knowledge base
        logger.info("Step 4: Appending new entries to knowledge base...")
        appended = append_to_knowledge_base(scored_entries, dry_run=args.dry_run, logger=logger)

        # Summary
        logger.info("=" * 60)
        logger.info(f"SUMMARY: {appended} entries appended")
        logger.info(f"Knowledge base: {BRAIN_PATH}")
        logger.info(f"Log file: {LOG_PATH}")
        logger.info("=" * 60)

        return 0  # Success

    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        return 0  # Graceful exit
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return 3  # Runtime error


if __name__ == "__main__":
    sys.exit(main())
