import pendulum
from datetime import timedelta

class Scheduler:
    class StartDate:
        @staticmethod
        def yesterday():
            yesterday = pendulum.now("America/Chicago")
            return yesterday.subtract(days=1, hours=yesterday.hour, minutes=yesterday.minute, seconds=yesterday.second,
                                      microseconds=yesterday.microsecond)

    class RetryDelay:
        @staticmethod
        def five_minutes():
            return timedelta(minutes=5)
