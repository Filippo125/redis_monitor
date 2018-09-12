from __future__ import print_function
from module import RedisStats
from argsparse import parse_cli
import json
from utils import seconds_to_human_readable, bytes_to_human_readable
import monitor
import time
import sys

def json_output(r,options):
    if options.raw:
        data = r.get_raw_stats()
    elif options.mem:
        data = r.get_memory_stats()
    elif options.sys:
        data = r.get_system_stats()
    elif options.perf:
        data = r.get_performance_stats()
    elif options.conn:
        data = r.get_connection_stats()
    elif options.dbinstance:
        data = r.get_instance_stats(options.dbinstance)
    else:
        data = r.get_full_summary_stats()    
    if options.debug:
        print(json.dumps(data,indent=2))
    else:
        print(json.dumps(data))

def console_output(r,options):
    screen = None
    try:
        data = r.get_full_summary_stats()
        screen = monitor.monitor_active()
        while monitor.monitor_watch(screen,data):
            data = r.get_full_summary_stats()
            time.sleep(options.watch)           
    except Exception as e:
        print(e)
    finally:
        if screen != None:
            monitor.monitor_deactivate(screen)



if __name__ == "__main__":
    options,args = parse_cli()
    r = RedisStats(host=options.host,
                   port=options.port,
                   password=options.pwd,)
#                   simulate=options.debug)
    if options.json:
        json_output(r,options)
    else:
        console_output(r,options)