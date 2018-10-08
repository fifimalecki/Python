import pygame
from pygame.math import Vector2
import colors
import random

class Enemy(object):
    """Klasa ENEMY - obiekt który gracz musi zestrzelić"""
    def __init__(self, game):
        """Konstruktor klasy enemy"""

        # Stowrzenie obiektu z oknem na którym ma być wyświetlony gracz
        self.game = game

        # Zmienne dotyczące inicjowanych właściwości przeciwników
        self.position = Vector2(random.randint(10, 700), random.randint(10, 500))
        self.velocityX = random.randint(-self.game.speedOfEnemies, self.game.speedOfEnemies)
        self.velocityY = random.randint(-self.game.speedOfEnemies, self.game.speedOfEnemies)

        # Dodanie obiektu do list
        self.game.enemies.append(self)
        self.game.sprites.append(self)

    def __str__(self):
        """"Funkcja specjalna zwracająca nazwę[numer] i pozycję obiektu"""
        return str(__name__ + "[" + str(len(self.game.enemies)+1) + "] " + str(self.position))

    def tick(self):
        """Funkcja wykonująca się co milisekundę"""

        # Zmiana pozycji
        self.position += Vector2(self.velocityX,self.velocityY)

    def draw(self):
        """Funkcja rysująca obiekt"""

        # Właściwości "HitBoxa"
        self.rect = pygame.Rect(self.position.x-5,self.position.y-5,15,15)

        # Rysownia obiektu
        pygame.draw.rect(self.game.screen,colors.RED,self.rect,0)