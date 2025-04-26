# AlertMCP

デスクトップ通知機能を提供するMCPツールです。ClaudeやCursorなどのAIアシスタントから通知を送信できます。

## 機能

- デスクトップ通知の送信
- エージェント名の設定
- 特定の時刻に通知をスケジュール
- 一定時間後に通知をスケジュール

## インストール

uvを使用したインストール:

```bash
# GitHub からインストール
uv run --with git+https://github.com/kousunh/alertmcp.git python -m alertmcp.server
```

### OS別の注意点

- **macOS**: 通知機能には`plyer`と`pyobjus`が必要です。uvを使用する場合は`pyobjus`が自動的にインストールされます。pipでインストールする場合は、`pyobjus`を別途インストールする必要があります:
  ```bash
  pip install pyobjus
  ```
- **Windows**: 通知機能には`plyer`を使用しており、依存関係として自動的にインストールされます。

## 使用方法

### Claude desktopでの設定

1. Claude desktop設定を開く
2. 設定ファイルを探して編集:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. 以下の設定を追加:

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

### Cursorでの設定

1. Cursor設定を開き、MCP Serversセクションに移動
2. 「Add New MCP Server」をクリック
3. 以下の設定を入力:
   - Name: AlertMCP（またはお好みの名前）
   - Type: command
   - Command: `uv run --with git+https://github.com/kousunh/alertmcp.git python -m alertmcp.server`

### エージェント名の設定

以下のようにエージェント名をカスタマイズできます：

```
あなたの名前を「AIエージェント名」に設定してください
```

### 指示例

MCP対応AIアシスタントに以下の指示を出せます:

```
作業が終了したら通知を送ってください
```

```
今日の15:30に「プレゼン資料を確認する」と通知してください
```

```
5分後に「休憩を取る時間です」と通知してください
```

## ライセンス

MITライセンス 