from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

# التوكن الخاص بالبوت
TOKEN = "8059095055:AAFDNheYKWSsuQISuK3cEUd12B2ZtY-jTjM"

def start(update, context):
    """دالة البوت عند بدء المحادثة"""
    update.message.reply_text("مرحبًا! من فضلك، أدخل اسمك.")

def handle_message(update, context):
    """دالة لالتقاط الرسائل وتنفيذ الرد"""
    user_name = update.message.text
    # الرد بحسب الاسم المدخل
    responses = {
        "رغد": "موزة",
        "محمد": "الملك",
        "عبدالله": "بطيخة",
        "خالد": "خيارة",
        "رهف": "جزرة",
        "رؤيا": "القمر",
        "صالح": "الكنق",
        "حمده": "الملكة",
        "سهام": "دبية",
        "صِبا": "القمر",
    }

    response = responses.get(user_name, "اسم غير معرف")
    update.message.reply_text(f"{response}")

def main():
    """إعدادات البوت"""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة معالجات الأوامر
    dp.add_handler(CommandHandler("start", start))
    
    # إضافة معالج للرسائل
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
