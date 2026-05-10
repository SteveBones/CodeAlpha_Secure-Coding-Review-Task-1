# Secure Coding Review Project

## Objective
This project demonstrates a secure coding review process using Python applications on Kali Linux.

## Tools Used
- Kali Linux
- Python
- Bandit
- Git
- VMware

## Vulnerabilities Identified
- SQL Injection
- Unsafe command execution
- Lack of input validation

## Security Improvements
- Parameterized SQL queries
- Removal of os.system()
- Better handling of user input

## Static Analysis
Bandit was used to identify insecure coding practices.

## Files Included
- vulnerable_app.py
- secure_app.py
- findings.md

## Outcome
The vulnerable application was reviewed, security flaws identified, and remediation implemented successfully.
