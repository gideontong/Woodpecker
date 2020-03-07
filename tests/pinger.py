"""
Some old, example code
"""

from mcstatus import MinecraftServer
import click
from json import dumps as json_dumps

# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
server = MinecraftServer.lookup("example.com")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
status = server.status()
print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

# 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
# It is included in a 'status' call, but is exposed separate if you do not require the additional info.
latency = server.ping()
print("The server replied in {0} ms".format(latency))

# 'query' has to be enabled in a servers' server.properties file.
# It may give more information than a ping, such as a full player list or mod information.

# from mcstatus.scripts.mcstatus import cli, json

# cli("ucsd.pocketmc.net")

data = {'online': False}
# Build data with responses and quit on exception
try:
    ping_res = server.ping()
    data['online'] = True
    data['ping'] = ping_res

    # status_res = server.status(retries=1)
    status_res = status
    data['version'] = status_res.version.name
    data['protocol'] = status_res.version.protocol
    data['motd'] = status_res.description
    data['player_count'] = status_res.players.online
    data['player_max'] = status_res.players.max
    data['players'] = []
    if status_res.players.sample is not None:
        data['players'] = [{'name': player.name, 'id': player.id} for player in status_res.players.sample]

    query_res = server.query(retries=1)
    data['host_ip'] = query_res.raw['hostip']
    data['host_port'] = query_res.raw['hostport']
    data['map'] = query_res.map
    data['plugins'] = query_res.software.plugins
except:
    pass
click.echo(json_dumps(data))
# query = json()
# print(query)
