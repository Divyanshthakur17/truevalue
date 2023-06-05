from celery import shared_task
import time

@shared_task
def handle_sleep():
    for i in range(10):
        print('handle sleep started',i)
    # time.sleep(30)