import pygame, fight, mapview, json



def run(screen, location):
    with open("assets/characters.json", "r") as f:
        data = json.load(f)
    fight.run(screen, location, data['locations'][location.name]['fighter'])
    


class Place():
    def __init__(self, location, characters = []):
        self.location = location
    
