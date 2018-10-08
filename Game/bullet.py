import pygame
from pygame.math import Vector2
import math
import colors

class Bullet(object):
    """Klasa Bullet - nabój wygenerowany po naciśnięciu spacji, lecący z pozycji gracza"""
    def __init__(self,player,game):
        """Konstruktor klasy Bullet"""

        # Stworzenie obiektów
        # GAME - okna na którym ma być wyświetlany obiekt
        # PLAYER - obiekt z którym powiązany jest nabój
        self.game = game
        self.player = player

        # Zmienne dotyczące inicjowanych właściwości naboju
        self.position = player.position
        self.x = self.position.x
        self.y = self.position.y
        self.speed = 3.0
        self.angle = math.radians(self.player.vel.angle_to(Vector2(0,1))) - math.pi / 2

        # Dodanie powstałego naboju do listy istniejących obecnie naboi
        self.game.bullets.append(self)

    def __str__(self):
        """Funkcja specjalna zwracająca nazwę obiektu i jego pozycję"""
        return str(__name__ + " " + str(self.position))

    def draw(self):
        """Funkcja rysująca obiekt"""

        # Właściwości "HitBoxa"
        self.rect = pygame.Rect(self.x,self.y-2,5,5)

        # Rysowanie obiektu
        pygame.draw.rect(self.game.screen,colors.GREEN,self.rect)

    def tick(self):
        """Funkcja wykonująca się raz na milisekundę"""

        # Zmiana położenia pod odpowiednim kątem
        self.x += 2*self.speed*math.cos(self.angle)
        self.y -= 2*self.speed*math.sin(self.angle)

        # Zdażenie jeśli nabój wyleci poza okno
        if self.x > self.game.width or self.x < 0 or self.y > self.game.height or self.y < 0:
            self.game.sprites.remove(self)
            self.game.bullets.remove(self)