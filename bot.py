import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from number_generator import generate_fake_number
from otp_receiver import receive_otp

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Welcome! I'm your fake number bot. Use /generate to get a fake number.")

async def generate_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Generate a fake phone number for the user."""
    user_id = update.effective_user.id
    fake_number = generate_fake_number()
    await update.message.reply_text(f"Generated fake number: {fake_number}")
    context.user_data['fake_number'] = fake_number

async def receive_otp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Receive OTP for the user's fake number."""
    user_id = update.effective_user.id
    fake_number = context.user_data.get('fake_number')
    if not fake_number:
        await update.message.reply_text("You haven't generated a fake number yet. Use /generate first.")
        return

    otp = receive_otp(fake_number)
    if otp:
        await update.message.reply_text(f"Received OTP: {otp}")
    else:
        await update.message.reply_text("No OTP received yet. Please wait or try again later.")

def main() -> None:
    """Start the bot."""
    application = ApplicationBuilder().token("8695676689:AAEHYGvfv8M2EnMJ4OtPOcmevQVX0YJjdLY").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate", generate_number))
    application.add_handler(CommandHandler("receive", receive_otp))

    logger.info("Bot started")
    application.run_polling()

if __name__ == "__main__":
    main()
