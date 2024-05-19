from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="꧁ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ꧂",              
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✰ 𝙷𝙴𝙻𝙿 ✰",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="꧁ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ ꧂",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✫ Hᴇʟᴘ ✫", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✰ Sᴜᴘᴘᴏʀᴛ ✰", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✰ ᴏᴡɴᴇʀ ✰", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✰Gʀᴏᴜᴘ✰", url=f"https://t.me/indian_hacker_group"
            )
        ],
     ]
    return buttons
