import os
from pyrogram import Client, filters
from pyrogram.types import *

from aditya.conf import get_str_key
from aditya import pbot

REPO_TEXT = "**A Powerful BOT to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Aditya](t.me/adityahalder) 』\n╭──────────────\n┣─ » Python ~ Lastest ...\n┣─ » Update ~ Recently ...\n╰──────────────\n\n»»» @adityaserver «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 🔥", url=f"https://t.me/adityahalder"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
