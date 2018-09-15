import unittest
from redis_monitor.redis_monitor import RedisStats,NotSupportedVersion


class TestRedisStats(unittest.TestCase):

    def test_redis_mem_unsupp(self):
        r = RedisStats(simulate="test_file/redis_2_8_17.json")
        with self.assertRaises(NotSupportedVersion):
            r.get_memory_stats()
    
    def test_redis_mem_supp(self):
        r = RedisStats(simulate="test_file/redis_3_2_6_db.json")
        r.get_memory_stats()
