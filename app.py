# Python For All, east-coast-group
# name = Garden-Game
# version = 0.1.0
# description = LPTHW Ex. 45 You Make a Game
# authors = Gillian, Grace, Haja, Lori, Natalie
# url = https://github.com/PythonForAll-east-coast-group/garden-game

from sys import exit
from random import randint
from textwrap import dedent


class Scene(object)

   def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

    class Engine(object):

        def __init__(self, garden_map):
            pass

        def play(self):
            pass

    class DestroyedGarden(Scene):

        quips = [
        "Your garden is destroyed. The animals are formidable foes!",
        "Maybe you should take up dirt farming."
        "Raking is not your strength."
        "Maybe some garden gnomes would help."
        "Better luck next season!"

    ]

        def enter(self):
            pass

    class HerbGarden(Scene):

        def enter(self):
            pass

    class RoseGarden(Scene):

        def enter(self):
            pass

    class StrawberryPatch(Scene):

        def enter(self):
            pass

    class Hammock(Scene):

        def enter(self):
            pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('HerbGarden')
a_game = Engine(a_map)
a_game.play()
