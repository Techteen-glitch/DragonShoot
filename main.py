from settings import *
from custom_timer import Timer
from sprites import Player, Laser, Meteor, ExplosionAnimation
class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Space shooter")
        init_audio_device()
        self.import_assets()
        self.lasers, self.meteors, self.explosions=[], [], []
        self.player=Player(self.assets['player'], Vector2(WINDOW_WIDTH/2, WINDOW_HEIGHT/2), self.shoot_laser)
        self.meteor_timer=Timer(METEOR_TIMER_DURATION, True, True, self.create_meteor)
        play_music_stream(self.audio['music'])
    def import_assets(self):
        self.assets={
            'player': load_texture(join('..', 'audio', 'spaceship.png')),
            'star': load_texture(join('..', 'audio', 'star.png')),
            'laser': load_texture(join('..', 'audio', 'laser.png')),
            'meteor': load_texture(join('..', 'audio', 'meteor.png')),
            'explosion': [load_texture(join('..', 'audio', 'explosion', f'{i}.png')) for i in range(1, 29)],
            'font': load_font_ex(join('..', 'audio', 'Stormfaze.otf'), FONT_SIZE, ffi.NULL, 0)
        }
        self.audio={
            'laser': load_sound(join('..', 'audio', 'laser.wav')),
            'explosion': load_sound(join('..', 'audio', 'explosion.wav')),
            'music': load_music_stream(join('..', 'audio', 'music.wav'))
        }

        self.star_data=[
            (Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)),
            uniform(0.5, 1.2)
            )for i in range (30)
        ]
    def draw_stars(self):
        for star in self.star_data:
            draw_texture_ex(self.assets['star'], star[0], 0, star[1], WHITE)
    def draw_score(self):
        score=int(get_time())
        text_size=measure_text_ex(self.assets['font'], str(score), FONT_SIZE,0)
        draw_text_ex(self.assets['font'], str(score), Vector2(WINDOW_WIDTH/2-text_size.x/2,100), FONT_SIZE, 0, WHITE)
    def check_collisions(self):
        for laser in self.lasers:
            for meteor in self.meteors:
                if check_collision_circle_rec(meteor.get_center(), meteor.collision_radius, laser.get_rect()):
                    laser.discard, meteor.discard=True, True
                    pos=Vector2(laser.pos.x-laser.size.x/2, laser.pos.y)
                    play_sound(self.audio['explosion'])
                    self.explosions.append(ExplosionAnimation(pos, self.assets['explosion']))

        for meteor in self.meteors:
            if check_collision_circles(self.player.get_center(), self.player.collision_radius, meteor.get_center(), meteor.collision_radius):
                close_window()
    def update(self):
        dt=get_frame_time()
        self.player.update(dt)
        self.meteor_timer.update()
        self.discard_sprites()
        for sprite in self.lasers + self.meteors + self.explosions:
            sprite.update(dt)
        self.check_collisions()
        update_music_stream(self.audio['music'])
    def create_meteor(self):
        self.meteors.append(Meteor(self.assets['meteor']))
    def shoot_laser(self, pos):
        self.lasers.append(Laser(self.assets['laser'], pos))
        play_sound(self.audio['laser'])
    def discard_sprites(self):
        self.lasers=[laser for laser in self.lasers if not laser.discard]
        self.meteors=[meteor for meteor in self.meteors if not meteor.discard]
        self.explosions=[explosion for explosion in self.explosions if not explosion.discard]
    def draw(self):
        begin_drawing()
        clear_background(BG_COLOR)
        self.draw_stars()
        self.draw_score()
        self.player.draw()
        for laser in self.lasers:
            laser.draw()
        for meteor in self.meteors:
            meteor.draw()
        for explosion in self.explosions:
            explosion.draw()
        end_drawing()



    def run(self):
        while not window_should_close():
            game.draw()
            game.update()
        unload_music_stream(self.audio['music'])
        close_audio_device()
        close_window()
if __name__=='__main__':
    game=Game()
    game.run()