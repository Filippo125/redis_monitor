from __future__ import print_function
from optparse import OptionParser
from redisstats import RedisStats
import json

if __name__ == "__main__":
    usageInfo = "usage: %prog [options]"

    parser = OptionParser(usage=usageInfo, version="%prog 1.0")
    ###############################################################################################################
    parser.add_option("-d", "--debug", dest="debug", action="store_true", help="debug mode")
    parser.add_option("-f", "--full", dest="full", action="store_true", help="show full summary statistics")
    parser.add_option("-r", "--raw", dest="raw", action="store_true", help="show raw statistics")
    parser.add_option("-m", "--memory", dest="mem", action="store_true", help="show memory statistics")
    parser.add_option("-s", "--system", dest="sys", action="store_true", help="show system statistics")
    parser.add_option("-p", "--performance", dest="perf", action="store_true", help="show performance statistics")
    parser.add_option("-c", "--connection", dest="conn", action="store_true", help="show connection statistics")
    ###############################################################################################################
    parser.add_option("-H", "--host", dest="host", help="redis host",default="localhost")
    parser.add_option("-P", "--port", dest="port",  help="redis port",default=6379)
    parser.add_option("-W", "--password", dest="pwd",help="redis password",default=None)
    ###############################################################################################################
    (options, args) = parser.parse_args()

    r = RedisStats(host=options.host,port=options.port,password=options.pwd)
    if options.debug:
        print("## HOST: ", options.host)
        print("## PORT: ", options.port)
        print("## PWD:  ",options.pwd)
    data = None
    if options.raw:
        data = r.get_raw_stats()
    elif options.mem:
        data = r.get_memory_stats()
    elif options.sys:
        data = r.get_memory_stats()
    elif options.perf:
        data = r.get_performance_stats()
    elif options.conn:
        data = r.get_connection_stats()
    else:
        data = r.get_full_summary_stats()
    if options.debug:
        print(json.dumps(data,indent=2))
    else:
        print(json.dumps(data))