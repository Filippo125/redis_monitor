import unittest
from redis_monitor.redis_monitor import RedisStats, NotSupportedVersion


class TestRedisStats2817(unittest.TestCase):

    def _get_RedisStats(self):
        return RedisStats(simulate="test_file/redis_2_8_17.json")


    def test_get_memory(self):
        r = self._get_RedisStats()
        mem = r.get_memory_stats()
        self.assertTrue("used" in mem.keys(), "used not found in key")
        self.assertTrue("rss" in mem.keys(), "rss not found in key")
        self.assertTrue("peak" in mem.keys(), "peak not found in key")
        self.assertTrue("total" not in mem.keys(), "total found in key")
        self.assertTrue("max" not in mem.keys(), "total found in key")

    def test_get_connection_stats(self):
        r = self._get_RedisStats()
        conn = r.get_connection_stats()
        self.assertTrue("connected" in conn.keys(), "connected not found in key")
        self.assertTrue("blocked" in conn.keys(), "blocked not found in key")
        self.assertTrue(conn["connected"] == 5)
        self.assertTrue(conn["blocked"] == 0)

    def test_get_perf_stats(self):
        r = self._get_RedisStats()
        perf = r.get_performance_stats()
        self.assertTrue("fragment_ratio" in perf.keys(), "fragment_ratio not found in key")
        self.assertTrue("hit_rate" in perf.keys(), "hit_rate not found in key")
        self.assertTrue("ops_per_sec" in perf.keys(), "ops_per_sec not found in key")
        self.assertTrue(perf["fragment_ratio"] == 2.86)
        self.assertTrue(perf["hit_rate"] >= 0)

    def test_get_sys(self):
        r = self._get_RedisStats()
        sys = r.get_system_stats()
        self.assertTrue("cpu_sys" in sys.keys(), "cpu_sys not found in key")
        self.assertTrue("cpu_user" in sys.keys(), "cpu_user not found in key")
        self.assertTrue("uptime" in sys.keys(), "uptime not found in key")