# noqa: E501,E221
from __future__ import print_function
import json
import redis
import re


class NotSupportedVersion(BaseException):
    def __init__(self, *args, **kwargs):
        super(NotSupportedVersion, self).__init__()
        version = kwargs['version']
        self.message = "Server %s is not supported" % str(version)


class RedisStats:
    VERSION = "1.0"
    regex = r"db[0-9]+"

    def __init__(self, **kwargs):
        """
        Initialize RedisStats object
        """
        self.host     = kwargs.get("host", "localhost")
        self.port     = kwargs.get("port", 6379)
        self.password = kwargs.get("password", None)
        self.simulate = kwargs.get("simulate", None)

    def _conn(self):
        return redis.Redis(host=self.host, port=self.port, password=self.password)

    @staticmethod
    def _is_compatible(version):
        return version >= "3.2.0"

    @staticmethod
    def _db_instance(keys):
        dbi = list()
        for key in keys:
            if re.match(RedisStats.regex, key) is not None:
                dbi.append(key)
        return dbi

    @staticmethod
    def _get_perf(self, raw_stats):
        performance = dict()
        performance["fragment_ratio"] = raw_stats["mem_fragmentation_ratio"]
        performance["hit_rate"] = 0
        hits   = raw_stats["keyspace_hits"]
        misses = raw_stats["keyspace_misses"]
        total  = hits + misses
        if total > 0:
            performance["hit_rate"] = hits / (hits + misses)
        performance["ops_per_sec"] = raw_stats["instantaneous_ops_per_sec"]
        return performance

    @staticmethod
    def _get_conn(self, raw_stats):
        connection = dict()
        connection["connected"] = raw_stats["connected_clients"]
        connection["blocked"]   = raw_stats["blocked_clients"]
        return connection

    @staticmethod
    def _get_sys(self, raw_stats):
        sys = dict()
        sys["cpu_sys"]  = raw_stats["used_cpu_sys"]
        sys["cpu_user"] = raw_stats["used_cpu_user"]
        sys["uptime"]   = raw_stats["uptime_in_seconds"]
        return sys

    @staticmethod
    def _get_memory(self, raw_stats):
        memory = dict()
        memory["used"]  = raw_stats["used_memory"]
        memory["rss"]   = raw_stats["used_memory_rss"]
        memory["peak"]  = raw_stats["used_memory_peak"]
        memory["total"] = raw_stats["total_system_memory"]
        memory["max"]   = raw_stats["maxmemory"]
        return memory

    @staticmethod
    def _get_instance(self, raw_stats, instance):
        i = dict()
        i["keys"]    = raw_stats["keys"]
        i["expires"] = raw_stats["expires"]
        i["avg_ttl"] = raw_stats["avg_ttl"]
        i["instance"] = instance
        return i

    @staticmethod
    def _get_sum_instance(self, raw_stats):
        i = dict()
        dbis = RedisStats._db_instance(raw_stats.keys())
        i["total_keys"] = 0
        i["total_expires"] = 0
        i["avg_ttl"] = 0
        i["total_instances"] = len(dbis)
        i["instaces"] = dbis
        for dbi in dbis:
            i["total_keys"]  += raw_stats[dbi]["keys"]
            i["total_expires"] += raw_stats[dbi]["expires"]
            i["avg_ttl"] += raw_stats[dbi]["avg_ttl"]
        i["avg_ttl"] = i["avg_ttl"] / i["total_instances"]
        return i

    def get_raw_stats(self):
        if self.simulate:
            return json.load(open(self.simulate, "r"))
        conn = self._conn()
        return conn.info()

    def get_version(self):
        return self.get_raw_stats()["redis_version"]

    def get_uptime(self):
        return self.get_raw_stats()["uptime_in_seconds"]

    def get_performance_stats(self):
        raw = self.get_raw_stats()
        return self._get_perf(raw_stats=raw)

    def get_system_stats(self):
        raw = self.get_raw_stats()
        return self._get_sys(raw_stats=raw)

    def get_memory_stats(self):
        raw = self.get_raw_stats()
        version = raw["redis_version"]
        if not self._is_compatible(version):
            raise NotSupportedVersion(version=version)
        return self._get_memory(raw_stats=raw)

    def get_connection_stats(self):
        raw = self.get_raw_stats()
        return self._get_conn(raw_stats=raw)

    def get_full_summary_stats(self):
        raw = self.get_raw_stats()
        performance = self._get_perf(raw_stats=raw)
        connection  = self._get_conn(raw_stats=raw)
        sys         = self._get_sys(raw_stats=raw)
        memory      = self._get_memory(raw_stats=raw)
        instances   = self._get_sum_instance(raw_stats=raw)
        return dict(connection=connection, sys=sys, memory={}, performance=performance, dbi=instances)

    def get_instance_stats(self, instance=None):
        raw = self.get_raw_stats()
        if instance is None:
            dbi = self._db_instance(raw.keys())
            return [self._get_instance(raw_stats=raw[x], instance=x) for x in dbi]
        else:
            return [self._get_instance(raw_stats=raw[instance], instance=instance)]

    def get_instances_summary_stats(self):
        raw = self.get_raw_stats()
        return self._get_sum_instance(raw)
