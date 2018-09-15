from argparse import ArgumentParser

def parse_cli():
    parser = ArgumentParser()
    conn_group = parser.add_argument_group("Connection options")
    output_group = parser.add_argument_group("Output options")
    ###############################################################################################################
    parser.add_argument("-d", "--debug", dest="debug", action="store_true", help="debug mode")
    parser.add_argument("-f", "--full", dest="full", action="store_true", help="show full summary statistics")
    parser.add_argument("-r", "--raw", dest="raw", action="store_true", help="show raw statistics")
    parser.add_argument("-m", "--memory", dest="mem", action="store_true", help="show memory statistics")
    parser.add_argument("-s", "--system", dest="sys", action="store_true", help="show system statistics")
    parser.add_argument("-p", "--performance", dest="perf", action="store_true", help="show performance statistics")
    parser.add_argument("-i", "--dbinstance", dest="dbinstance", nargs='?',const="SENT" ,help="show instance")
    parser.add_argument("-c", "--connection", dest="conn", action="store_true", help="show connection statistics")
    ###############################################################################################################
    output_group.add_argument("-j", "--json", dest="json", action="store_true", help="output in json format",default=False)
    output_group.add_argument("-w", "--watch", dest="watch", help="seconds to watch mode",default=-1)
    ###############################################################################################################
    conn_group.add_argument("-H", "--host", dest="host", help="redis host",default="localhost")
    conn_group.add_argument("-P", "--port", dest="port",  help="redis port",default=6379)
    conn_group.add_argument("-W", "--password", dest="pwd",help="redis password",default=None)
    ###############################################################################################################
    options = parser.parse_args()
    try:
        w = int(options.watch)
        options.watch = w
    except:
        print("-w option must be a number")
    return options