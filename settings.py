import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
FROM = os.environ.get("FROM")
TO = os.environ.get("TO")
