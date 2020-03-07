"""
Main function of mc-server-poker.
"""

from lib import *
from time import sleep

def main():
    """
    Main function of mc-server-poker.
    """

    Server.init()
    Email.init()
    oldPlayers = []
    while True:
        status = Server.query()
        time = status['time']
        ping = status['ping']
        players = status['players']
        if players != oldPlayers and len(players) > 0:
            oldPlayers = players
            print("Notifying of", status)
            Email.notify(time, ping, players)
        else:
            print("Ping completed in", ping, "at", time, "with no change")
        sleep(300)

main()