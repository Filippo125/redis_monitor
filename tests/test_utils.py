import unittest
from redis_monitor.utils import seconds_to_human_readable, bytes_to_human_readable

class TestSecondToHumanReadableUtils(unittest.TestCase):
    def test_seconds_to_human_readable_zero(self):
        """
        Test zero value
        """
        s = seconds_to_human_readable(0)
        self.assertEqual(s,"0")

    def test_seconds_to_human_readable_sixty(self):
        """
        Test sixty seconds value
        """
        s = seconds_to_human_readable(60)
        self.assertEqual(s,"1 minute")
    
    def test_seconds_to_human_readable_one_hour(self):
        """
        Test one hours value
        """
        s = seconds_to_human_readable(3600)
        self.assertEqual(s,"1 hour")
    
    def test_seconds_to_human_readable_one_day(self):
        """
        Test one days value
        """
        s = seconds_to_human_readable(3600*24)
        self.assertEqual(s,"1 day")
    
    def test_seconds_to_human_readable_one_week(self):
        """
        Test one weeks value
        """
        s = seconds_to_human_readable(3600*24*7)
        self.assertEqual(s,"1 week")

    def test_seconds_to_human_readable_1(self):
        """
        Test with 1 hours 32 minutes 
        """
        s = seconds_to_human_readable(5520)
        self.assertEqual(s,"1 hour, 32 minutes")