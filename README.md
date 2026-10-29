# Ollang for Cursor

<img src="assets/ollang.svg" alt="Ollang" width="160" />

Connect Cursor to your Ollang workspace to manage localization projects,
orders and review workflows. The plugin includes an OAuth-enabled remote MCP
connection and a workflow skill. It requires no local server or API key in a file.

## Requirements

- A Cursor installation that supports plugins.
- An existing Ollang account with access to the intended workspace.
- Appropriate permissions and existing credits for any paid processing you request.

The plugin is free to install. Ollang is a separate service: starting or rerunning
orders and requesting paid processing or human review may consume existing
account credits. The plugin does not purchase credits or operate a checkout.

## Install and connect

Once approved in Cursor Marketplace, search for **Ollang** in Customize and
install the plugin. Until then, use the local development instructions below.

1. Open the plugin's MCP connection and choose to connect/authenticate.
2. Sign in on Ollang's hosted sign-in page. Existing password accounts can use
   **Ollang Password**; email/social methods are also available.
3. Review the app and requested access, then authorize the connection.
4. Return to Cursor and ask a read-only question such as “Show my five newest
   Ollang orders, newest first.”

Each user connects their own Ollang account. No credentials are distributed in
this repository. If a connection expires, reconnect through Cursor's MCP UI.
Do not paste passwords, API keys, authorization codes or tokens into agent chat.

## What you can do

- Browse projects, orders, status, quality information and credit balances.
- Resolve supported language codes from Ollang's live catalogue.
- Upload selected source files to an Ollang project.
- Create and manage localization orders when explicitly requested.
- Manage instructions and translation memories, and request quality checks or
  human review within your account permissions.

Supported workflows include documents, subtitle/caption files, audio and video.
The integration manages Ollang workflows; it is not a direct chat translation
tool. Availability depends on the connected account and service.

## Example prompts

- “Show my five most recent Ollang orders, newest first.”
- “List my newest Ollang projects, then show the first project's details.”
- “Which Ollang language code should I use for Brazilian Portuguese?”
- “Check whether Ollang accepts the exact tag pt-BR. Do not create an order.”
- “Upload this selected English JSON file to Ollang as a source project. Do not
  start an order.”

Uploading sends the selected content to Ollang. Order creation, reruns, review
requests and cancellation can change workspace state or consume credits. Confirm
the intended files, workspace, languages and cost-bearing actions before starting.

## Privacy and support

Tool requests send the selected task inputs to Ollang; requested results return
to Cursor. The connector does not independently retrieve your whole chat or
repository. Disconnecting the plugin does not delete content already stored in
Ollang or copies already returned to Cursor.

- [Privacy policy and MCP disclosures](https://ollang.com/privacy#mcp-integrations)
- [Terms of service](https://ollang.com/terms)
- [API documentation](https://api-docs.ollang.com)
- Support: [support@ollang.com](mailto:support@ollang.com)
- Data access/deletion requests: [privacy@ollang.com](mailto:privacy@ollang.com)

## Local development

Validate the package with Python 3 (no dependencies):

```sh
python3 scripts/validate.py
```

To load it for a temporary Cursor CLI session:

```sh
cursor agent --plugin-dir /absolute/path/to/ollang-cursor-plugin
```

For IDE development, copy this directory into
`~/.cursor/plugins/local/ollang` and reload Cursor. Do not use a symlink pointing
outside the local plugin folder. Local imports may require your team admin's
permission. See [Cursor's plugin documentation](https://cursor.com/docs/plugins).

The package has no executable hooks, installation scripts or local dependencies.
The hosted MCP service is maintained and deployed separately from this plugin.

## License and branding

Plugin source and documentation are provided under the [MIT license](LICENSE).
Ollang names and logos are Ollang Inc. trademarks; the software license does not
grant trademark rights or imply endorsement of modified distributions. The SVG
assets are the official Ollang wordmark and symbol used by the Ollang web app.
