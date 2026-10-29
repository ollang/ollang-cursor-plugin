# Official MCP Registry

`server.json` describes the hosted Ollang MCP server for the
[Official MCP Registry](https://registry.modelcontextprotocol.io/). Its identifier
is `io.github.ollang/ollang`. This remote-only listing uses the existing OAuth
service; it does not install or deploy server code.

From the repository root, use the official
[mcp-publisher CLI](https://github.com/modelcontextprotocol/registry):

```sh
mcp-publisher validate registry/server.json
mcp-publisher login github
mcp-publisher publish registry/server.json
```

The GitHub account must have permission to publish under the `ollang`
organization namespace. Complete the CLI's device authorization in a browser.
Keep credentials outside this repository.

For updates, increment the registry manifest's version before publishing; an
existing published version cannot be overwritten. This version is independent
of the Cursor plugin version. Keep the remote URL consistent with `mcp.json` and
use a publicly accessible, immutable URL for the official logo.

Registry publication makes metadata discoverable. It does not establish Cursor
Marketplace approval or certify authenticated client behavior.
