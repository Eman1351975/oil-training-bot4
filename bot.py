from keep_alive import keep_alive
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8561450874:AAFlGZo_Oi_WqGlQiphcrz_sISVWeC4ETjM"

# قاعدة معرفة بسيطة (سؤال -> جواب)
FAQ = {
    "التسجيل": "✅ التسجيل يتم عبر شعبة شؤون الطلبة داخل المعهد أو حسب إعلان الإدارة.",
    "الدوام": "🕗 الدوام عادةً من 8 صباحاً إلى 2 ظهراً (قد يختلف حسب القسم).",
    "الغياب": "📌 الغياب يتم احتسابه حسب نظام المعهد. راجعي شؤون الطلبة للتفاصيل الدقيقة.",
    "النتائج": "📊 النتائج تُعلن عبر القسم/الإدارة أو القنوات الرسمية للمعهد.",
    "الامتحان": "📝 جدول الامتحانات يُنشر قبل الامتحانات بوقت كافٍ عبر إدارة المعهد.",
    "موقع المعهد": "📍 معهد التدريب النفطي / بغداد."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "👋 أهلاً بك في بوت طلاب معهد التدريب النفطي/بغداد\n\n"
        "اكتب كلمة من هذي الكلمات حتى أجاوبك:\n"
        "• التسجيل\n• الدوام\n• الغياب\n• النتائج\n• الامتحان\n• موقع المعهد\n\n"
        "أو اكتب /help"
    )
    await update.message.reply_text(msg)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 اكتب كلمة من الكلمات التالية:\n"
        "التسجيل - الدوام - الغياب - النتائج - الامتحان - موقع المعهد\n\n"
        "مثال: اكتب (الدوام)"
    )

def normalize(text: str) -> str:
    # تنظيف بسيط للنص
    return text.strip().lower().replace("؟", "").replace("?", "")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = normalize(update.message.text)

    # إذا المستخدم كتب جملة تحتوي كلمة من FAQ
    for key, answer in FAQ.items():
        if normalize(key) in user_text:
            await update.message.reply_text(answer)
            return

    await update.message.reply_text(
        "ما فهمت سؤالك 😅\n"
        "اكتب: التسجيل / الدوام / الغياب / النتائج / الامتحان / موقع المعهد\n"
        "أو اكتب /help"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 Bot is running...")
keep_alive()

app.run_polling()
