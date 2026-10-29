# Ollang Cursor plugin

This repository is the public distribution package for the hosted Ollang MCP
connector. It contains a Cursor manifest, remote endpoint configuration,
workflow skill and brand assets. It does not contain the MCP server or auth UI.

- Keep secrets, test-account credentials, tokens and private review evidence out
  of this repository. Authentication is per-user OAuth through the hosted service.
- Preserve the endpoint in `mcp.json` unless a server migration is authorized.
- Keep skill guidance aligned with actual tool schemas; distinguish reads,
  uploads, billable processing, and completed results.
- Do not add automatic hooks, installers or dependencies for simple documentation
  or configuration changes.
- Run `python3 scripts/validate.py` and `git diff --check` before delivery.
- Keep local/static validation distinct from authenticated Cursor runtime tests.
- Manifest changes require a version bump for an already-published release.
- Submit/re-index through Cursor's publisher portal; repository publication alone
  does not establish marketplace approval.
