from apscheduler.schedulers.background import BackgroundScheduler
from api import tasks

from api.models import Pipeline

def start():
	scheduler = BackgroundScheduler()
	tasks.get_jobs(scheduler)
	scheduler.start()
