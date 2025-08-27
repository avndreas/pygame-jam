import pygame, fight, mapview, json



def run(screen, location):
    with open("assets/characters.json", "r") as f:
        data = json.load(f)
    if not location.cleared:
        for item in data['locations']:
            if item["name"] == location.name and "fighter" in item:
                print("Starting fight with", item["fighter"])
                fight.run(screen, location, item["fighter"])
    print("Cleared ", location.name)
    location.cleared = True



class Place():
    def __init__(self, location, characters = []):
        self.location = location
    
