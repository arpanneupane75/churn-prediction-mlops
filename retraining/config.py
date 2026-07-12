from pathlib import Path

# =====================================================
# Project Root
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =====================================================
# Data
# =====================================================

DATA_DIR = PROJECT_ROOT / "data"

TRAIN_DATA = DATA_DIR / "train_data.csv"
TEST_DATA = DATA_DIR / "test_data.csv"

# =====================================================
# Saved Models
# =====================================================

MODEL_PATH = PROJECT_ROOT / "churn_model.pkl"
SCALER_PATH = PROJECT_ROOT / "scaler.pkl"
FEATURE_PATH = PROJECT_ROOT / "feature_names.pkl"
BASELINE_PATH = PROJECT_ROOT / "baseline.json"

# =====================================================
# Production Logs
# =====================================================

PRODUCTION_LOGS = PROJECT_ROOT / "production_logs.csv"

# =====================================================
# MLflow
# =====================================================

EXPERIMENT_NAME = "Customer Churn"

# =====================================================
# Random State
# =====================================================

RANDOM_STATE = 42

TEST_SIZE = 0.2