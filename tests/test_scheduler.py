import unittest
from zeppos_airflow.scheduler import Scheduler
from datetime import datetime, timedelta

class TestTheProjectMethods(unittest.TestCase):
    def test_yesterday_methods(self):
        now = datetime.now() - timedelta(days=1)
        self.assertEqual(now.year, Scheduler.yesterday().year)
        self.assertEqual(now.month , Scheduler.yesterday().month)
        self.assertEqual(now.day, Scheduler.yesterday().day)
        self.assertEqual(0, Scheduler.yesterday().hour)
        self.assertEqual(0, Scheduler.yesterday().minute)
        self.assertEqual(0, Scheduler.yesterday().second)
        self.assertEqual(0, Scheduler.yesterday().microsecond)


if __name__ == '__main__':
    unittest.main()
