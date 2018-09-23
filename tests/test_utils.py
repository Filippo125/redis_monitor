# noqa: E501
import unittest
from redis_monitor.utils import seconds_to_human_readable
from redis_monitor.utils import bytes_to_human_readable


class TestSecondToHumanReadableUtils(unittest.TestCase):
    def test_seconds_to_human_readable_zero(self):
        """
        Test zero value
        """
        s = seconds_to_human_readable(0)
        self.assertEqual(s, "0")

    def test_seconds_to_human_readable_sixty(self):
        """
        Test sixty seconds value
        """
        s = seconds_to_human_readable(60)
        self.assertEqual(s, "1 minute")

    def test_seconds_to_human_readable_one_hour(self):
        """
        Test one hours value
        """
        s = seconds_to_human_readable(3600)
        self.assertEqual(s, "1 hour")

    def test_seconds_to_human_readable_one_day(self):
        """
        Test one days value
        """
        s = seconds_to_human_readable(3600 * 24)
        self.assertEqual(s, "1 day")

    def test_seconds_to_human_readable_one_week(self):
        """
        Test one weeks value
        """
        s = seconds_to_human_readable(3600 * 24 * 7)
        self.assertEqual(s, "1 week")

    def test_seconds_to_human_readable_1(self):
        """
        Test with 1 hours 32 minutes
        """
        s = seconds_to_human_readable(5520)
        self.assertEqual(s, "1 hour, 32 minutes")


class TestBytesToHumanReadableUtils(unittest.TestCase):
    def test_bytes_to_human_readable_zero(self):
        """
        Test zero value
        """
        s = bytes_to_human_readable(0)
        self.assertEqual(s, "0 B")

    def test_bytes_to_human_readable_1k(self):
        """
        Test 1k bytes value
        """
        s = bytes_to_human_readable(1024)
        self.assertEqual(s, "1 kB")

    def test_bytes_to_human_readable_1M(self):
        """
        Test 1M bytes
        """
        s = bytes_to_human_readable(1024 * 1024)
        self.assertEqual(s, "1 MB")

    def test_bytes_to_human_readable_1G(self):
        """
        Test 1GB
        """
        s = bytes_to_human_readable(1024 * 1024 * 1024)
        self.assertEqual(s, "1 GB")

    def test_bytes_to_human_readable_1T(self):
        """
        Test 1TB
        """
        s = bytes_to_human_readable(1024 * 1024 * 1024 * 1024)
        self.assertEqual(s, "1 TB")

    def test_bytes_to_human_readable_1P(self):
        """
        Test 1PB
        """
        s = bytes_to_human_readable(1024 * 1024 * 1024 * 1024 * 1024)
        self.assertEqual(s, "1 PB")

    def test_bytes_to_human_readable_12M(self):
        """
        Test 12MB
        """
        s = bytes_to_human_readable(12 * 1024 * 1024)
        self.assertEqual(s, "12 MB")

    def test_bytes_to_human_readable_45B(self):
        """
        Test 45B
        """
        s = bytes_to_human_readable(45)
        self.assertEqual(s, "45 B")
