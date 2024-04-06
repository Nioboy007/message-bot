from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the Pyrogram client
api_id = 10471716
api_hash = 'f8a1b21a13af154596e2ff5bed164860'
bot_token = '6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU'

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# IDs of the channel and groups
channel_id = "-1002030156196"
group_ids = ["-1004128574812", "-1004101770283"]

# Error handling
def error_handler(client, exception):
    print(exception)

# Start command handler
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Welcome to the bot! Use /new to post messages in partner groups.")

# Help command handler
@app.on_message(filters.command("help"))
def help(client, message):
    message.reply_text("This bot allows you to post messages in partner groups. Use /new to start posting.")

# New command handler
@app.on_message(filters.command("new"))
def new_post(client, message):
    message.reply_text("Send your message to be posted in your partner groups.")

# Message handler
@app.on_message(~filters.command)
def handle_message(client, message):
    if message.chat.type == "private":
        post_message(message.text)

# Function to post message in groups and channel
def post_message(text):
    try:
        for group_id in group_ids:
            app.send_message(chat_id=group_id, text=text)
        app.send_message(chat_id=channel_id, text=text)
    except Exception as e:
        print("Error posting message:", e)

# Register error handler
app.on_error += error_handler

# Start the bot
app.run()
