import unittest
from redis_monitor.redis_monitor import RedisStats,NotSupportedVersion


class TestRedisStats2817(unittest.TestCase):

    def _get_RedisStats(self):
        return RedisStats(simulate="test_file/redis_2_8_17.json")


    def test_redis_mem_unsupp(self):
        r = self._get_RedisStats()
        with self.assertRaises(NotSupportedVersion):
            r.get_memory_stats()