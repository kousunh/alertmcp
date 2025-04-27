# AlertMCP

デスクトップ通知機能を提供するMCPツールです。ClaudeやCursorなどのAIクライアントツールから通知を送信できます。

## 機能

- エージェント名の設定
- デスクトップ通知の送信
- 特定の時刻に通知をスケジュール
- 一定時間後に通知をスケジュール

## インストール

### UVのインストールについて

alertmcpのインストールや依存関係の管理には、高速なPythonパッケージマネージャー「uv」の利用を推奨しています。uvはpipよりも効率的に仮想環境の構築やパッケージのインストールが可能です。

#### UVのインストール方法

Windows（powershell）でもmacOS（bash）でも、以下のコマンドでインストールできます：

```
pip install uv
```

インストール後、以下のコマンドでバージョンを確認できます：

```
uv --version
```

### GitHubからのインストール
Githubのリポジトリからローカルにクローンしてください。

#### PowerShellを使用する場合（Windows）:

```powershell
# リポジトリをクローン
git clone https://github.com/kousunh/alertmcp.git

# クローンしたディレクトリに移動
cd alertmcp

# 仮想環境を作成
uv venv

# パッケージをインストール
uv pip install .
```

#### Bashを使用する場合（macOS/Linux）:

```bash
# リポジトリをクローン
git clone https://github.com/kousunh/alertmcp.git

# クローンしたディレクトリに移動
cd alertmcp

# 仮想環境を作成
uv venv

# パッケージをインストール
uv pip install .

# macOSの場合は追加で pyobjus をインストール（仮想環境内に）
uv pip install pyobjus
```

### OS別の注意点

- **Windows**: 通知機能には`plyer`を使用しており、依存関係として自動的にインストールされます。
- **macOS**: 通知機能には`plyer`と`pyobjus`が必要です。uvを使用する場合でも`pyobjus`を別途インストールする必要があります。

## AIツールでの設定と使用方法

ローカルにディレクトリをクローンした後、各AIツールで以下の設定を行ってください。

### Claude desktopでの設定

1. Claude desktop設定を開く
2. 設定ファイルを探して編集:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. 以下の設定を追加:

```json
{
  "mcpServers": {
    "alert_mcp":{
      "command": "uv",
      "args": [
        "--directory",
        "<Git cloneしたフォルダパス>\\alert_mcp",
        "run",
        "python",
        "-m",
        "alertmcp.server"
      ],
      "alwaysAllow": ["add"],
      "disabled": false
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
   - Command: `uv --directory <Git cloneしたフォルダパス>\alert_mcp run python -m alertmcp.server`

#### 2. JSON設定ファイルでの設定

Cursorの設定ファイル"mcp.json"を直接編集することもできます。

```json
{
  "alert_mcp": {
    "command": "uv",
    "args": [
      "--directory",
      "<Git cloneしたフォルダパス>\\alert_mcp",
      "run",
      "python",
      "-m",
      "alertmcp.server"
    ],
    "alwaysAllow": ["add"],
    "disabled": false
  }
}
```

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
