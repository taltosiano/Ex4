import random

from Agent import Agent
from Pokemon import Pokemon
from student_code import client, WIDTH, HEIGHT, scale, screen, min_x, max_x, min_y, max_y
from types import SimpleNamespace
import GraphAlgo
import DiGraph

import json
from pygame import gfxdraw
import pygame
from pygame import *


class MyGame:

    def __init__(self):
        pass

    def load_pokemons(self, file: str) -> list:
        pokemonLoad = json.loads(file)
        pokemoneList = []
        for poke in pokemonLoad["Pokemons"]:
            value = poke['value']
            ty = poke['type']
            posSplit = poke['pos'].split(",")
            pos = (float(posSplit[0]), float(posSplit[1]), float(posSplit[2]))
            pokemoneList.append(Pokemon(value, ty, pos))

        return pokemoneList

    def load_agents(self, file: str) -> list:
        agentLoad = json.loads(file)
        agentsList = []
        for age in agentLoad['Agents']:
            data = age['Agent']
            posData = str(data['pos'])
            posSplit = posData.split(',')
            pos = (float(posSplit[0]), float(posSplit[1]), float(posSplit[2]))
            agentsList.append(age.agent(int(data['id']), float(data['value']), int(data['src']), int(data['dest']),
                                        float(data['speed']), pos))
        return agentsList

    def find_pokemones_locate(self, pokemon: Pokemon ) :
        pok_x = pokemon.get_pos(0)
        pok_y = pokemon.get_pos(1)
        for src in self.graphAlgo.graph.src_dst.keys():
            for dst in self.graphAlgo.graph.src_dst.get(src).keys():
                src_x = self.graphAlgo.graph.Nodes.get(src).pos[0]
                src_y = self.graphAlgo.graph.Nodes.get(src).pos[1]

                dst_x = self.graphAlgo.graph.Nodes.get(dst).pos[0]
                dst_y = self.graphAlgo.graph.Nodes.get(dst).pos[1]

                if abs(distance(src_x, src_y, poke_x, poke_y) + distance(poke_x, poke_y, dst_x, dst_y)
                       - distance(src_x, src_y, dst_x, dst_y)) < sys.float_info.epsilon:
                    if pokemon.type < 0:
                        return dst, src

                    return src, dst