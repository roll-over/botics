import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv('ME_CONFIG_MONGODB_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client['collaboration']
collection = db['users']
