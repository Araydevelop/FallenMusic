from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/521c2fe417b62ecfe2a22.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/142a4ff07cf2da3387ffb.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Coder_X_Network")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Hexa_Updates")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5884723781").split()))


FAILED = "https://graph.org/file/60979122df03cc8140562.jpg"
