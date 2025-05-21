from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_6"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_5"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [InlineKeyboardButton(text="• sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ •", url=f"𝗕𝗛𝗔𝗜 𝗦𝗢𝗝𝗔 𝗧𝗘𝗥𝗘𝗞𝗢 𝗡𝗛𝗜 𝗠𝗜𝗟𝗘𝗚𝗔 𝗥𝗘𝗣𝗢 ☠️

𝗔𝗚𝗔𝗥 𝗕𝗢𝗛𝗨𝗧 𝗨𝗥𝗚𝗘𝗡𝗗 𝗛𝗔𝗜 𝗧𝗢𝗛 𝗗𝗠 𝗞𝗔𝗥𝗢 𝗢𝗪𝗡𝗘𝗥 𝗞𝗢")],
    
    ]
    
    return buttons
