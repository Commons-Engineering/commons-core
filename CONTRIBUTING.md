# Contributing to Commons OS

Commons OS is a shared operating system. Improvements made in any fork can flow back upstream to benefit all commons.

## What You Can Contribute

| Contribution | How |
|---|---|
| **Core pattern improvements** | PR against `commons/patterns/` |
| **New core patterns** | PR with pattern following PATTERN_SPEC v8.2 |
| **Specification fixes** | PR against `commons/specs/` |
| **Manifest updates** | PR against `commons/manifests/` |
| **Template improvements** | PR against `commons/templates/` |
| **Workflow improvements** | PR against `.github/workflows/` |
| **Bug fixes** | Issue + PR |

## What Stays Local

Your `instance/` directory and `extensions/` are yours. We will never ask you to upstream operational data, extension packs, or instance patterns — those belong to your commons.

## Process

1. **Fork** the commons-os repository (if you haven't already)
2. **Create a branch** for your change
3. **Make your change** following the relevant spec (PATTERN_SPEC for patterns, etc.)
4. **Open a PR** against `commons-engineering/commons-os`
5. **Describe** what you changed and why

## Guidelines

- Follow the existing specifications — PATTERN_SPEC v8.2 for patterns, etc.
- Keep core content domain-neutral where possible
- Use English for file names and YAML keys (content can be localised)
- One logical change per PR

## Questions?

Open an issue on this repository or reach out to the Commons Engineering community.
