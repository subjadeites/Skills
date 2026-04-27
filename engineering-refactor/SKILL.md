---
name: engineering-refactor
description: Use this skill to clean up, refactor, and prepare an existing codebase for mature delivery-grade engineering standards.
---

# Delivery-Grade Engineering Refactor

## Purpose

Use this skill to bring an existing codebase closer to mature, delivery-grade engineering quality.

The goal is not to make the project merely work. The goal is to make the codebase clean, consistent, maintainable, reviewable, and aligned with the language, framework, runtime, and project conventions already in use.

This is an execution-oriented skill. You should inspect the project, make focused improvements, run available validation commands, and report what changed.

## Core Principles

### Treat the project as a mature product

All changes should support long-term maintainability and production-quality delivery.

Prioritize:

- Clear module boundaries.
- Explicit responsibility ownership.
- Stable types and interfaces.
- Predictable error handling.
- Consistent code style.
- Reviewable change scope.
- Verifiable quality checks.
- Maintainable implementation choices.

Remove:

- Demo code.
- Temporary code.
- Debug code.
- Dead code.
- Unused exports.
- Unused files.
- Mock leftovers.
- Expired TODOs.
- Meaningless comments.
- Experimental implementations.
- Fallbacks that hide real problems.

### Follow existing project conventions first

Before making changes, inspect the project’s existing patterns:

- Directory structure.
- Naming conventions.
- Module boundaries.
- Configuration style.
- Error handling.
- Logging.
- Type definitions.
- Test structure.
- Build, lint, format, typecheck, and test scripts.
- Internal utilities, services, hooks, validators, formatters, loggers, components, fixtures, and test helpers.

Do not introduce a new style or architecture that conflicts with the existing project.

Do not rewrite stable code just to match personal preference.

Do not perform unrelated formatting changes unless they are produced by the project’s formatter.

### Do not reinvent existing tools

Prefer existing internal tools and project dependencies over new implementations.

Before adding code, search for existing:

- Utility functions.
- Shared types.
- Error classes.
- Logging wrappers.
- Request clients.
- Cache helpers.
- Validators.
- Date, money, permission, and formatting utilities.
- Hooks.
- Services.
- Shared components.
- Test helpers.
- Fixtures.
- Mock factories.

If a mature dependency already exists in the project, prefer it.

Add a new dependency only when it is clearly justified. Consider maintenance cost, bundle size, security risk, license risk, and whether the same result can be achieved through existing project code.

Do not add heavy dependencies for simple local logic.

Do not bypass project wrappers unless they are clearly unsuitable.

### Use language and framework best practices

Follow the idiomatic practices of the current language, framework, build system, and runtime.

Avoid:

- Outdated patterns.
- Non-idiomatic code.
- Hidden side effects.
- Overly clever implementations.
- Fighting the type system.
- Unnecessary global state.
- Unstable shared mutable state.
- `any`, unsafe casts, reflection, or dynamic access used only to bypass checks.

Prefer:

- Clear type boundaries.
- Focused modules.
- Stable public APIs.
- Small composable functions.
- Meaningful names.
- Explicit error semantics.
- Framework-recommended data flow and lifecycle patterns.

### Avoid excessive fallback behavior

Do not add fallback logic just to make the code appear more defensive.

Avoid patterns such as:

- Empty `catch` blocks.
- `catch { return null }`.
- Treating all errors as empty data.
- Returning empty arrays to hide request failures.
- Broad default values that hide invalid state.
- Mixing network errors, permission errors, and data-shape errors.
- Using `value || defaultValue` when valid falsy values may exist.
- Adding runtime checks for states already guaranteed by internal types.
- Using layers of optional chaining to hide data that should be required.
- Silently repairing states that should be impossible in the business domain.

Fail fast for clear invalid states.

Validate external input at system boundaries.

Represent internal invariants with types, assertions, explicit errors, or clear module boundaries.

Do not convert invalid states into apparently usable results.

## Workflow

### 1. Inspect the project

Before editing, review:

- Entry points.
- Configuration files.
- Dependency list.
- Build scripts.
- Formatter, linter, typecheck, and test configuration.
- Core modules.
- Reusable internal tools and abstractions.
- Existing test style and test boundaries.

Do not rewrite code before understanding the project’s conventions.

### 2. Identify engineering issues

Look for:

- Duplicate implementations.
- Inconsistent style.
- Unclear types.
- Confused module responsibilities.
- Over-abstraction.
- Under-abstraction.
- Meaningless fallback behavior.
- Overly broad error handling.
- Dead code.
- Temporary code.
- Debug code.
- Unused dependencies.
- Unused exports.
- Non-idiomatic language or framework usage.
- Low-value tests.
- Brittle implementation-detail tests.
- Tests written only for coverage numbers.

### 3. Apply focused improvements

When editing:

- Prefer small, clear changes.
- Preserve behavior unless the current behavior is clearly a bug or conflicts with requirements.
- Merge duplicate logic.
- Reuse internal tools.
- Remove unused code.
- Simplify complex branches.
- Strengthen type boundaries.
- Make error semantics clearer.
- Remove meaningless fallback logic.
- Keep public APIs, configuration formats, and data shapes stable unless there is a strong reason to change them.
- Avoid unrelated file changes.
- Avoid introducing architecture that does not match the project.

## Unit Test Standards

Do not add unit tests by default.

Before adding any unit test, decide whether the test is warranted.

Ask:

- Will this test catch a real regression?
- Does it verify a public contract, public API, user-visible result, or stable error semantic?
- Is this already guaranteed by the compiler, type system, linter, IDE, or static analysis?
- Is unit testing the right tool?
- Would a real path or integration path validate this better?
- Is this a high-risk area such as a state machine, edge case, error path, concurrency, serialization/deserialization, auth/security, or historical bug zone?
- Will this test remain valid after refactoring, or does it only pin the current implementation?

If the test does not have clear value, do not write it.

### Remove or rewrite low-value tests

Remove or rewrite tests that:

- Only verify that a component renders without asserting useful behavior.
- Only verify that a mock was called without validating the business result.
- Only verify syntax, types, or compile-time behavior.
- Test framework or third-party library behavior.
- Test simple getters, setters, constants, or pass-through logic with no business value.
- Test issues already caught by IDEs, linters, or the type system.
- Depend on implementation details and fail during harmless refactors.
- Use snapshots unrelated to real business behavior.
- Duplicate the same simple path.
- Exist only to increase coverage numbers.
- Test mocks instead of system behavior.
- Test private implementation steps instead of observable outcomes.

### Keep or add high-value tests

Keep or add tests for:

- Core business rules.
- User-visible behavior.
- Public API contracts.
- Stable error semantics.
- Permission logic.
- State machines.
- Money, time, billing, sorting, pagination, and other high-risk logic.
- Concurrency, caching, retry, and idempotency behavior.
- Serialization and deserialization.
- Data migrations.
- Authentication and authorization.
- External boundary data transformation.
- Historical regression cases.
- Important edge cases.
- Explicit error paths.
- Critical integration behavior.

Tests should verify behavior, not the current implementation shape.

## Refactor Boundaries

Allowed:

- Remove dead code.
- Merge duplicate logic.
- Remove meaningless fallbacks.
- Normalize naming.
- Normalize error handling.
- Strengthen types.
- Reuse existing tools.
- Simplify branches.
- Remove low-value tests.
- Add high-value tests.
- Locally restructure code for clarity.

Use caution when changing:

- Public APIs.
- Configuration formats.
- Data shapes.
- Error semantics.
- Persistence formats.
- Cross-module call patterns.
- Test strategy.
- Dependencies.
- Large-scale names.
- Directory structure.

Do not:

- Rewrite indiscriminately.
- Refactor stable code only to make it look more modern.
- Introduce architecture inconsistent with the project.
- Build complex frameworks around simple logic.
- Keep unused code.
- Add comments with no business value.
- Swallow errors.
- Hide data problems with broad fallback behavior.
- Reimplement existing utilities.
- Modify unrelated files.
- Delete tests that protect real business behavior.
- Fabricate validation results.
- Claim to have run commands that were not actually run.

## Validation

Run the project’s existing validation commands when available, such as:

- Format.
- Lint.
- Typecheck.
- Unit tests.
- Integration tests.
- Build.

Do not invent commands that are not present in the project.

If a command cannot run, report the real reason.

Do not fabricate passing results.

## Final Report

After completing the work, provide a concise delivery report.

Include:

### Change Summary

Describe:

- Which modules were cleaned up.
- What redundant code was removed.
- Which style inconsistencies were fixed.
- Which internal tools or existing dependencies were reused.
- Whether error handling was changed.
- Whether low-value tests were removed or rewritten.

### Engineering Quality Impact

Describe whether the changes:

- Reduced duplicate implementation.
- Improved type clarity.
- Reduced excessive fallback behavior.
- Removed dead code.
- Clarified module boundaries.
- Made tests focus more on real risks.

### Test Handling

If tests were added, removed, or modified, explain:

- Why the remaining or added tests have value.
- Which low-value tests were removed.
- Whether core behavior remains covered.
- Whether implementation-detail testing was avoided.
- Whether any behavior is better validated through an integration path.

### Validation Results

List the actual commands run and their results.

Example:

- `npm run lint`: passed
- `npm run typecheck`: passed
- `npm test`: passed
- `npm run build`: passed

If a command failed or could not run, explain why.

Do not claim success for commands that were not executed.

### Risks and Notes

List only real risks, unverified areas, or business decisions that require human confirmation.

Do not add generic filler.