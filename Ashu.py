import pyrogram
import asyncio
from config import *
# Don't Remove Credit @AshutoshGoswami24
Ashu = pyrogram.Client(
    name="Ashu", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Don't Remove Credit @AshutoshGoswami24
start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is add me to your channel and I will show you my power</b>
<b>@PandaWep</b>"""

# Don't Remove Credit @AshutoshGoswami24
about_message = """
<b>• Name : <a href=https://t.me/PandaWep>PandaWep</a></b>
<b>• Developer : <a href=https://github.com/AshutoshGoswami24>[Ashu]</a></b>
<b>• Language : Python3</b>
<b>• Library : Pyrogram v{version}</b>
<b>• Updates : <a href=https://t.me/PandaWep>Click Here</a></b>
<b>• Source Code : <a href=https://github.com/AshutoshGoswami24/AutoCaptionBot-By-Ashu>Click Here</a></b>"""

@Ashu.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
    update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update),
                  parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@Ashu.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
    update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message),
                        parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@Ashu.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update):
    bot = bot.get_me()
    update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention),
                        reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML,
                        disable_web_page_preview=True)

@Ashu.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
    motech, file_name = get_file_details(update)
    try:
        try:
            update.edit(custom_caption.format(file_name=file_name))
        except pyrogram.errors.FloodWait as FloodWait:
            asyncio.sleep(FloodWait.value)
            update.edit(custom_caption.format(file_name=file_name))
    except pyrogram.errors.MessageNotModified:
        pass

def get_file_details(update: pyrogram.types.Message):
    if update.media:
        for message_type in (
                "photo",
                "animation",
                "audio",
                "document",
                "video",
                "video_note",
                "voice",
                "sticker"
        ):
            obj = getattr(update, message_type)
            if obj:
                # Extract file name based on message type
                if message_type in ["photo", "animation", "document", "video"]:
                    file_name = obj.file_name
                elif message_type == "audio":
                    file_name = obj.title
                elif message_type == "sticker":
                    file_name = f"sticker_{obj.file_unique_id}.webp"
                else:
                    file_name = f"{message_type}.mp4"  # Default name for other media types
                return obj, file_name

def start_buttons(bot, update):
    bot = bot.get_me()
    buttons = [[
        pyrogram.types.InlineKeyboardButton("Updates", url="t.me/PandaWep"),
        pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
    ], [
        pyrogram.types.InlineKeyboardButton("➕️ Add To Your Channel ➕️",
                                            url=f"http://t.me/{bot.username}?startchannel=true")
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
    buttons = [[
        pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

print("Bot Working ")
print("Bot Created By https://t.me/PandaWep")

Ashu.run()
