from dotenv import load_dotenv
import os

load_dotenv()

mode = os.getenv("MATRIX_MODE") or "development"
database = os.getenv("DATABASE_URL") or "localhost"
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL") or "DEBUG"
endpoint = os.getenv("ZION_ENDPOINT")

print("ORACLE STATUS: Consulting the configuration...\n")
print("Configuration loaded:")

print(f"Mode: {mode}")
if mode == "development":
    print("Development: detailed diagnostics enabled!")
elif mode == "production":
    print("Production: restricted diagnostics enabled!")

if not database:
    print("DATABASE_URL is missing")
else:
    print("Database: Connected to local instance")

if not api_key:
    print("API_KEY is missing")
else:
    print("API Access: Authenticated")

if not log_level:
    print("LOG_LEVEL is missing")
else:
    print(f"Log Level: {log_level}")

if not endpoint:
    print("ZION_ENDPOINT is missing")
else:
    print("Remote Network: Online")
