# AlertMCP

An MCP tool that provides desktop notification functionality. You can send notifications from AI assistants like Claude and Cursor.

## Features

- Send desktop notifications
- Set agent name
- Schedule notifications at specific times
- Schedule notifications after a delay

## Installation

Install using uv:

```bash
# Install from GitHub
uv run --with git+https://github.com/kousunh/alertmcp.git python -m alertmcp.server
```

### OS-specific Notes

- **macOS**: The notification function requires `plyer` and `pyobjus`. If using uv, `pyobjus` will be installed automatically. If installed with pip, you need to install `pyobjus` separately:
  ```bash
  pip install pyobjus
  ```
- **Windows**: The notification function uses `plyer`, which is automatically installed as a dependency.

## Usage

### Setup in Claude

1. Open Claude settings
2. Find and edit the settings file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. Add the following settings:

```json
{
  "mcpServers": {
    "alertmcp": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "git+https://github.com/kousunh/alertmcp.git",
        "python",
        "-m",
        "alertmcp.server"
      ]
    }
  }
}
```

### Setup in Cursor

1. Open Cursor settings and navigate to the MCP Servers section
2. Click "Add New MCP Server"
3. Enter the following settings:
   - Name: AlertMCP (or any name you prefer)
   - Type: command
   - Command: `uv run --with git+https://github.com/kousunh/alertmcp.git python -m alertmcp.server`

### Setting Agent Name

You can set a custom agent name with:

```
Please set your name to 'Personal Assistant'
```

### Example Instructions

You can give the following instructions to your MCP-enabled AI assistant:

```
When you finish your task, please send a notification
```

```
Please notify me at 15:30 today to "Check presentation materials"
```

```
Please notify me in 5 minutes that "It's time to take a break"
```

## Documentation

For Japanese documentation, see [README_JA.md](README_JA.md)

## License

MIT License 