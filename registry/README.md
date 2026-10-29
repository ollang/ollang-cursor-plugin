# Official MCP Registry

`server.json` describes the hosted Ollang MCP server for the
[Official MCP Registry](https://registry.modelcontextprotocol.io/). Its identifier
is `io.github.ollang/ollang`. This remote-only listing uses the existing OAuth
service; it does not install or deploy server code.

From the repository root, validate with the official
[mcp-publisher CLI](https://github.com/modelcontextprotocol/registry):

```sh
mcp-publisher validate registry/server.json
```

To publish, manually run the **Publish MCP Registry** GitHub Actions workflow
on `main`. It uses GitHub OIDC to establish ownership of the `ollang` namespace;
no long-lived publishing secret is required. It validates metadata before
publication and does not run automatically on pushes or pull requests.

The interactive `mcp-publisher login github` flow only grants the personal
namespace and cannot read organization roles. Use the workflow for this listing.
Keep any local publisher credentials outside this repository.

For updates, increment the registry manifest's version before publishing; an
existing published version cannot be overwritten. This version is independent
of the Cursor plugin version. Keep the remote URL consistent with `mcp.json` and
use a publicly accessible, immutable URL for the official logo.

Registry publication makes metadata discoverable. It does not establish Cursor
Marketplace approval or certify authenticated client behavior.
