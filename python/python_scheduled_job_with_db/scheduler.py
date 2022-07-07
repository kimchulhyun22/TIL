from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from pytz import timezone


class SingleJobScheduler:
    def __init__(self) -> None:
        self._schedule = BlockingScheduler()

    def execute_interval_job_by_seconds(self, job, *args, seconds=0) -> None:
        self._schedule.add_job(job, "interval", seconds=seconds, args=args)
        self._schedule.start()

    def execute_interval_job_by_minutes(self, job, *args, minutes=0) -> None:
        self._schedule.add_job(job, "interval", minutes=minutes, args=args)
        self._schedule.start()

    def execute_cron_job(
        self, job, *args, day_of_week="mon-sun", hour="0-23", minute=1, second=1
    ):
        self._schedule.add_job(
            job,
            "cron",
            day_of_week=day_of_week,
            hour=hour,
            minute=f"*/{minute}",
            second=f"*/{second}",
            args=args,
        )
        self._schedule.start()


scheduler = SingleJobScheduler()


def print_interval(type, detail):
    print(f"{type} job {detail}= ", datetime.now(tz=timezone("Asia/Seoul")))


def main():
    scheduler.execute_cron_job(print_interval, "cron", "test", second=5)


if __name__ == "__main__":
    main()
