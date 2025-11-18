import logging
from pathlib import Path
from .utils import read_text, write_text
from .gemini_client import summarize_with_gemini

# Correct project root (one level up from src/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data directories
INPUT_DIR = PROJECT_ROOT / "data" / "input"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
LOG_DIR = PROJECT_ROOT / "data" / "logs"


def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_DIR / "run.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def main():
    setup_logging()
    logging.info("Starting Gemini summarization pipeline...")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Process all .txt files in data/input
    for file_path in INPUT_DIR.glob("*.txt"):
        logging.info(f"Processing {file_path.name}")

        text = read_text(file_path)
        summary = summarize_with_gemini(text)

        out_path = OUTPUT_DIR / f"{file_path.stem}.summary.txt"
        write_text(out_path, summary)

        logging.info(f"Summary written to: {out_path}")

    logging.info("Pipeline complete.")


if __name__ == "__main__":
    main()
