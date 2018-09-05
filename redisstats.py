#!/bin/env python
#-*- coding:utf-8 -*-
from __future__ import print_function
import json
import redis

class RedisStats:
    def __init__(self, **kwargs):
        """
        Initialize RedisStats object
        """
        self.host     = kwargs.get("host","localhost")
        self.port     = kwargs.get("port",6379)
        self.password = kwargs.get("password",None)

    def _conn(self):
        return redis.Redis(host=self.host,port=self.port,password=self.password)

    def get_raw_stats(self):
        conn = self._conn()
        return conn.info()
    def get_version(self):
        return self.get_raw_stats()["redis_version"]
    def get_uptime(self):
        return self.get_raw_stats()["uptime_in_seconds"]

    def _get_perf(self,raw_stats):
        performance = dict()
        performance["fragment_ratio"]  = raw_stats["mem_fragment_ratio"]
        hits   = raw_stats["keyspace_hits"]
        misses = raw_stats["keyspace_misses"]
        performance["hit_rate"]   = hits/(hits+misses)
        performance["ops_per_sec"] = raw_stats["instantaneous_ops_per_sec"]
        return performance

    def _get_conn(self,raw_stats):
        connection = dict()
        connection["connected"] = raw_stats["connected_clients"]
        connection["blocked"]   = raw_stats["blocked_clients"]
        return connection        
    def _get_sys(self,raw_stats):
        sys        = dict()
        sys["cpu_sys"]  = raw_stats["used_cpu_sys"]
        sys["cpu_user"] = raw_stats["used_cpu_user"]
        sys["uptime"]   = raw_stats["uptime_in_seconds"]
        return sys
    def _get_memory(self,raw_stats):
        memory     = dict()        
        memory["used"]  = raw_stats["used_memory"]
        memory["rss"]   = raw_stats["used_memory_rss"]
        memory["peak"]  = raw_stats["used_memory_peak"]
        memory["total"] = raw_stats["total_system_memory"]
        memory["max"]   = raw_stats["maxmemory"]
        return memory

    def get_performance_stats(self):
        raw = self.get_raw_stats()
        return self._get_perf(raw_stats=raw)

    def get_system_stats(self):
        raw = self.get_raw_stats()
        return self._get_sys(raw_stats=raw)

    def get_memory_stats(self):
        raw = self.get_raw_stats()
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
        return dict(connection=connection,sys=sys,memory=memory,performance=performance)