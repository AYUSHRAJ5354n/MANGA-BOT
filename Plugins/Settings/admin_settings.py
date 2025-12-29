# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat


from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Database.database import Seishiro
from Plugins.helper import get_styled_text, user_states, edit_msg_with_pic
from Plugins.Settings.input_helper import timeout_handler
from Plugins.Settings.main_settings import settings_main_menu_2
import asyncio
from config import Config


@Client.on_callback_query(filters.regex("^admin_menu_btn$"))
async def admin_menu_cb(client, callback_query):
    if callback_query.from_user.id != Config.USER_ID and not await Seishiro.is_admin(callback_query.from_user.id):
        await callback_query.answer("❌ Admin Only area!", show_alert=True)
        return

    text = get_styled_text(
        "<b>👮‍♂️ Admin Controls</b>\n\n"
        "Manage bot administrators and other restricted settings."
    )
    
    buttons = [
        [
            InlineKeyboardButton("Add Admin ➕", callback_data="admin_add_btn"),
            InlineKeyboardButton("Del Admin ➖", callback_data="admin_del_btn")
        ],
        [
            InlineKeyboardButton("Ban User 🚫", callback_data="admin_ban_btn"),
            InlineKeyboardButton("Unban User ✅", callback_data="admin_unban_btn")
        ],
        [
            InlineKeyboardButton("List Admins 📋", callback_data="admin_list_btn"),
            InlineKeyboardButton("View Watermark 💧", callback_data="admin_view_wm_btn")
        ],
         [
            InlineKeyboardButton("Add FSub ➕", callback_data="add_fsub_btn"),
            InlineKeyboardButton("Rem FSub ➖", callback_data="rem_fsub_btn"),
            InlineKeyboardButton("FSub Config 📢", callback_data="fsub_config_btn")
        ],
        [
            InlineKeyboardButton("Broadcast 📢", callback_data="broadcast_btn"),
            InlineKeyboardButton("Channels 📺", callback_data="admin_channels_btn")
        ],
        [
            InlineKeyboardButton("⬅ Back", callback_data="settings_menu_2")
        ]
    ]
    
    await edit_msg_with_pic(
        message=callback_query.message,
        text=text,
        buttons=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex("^admin_add_btn$"))
async def add_admin_btn_cb(client, callback_query):
    text = get_styled_text(
        "<b>➕ Add Admin</b>\n\n"
        "Send the <b>User ID</b> of the new admin.\n"
        "<i>(Auto-close in 30s)</i>"
    )
    user_states[callback_query.from_user.id] = {"state": "waiting_add_admin"}
    buttons = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_input")]]
    await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    asyncio.create_task(timeout_handler(client, callback_query.message, callback_query.from_user.id, "waiting_add_admin"))

@Client.on_callback_query(filters.regex("^admin_del_btn$"))
async def del_admin_btn_cb(client, callback_query):
    text = get_styled_text(
        "<b>➖ Remove Admin</b>\n\n"
        "Send the <b>User ID</b> to remove.\n"
        "<i>(Auto-close in 30s)</i>"
    )
    user_states[callback_query.from_user.id] = {"state": "waiting_del_admin"}
    buttons = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_input")]]
    await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    asyncio.create_task(timeout_handler(client, callback_query.message, callback_query.from_user.id, "waiting_del_admin"))

@Client.on_callback_query(filters.regex("^admin_ban_btn$"))
async def ban_user_btn_cb(client, callback_query):
    text = get_styled_text(
        "<b>🚫 Ban User</b>\n\n"
        "Send the <b>User ID</b> to ban.\n"
        "<i>(Auto-close in 30s)</i>"
    )
    user_states[callback_query.from_user.id] = {"state": "waiting_ban_id"}
    buttons = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_input")]]
    await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    asyncio.create_task(timeout_handler(client, callback_query.message, callback_query.from_user.id, "waiting_ban_id"))

@Client.on_callback_query(filters.regex("^admin_unban_btn$"))
async def unban_user_btn_cb(client, callback_query):
    text = get_styled_text(
        "<b>✅ Unban User</b>\n\n"
        "Send the <b>User ID</b> to unban.\n"
        "<i>(Auto-close in 30s)</i>"
    )
    user_states[callback_query.from_user.id] = {"state": "waiting_unban_id"}
    buttons = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_input")]]
    await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    asyncio.create_task(timeout_handler(client, callback_query.message, callback_query.from_user.id, "waiting_unban_id"))

@Client.on_callback_query(filters.regex("^admin_list_btn$"))
async def list_admins_cb(client, callback_query):
    try:
        admins = await Seishiro.get_admins()
        list_text = f"<b>👮‍♂️ Admin List:</b>\n\n"
        
        try:
             owner = await client.get_users(Config.USER_ID)
             owner_name = owner.first_name
        except:
             owner_name = "Owner"
        list_text += f"• {owner_name} (`{Config.USER_ID}`) (Owner)\n"

        for uid in admins:
            try:
                user = await client.get_users(uid)
                name = user.first_name
            except:
                name = "Unknown"
            list_text += f"• {name} (`{uid}`)\n"
        
        buttons = [[InlineKeyboardButton("⬅ Back", callback_data="admin_menu_btn")]]
        await edit_msg_with_pic(callback_query.message, get_styled_text(list_text), InlineKeyboardMarkup(buttons))
    except Exception as e:
        await callback_query.answer(f"Error: {e}", show_alert=True)

# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat

        
@Client.on_callback_query(filters.regex("^fsub_config_btn$"))
async def fsub_config_menu(client, callback_query):
    channels = await Seishiro.get_fsub_channels()
    buttons = []
    for cid in channels:
        try:
            chat = await client.get_chat(cid)
            mode = await Seishiro.get_channel_mode(cid)
            status = "🟢" if mode == "on" else "🔴"
            buttons.append([InlineKeyboardButton(f"{status} {chat.title}", callback_data=f"rfs_ch_{cid}")])
        except Exception:
             buttons.append([InlineKeyboardButton(f"Invalid {cid}", callback_data=f"rfs_ch_{cid}")])
    
    if not buttons:
        buttons.append([InlineKeyboardButton("No Channels Found", callback_data="no_channels")])
        
    buttons.append([InlineKeyboardButton("⬅ Back", callback_data="admin_menu_btn")])
        
    await edit_msg_with_pic(callback_query.message, get_styled_text("<b>📢 FSub Configuration</b>\nTap to toggle Mode."), InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("^admin_view_wm_btn$"))
async def view_wm_cb(client, callback_query):
    try:
        current_wm = await Seishiro.get_watermark()
        if current_wm:
            text = (
                f"<b>💧 Current Watermark:</b>\n\n"
                f"<b>Text:</b> `{current_wm['text']}`\n"
                f"<b>Pos:</b> `{current_wm['position']}`\n"
                f"<b>Col:</b> `{current_wm['color']}` | <b>Op:</b> `{current_wm['opacity']}`\n"
                f"<b>Size:</b> `{current_wm['font_size']}`"
            )
        else:
            text = "<b>💧 Watermark:</b> Not Set"
            
        buttons = [[InlineKeyboardButton("⬅ Back", callback_data="admin_menu_btn")]]
        await edit_msg_with_pic(callback_query.message, get_styled_text(text), InlineKeyboardMarkup(buttons))
    except Exception as e:
        await callback_query.answer(f"Error: {e}", show_alert=True)

@Client.on_callback_query(filters.regex("^add_fsub_btn$"))
async def add_fsub_btn_cb(client, callback_query):
    text = get_styled_text(
        "<b>➕ Add Force-Sub Channel</b>\n\n"
        "Send the <b>Channel ID</b> (bot must be admin there).\n"
        "<i>(Auto-close in 30s)</i>"
    )
    user_states[callback_query.from_user.id] = {"state": "waiting_fsub_id"} # Reuse existing state
    buttons = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_input")]]
    await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    asyncio.create_task(timeout_handler(client, callback_query.message, callback_query.from_user.id, "waiting_fsub_id"))

@Client.on_callback_query(filters.regex("^rem_fsub_btn$"))
async def rem_fsub_btn_cb(client, callback_query):
    text = get_styled_text(
        "<b>➖ Remove Force-Sub Channel</b>\n\n"
        "Send the <b>Channel ID</b> to remove.\n"
        "<i>(Auto-close in 30s)</i>"
    )
    user_states[callback_query.from_user.id] = {"state": "waiting_fsub_rem_id"} # Reuse existing state
    buttons = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_input")]]
    await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    asyncio.create_task(timeout_handler(client, callback_query.message, callback_query.from_user.id, "waiting_fsub_rem_id"))

@Client.on_callback_query(filters.regex("^broadcast_btn$"))
async def broadcast_btn_cb(client, callback_query):
    text = get_styled_text(
        "<b>📢 Broadcast Message</b>\n\n"
        "Send the message you want to broadcast to all users.\n"
        "<i>(Text, Photo, Video, Sticker, etc.)</i>\n"
        "<i>(Auto-close in 30s)</i>"
    )
    user_states[callback_query.from_user.id] = {"state": "waiting_broadcast_msg"}
    buttons = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_input")]]
    await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    asyncio.create_task(timeout_handler(client, callback_query.message, callback_query.from_user.id, "waiting_broadcast_msg"))

@Client.on_callback_query(filters.regex("^admin_channels_btn$"))
async def admin_channels_cb(client, callback_query):
    try:
        dump_id = await Seishiro.get_config("dump_channel")
        update_id = await Seishiro.get_default_channel()
        auto_chs = await Seishiro.get_auto_update_channels()

        async def get_name(cid):
            if not cid: return "Not Set"
            try:
                chat = await client.get_chat(int(cid))
                return f"{chat.title} (`{cid}`)"
            except:
                return f"Unknown (`{cid}`)"

        dump_str = await get_name(dump_id)
        update_str = await get_name(update_id)
        
        auto_text = ""
        if auto_chs:
            for c in auto_chs:
                db_title = c.get('title', 'Unknown')
                cid = c.get('_id')
                auto_text += f"\n• {db_title} (`{cid}`)"
        else:
            auto_text = "\n• None"

        text = get_styled_text(
            f"<b>📺 Channel Configuration</b>\n\n"
            f"<b>🗑️ Dump Channel:</b>\n➥ {dump_str}\n\n"
            f"<b>📢 Update Channel:</b>\n➥ {update_str}\n\n"
            f"<b>🤖 Auto-Update Channels:</b>{auto_text}"
        )
        
        buttons = [[InlineKeyboardButton("⬅ Back", callback_data="admin_menu_btn")]]
        await edit_msg_with_pic(callback_query.message, text, InlineKeyboardMarkup(buttons))
    except Exception as e:
        await callback_query.answer(f"Error: {e}", show_alert=True)



# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat