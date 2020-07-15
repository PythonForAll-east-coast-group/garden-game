# Python For All, east-coast-group
# name = Garden-Game
# version = 0.1.0
# description = LPTHW Ex. 45 You Make a Game
# authors = Gillian, Grace, Haja, Lori, Natalie
# url = https://github.com/PythonForAll-east-coast-group/garden-game

from sys import exit
from random import randint
from textwrap import dedent
import weapons_tools


def print_inventory():
    print("You currently have these items in your inventory:")
    for item in weapons_tools.inventory:
        print("- " + item.name)


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, garden_map):
        self.garden_map = garden_map
        pass

    def play(self):
        current_scene = self.garden_map.opening_scene()
        last_scene = self.garden_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.garden_map.next_scene(next_scene_name)

        current_scene.enter()


class DestroyedGarden(Scene):
    quips = [
        "Your garden is destroyed. The animals are formidable foes!",
        "Maybe you should take up dirt farming.",
        "Raking is not your strength.",
        "Maybe some garden gnomes would help.",
        "Better luck next season!",
    ]

    def enter(self):
        print(DestroyedGarden.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class HerbGarden(Scene):

    def enter(self):
        print(dedent("""
            You enter a lovely herb garden bristling with life. 
            You can smell rosemary, lavender, and cilantro.
            Faintly you can smell roses and strawberries, somewhere a bit away from here.
            What would you like to do?
        """))

        print_inventory()

        answer = input("> ")

        if 'rake' in answer:
            print("You rake and tear up all the herbs.")
            return 'destroyed_garden'

        elif 'spray_bottle' in answer:
            print("You")


class RoseGarden(Scene):

    def enter(self):
        pass


class StrawberryPatch(Scene):

    def enter(self):
        print(dedent("""
            You enter the Strawberry Patch. Just yesterday the patch
            was full of ripe berries ready for picking. Your mouth is
            watering as you bend down. But wait, as you move
            the large green leaves aside to look for the berries
            underneath, what you see shocks you. What do you see? 
            """))

        print_inventory()

        action = input("> ")

        if action == "don't see berries":
            print(dedent("""
                You fall to the ground, devastated. The deer decimated your berries.
                """))
            return 'destroyed_garden'

        elif action == "see berries":
            print(dedent("""
                You see more berries than ever! You gather as 
                many as you can hold. It's time for some well-
                deserved rest in the hammock.
                """))

            return 'hammock'
        else:
            print("DOES NOT COMPUTE!")
            return "strawberry_patch"


class Hammock(Scene):

    def enter(self):
        pass


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'destroyed_garden': DestroyedGarden(),
        'hammock': Hammock(),
        'herb_garden': HerbGarden(),
        'rose_garden': RoseGarden(),
        'strawberry_patch': StrawberryPatch(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('herb_garden')
a_game = Engine(a_map)
a_game.play()
