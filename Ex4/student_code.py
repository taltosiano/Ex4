"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import random
import sys
from math import sqrt
from types import SimpleNamespace

from MyGame import MyGame
from Pokemon import Pokemon
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from src.Edge import Edge
from src.GeoLocation import GeoLocation
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph
from src.Node import Node

epsilon = 0.0000001
# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

# def load_pokemons(self, file: str) -> list:
#     pokemonLoad = json.loads(file)
#     pokemoneList = []
#     for poke in pokemonLoad["Pokemons"]:
#         value = poke['value']
#         type = poke['type']
#         posSplit = poke['pos'].split(",")
#         pos = (float(posSplit[0]), float(posSplit[1]), float(posSplit[2]))
#         self.pokemons.append(Pokemon(value, type, pos))
#         return pokemoneList


# def load_agents(file: str) -> list:
#     agentLoad = json.loads(file)
#     agentsList = []
#     for age in agentLoad['Agents']:
#         data = age['Agent']
#         posData = str(data['pos'])
#         posSplit = posData.split(',')
#         pos = (float(posSplit[0]), float(posSplit[1]), float(posSplit[2]))
#         agentsList.append(age.agent(int(data['id']), float(data['value']), int(data['src']), int(data['dest']),
#                                     float(data['speed']), pos))
#         return agentsList


# st = client.get_pokemons()
# pokemons = load_pokemons(st)
pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))
print(pokemons)
graph_json = client.get_graph()

FONT = pygame.font.SysFont('Arial', 20, bold=True)
# load the json string into SimpleNamespace Object
# graph = json.loads(
#     graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

graphAlgo = GraphAlgo()
# graphAlgo.load_from_json(graph_json)
graphAlgo.load_from_json("data/A1")
graph = graphAlgo.get_graph()
print(graph)

for n in graph.get_all_v().keys():
    node = graph.get_node(n)
    print(node.get_id())
    # pos = node.get_pos().split(',')
    # x, y, z = pos[0], pos[1], pos[2]

    # node.set_pos(SimpleNamespace(x=float(x), y=float(y)))

# get data proportions
# min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
# min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
# max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
# max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y


min_x = sys.float_info.max
min_y = sys.float_info.max
max_x = sys.float_info.min
max_y = sys.float_info.min

for n in graph.get_all_v().keys():
    node = graph.get_node(n)
    x = float(node.get_pos()[0])
    y = float(node.get_pos()[1])
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


radius = 15

client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# this commnad starts the server - the game is running now
client.start()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""


def theNextNode(point: tuple) -> int:
    mini = 0
    for next in graph.get_all_v.keys():
        getNode = graph.get_node(next)
        d = sqrt(pow(getNode[0] - point[0], 2) + pow(getNode[1] - point[1]))
        if d < mini:
            mini = getNode.get_id()

    return mini


while client.is_running() == 'true':
    pokemons = json.loads(client.get_pokemons(),
                          object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for n in graph.get_all_v().keys():
        node = graph.get_node(n)
        x = my_scale(node.get_pos()[0], x=True)
        y = my_scale(node.get_pos()[1], y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    for n in graph.get_all_v().values():
        nodeV = graph.get_node(n)
        # draw edges
        for e in graph.all_out_edges_of_node(nodeV.get_id()).values():
            src_x = 0
            src_y = 0
            dest_x = 0
            dest_y = 0
            # find the edge nodes
            if nodeV.get_id() == e.get_src:
                src = nodeV
                src_x = my_scale(src.get_pos()[0], x=True)
                src_y = my_scale(src.get_pos()[1], y=True)
            if nodeV.get_id() == e.get_dst:
                dest = nodeV
                dest_x = my_scale(dest.get_pos()[0], x=True)
                dest_y = my_scale(dest.get_pos()[1], y=True)
            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        pygame.draw.circle(screen, Color(122, 61, 23),
                           (int(agent.pos.x), int(agent.pos.y)), 10)
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked
    # in the same way).
    for p in pokemons:
        pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)
    print(client.get_agents())
    game = MyGame
    newPoke = game.load_pokemons((client.get_pokemons()))
    # choose next edge
    for agent in agents:
        if agent.get_dest() == -1:
            next_node = theNextNode(agent.get_pos())
            for p in pokemons:
                next_node = theNextNode(tuple(p.pos))
                if (game.theClosePokemon(agent.get_pos(), graph.get_node(next_node).get_pos(), tuple(p.pos))) < epsilon:
                    client.choose_next_edge(
                        '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
            client.choose_next_edge(
                '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())

    client.move()
# game over:
