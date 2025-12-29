# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat


import logging
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import Config
from Database.database import Seishiro
from Plugins.helper import admin, check_ban, get_styled_text, user_states

logger = logging.getLogger(__name__)


@Client.on_message(filters.command("add_admin") & filters.private & admin)
async def add_admin_handler(client, message):
    try:
        logger.info(f"Add admin command from {message.from_user.id}")
        if len(message.command) != 2:
            return await message.reply("<b>Usage: /add_admin <user_id></b>")
        
        user_id = int(message.command[1])
        await Seishiro.add_admin(user_id)
        await message.reply(f"<b>✅ User {user_id} added as admin</b>", parse_mode=enums.ParseMode.HTML)
        logger.info(f"User {user_id} added as admin by {message.from_user.id}")
    except ValueError:
        await message.reply("<b>Invalid User ID</b>", parse_mode=enums.ParseMode.HTML)
    except Exception as e:
        logger.error(f"Error adding admin: {e}")
        await message.reply(f"❌ Error: {str(e)}")

@Client.on_message(filters.command("deladmin") & filters.private & admin)
async def del_admin_handler(client, message):
    try:
        logger.info(f"Del admin command from {message.from_user.id}")
        if len(message.command) != 2:
            return await message.reply("<b>Usage: /deladmin <user_id></b>")
        
        user_id = int(message.command[1])
        if user_id == Config.USER_ID:
            return await message.reply("<b>❌ Cannot remove owner</b>")
            
        await Seishiro.remove_admin(user_id)
        await message.reply(f"<b>✅ User {user_id} removed from admins</b>")
        logger.info(f"User {user_id} removed from admins by {message.from_user.id}")
    except ValueError:
        await message.reply("<b>Invalid User ID</b>")
    except Exception as e:
        logger.error(f"Error removing admin: {e}")
        await message.reply(f"❌ Error: {str(e)}")

@Client.on_message(filters.command("admins") & filters.private & admin)
async def view_admins_handler(client, message):
    try:
        admins = await Seishiro.get_admins()
        text = "<b>👮‍♂️ Admin List:</b>\n\n"
        text += f"• {Config.USER_ID} (Owner)\n"
        for uid in admins:
            text += f"• `{uid}`\n"
        await message.reply(text)
    except Exception as e:
        logger.error(f"Error listing admins: {e}")
        await message.reply(f"❌ Error: {str(e)}")



@Client.on_message(filters.command("set_watermark") & filters.private & admin)
async def set_watermark_msg(client: Client, message: Message):
    try:
        
        if len(message.command) < 2:
            await message.reply_text(
                "💧 **Set Watermark**\n\n"
                "**Usage:**\n"
                "`/set_watermark <text> <position> <color> <opacity> <fontsize>`\n\n"
                "**Example:**\n"
                "`/set_watermark {manga_name} Ch-{chapter} center #FF0000 100 30`\n\n"
                "**Parameters:**\n"
                "• Position: `top-left`, `top-right`, `bottom-left`, `bottom-right`, `center` (default: bottom-right)\n"
                "• Color: Hex code like `#FFFFFF` (default: white)\n"
                "• Opacity: 0-255 (default: 128)\n"
                "• Font Size: Number (default: 20)",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            return
        
        args = message.text.split()
        args.pop(0)

        position = "bottom-right"
        color = "#FFFFFF"
        opacity = 128
        font_size = 20

        
        valid_positions = ["top-left", "top-right", "bottom-left", "bottom-right", "center"]
        
        if len(args) > 1 and args[-1].isdigit():
            val = int(args[-1])
            if 10 <= val <= 100:
                font_size = val
                args.pop()
        
        if len(args) > 1 and args[-1].isdigit():
            val = int(args[-1])
            if 0 <= val <= 255:
                opacity = val
                args.pop()
        
        if len(args) > 1 and args[-1].startswith("#") and len(args[-1]) == 7:
            color = args[-1]
            args.pop()

        if len(args) > 1 and args[-1] in valid_positions:
            position = args[-1]
            args.pop()

        text = " ".join(args)
        
        if not text:
             await message.reply_text("❌ Watermark text is missing.")
             return
        
        success = await Seishiro.set_watermark(text, position, color, opacity, font_size)
        
        if success:
            await message.reply_text(
                f"✅ Watermark set successfully!\n\n"
                f"**Text:** `{text}`\n"
                f"**Position:** `{position}`\n"
                f"**Color:** `{color}`\n"
                f"**Opacity:** `{opacity}/255` ({int((opacity/255)*100)}%)\n"
                f"**Font Size:** `{font_size}`\n\n"
                "💧 Watermark will be applied to all new chapter uploads.",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            logger.info(f"Watermark set by admin {message.from_user.id}: {text}")
        else:
            await message.reply_text("❌ Failed to save watermark to database.")
            
    except ValueError as e:
        await message.reply_text("❌ Invalid number format for opacity or font size.")
    except Exception as e:
        logger.error(f"Error in set_watermark_msg: {e}", exc_info=True)
        await message.reply_text(f"❌ Error: {str(e)}")

@Client.on_message(filters.command("view_watermark") & filters.private & admin)
async def view_watermark_msg(client: Client, message: Message):
    try:
        logger.info(f"View watermark command from admin {message.from_user.id}")
        
        current_wm = await Seishiro.get_watermark()
        
        if current_wm:
            await message.reply_text(
                f"💧 **Current Watermark Configuration:**\n\n"
                f"**Text:** `{current_wm['text']}`\n"
                f"**Position:** `{current_wm['position']}`\n"
                f"**Color:** `{current_wm['color']}`\n"
                f"**Opacity:** `{current_wm['opacity']}/255` ({int((current_wm['opacity']/255)*100)}%)\n"
                f"**Font Size:** `{current_wm['font_size']}`\n\n"
                "**Available Variables:**\n"
                "• `{manga_name}` - Manga name\n"
                "• `{chapter}` - Chapter number\n\n"
                "**Available Positions:**\n"
                "`top-left`, `top-right`, `bottom-left`, `bottom-right`, `center`\n\n"
                "Use /set_watermark to change or /rem_watermark to remove it.",
                parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await message.reply_text(
                "❌ No watermark configured.\n\n"
                "Use /set_watermark to add a watermark to your chapter pages.\n\n"
                "**Example:**\n`/set_watermark @YourChannel bottom-right #FFFFFF 128 20`",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            
    except Exception as e:
        logger.error(f"Error viewing watermark: {e}", exc_info=True)
        await message.reply_text(f"❌ Failed to get watermark: {str(e)}")

@Client.on_message(filters.command("rem_watermark") & filters.private & admin)
async def rem_watermark_msg(client: Client, message: Message):
    try:
        logger.info(f"Remove watermark command from admin {message.from_user.id}")
        
        current_wm = await Seishiro.get_watermark()
        
        if not current_wm:
            await message.reply_text("❌ No watermark is configured.")
            return
        
        success = await Seishiro.delete_watermark()
        
        if success:
            await message.reply_text(
                "✅ Watermark removed successfully!\n\n"
                "📖 Chapters will now be uploaded without watermark.",
                parse_mode=enums.ParseMode.MARKDOWN
            )
            logger.info(f"Watermark removed by admin {message.from_user.id}")
        else:
            await message.reply_text("❌ Failed to remove watermark from database.")
            
    except Exception as e:
        logger.error(f"Error removing watermark: {e}", exc_info=True)
        await message.reply_text(f"❌ Failed to remove watermark: {str(e)}")


# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat


@Client.on_message(filters.command("broadcast") & filters.private & admin)
async def broadcast_handler(client: Client, m: Message):
    try:
        if not m.reply_to_message and len(m.command) < 2:
            return await m.reply("Reply to a message OR provide text to broadcast it.\nUsage: `/broadcast <message>`")
            
        all_users = await Seishiro.get_all_users()
        total = len(all_users)
        successful = 0
        unsuccessful = 0
        
        status = await m.reply(f"🚀 Broadcasting to {total} users...")
        
        for user_id in all_users:
            try:
                if m.reply_to_message:
                    await m.reply_to_message.copy(chat_id=user_id)
                else:
                    text = m.text.split(None, 1)[1]
                    await client.send_message(user_id, text)
                successful += 1
            except Exception as e:
                unsuccessful += 1
            
            if (successful + unsuccessful) % 20 == 0:
                await status.edit(f"🚀 Broadcasting... {successful}/{total} sent.")
                
        await status.edit(
            f"✅ **Broadcast Complete**\n\n"
            f"👥 Total: {total}\n"
            f"✅ Sent: {successful}\n"
            f"❌ Failed: {unsuccessful}"
        )
    except Exception as e:
        logger.error(f"Broadcast error: {e}")
        await m.reply(f"❌ Error: {str(e)}")


@Client.on_message(filters.command("fsub_mode") & filters.private & admin)
async def fsub_mode(client: Client, message: Message):
    channels = await Seishiro.show_channels()
    buttons = []
    for cid in channels:
        try:
            chat = await client.get_chat(cid)
            mode = await Seishiro.get_channel_mode(cid)
            status = "🟢" if mode == "on" else "🔴"
            buttons.append([InlineKeyboardButton(f"{status} {chat.title}", callback_data=f"rfs_ch_{cid}")])
        except Exception:
            continue
    
    if not buttons:
        buttons.append([InlineKeyboardButton("No Channels Found", callback_data="no_channels")])
        
    await message.reply_text(
        "Select a channel to toggle its force-sub mode:",
        reply_markup=InlineKeyboardMarkup(buttons + [
            [InlineKeyboardButton("Close", callback_data="close")]
        ])
    )

@Client.on_message(filters.command("add_fsub_chnl") & filters.private & admin)
async def add_fsub(client: Client, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply("Usage: /add_fsub_chnl <channel_id>")
        
        cid = int(message.command[1])
        try:
            chat = await client.get_chat(cid)
        except:
            return await message.reply("❌ Bot cannot access this channel or invalid ID")
            
        await Seishiro.add_fsub_channel(cid)
        await message.reply(f"✅ Added {chat.title} to Force-Sub list")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

@Client.on_message(filters.command("rem_fsub_chnl") & filters.private & admin)
async def rem_fsub(client: Client, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply("Usage: /rem_fsub_chnl <channel_id>")
            
        cid = int(message.command[1])
        await Seishiro.remove_fsub_channel(cid)
        await message.reply("✅ Removed channel from Force-Sub list")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

@Client.on_message(filters.command("fsub_chnls") & filters.private & admin)
async def view_fsub(client: Client, message: Message):
    channels = await Seishiro.get_fsub_channels()
    if not channels:
        return await message.reply("No Force-Sub channels set")
        
    text = "<b>📢 Force-Sub Channels:</b>\n"
    for cid in channels:
        try:
            chat = await client.get_chat(cid)
            text += f"• {chat.title} (`{cid}`)\n"
        except:
            text += f"• `{cid}` (Inaccessible)\n"
            
    await message.reply(text)

@Client.on_callback_query(filters.regex(r"^(rfs_|fsub_back)"))
async def fsub_settings_callback(client: Client, callback_query):
    user_id = callback_query.from_user.id
    cb_data = callback_query.data

    if cb_data.startswith("rfs_ch_"):
        cid = int(cb_data.split("_")[2])
        try:
            chat = await client.get_chat(cid)
            mode = await Seishiro.get_channel_mode(cid)
            status = "ON" if mode == "on" else "OFF"
            new_mode = "off" if mode == "on" else "on"
            buttons = [
                [InlineKeyboardButton(f"ForceSub Mode {'OFF' if mode == 'on' else 'ON'}",
                                      callback_data=f"rfs_toggle_{cid}_{new_mode}")],
                [InlineKeyboardButton("back", callback_data="fsub_back")]
            ]
            await callback_query.message.edit_text(
                f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        except Exception:
            await callback_query.answer("Failed to fetch channel info", show_alert=True)

    elif cb_data.startswith("rfs_toggle_"):
        parts = cb_data.split("_")[2:]
        cid = int(parts[0])
        action = parts[1]
        mode = "on" if action == "on" else "off"

        await Seishiro.set_channel_mode(cid, mode)
        await callback_query.answer(f"Force-Sub set to {'ON' if mode == 'on' else 'OFF'}")

        chat = await client.get_chat(cid)
        status = "ON" if mode == "on" else "OFF"
        new_mode = "off" if mode == "on" else "on"
        buttons = [
            [InlineKeyboardButton(f"ForceSub Mode {'OFF' if mode == 'on' else 'ON'}",
                                  callback_data=f"rfs_toggle_{cid}_{new_mode}")],
            [InlineKeyboardButton("back", callback_data="fsub_back")]
        ]
        await callback_query.message.edit_text(
            f"Channel: {chat.title}\nCurrent Force-Sub Mode: {status}",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif cb_data == "fsub_back":
        channels = await Seishiro.show_channels()
        buttons = []
        for cid in channels:
            try:
                chat = await client.get_chat(cid)
                mode = await Seishiro.get_channel_mode(cid)
                status = "🟢" if mode == "on" else "🔴"
                buttons.append([InlineKeyboardButton(f"{status} {chat.title}", callback_data=f"rfs_ch_{cid}")])
            except Exception:
                continue

        if not buttons:
            buttons.append([InlineKeyboardButton("No Channels Found", callback_data="no_channels")])

        await callback_query.message.edit_text(
            "Select a channel to toggle its force-sub mode:",
            reply_markup=InlineKeyboardMarkup(buttons + [
                [InlineKeyboardButton("Close", callback_data="close")]
            ])
        )



# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official 
#Supoort group @rexbotschat