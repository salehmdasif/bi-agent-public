"""
AI insight generation Celery task.
Produces daily narrative summaries of metric trends.
"""
from app.celery_app import celery_app


@celery_app.task(name="tasks.generate_daily_insights", bind=True, max_retries=2)
def generate_daily_insights(self):
    """
    Generate AI-written insights summarizing recent metric trends.

    For each connected data source, fetches the last 7 and 30 days of
    KPI data, passes it to the configured LLM with a structured prompt,
    and saves the generated narrative as an Insight record.

    Note:
        Insight generation logic and prompts are proprietary
        and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
