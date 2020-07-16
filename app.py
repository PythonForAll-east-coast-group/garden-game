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
    print("Which item would you like to use?")


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
            print("You rake and tear up all the herbs. Why would you do such a thing?!")
            return 'destroyed_garden'

        elif 'spray bottle' in answer:
            print(
                "You use the spray bottle to give the herbs something to drink. They sparkle in the sunglight.")
            print("You head towards the scent of roses.")
            return 'rose_garden'

        else:
            print("That's not the right tool!")
            return 'herb_garden'


class RoseGarden(Scene):

    def enter(self):
        print(dedent("""
            You enter a rose garden with lots of blooming roses. 
            However there are thorns everywhere on the ground,
            mice running through the plants, and Japanese beetles everywhere!!
        """))

        print_inventory()

        answer = input("> ")

        if 'stones' in answer:
            print(dedent("""
            You try to hit the beetles with stones and end up pelting the roses.
            Who taught you how to aim?
            """))
            return 'destroyed_garden'
        elif 'broom' in answer:
            print(dedent("""
            You move all of the thorns on the ground out of the way. 
            Now you can leave and let the small critters duke it out.
            """))
            return 'strawberry_patch'
        elif 'small trap' in answer:
            print(dedent("""
            You catch some mice with your small trap. If you release them
            away from your gardens maybe they won't come back.
            """))
            return 'strawberry_patch'
        elif 'water hose' in answer:
            print(dedent("""
            You try to force the mice out by soaking them wet. 
            But the power of the hose makes the roses bend and some break.
            """))
            return 'destroyed_garden'
        else:
            print(dedent("""
            That's not the right tool! Try a different one.
            """))
            return 'rose_garden'


class StrawberryPatch(Scene):

    def enter(self):
        print(dedent("""
            You enter the Strawberry Patch. Just yesterday the patch
            was full of ripe berries ready for picking. Your mouth is
            watering as you bend down. But wait, as you move
            the large green leaves aside to look for the berries
            underneath, what you see shocks you. 
            There are hoof prints in the dirt and no berries!
            """))

        print_inventory()

        answer = input("> ")

        if 'rake' in answer:
            print(dedent("""
                You angrily rake away the hoofprints leaving nothing behind.
                You fall to the ground, devastated. The deer decimated your berries.
                """))
            return 'destroyed_garden'

        elif 'shovel' in answer:
            print(dedent("""
                You use the shovel to hold up some of the giant leaves.
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
        print(dedent("""
            You enter a grassy field with two trees and a hammock between them.
            One of the trees is a bit wobbly and you are unsure if the hammock will hold you.
            """))

        print_inventory()

        answer = input("> ")

        if 'fence board' in answer:
            print(dedent("""
            You use the fence board to steady the small tree and tie your hammock.
            You climb in and get ready to watch the sun set after a hard day of gardening.
            """))
            return 'finished'
        else:
            print("Why would you use that on a hammock?")
            return 'hammock'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")


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
