import random
from math import sqrt

from Agent import Agent
from Pokemon import Pokemon
from student_code import client, WIDTH, HEIGHT, scale, screen, min_x, max_x, min_y, max_y
from types import SimpleNamespace

import json
from pygame import gfxdraw
import pygame
from pygame import *

epsilon = 0.0000001


class MyGame:

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

    def theClosePokemon(self, src: tuple, dest: tuple, pokemonPos: tuple) -> int:
        m = (dest[1] - src[1]) / (dest[0] - src[0])
        n = src[1] - (m * (src[0]))
        d = abs(((m * (pokemonPos[0])) - pokemonPos[1] + n) / (sqrt(pow(m, 2) + 1)))
        return d

