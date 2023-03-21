import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, filters, CommandHandler, CallbackQueryHandler
import requests

telegram_bot_token = "6298326650:AAFeSs_OpoQqOUotjmsyXc0TyFz0bGkTX7o"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello there. I am Laddie, this is my first time working on a telegram bot. Thank you for using my telegram bot.")
dispatcher.add_handler(CommandHandler("start", start))

def help(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='If you need help, please use Google instead.')

dispatcher.add_handler(CommandHandler("help", help))

def returnTrendingTopics(update, context):
    output = "Here are the top 7 trending search: \n"
    BASE = 'http://127.0.0.1:5000/'
    response = requests.get(BASE)
    topics = response.json()
    chat_id = update.effective_chat.id
    for i, topic in enumerate(topics):
        output += "\n" + f"*{i+1}.{topic[0]}* \n{topic[1]} ago, {topic[-1]} searches \nLink: [{topic[2]}] \n "
    context.bot.send_message(chat_id=chat_id, text=output, parse_mode=telegram.ParseMode.MARKDOWN)
# invoke the get_word_info function when the user sends a message 
# that is not a command.
dispatcher.add_handler(CommandHandler('trending', returnTrendingTopics))

def levelFour(update, context):
    levelFourText = "Hi, This is level four of the marking scheme. Click on the button to view more."
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=levelFourText, parse_mode=telegram.ParseMode.MARKDOWN)
    buttons = [[InlineKeyboardButton('Development Stacks', callback_data='development')],[InlineKeyboardButton('Cloud Computing', callback_data='cloud')],[InlineKeyboardButton('Trade-offs', callback_data='tf')]]
    
    context.bot.send_message(chat_id=chat_id, reply_markup=InlineKeyboardMarkup(buttons), text='Choose one of the options')
    
   
    # context.bot.send_message(chat_id=chat_id, text=stackOutput+cloudOutput+tradeOff, parse_mode=telegram.ParseMode.MARKDOWN)

def stackQueryHandler(update, context):
    query = update.callback_query.data
    update.callback_query.answer()
    chat_id = update.effective_chat.id
    if 'development' in query:
        stackOutput = "*Development Stacks*:\n\n*1. LAMP Stack:*\n-Linux, Apache, MySQL, and PHP.\n-Widely used for building dynamic web applications.\n-Pros: open-source, low cost, and easily customizable.\n-Cons: relatively slower than other stacks, requires manual configurations and setup.\n\n*2. MEAN Stack:*\n-MongoDB, ExpressJS, AngularJS, and NodeJS.\n-Popular for building scalable and real-time applications.\n-Pros: allows developers to write code in a single language (JavaScript), great for real-time data processing, and provides high performance.\n-Cons: limited community support, requires more technical expertise, and may have difficulty handling large amounts of data. \n\n*3. MERN Stack:*\n-MongoDB, ExpressJS, ReactJS, and NodeJS.\n-Similar to MEAN Stack, but with ReactJS instead of AngularJS.\n-Pros: easy to learn, good for building complex user interfaces, and allows for real-time data processing.\n-Cons: requires more technical expertise, can be difficult to debug, and may have difficulty handling large amounts of data.\n\n\n"
        context.bot.send_message(chat_id=chat_id, text=stackOutput, parse_mode=telegram.ParseMode.MARKDOWN)


    if 'cloud' in query:
        cloudOutput = "*Cloud Computing Services:*\n\n*1. Amazon Web Services (AWS):*\n-Provides a range of cloud-based services for computing, storage, and networking.\n-Pros: offers a wide range of services, easy to use, and has a large community of users.\n-Cons: can be expensive, requires more technical expertise, and may have a steep learning curve.\n\n*2. Google Cloud Platform (GCP):*\n-Provides a range of cloud-based services for computing, storage, and networking.\n-Pros: easy to use, offers advanced machine learning capabilities, and has a strong emphasis on security.\n-Cons: can be expensive, limited support for some services, and less established than AWS.\n\n*3. Microsoft Azure:*\n-Provides a range of cloud-based services for computing, storage, and networking.\n-Pros: easy to use, offers excellent hybrid cloud capabilities, and has a strong emphasis on security.\n-Cons: can be expensive, requires more technical expertise, and may have a steep learning curve."
        context.bot.send_message(chat_id=chat_id, text=cloudOutput, parse_mode=telegram.ParseMode.MARKDOWN)

    if 'tf' in query:
        tradeOff = "\n\n\n*Trade-offs:*\n\n-*LAMP*: good for low-cost and easily customizable development, but may have slower performance and require more manual configuration.\n-*MEAN*: great for real-time data processing and high performance, but may require more technical expertise and have limited community support.\n-*MERN*: easy to learn and good for complex user interfaces, but may be difficult to debug and have difficulty handling large amounts of data.\n-*AWS*: offers a wide range of services and a large community of users, but can be expensive and have a steep learning curve.\n-*GCP*: easy to use and offers advanced machine learning capabilities, but can be expensive and have limited support for some services.\n-*Azure*: easy to use and offers excellent hybrid cloud capabilities, but can be expensive and require more technical expertise."
        context.bot.send_message(chat_id=chat_id, text=tradeOff, parse_mode=telegram.ParseMode.MARKDOWN)
        
dispatcher.add_handler(CommandHandler('level4', levelFour))
dispatcher.add_handler(CallbackQueryHandler(stackQueryHandler))
updater.start_polling()