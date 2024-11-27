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

@app.post("/webhook")
async def webhook(request: Request):
    """Nhận webhook từ TradingView."""
    try:
        data = await request.json()
        message = data.get("message", "No message provided")
        send_telegram_message(f"📢 <b>TradingView Alert</b>\n\n{message}")
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
