import logging
import os
from pathlib import Path
def setup_logging():
    # LOG_DIR = "logs"
    LOG_DIR = Path(
    os.getenv("LOG_DIR", "C:/AI/ai-logs")
)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    # print("Current Working Directory:", os.getcwd())
    # print("Log File:", os.path.abspath("logs/agent.log"))
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_DIR / "agent.log", encoding="utf-8"),
            logging.StreamHandler()
        ],
        force=True
    )

    logging.getLogger(__name__).info("Logging configured successfully.")