from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from send_message import send_love



sched = BlockingScheduler()
sched.add_job(send_love,'interval', seconds=2)

sched.start()

