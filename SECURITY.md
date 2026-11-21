# Security Policy

## Scope
This project is a World Of Tanks cheat overlay for offline research and
reverse-engineering education. It does **not** ship a kernel driver, does not
touch the game's anti-cheat handshake, and does not persist after exit.

## Reporting
If you find an issue that could get users harmed (e.g. an unintended disk write
outside `logs/`, or a leak of the game process handle to other processes),
open a private security advisory. Do not file a public issue.

## Out of scope
- "My account got banned" — expected; see disclaimer.
- Detection reports for the overlay — off topic, close immediately.