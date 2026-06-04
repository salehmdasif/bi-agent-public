"""
Telegram Bot integration.
Handles webhook registration, message routing, and notification delivery.
"""


async def register_webhook(webhook_url: str, secret: str) -> None:
    """
    Register the backend's webhook URL with Telegram.

    Called automatically on startup if TELEGRAM_BOT_TOKEN is configured.

    Args:
        webhook_url: The full HTTPS URL that Telegram will POST updates to.
        secret: A secret token used to verify that updates come from Telegram.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def handle_incoming_message(update: dict) -> None:
    """
    Route an incoming Telegram update to the agent.

    Extracts the message text and chat ID, runs the agent, and sends
    the response back to the Telegram chat.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def send_alert_notification(chat_id: str, message: str) -> None:
    """
    Send an alert notification to a Telegram chat.

    Used by the monitoring Celery task when a threshold is breached.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def send_report_summary(chat_id: str, summary: str) -> None:
    """
    Send a weekly report summary to a Telegram chat.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
