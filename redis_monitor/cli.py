import curses
from redis_monitor.utils import seconds_to_human_readable, bytes_to_human_readable
import datetime


def monitor_active():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.timeout(100)
    stdscr.keypad(True)
    stdscr.nodelay(True)
    return stdscr


def monitor_deactivate(stdscr):
    stdscr.nodelay(False)
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


def monitor_watch(stdscr, data):
    stdscr.clear()  # pulisci schermo
    stdscr.addstr(0, 0, "Update %s Press any button to exit" % datetime.datetime.now())
    stdscr.addstr(1, 0, "# Connection: Active  {0:3}".format(data['connection']["connected"]))
    stdscr.addstr(2, 0, "              Blocked {0:3}".format(data['connection']["blocked"]))
    stdscr.addstr(3, 0, "# Sys Info: Uptime %s" % seconds_to_human_readable(data['sys']['uptime']))
    stdscr.addstr(4, 0, "            SysCPU %.2f" % data['sys']['cpu_sys'])
    stdscr.addstr(5, 0, "            UsrCPU %.2f" % data['sys']['cpu_user'])
    stdscr.addstr(6, 0, "# DB Info: Instances    %d" % data['dbi']['total_instances'])
    stdscr.addstr(7, 0, "           Keys Total   %.2f" % data['dbi']['total_keys'])
    stdscr.addstr(8, 0, "           Keys Expired %.2f" % data['dbi']['total_expires'])
    # stdscr.addstr(6,0,"# Memory: Used %s" % bytes_to_human_readable(data['memory']["used"]))
    # stdscr.addstr(7,0,"          Rss  %s" % bytes_to_human_readable(data['memory']['rss']))
    # stdscr.addstr(8,0,"          Peak %s" % bytes_to_human_readable(data['memory']['peak']))
    # stdscr.addstr(9,0,"          Max  %s" % bytes_to_human_readable(data['memory']['max']))
    # stdscr.addstr(10,0,"          Total %s" % bytes_to_human_readable(data['memory']['total']))
    char = stdscr.getch()
    if char > -1:
        return False
    return True
