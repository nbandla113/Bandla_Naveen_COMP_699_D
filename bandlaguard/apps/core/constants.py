# apps/core/constants.py

# Risk Levels
RISK_LOW = "low"
RISK_MEDIUM = "medium"
RISK_HIGH = "high"

RISK_CHOICES = [
    (RISK_LOW, "Low"),
    (RISK_MEDIUM, "Medium"),
    (RISK_HIGH, "High"),
]

# Content Types
CONTENT_TEXT = "text"
CONTENT_IMAGE = "image"
CONTENT_DRAFT = "draft"

CONTENT_TYPES = [
    (CONTENT_TEXT, "Text"),
    (CONTENT_IMAGE, "Image"),
    (CONTENT_DRAFT, "Draft"),
]

# Status Types
STATUS_PENDING = "pending"
STATUS_REVIEWED = "reviewed"
STATUS_DISCARDED = "discarded"

STATUS_CHOICES = [
    (STATUS_PENDING, "Pending"),
    (STATUS_REVIEWED, "Reviewed"),
    (STATUS_DISCARDED, "Discarded"),
]

# Default Suggestions
DEFAULT_SAFE_MESSAGE = "Your content looks safe."

# File Paths
LOG_FILE_PATH = "logs/system.log"
REPORTS_FOLDER = "reports/"

# Limits
MAX_TEXT_LENGTH = 1000
MAX_IMAGE_SIZE_MB = 5