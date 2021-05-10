from apscheduler.schedulers.blocking import BlockingScheduler

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=21)
from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from updater import update


def start():
    print("Start")
    scheduler = BackgroundScheduler()
    scheduler.add_job(update.getZip, 'cron',day_of_week='mon-fri',hour=12 ,minute = 30)
    #scheduler.add_job(update.getZip,'interval',minutes=15)
    scheduler.start()
