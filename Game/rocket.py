import pygame
from pygame.math import Vector2
from bullet import Bullet
import colors

class Rocket(object):
    """Klasa Rocket - gracz steruje tym obiektem i robi pewpewpew"""
    def __init__(self, game):
        """Konstruktor klasy Rocket z argumentem w jakim oknie ma być on rysowany"""

        # Stowrzenie obiektu z oknem na którym ma być wyświetlony gracz
        self.game = game

        # Zmienne dotyczące inicjowanych właściwości gracza
        self.position = Vector2(self.game.width/2,self.game.height/2)
        self.speed = 2.0
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.trigger = False

        # Dodanie Gracza do listy sprite'ów do wyświetlenia
        self.game.sprites.append(self)

    def __str__(self):
        """Funkcja specjalna zwracająca nazwę obiektu i pozycję"""
        return str(__name__ + " " + str(self.position))

    def add_force(self, force):
        """Funkcja dodająca "siłę" do przyspieszenia"""
        self.acc += force

    def tick(self):
        """Funkcja wykonująca się raz na milisekunde"""
        # Obsługa przycisków
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0,-self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))
        if pressed[pygame.K_SPACE] and self.trigger == False:
            self.shoot()
            self.trigger = True
        if pressed[pygame.K_SPACE] == False:
            self.trigger = False

        # Fizyka ruchu
        self.vel *= 0.5
        self.vel += self.acc
        self.position += self.vel
        self.acc *= 0

    def draw(self):
        """Funkcja rysująca obiekt"""

        # Właściwości "HitBoxa"
        self.rect = pygame.Rect(self.position.x-5,self.position.y-5,15,15)

        # Baza punktów na podstawie których jest tworzony polygon-ROCKET
        points = [Vector2(0,-10),Vector2(5,5),Vector2(0,2),Vector2(-5,5)]

        # Obrót punktów
        angle = self.vel.angle_to(Vector2(0,1))
        points = [p.rotate(angle) for p in points]

        # Naprawa osi Y
        points = [Vector2(p.x,p.y*-1) for p in points]

        # Przekazanie nowej pozycji + wielkość obiektu ( odległości punktów )
        points = [self.position+p*2 for p in points]

        # Rysowanie obiektu
        pygame.draw.polygon(self.game.screen,colors.BLUE,points)

    def shoot(self):
        """Funkcja obsługująca zdarzenie "STRZELANIE" """
        bullet = Bullet(self,self.game)
        self.game.sprites.append(bullet)
        self.game.bullets.append(bullet)
