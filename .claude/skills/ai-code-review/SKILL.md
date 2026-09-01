---
name: ai-code-review
description: Review AI-generated code for correctness, error handling, tests, security, quality and performance. Use when reviewing code an AI assistant produced, before merging a generated change, or when the user asks to check generated code for defects.
---

# AI Code Review

Review the code against every check below in one pass. If a diff and the original prompt are available, use them; the correctness checks need them, the rest read the file as it stands.

## Checks

**Correctness and logic**

- **Missed requirement**: go through the prompt point by point and mark each one done, partial or missing.
- **Unrequested functionality**: anything not asked for, including extra features, dependencies, file writes and network calls.
- **Wrong business logic**: code that runs but returns the wrong result. For every formula and condition, say what it actually does, then trace one input and give expected vs actual.
- **Hallucinated functionality**: functions, methods, parameters, imports or endpoints that do not exist. List every external symbol and mark it verified or not.
- **Incorrect assumption**: decisions made about things the prompt left open, such as argument order, arity, units, formats, empty values or error behaviour.
- **Broken existing code**: every removed guard, changed signature, changed return type, renamed symbol or altered error handling.

**Error handling and input validation**

- **Empty values**: everywhere the code reads input, confirm it handles an empty string, and check any output that reads from an empty collection.
- **Invalid input**: every conversion from text to a number, confirm it is guarded against text that isn't numeric.
- **Unexpected data**: every function whose return can be an error string, `None`, or another sentinel, confirm every caller checks for it before treating it as the expected type.
- **Boundary cases**: every arithmetic operation, confirm it is bounded against zero, negative, and very large inputs.
- **Exceptions**: confirm anything that can raise is caught, and that state isn't lost when it does.
- **Missing error handling**: every function that can fail, confirm it reports failure through its return value or an exception, not through a `print()` plus a sentinel.

**Tests and edge cases**

- **Missing scenarios**: for every function, check whether its behavior is defined for every input it can receive. Flag any input with no stated expected result.
- **Edge cases**: for every guard, find one input outside what it checks and show it still failing. For every rounding call or float comparison, give one input where the result differs from what a person would get by hand.
- **Test coverage**: say whether a test suite exists and what it covers. If coverage is below 60% or there is no suite at all, write the missing tests, covering every scenario and edge case found above.

**Quality and performance**

- **Duplicated logic**: any function, guard or test block that only repeats something already available, and what it could call instead.
- **Poor structure**: any global state mutated from outside the scope that owns it, and any function mixing input, computation, formatting and storage that could be split.
- **Overengineering**: any field, branch or class boundary serving fewer cases than its presence implies, and what could be removed without changing behavior.
- **Inefficient code**: any value that grows without bound relative to what's read back, and any work repeated every loop pass that doesn't need to be.

**Security**

- **Unsafe user input**: any input reaching a shell, a query, a path, a deserializer or an eval without validation.
- **Exposed credentials**: any key, token, password or connection string in source.
- **Problematic dependencies**: any import that is unpinned, unused, unnecessary, or duplicates the standard library.

## Output

Report findings ranked by severity: silent wrong behaviour first, crashes second, cosmetic last. One block each:

```
[severity] Wrong business logic — discount applied before tax
  cart.py:42
  > total = total - voucher
  What happens: a 100 cart with a 10 voucher and 20% tax charges 108, not 110
  Fix: apply tax to the subtotal, then subtract the voucher
```

Do not rewrite the code under review. Tests are the exception, write those in full.

Do not invent issues. A check with nothing to report is a valid result.

End with this checklist, marking each check found, clean, or not applicable:

```
Correctness and logic
  ✗ Missed requirement
  ✓ Unrequested functionality
  ✗ Wrong business logic
  ✓ Hallucinated symbols
  ✓ Incorrect assumption
  — Broken existing code

Error handling
  ✓ Empty values
  ✗ Invalid input
  ✓ Unexpected data
  ✓ Boundary cases
  ✗ Exceptions
  ✓ Missing error handling

Tests and edge cases
  ✗ Missing scenarios
  ✗ Edge cases
  ✗ Test coverage

Security, quality and performance
  ✗ Duplicated logic
  ✗ Poor structure
  ✗ Overengineering
  ✗ Inefficient code

Security
  — Unsafe user input
  — Exposed credentials
  ✓ Dependencies

✓ clean
✗ finding
— not applicable
```
