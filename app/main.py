from fastapi import FastAPI, Request
import requests

app = FastAPI()

TELEGRAM_TOKEN = "7636088878:AAEPClIL7zPeVHbQ6ZnmsSYjSG3Fa4KNST8"  # Thay bằng token Telegram bot của bạn
CHAT_ID = "-4205810725"          # Thay bằng chat_id của bạn

def send_telegram_message(message: str):
    token = "7636088878:AAEPClIL7zPeVHbQ6ZnmsSYjSG3Fa4KNST8"
    chat_id = "-4205810725"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Telegram message sent: {message}")
    else:
        print(f"Failed to send message: {response.json()}")

from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    """Nhận webhook từ TradingView."""
    try:
        # Lấy dữ liệu JSON từ yêu cầu
        data = await request.json()
        print(f"Received data: {data}")

        # Lấy thông tin tin nhắn từ dữ liệu
        message = data.get("message", "No message provided")
        
        # Gửi tin nhắn đến Telegram
        send_telegram_message(message)
        print(f"Message sent to Telegram: {message}")

        return {"status": "success", "message_sent": message}
    except Exception as e:
        # Xử lý lỗi và trả về phản hồi lỗi
        return {"status": "error", "message": str(e)}
