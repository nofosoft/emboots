from apscheduler.schedulers.background import BackgroundScheduler
from tasks import generate_article

scheduler = BackgroundScheduler()


def start_scheduler():

    # scheduler harian jam 07:00
    scheduler.add_job(
        generate_article,
        "cron",
        hour=7,
        minute=0,
        id="daily_article",
        replace_existing=True,
    )

    # jalankan setiap 20 detik
    # scheduler.add_job(
    #     generate_article,
    #     "interval",
    #     seconds=20,
    #     id="generate_article_job",
    #     replace_existing=True,
    # )

    scheduler.start()

    print("Scheduler started")
