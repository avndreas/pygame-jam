import pygame, fight, mapview


def run(screen, location):
    print("Placeview ran, now running fight...")
    fight.run(screen, location)


class Place():
    def __init__(self, location):
        self.location = location
    
