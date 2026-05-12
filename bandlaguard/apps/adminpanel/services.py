# apps/adminpanel/services.py

from django.contrib.auth import get_user_model
from apps.content.models import Content, ReviewResult
from django.utils import timezone
import os
import logging

User = get_user_model()

logger = logging.getLogger(__name__)


# -------------------------------
# PLATFORM STATS
# -------------------------------
def get_platform_stats():
    """
    Returns overall platform statistics
    """

    total_users = User.objects.count()
    total_content = Content.objects.count()
    total_reviews = ReviewResult.objects.count()

    # 🔥 FIX: correct case for risk_level
    high_risk = ReviewResult.objects.filter(risk_level__iexact='High').count()

    return {
        "total_users": total_users,
        "total_content": total_content,
        "total_reviews": total_reviews,
        "high_risk": high_risk
    }


# -------------------------------
# BLOCK USER
# -------------------------------
def block_user(user_id):
    """
    Block a user by ID
    """

    try:
        user = User.objects.get(id=user_id)

        if user.is_blocked:
            return False  # already blocked

        user.is_blocked = True
        user.save()

        logger.info(f"User blocked: {user.email}")
        return True

    except User.DoesNotExist:
        logger.error(f"User not found: {user_id}")
        return False

    except Exception as e:
        logger.error(f"Error blocking user: {str(e)}")
        return False


# -------------------------------
# REMOVE INACTIVE USERS
# -------------------------------
def remove_inactive_users():
    """
    Delete inactive users
    """

    try:
        inactive_users = User.objects.filter(is_active=False)

        count = inactive_users.count()

        inactive_users.delete()

        logger.info(f"Removed {count} inactive users")

        return count

    except Exception as e:
        logger.error(f"Error removing inactive users: {str(e)}")
        return 0


# -------------------------------
# GET SYSTEM LOGS
# -------------------------------
def get_system_logs(log_file_path):
    """
    Fetch last 50 log entries
    """

    try:
        if not os.path.exists(log_file_path):
            logger.warning("Log file not found")
            return []

        with open(log_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        return lines[-50:]  # last 50 logs

    except Exception as e:
        logger.error(f"Error reading logs: {str(e)}")
        return []


# -------------------------------
# TRIGGER MODEL UPDATE
# -------------------------------
def trigger_model_update():
    """
    Simulated model update process
    """

    try:
        logger.info("Model update triggered")

        # 🔥 You can plug real model retraining here
        return {
            "status": "success",
            "message": "Model update started successfully",
            "timestamp": timezone.now()
        }

    except Exception as e:
        logger.error(f"Model update failed: {str(e)}")

        return {
            "status": "error",
            "message": "Model update failed",
            "timestamp": timezone.now()
        }