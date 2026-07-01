# Contributing to Podcast / Talkshow Content & Script Producer

Thank you for your interest in contributing to this skill! This document provides guidelines for contributing effectively.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Standards](#documentation-standards)
- [Submitting Contributions](#submitting-contributions)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Description**: Clear and concise description of the bug
- **Steps to Reproduce**: Minimal steps to reproduce the behavior
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: Claude Code version, OS, any relevant details
- **Screenshots/Logs**: If applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When suggesting an enhancement:

- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful
- List any examples or reference implementations

### Contributing Code

#### Areas That Need Contributions

1. **Additional Frameworks**: New evidence-backed frameworks for podcast/talkshow production
2. **Research Curation**: High-quality entries for SECOND-KNOWLEDGE-BRAIN.md
3. **Test Scenarios**: Real-world regression cases from user runs
4. **Documentation**: Improved examples, guides, or explanations
5. **Localization**: Frameworks adapted for non-English contexts

#### Before You Start

1. Check the [PROJECT-DEVELOPMENT-PHASE-TRACKING.md](./PROJECT-DEVELOPMENT-PHASE-TRACKING.md) for current status
2. Review existing code and documentation
3. Consider discussing major changes in an issue first

## Development Workflow

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
```bash
git clone https://github.com/YOUR_USERNAME/skills.git
cd skills/podcast-talkshow-producer
```

### Create a Branch

Create a descriptive branch for your work:
```bash
git checkout -b feature/description-of-change
```

Branch naming conventions:
- `feature/` — New features or enhancements
- `fix/` — Bug fixes
- `doc/` — Documentation improvements
- `test/` — Test additions or improvements

### Make Changes

Follow these standards:

1. **Production-Grade Code**: No dummy code, no TODO comments, fully implemented
2. **Evidence-Based**: Every assertion must cite a source
3. **Traceable**: Every recommendation must trace to findings
4. **Tested**: New features require test coverage

#### File-Specific Guidelines

**Skill Files (skills/*.md)**:
- Follow frontmatter format: `name`, `description`
- Include required sections: Role, Purpose, Process, Quality Gates
- Use clear, professional language
- Provide specific examples

**Knowledge Base (SECOND-KNOWLEDGE-BRAIN.md)**:
- Cite authoritative sources only
- Include DOI/URL for verification
- Add relevance score
- Use consistent markdown format

**Python Tools (tools/*.py)**:
- Follow PEP 8 style guidelines
- Include docstrings for all functions
- Add type hints
- Handle errors gracefully

**Test Scenarios (tests/*.md)**:
- Include validation criteria
- Provide expected outputs
- Document edge cases covered

### Commit Changes

Write clear, descriptive commit messages:
```bash
git add .
git commit -m "Add: Three-act structure framework for interview scoring

- Implement sub-framework-selector enhancement
- Add NPR Production Handbook citations
- Include test scenario validation
- Update tracking document"
```

Commit message format:
- `Add:` — New features
- `Fix:` — Bug fixes
- `Update:` — Enhancements to existing features
- `Refactor:` — Code restructuring without behavior change
- `Doc:` — Documentation changes

### Push and Create Pull Request

1. Push to your fork:
```bash
git push origin feature/description-of-change
```

2. Create a pull request on GitHub with:
   - Clear title and description
   - Reference related issues
   - Summary of changes
   - Testing performed

## Testing Guidelines

### Test Scenarios

All 7 test scenarios in `tests/test-scenarios.md` must pass:
- Scenario 1: Episode plan (happy path)
- Scenario 2: Interview script (framework-specific)
- Scenario 3: Cold open (single-dimension)
- Scenario 4: Series arc (multi-episode)
- Scenario 5: Degraded mode (offline)
- Scenario 6: Minimal input (clarification)
- Scenario 7: Conflicting evidence (challenge stage)

### Validation Checklist

Before submitting, verify:
- [ ] All test scenarios pass
- [ ] Quality gates enforce citations
- [ ] Recommendations trace to findings
- [ ] Limitations are stated explicitly
- [ ] Code is production-ready (no dummy code)
- [ ] Documentation is updated

### Adding Test Scenarios

New test scenarios should:
- Cover a unique use case or edge case
- Include validation criteria
- Provide expected outputs
- Document what is being tested

## Documentation Standards

### Skill Files

Include these sections:
- **Role**: Who/what the sub-skill is
- **Purpose**: What it accomplishes
- **Inputs**: What data it receives
- **Process**: Step-by-step workflow
- **Output**: What it produces
- **Quality Gates**: Validation criteria

### Code Comments

- Explain WHY, not WHAT (code shows what)
- Comment non-obvious business logic
- No comments for obvious code
- Keep comments concise and professional

### README Updates

When contributing features:
- Update README.md with new capabilities
- Add usage examples
- Document any new configuration
- Update performance benchmarks if relevant

## Submitting Contributions

### Pull Request Checklist

Before submitting a PR:
- [ ] Code follows project standards
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] PR description summarizes changes
- [ ] Related issues are referenced

### Review Process

Maintainers will review for:
- Production-ready code quality
- Evidence-based assertions
- Traceable recommendations
- Comprehensive testing
- Clear documentation

### After Merge

- Update your local branch
- Delete your feature branch
- Consider contributing to other areas!

## Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Pull Requests**: For code contributions
- **Discussions**: For questions and ideas

## Recognition

Contributors are recognized in the CONTRIBUTORS.md file. Major contributions may be highlighted in release notes.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Podcast / Talkshow Content & Script Producer skill!
