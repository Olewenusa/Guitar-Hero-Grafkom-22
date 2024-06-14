from ursina import *
import random

app = Ursina()

class Health_Bar(Entity):
    def __init__(self, y, z, r, g, b, length=10):
        super().__init__()
        self.model = "quad"
        self.scale = (length, 0.5)
        self.color = color.rgb(r, g, b)
        self.y = y
        self.z = z
        self.origin = (-.5, -.5)

camera.fov = 100
camera.y = 10
camera.x = 15

Button1 = Entity(model='quad', texture='vignette', scale=(4, 3), x=-5, y=19.5, collider='box' )
Button2 = Entity(model='quad', texture='vignette', scale=(4, 3), x=-5, y=16, collider='box' )
Button3 = Entity(model='quad', texture='vignette', scale=(4, 3), x=-5, y=12, collider='box' )
Button4 = Entity(model='quad', texture='vignette', scale=(4, 3), x=-5, y=8, collider='box' )
Button5 = Entity(model='quad', texture='vignette', scale=(4, 3), x=-5, y=4, collider='box' )

Button_back = Entity(model='quad', texture='vignette', color=color.rgba(0, 255, 255, 0.3), z=1, scale=(4, 19), x=-6, y=11.8, collider='box' )

class ObsButton(Entity):
    def __init__(self, x_pos, y_pos):
        super().__init__(
            model='circle',
            texture='vignette',
            color=color.rgb(255, 255, 255),
            scale=2,
            x=x_pos,
            y=y_pos,
            collider='box'
        )

obs_buttons1 = [ObsButton(40, 20), ObsButton(60, 20), ObsButton(110, 20), ObsButton(190, 20), ObsButton(230, 20), ObsButton(400, 20)]
obs_buttons2 = [ObsButton(40, 16), ObsButton(90, 16), ObsButton(100, 16), ObsButton(200, 16), ObsButton(240, 16), ObsButton(350, 16)]
obs_buttons3 = [ObsButton(40, 12), ObsButton(100, 12), ObsButton(160, 12), ObsButton(220, 12), ObsButton(250, 12), ObsButton(320, 12)]
obs_buttons4 = [ObsButton(40, 8), ObsButton(80, 8), ObsButton(140, 8), ObsButton(220, 8), ObsButton(250, 8), ObsButton(360, 8)]
obs_buttons5 = [ObsButton(40, 4), ObsButton(70, 4), ObsButton(110, 4), ObsButton(215, 4), ObsButton(290, 4), ObsButton(370, 4), ObsButton(360, 4)]

current_index1 = 0
current_index2 = 0
current_index3 = 0
current_index4 = 0
current_index5 = 0

bad_note_list = [
    Audio('assets/Bad_note1.wav', autoplay=False),
    Audio('assets/Bad_note2.wav', autoplay=False),
    Audio('assets/Bad_note3.wav', autoplay=False),
    Audio('assets/Bad_note4.wav', autoplay=False),
    Audio('assets/Bad_note5.wav', autoplay=False),
]

    

score = 0

full_bar = Health_Bar(22, 0, 255, 0, 0, length=30)
green_bar = Health_Bar(22, -.01, 0, 255, 0, length=18)

def stop_music():
    music.stop()

def play_music():
    music.play()

musicintro = Audio('assets/intro.mp3')
music = Audio('assets/Twinkle_little_star.mp3', autoplay=False)

invoke(play_music, delay=musicintro.length)
invoke(stop_music, delay=38)


fret = Entity(model='quad', texture='assets/Fret_twinkle', scale=(60.5, 21), x=60, y=12, z=2)
fret1 = Entity(model='quad', texture='assets/Fret_twinkle', scale=(60.5, 21), x=120, y=12, z=2)

fret_up = Entity(model='quad', texture='vignette', color=color.white, scale=(62, .5), x=-5, y=21.5)
fret_up1 = Entity(model='quad', texture='vignette', color=color.white, scale=(62, .5), x=54, y=21.5)

fret_down = Entity(model='quad', texture='vignette', color=color.white, scale=(62, .5), x=-5, y=2)
fret_down1 = Entity(model='quad', texture='vignette', color=color.white, scale=(62, .5), x=54, y=2)

background = Entity(model='quad', texture='assets/Background_twinkle', scale=(60, 32), x=13, y=10, z=3, color=color.rgba(255, 255, 255, 0.5) )

score_text = Text(text=f'Score: {score}', position=(-0.2, -0.3), color=color.white, scale=5 )

def update_score(points):
    global score
    score += points
    score_text.text = f'Score: {score}'

def toggle_fullscreen():
    window.fullscreen = not window.fullscreen

def quit_game():
    application.quit()

def resume_game():
    global game_paused
    pause_menu.disable()
    game_paused = False
    if music:
        music.play()

game_paused = False

pause_menu = Entity(parent=camera.ui, enabled=False)
pause_menu_background = Entity(parent=pause_menu, model='quad', color=color.rgba(255, 255, 255, 0.3), scale=(0.6, 0.6), position=(0, 0, -1))
resume_button = Button(parent=pause_menu, text='Resume', scale=(0.3, 0.1), position=(0, 0.1), on_click=resume_game)
quit_button = Button(parent=pause_menu, text='Quit', scale=(0.3, 0.1), position=(0, -0.1), on_click=quit_game)

def update():
    global current_index1, current_index2, current_index3, current_index4, current_index5, game_paused

    if game_paused:
        return

    fret.x -= 20 * time.dt
    fret1.x -= 20 * time.dt
    fret_up.x -= 20 * time.dt
    fret_up1.x -= 20 * time.dt
    fret_down.x -= 20 * time.dt
    fret_down1.x -= 20 * time.dt

    if fret.x < -40:
        fret.x = 80

    if fret1.x < -40:
        fret1.x = 80

    if fret_up.x < -40:
        fret_up.x = 80

    if fret_up1.x < -40:
        fret_up1.x = 80

    if fret_down.x < -40:
        fret_down.x = 80

    if fret_down1.x < -40:
        fret_down1.x = 80

    Button1.color = color.green
    Button2.color = color.red
    Button3.color = color.yellow
    Button4.color = color.blue
    Button5.color = color.orange

    for obj in obs_buttons1:
        obj.x -= 20 * time.dt
    for obj in obs_buttons2:
        obj.x -= 20 * time.dt
    for obj in obs_buttons3:
        obj.x -= 20 * time.dt
    for obj in obs_buttons4:
        obj.x -= 20 * time.dt
    for obj in obs_buttons5:
        obj.x -= 20 * time.dt

    if held_keys['a']:
        Button1.color = color.turquoise
        if Button1.intersects(obs_buttons1[current_index1]).hit:
            current_index1 += 1
            green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
            update_score(50)
            if current_index1 >= len(obs_buttons1):
                current_index1 = 0

    if held_keys['s']:
        Button2.color = color.pink
        if Button2.intersects(obs_buttons2[current_index2]).hit:
            current_index2 += 1
            green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
            update_score(50)
            if current_index2 >= len(obs_buttons2):
                current_index2 = 0

    if held_keys["l"]:
        Button3.color = color.light_gray
        if Button3.intersects(obs_buttons3[current_index3]).hit:
            current_index3 += 1
            green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
            update_score(50)
            if current_index3 >= len(obs_buttons3):
                current_index3 = 0

    if held_keys[';']:
        Button4.color = color.cyan
        if Button4.intersects(obs_buttons4[current_index4]).hit:
            current_index4 += 1
            green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
            update_score(50)
            if current_index4 >= len(obs_buttons4):
                current_index4 = 0

    if held_keys['space']:
        Button5.color = color.violet
        if Button5.intersects(obs_buttons5[current_index5]).hit:
            current_index5 += 1
            green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
            update_score(50)
            if current_index5 >= len(obs_buttons5):
                current_index5 = 0


def input(key):
    global game_paused

    if key == 'p':
        game_paused = not game_paused
        pause_menu.enabled = game_paused
        if game_paused:
            if music:
                music.pause()
        else:
            if music:
                music.play()

    if game_paused:
        return

    if key == "a" and not Button1.intersects(obs_buttons1[current_index1]).hit:
        green_bar.scale_x = max(0, green_bar.scale_x - 1)
        random.choice(bad_note_list).play()
    if key == "s" and not Button2.intersects(obs_buttons2[current_index2]).hit:
        green_bar.scale_x = max(0, green_bar.scale_x - 1)
        random.choice(bad_note_list).play()
    if key == "l" and not Button3.intersects(obs_buttons3[current_index3]).hit:
        green_bar.scale_x = max(0, green_bar.scale_x - 1)
        random.choice(bad_note_list).play()
    if key == ";" and not Button4.intersects(obs_buttons4[current_index4]).hit:
        green_bar.scale_x = max(0, green_bar.scale_x - 1)
        random.choice(bad_note_list).play()
    if key == "space" and not Button5.intersects(obs_buttons5[current_index5]).hit:
        green_bar.scale_x = max(0, green_bar.scale_x - 1)
        random.choice(bad_note_list).play()

    if key == 'f':
        toggle_fullscreen()


def stop_all():
    Button1.disable()
    Button2.disable()
    Button3.disable()
    Button4.disable()
    Button5.disable()
    Button_back.disable()

    for obj in obs_buttons1 + obs_buttons2 + obs_buttons3 + obs_buttons4 + obs_buttons5:
        obj.disable()
        fret.disable()
        fret1.disable()
        fret_up.disable()
        fret_up1.disable()
        fret_down.disable()
        fret_down1.disable()
        music.stop()
        score_text.position = (-.23, .29)

invoke(stop_all, delay=38)

app.run()
