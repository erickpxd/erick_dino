import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, BIG_BG, MP3, PARALAX1,PARALAX2
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.text_utils import set_print_text
pygame.init()
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 15
        self.score = 0
        self.high_score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 555
        self.x_pos_paralax = 0
        self.y_pos_paralax = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.big_bg = BIG_BG

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                pygame.mixer.music.play(-1)
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.score = 0
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        if self.score % 100 == 0:
            self.game_speed += 2

    def draw(self):
        self.clock.tick(FPS)
        self.screen.blit(self.big_bg,(0,0))  # '#FFFFFF'
        self.draw_paralax()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_paralax(self):
        image_width = PARALAX2.get_width()
        self.screen.blit(PARALAX2, (self.x_pos_paralax, self.y_pos_paralax))
        self.screen.blit(PARALAX2, (image_width + self.x_pos_paralax, self.y_pos_paralax))
        if self.x_pos_paralax <= -image_width:
            self.screen.blit(PARALAX2, (image_width + self.x_pos_paralax, self.y_pos_paralax))
            self.x_pos_paralax = 0
        x = 0.1
        self.x_pos_paralax -= (2 - x)

    def draw_score(self):
            set_print_text(f"High score: {self.high_score - 1} | Score: {self.score}",self.screen,font_color=(255, 255, 255),pos_x_center=900,pos_y_center=50)

    def draw_power_up_time(self):
            if self.player.has_power_up:
                time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 1)
                if time_to_show >= 0:
                    set_print_text(
                        f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                        self.screen,
                        font_color=(255, 255, 255),
                        font_size=22,
                        pos_x_center=180,
                        pos_y_center=50
                    )
                else :
                    self.player.has_power_up = False
                    self.player.type = DEFAULT_TYPE

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:  # Tela de inicio
            set_print_text("Press any key to start",self.screen,)
        else:  # Tela de restart
            set_print_text("Press any key to restart", self.screen, pos_x_center= half_screen_width + 20, pos_y_center=half_screen_height - 20)
            set_print_text(f"High score: {self.high_score -1} | Score: {self.score -1}", self.screen, pos_x_center= 570, pos_y_center=half_screen_height + 40)
            set_print_text(f"Deaths: {self.death_count}",self.screen, pos_x_center= 570, pos_y_center=half_screen_height + 60)
            self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))

        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()