from mcp.server.fastmcp import FastMCP
import platform
import threading
import time
from datetime import datetime, timedelta
from plyer import notification

mcp = FastMCP("Alert Service")

# チャットごとにエージェント名を保持する（例：セッションIDごとに管理）
agent_names = {}

@mcp.tool()
def send_notification(session_id: str, title: str, message: str) -> dict:
    """デスクトップ通知を送信します（タイトルは【エージェント名】 ヘッダー、メッセージは本文のみ）"""
    agent_name = agent_names.get(session_id, "AIエージェント")
    # タイトルを【エージェント名】 ヘッダー の形に
    full_title = f"【{agent_name}】 {title}"
    full_message = message  # 本文のみ
    try:
        notification.notify(
            title=full_title,
            message=full_message,
            app_name="AlertMCP",
            timeout=5
        )
        return {
            "status": "ok",
            "title": full_title,
            "message": full_message
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

@mcp.tool()
def set_agent_name(session_id: str, name: str) -> dict:
    """エージェント名を設定"""
    agent_names[session_id] = name
    return {"status": "ok", "agent_name": name}
    
@mcp.tool()
def notify_at_time(session_id: str, title: str, message: str, notify_time: str) -> dict:
    """
    指定した時刻（HH:MM形式、24時間表記）に通知を出します
    例: notify_time="15:30"
    """
    try:
        now = datetime.now()
        target_time = datetime.strptime(notify_time, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )
        # もし指定時刻がすでに過ぎていたら翌日に設定
        if target_time < now:
            target_time += timedelta(days=1)
        wait_seconds = (target_time - now).total_seconds()

        def notify_later():
            time.sleep(wait_seconds)
            agent_name = agent_names.get(session_id, "AIエージェント")
            full_title = f"【{agent_name}】 {title}"
            full_message = message
            notification.notify(
                title=full_title,
                message=full_message,
                app_name="AlertMCP",
                timeout=5
            )

        threading.Thread(target=notify_later).start()
        return {
            "status": "ok",
            "notify_time": target_time.strftime("%Y-%m-%d %H:%M"),
            "title": title,
            "message": message
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

@mcp.tool()
def notify_after_delay(session_id: str, title: str, message: str, minutes: int = 0, hours: int = 0) -> dict:
    """
    指定した分数・時間後に通知を出します
    例: minutes=5, hours=0 なら5分後
    """
    try:
        wait_seconds = hours * 3600 + minutes * 60

        def notify_later():
            time.sleep(wait_seconds)
            agent_name = agent_names.get(session_id, "AIエージェント")
            # タイトルを【エージェント名】 ヘッダー の形に
            full_title = f"【{agent_name}】 {title}"
            full_message = message
            notification.notify(
                title=full_title,
                message=full_message,
                app_name="AlertMCP",
                timeout=5
            )

        threading.Thread(target=notify_later).start()
        return {
            "status": "ok",
            "delay_seconds": wait_seconds,
            "title": title,
            "message": message
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def main():
    print("AlertMCP サーバーを起動しています...")
    # macOSの場合、pyobjusの確認
    if platform.system() == 'Darwin':
        try:
            import pyobjus
            print("macOS: pyobjus が正常にロードされました")
        except ImportError:
            print("警告: macOSでは通知機能のためにpyobjusパッケージが必要です")
            print("uvを使用する場合は alertmcp[macos] をインストールしてください")
    mcp.run()

if __name__ == "__main__":
    main() 