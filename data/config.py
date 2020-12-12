import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
DBHOST = str(os.getenv("DBHOST"))
INVITE_CODE = str(os.getenv("INVITE_CODE"))

admins = [
	os.getenv("ADMIN_ID"),
]

# ip = os.getenv("ip")

# aiogram_redis = {
# 	'host':ip,
# }

# redis = {
# 	'address':(ip, 6379),
# 	'encoding':'utf8'
# }

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
# POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"

QIWI_TOKEN = str(os.getenv("QIWI_TOKEN"))
QIWI_KEY_PUBLIC = str(os.getenv("QIWI_KEY_PUBLIC"))
QIWI_WALLET = str(os.getenv("QIWI_WALLET"))
