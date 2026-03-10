import os

from apscheduler.schedulers.background import BackgroundScheduler
from tasks import generate_article
from dotenv import load_dotenv

load_dotenv()   # membaca file .env

EMB_SCHEDULER_HOUR = os.getenv("EMB_SCHEDULER_HOUR")
EMB_SCHEDULER_MINUTE = os.getenv("EMB_SCHEDULER_MINUTE")

scheduler = BackgroundScheduler()


def start_scheduler():

    # scheduler harian jam 07:00
    scheduler.add_job(
        generate_article,
        "cron",
        hour=EMB_SCHEDULER_HOUR,
        minute=EMB_SCHEDULER_MINUTE,
        id="daily_article",
        replace_existing=True,
    )

    # # jalankan setiap 20 detik
    # scheduler.add_job(
    #     generate_article,
    #     "interval",
    #     seconds=20,
    #     id="generate_article_job",
    #     replace_existing=True,
    # )

    scheduler.start()

    print("Scheduler started")
