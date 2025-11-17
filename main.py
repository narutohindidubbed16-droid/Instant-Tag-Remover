from keep_alive import keep_alive
keep_alive()
import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User, InlineKeyboardMarkup, InlineKeyboardButton

bughunter0 = Client(
    "botname",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

WELCOME_TEXT = """
👋 Welcome to Instant Forward Tag Remover!

I'm your smart assistant — I clean any forwarded message and return a fresh copy with **zero tags**, fully original and clean.

⚙️ How it works:
🔹 Add me as an **Admin** in your channel  
   → I’ll auto-remove the “Forwarded from” tag from every post.

🔹 Or simply **forward any message directly** to me  
   → I’ll instantly return a clean version — no tags, no source, fully fresh.

✨ Fast • Clean • Secure  
Start by forwarding your first message or adding me to your channel!
"""

@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):

    me = await bot.get_me()

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Me to Channel",
                    url=f"https://t.me/{me.username}?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 Join Developer Channel",
                    url="https://t.me/AbdulBotz"
                )
            ],
            [
                InlineKeyboardButton(
                    "ℹ️ Help",
                    callback_data="help"
                )
            ]
        ]
    )

    await update.reply_text(
        WELCOME_TEXT,
        reply_markup=keyboard
    )


# Callback Handler
@bughunter0.on_callback_query()
async def callback(bot, query):
    if query.data == "help":
        await query.message.edit_text(
            "**🛠 Help Menu**\n\n"
            "Just forward any message to me — I'll return a clean copy.\n"
            "To auto-remove tags in your channel:\n"
            "▪️ Add me as Admin\n"
            "▪️ Post anything → I clean it instantly.",
        )


# Forwarded message handler
@bughunter0.on_message(filters.forwarded & filters.channel)
async def channeltag(bot, message):
    try:
        forward_msg = await message.copy(message.chat.id)
        await message.delete()
    except:
        await message.reply_text(
            "Oops, Recheck My Admin Permissions & Try Again."
        )


bughunter0.run()
