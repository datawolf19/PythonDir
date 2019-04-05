class Scene:
    
    def enter(self):
        pass

class Engine:

    def __init__(self, scene_map):
        pass
    
    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):
    counter = 0
    def enter(self):
        # Opening scene, hero wakes up after an explosion.
        if counter == 0:
            print("You are in the Central Corridor. You have escaped your cell.\n\
                now you must escape the ship.")
            print("Ahead of you stands a large, ferocious Gothon. What do you do?")
            print("1.) Punch him.")
            print("2.) Sneak by him.")
            print("3.) Tell a joke.")
            wrong_input = 0 
            while True:
                action = input("> ")

                if int(action) in [1,2,3] and wrong_input==0:
                    break
                elif wrong_input==0:
                    print("You only get one chance...don't screw this up.")
                    wrong_input+=1
                else:
                    

            action = input("> ")

        
        counter+=1 

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map:

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play() 