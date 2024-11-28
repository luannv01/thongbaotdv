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
        # Lấy header Content-Type
        content_type = request.headers.get("Content-Type", "").lower()
        print(f"Content-Type: {content_type}")

        # Kiểm tra Content-Type
        if "application/json" not in content_type:
            print("Warning: Content-Type is not application/json. Attempting to parse as JSON.")
        
        # Lấy dữ liệu thô từ body của yêu cầu
        raw_data = await request.body()
        print(f"Raw data received: {raw_data.decode('utf-8')}")

        # Thử chuyển đổi dữ liệu thô sang JSON
        try:
            data = await request.json()
        except Exception:
            raise ValueError("Invalid JSON format")

        if not data:
            raise ValueError("Request body is empty or not valid JSON")

        print(f"Parsed JSON: {data}")

        # Xử lý tin nhắn
        message = data.get("message", "No message provided")
        print(f"Message to send: {message}")

        # Gửi tin nhắn đến Telegram
        send_telegram_message(message)
        print("Message sent to Telegram.")

        return {"status": "success", "message_sent": message}
    except Exception as e:
        print(f"Error: {e}")
        return {"status": "error", "message": str(e)}
