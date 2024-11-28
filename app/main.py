from fastapi import FastAPI, Request
import requests

app = FastAPI()

TELEGRAM_TOKEN = "7636088878:AAEPClIL7zPeVHbQ6ZnmsSYjSG3Fa4KNST8"  # Thay bằng token Telegram bot của bạn
CHAT_ID = "-4205810725"          # Thay bằng chat_id của bạn

def send_telegram_message(message: str):
    token = "7636088878:AAEPClIL7zPeVHbQ6ZnmsSYjSG3Fa4KNST8"  # Thay bằng Token của bot bạn
    chat_id = "-4205810725"  # Thay bằng Chat ID của bạn
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message,
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Kiểm tra HTTP status
        print(f"Telegram message sent successfully: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram message: {e}")
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    """Nhận webhook từ TradingView."""
    try:
        # Kiểm tra và lấy dữ liệu JSON từ yêu cầu
        if request.headers.get("Content-Type") != "application/json":
            raise ValueError("Content-Type must be application/json")

        # Lấy dữ liệu thô từ body của yêu cầu
        raw_data = await request.body()
        print(f"Raw data received: {raw_data.decode('utf-8')}")  # Hiển thị dữ liệu thô

        # Chuyển đổi dữ liệu thô sang JSON
        try:
            data = await request.json()
        except Exception:
            raise ValueError("Invalid JSON format")

        if not data:
            raise ValueError("Request body is empty or not valid JSON")

        print(f"Parsed JSON: {data}")  # Hiển thị JSON đã phân tích

        # Lấy thông tin tin nhắn từ JSON
        message = data.get("message", "No message provided")
        print(f"Message to send: {message}")

        # Gửi tin nhắn đến Telegram
        send_telegram_message(message)
        print("Message sent to Telegram.")

        return {"status": "success", "message_sent": message}
    except Exception as e:
        print(f"Error: {e}")  # Log lỗi chi tiết
        return {"status": "error", "message": str(e)}
