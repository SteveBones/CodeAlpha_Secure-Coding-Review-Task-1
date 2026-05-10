# Secure Coding Review Findings

## Vulnerability 1 — SQL Injection

The application directly concatenates user input into SQL queries.

Risk:
Attackers can manipulate database queries.

Example:
' OR '1'='1

Impact:
Unauthorized access to accounts.

Recommendation:
Use parameterized queries.

---

## Vulnerability 2 — Command Execution

The application uses os.system().

Risk:
Can lead to command injection.

Impact:
Remote code execution.

Recommendation:
Avoid os.system() and use safer alternatives.

---

## Vulnerability 3 — No Input Validation

User input is not sanitized.

Risk:
Malicious payloads can be injected.

Recommendation:
Validate and sanitize all inputs.
