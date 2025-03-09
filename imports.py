import os
import json
import asyncio
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
