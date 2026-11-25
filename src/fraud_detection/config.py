"""Project-wide settings: file paths and constants."""

from pathlib import Path

# Project root folder: go up two levels from this file
# (config.py → fraud_detection → src → project root)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data folders
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

# Fixed random seed so results are reproducible
RANDOM_STATE = 42

# Name of the column we are predicting
TARGET = "is_fraud"