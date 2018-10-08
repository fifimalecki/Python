import pygame, sys
from rocket import Rocket
from enemy import Enemy
import colors

class Game(object):
    """Klasa Game - klasa odpowiadająca za wyświetlanie obiektów"""
    def __init__(self):
        """Konstruktor klasy Game"""

        # Podstawowe właściwości okna
        self.tps_max = 100.0
        self.width = 800
        self.height = 600
        self.running = True
        self.menuFlag = True

        # Inicjalizacja ekranu, czasu i czcionki
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.myfont = pygame.font.SysFont("Arial", 15)

        # Inicjalizacja list
        self.sprites = []
        self.bullets = []
        self.enemies = []

        # Stworzenie gracza
        self.player = Rocket(self)
        self.score = 0
        self.level = 1
        self.loose = False

        # Właściwości dotyczące wrogów
        self.numberOfEnemies = 10
        self.speedOfEnemies = 1

        # Główna pętla gry
        while True:
            # Pętla tworząca wrogów
            for i in range(self.numberOfEnemies):
                self.enemy = Enemy(self)
            self.running = True
            self.loose = False

            # Pętla rundy
            while self.running:
                # Obsługa zdarzeń (wyjście z gry)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)

                # Obsługa czasu
                self.tps_delta += self.tps_clock.tick() / 1000.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick()
                    self.tps_delta -= 1 / self.tps_max

                # Rysowanie
                self.screen.fill((0,0,0))
                if self.menuFlag == True:
                    self.menu()
                    pygame.display.flip()
                else:
                    self.draw()
                    pygame.display.flip()

                    # Obsługa zdarzenia - wyjście gracza po za ramy okna
                    if self.player.position.x < 0:
                        self.player.position.x = self.width
                    if self.player.position.x > self.width:
                        self.player.position.x = 0
                    if self.player.position.y < 0:
                        self.player.position.y = self.height
                    if self.player.position.y > self.height:
                        self.player.position.y = 0

                    # Obsługa zdarzenia - wyjście wrogów po za ramy okna
                    for enemy in self.enemies:
                        if enemy.position.x < 0:
                            enemy.position.x = self.width
                        if enemy.position.x > self.width:
                            enemy.position.x = 0
                        if enemy.position.y < 0:
                            enemy.position.y = self.height
                        if enemy.position.y > self.height:
                            enemy.position.y = 0

                    # Obsługa zdarzenia - trafienie nabojem we wroga
                    hits = []
                    for bullet in self.bullets:
                        hits = pygame.sprite.spritecollide(bullet,self.enemies,False)
                    if hits:
                        self.enemies.remove(hits[0])
                        self.sprites.remove(hits[0])
                        self.score += 10

                    # Obsługa zdarzenia - najechanie wroga na gracza
                    hitsInPlayer = pygame.sprite.spritecollide(self.player, self.enemies, False)
                    if hitsInPlayer:
                        self.loose = True
                        self.menuFlag = True
                        self.running = False
                        self.sprites = []
                        self.bullets = []
                        self.enemies = []
                        self.score = 0
                        self.level = 1
                        self.numberOfEnemies = 10
                        self.speedOfEnemies = 1
                        self.player.position = pygame.math.Vector2(self.width/2,self.height/2)
                        self.sprites.append(self.player)

                    # Obsługa zdarzenia - pokonanie wszystkich wrogów
                    if len(self.enemies) == 0 and self.loose is False:
                        self.numberOfEnemies += 5
                        self.level += 1
                        self.running = False

    def __str__(self):
        """Funkcja spejcjalna wyświetlająca właściwości okna"""
        return str(str(self.width) + " " + str(self.height))

    def menu(self):
        """Funkcja tworząca menu"""
        title = self.myfont.render("STRZELANIE RAKIETĄ DO CZERWONYCH KWADRATÓW", 1, colors.YELLOW)
        self.screen.blit(title, (self.width/2 - 160, self.height/2 - 140))
        steering = self.myfont.render("STEROWANIE: W,A,S,D - ruch   Spacja - strzał", 1, colors.YELLOW)
        self.screen.blit(steering, (self.width/2 - 125, self.height/2 - 100))
        startGame = self.myfont.render("Klinkij [ENTER], aby rozpocząć", 1, colors.YELLOW)
        self.screen.blit(startGame, (self.width/2 - 80, self.height/2 + 200))

        # Rozpoczęcie gry
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
                self.menuFlag = False

    def tick(self):
        """Funkcja wykonująca się co milisekundę"""
        for sprite in self.sprites:
            sprite.tick()

    def draw(self):
        """Funkcja rysująca"""
        # Napis wyświetający pozostałych wrogów
        enemiesLeft = self.myfont.render("Zostało: "+str(len(self.enemies)), 1, colors.YELLOW)
        self.screen.blit(enemiesLeft,(10,10))

        # Napis wyświetlający ilość zdobytych punktów
        score = self.myfont.render("Punkty: "+str(self.score),1,colors.YELLOW)
        self.screen.blit(score,(10,30))

        # Napis wyświetlający aktualny poziom
        level = self.myfont.render("Poziom: "+str(self.level),1,colors.YELLOW)
        self.screen.blit(level,(10,50))

        # Pętla rysująca obiekty
        try:
            for sprite in self.sprites:
                sprite.draw()
        except:
            print("Nie udało się wyrysować obiektów")
            sys.exit(0)

if __name__ == "__main__":
    Game()