# making weapons class


class Weapons:
    def __init__(self, start_scene):
        self.scene = start_scene

    def add_inventory(self, name):
        inventory.append(self)
        print(f"You have added the {name} to your inventory.")

    def use(self):
        pass
        # I want the introduction of the scene to queue the user to input "Use Rake"


class Rake(Weapons):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'rake'

    def use(self):
        if super.scene == 'Destroyed_Garden' and super.scene.hasDebris:
            print("""
            You use the rake to sweep away all the debris.
            """)

            super.start_scene.hasDebris = False

    def add_inventory(self):
        super().add_inventory(self.name)


class SprayBottle(Weapons):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'spray bottle'

    def use(self):
        if super.scene == 'rose_garden' and super.scene.hasBees:
            print("You use the spray bottle to scare off the bees!")
            super.scene.hasBees = False
        elif super.scene == 'rose_garden' and not super.scene.hasBees:
            print("You spray the roses to give them something to drink.")

    def add_inventory(self):
        super().add_inventory(self.name)


class SmallTrap(Weapons):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'small trap'

    def use(self):
        if super.scene == 'Herb_Garden' and super.scene.hasMice:
            print("You use the small trap to trap the mice!")
            super.scene.hasMice = False
        elif super.scene == 'Herb_Garden' and not super.scene.hasMice:
            print("You pass through the healthy Herb Garden quietly.")

    def add_inventory(self):
        super().add_inventory(self.name)


class LargeTrap(Weapons):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'large trap'

    def use(self):
        if super.scene == 'Strawberry_Patch' and super.scene.hasDeer:
            print("You use the large trap to trap a deer! This is ambitious.")
            super.scene.hasBees = False
        elif super.scene == 'Strawberry_Path' and not super.scene.hasDeer:
            print(
                "You pass through the strawberry patch and eat a few strawberries along the way.")

    def add_inventory(self):
        super().add_inventory(self.name)


class FenceBoard(Weapons):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'fence board'

    def use(self):
        if super.scene == 'Hammock' and super.scene.hasSmallTree:
            print(
                "You use the fence board to steady the small tree and tie your hammock.")
            super.scene.hasBees = False
        elif super.scene == 'rose_garden' and not super.scene.hasSmallTree:
            print("You spray the roses to give them something to drink.")
# used a new variable that's not an animal here....definitely check

    def add_inventory(self):
        super().add_inventory(self.name)


class Tools:
    def __init__(self, start_scene):
        pass

    def add_inventory(self, name):
        inventory.append(self)
        print(f"You have added the {name} to your inventory.")

    def use(self):
        pass


class Shovel(Tools):
    def __init__(self, start_scene):
        Tools.__init__(self, start_scene)
        self.name = 'shovel'

    def use(self):
        # hasDebris can be something else -- a variable to determine whether the shovel can be used on something in the scene
        if super.scene == 'rose_garden' and super.scene.hasDebris:
            print("You use the shovel to")
            super.scene.hasBees = False
        # hasRoses can be something else -- a variable to determine whether the spray bottle can be used on something in the scene
        elif super.scene == 'rose_garden' and not super.scene.hasRoses:
            print("You spray the roses to give them something to drink.")

    def add_inventory(self):
        super().add_inventory(self.name)


class Dirt(Tools):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'dirt'

    def use(self):
        pass

    def add_inventory(self):
        super().add_inventory(self.name)


class Broom(Tools):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'broom'

    def use(self):
        pass

    def add_inventory(self):
        super().add_inventory(self.name)


class WaterHose(Tools):
    def __init__(self, start_scene):
        Weapons.__init__(self, start_scene)
        self.name = 'water hose'

    def use(self):
        pass

    def add_inventory(self):
        super().add_inventory(self.name)


inventory = []

if __name__ == "__main__":
    my_weapon = Rake('scene')
    my_weapon.add_inventory()
    anotha_weapon = SprayBottle('scene')
    anotha_weapon.add_inventory()
