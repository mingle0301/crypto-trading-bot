from config import *
from telegram import Bot

bot = Bot(token=TELEGRAM_TOKEN)

def start_swing_mode():
    message = "✅ SWING MODE ACTIVATED\n" \
              "• Khung phân tích: 1W/1D/4H\n" \
              "• Thời gian nắm giữ: 3–7 ngày\n" \
              "• Risk/Lệnh: 2% tài khoản"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

if _name_ == "_main_":
    start_swing_mode()
