from fastapi import FastAPI, Request
import requests

app = FastAPI()

TELEGRAM_TOKEN = "7636088878:AAEPClIL7zPeVHbQ6ZnmsSYjSG3Fa4KNST8"  # Thay bằng token Telegram bot của bạn
CHAT_ID = "-4205810725"          # Thay bằng chat_id của bạn

def send_telegram_message(message: str):
    """Gửi tin nhắn đến Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }
    response = requests.post(url, json=payload)
    return response.json()


from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    """Nhận webhook từ TradingView."""
    try:
        # Gửi tin nhắn tự động khi ứng dụng khởi động
        message = "🚀 FastAPI bot has started successfully!"
        send_telegram_message(message)
        print(f"Sent message: {message}")

        # Lấy dữ liệu JSON từ yêu cầu
        data = await request.json()
        print(f"Received data: {data}")

        # Xử lý message từ dữ liệu JSON
        message = data.get("message", "No message provided")
        print(f"Message from request: {message}")

        return {"status": "success"}
    except Exception as e:
        # Xử lý lỗi và trả về phản hồi lỗi
        return {"status": "error", "message": str(e)}
