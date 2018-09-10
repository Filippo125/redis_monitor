from optparse import OptionParser


def parse_cli():
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
    parser.add_option("-j", "--json", dest="json", action="store_true", help="output in json format",default=False)
    parser.add_option("-w", "--watch", dest="watch", help="seconds to watch mode",default=-1)
    ###############################################################################################################
    parser.add_option("-H", "--host", dest="host", help="redis host",default="localhost")
    parser.add_option("-P", "--port", dest="port",  help="redis port",default=6379)
    parser.add_option("-W", "--password", dest="pwd",help="redis password",default=None)
    ###############################################################################################################
    (options, args) = parser.parse_args()
    try:
        w = int(options.watch)
        options.watch = w
    except:
        print("-w option must be a number")
    return options,args