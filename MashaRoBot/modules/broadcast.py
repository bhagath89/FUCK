from MashaRoBot.modules.helper_funcs.extraction import extract_user
from telegram import *
from telegram.ext import *
from MashaRoBot import DEMONS, dispatcher

chats_list = ["@createbot123"]
list1 = []
list2 = []

button = InlineKeyboardMarkup(list1)

def cmd_broadcast(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    args = context.args
    user_id = extract_user(message, args)
    if user_id in DEMONS:
        for item in chats_list:
            if item[1:] in list2:
                pass
            else:
                list1.append([InlineKeyboardButton(text=item[1:], url=f"https://t.me/{item[1:]}")])
                list2.append(item[1:])

        txt = update.effective_message.reply_to_message.text
        doc = update.effective_message.reply_to_message.document
        voi = update.effective_message.reply_to_message.voice
        vid = update.effective_message.reply_to_message.video
        vid_nt = update.effective_message.reply_to_message.video_note
        aud = update.effective_message.reply_to_message.audio
        pic = update.effective_message.reply_to_message.photo
        ctct = update.effective_message.reply_to_message.contact
        if pic:
            for chats in chats_list:
                context.bot.send_photo(chats, pic)
                context.bot.get_chat("@hackersdenkerala")
        elif txt:
            for chats in chats_list:
                context.bot.send_message(chats, txt)
        elif doc:
            for chats in chats_list:
                context.bot.send_document(chats, doc)
        elif voi:
            for chats in chats_list:
                context.bot.send_voice(chats, voi)
        elif vid:
            for chats in chats_list:
                context.bot.send_video(chats, vid)
        elif vid_nt:
            for chats in chats_list:
                context.bot.send_video_note(chats, vid_nt)
        elif aud:
            for chats in chats_list:
                context.bot.send_audio(chats, aud)
        elif ctct:
            for chats in chats_list:
                context.bot.send_contact(chats, ctct)
        else:
            update.message.reply_text("Mention something to broadcast! I can't broadcast if there is nothing to broadcast")

def cmd_addchat(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    args = context.args
    user_id = extract_user(message, args)
    if user_id in DEMONS:
        type = update.effective_chat.type
        if type == "private":
            chats = update.message.text.replace('/addchat ', '')
            if chats[0] != '@':
                update.message.reply_text("Please enter a valid username \n Example : @kgf_robot")
            else:
                if " " in chats:
                    update.message.reply_text("Add one username at a time.")
                else:
                    if chats in chats_list:
                        update.message.reply_text("This username is already in broadcast list. How am I supposed to add it again?")
                    else:
                        chats_list.append(chats)
                        list1.append([InlineKeyboardButton(text=chats[1:], url=f"https://t.me/{chats[1:]}")])
                        update.message.reply_text(f"Username {chats} successfully added to broadcast list \n "
                                                  f"Type /bdlist to see the list")

def cmd_rmchat(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    args = context.args
    user_id = extract_user(message, args)
    if user_id in DEMONS:
        type = update.effective_chat.type
        if type == "private":
            chats = update.message.text.replace('/rmchat ', '')
            if chats[0] != '@':
                update.message.reply_text("Please enter a valid username. \n Example : @kgf_robot \n "
                                          "And make sure that the broadcast list contain the username.")
            else:
                if " " in chats:
                    update.message.reply_text("Remove one username at a time.")
                else:
                    if chats in chats_list:
                        chats_list.remove(chats)
                        list1.remove([InlineKeyboardButton(text=chats[1:], url=f"https://t.me/{chats[1:]}")])
                        update.message.reply_text(f"Username {chats} successfully removed from the broadcast list. \n "
                                              f"Type /bdlist to see the list")
                    else:
                        update.message.reply_text("This user is not in the broadcast list. You may misspelled the username!")


def cmd_bdlist(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    args = context.args
    user_id = extract_user(message, args)
    if user_id in DEMONS:
        type = update.effective_chat.type
        if type == "private":
            for item in chats_list:
                if item[1:] in list2:
                    pass
                else:
                    list1.append([InlineKeyboardButton(text=item[1:], url=f"https://t.me/{item[1:]}")])
                    list2.append(item[1:])
            update.message.reply_text("Chats in broadcast list are: \n ",
                                    reply_markup=button)


dispatcher.add_handler(CommandHandler("bdlist", cmd_bdlist))
dispatcher.add_handler(CommandHandler("addchat", cmd_addchat))
dispatcher.add_handler(CommandHandler("rmchat", cmd_rmchat))
dispatcher.add_handler(CommandHandler("broadcast", cmd_broadcast))
