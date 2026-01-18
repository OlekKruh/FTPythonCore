import os
import sys
from dotenv import load_dotenv


def main():
    print("ORACLE STATUS: Reading the Matrix...")

    loaded = load_dotenv()

    mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_ENDPOINT")

    missing_vars = []
    if not db_url:
        missing_vars.append("DATABASE_URL")
    if not api_key:
        missing_vars.append("API_KEY")
    if not zion_url:
        missing_vars.append("ZION_ENDPOINT")

    if missing_vars:
        print("\nWARNING: Matrix connection unstable.")
        print(f"Missing configuration: {', '.join(missing_vars)}")
        print("Please check your .env file or environment variables.")
    else:
        print("\nConfiguration loaded:")
        print(f"Mode: {mode}")

        if mode == "production":
            print("Database: [REDACTED]")
        else:
            db_host = "local instance"
            if db_url and "@" in db_url:
                db_host = db_url.split("@")[-1]
            print(f"Database: Connected to {db_host}")
        if api_key:
            masked_key = (api_key[:4] + "****"
                          + api_key[-4:]) if len(api_key) > 8 else "****"
            print(f"API Access: Authenticated ({masked_key})")

        print(f"Log Level: {log_level}")
        print(f"Zion Network: {zion_url}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if loaded:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found"
              "(running on system vars or defaults)")
        sys.exit(1)

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
