from ursina import *
import random


app = Ursina()

def reset():
    green_bar.scale_x = 30
    B.y = 1
    update_score(0)

class Healt_Bar(Entity):
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

Button1 = Entity(model='quad', texture='vignette', color=color.rgb(255, 255, 255), scale=(4,3), x=-5, y=20, collider='box')
Button2 = Entity(model='quad', texture='vignette', color=color.rgb(255, 255, 255), scale=(4,3), x=-5, y=16, collider='box')
Button3 = Entity(model='quad', texture='vignette', color=color.rgb(255, 255, 255), scale=(4,3), x=-5, y=12, collider='box')
Button4 = Entity(model='quad', texture='vignette', color=color.rgb(255, 255, 255), scale=(4,3), x=-5, y=8, collider='box')
Button5 = Entity(model='quad', texture='vignette', color=color.rgb(255, 255, 255), scale=(4,3), x=-5, y=4, collider='box')
Button_back = Entity(model='quad', texture='vignette', color=color.rgba(0,255,255,0.3), scale=(3,19), x=-5, y=11.8, collider='box')


class ObsButton(Entity):
    def __init__(self, x_pos, y_pos):
        super().__init__(
            model='quad',
            texture='vignette',
            color=color.rgb(255, 255, 255),
            scale=2,
            x=x_pos,
            y=y_pos,
            collider='box'
        )

obs_buttons1 = [ObsButton(40, 20), ObsButton(40, 20), ObsButton(70, 20), ObsButton(200, 20), ObsButton(250, 20), ObsButton(315, 20)]
obs_buttons2 = [ObsButton(40, 16), ObsButton(90, 16), ObsButton(160, 16), ObsButton(210, 16), ObsButton(250, 16), ObsButton(320, 16)]
obs_buttons3 = [ObsButton(40, 12), ObsButton(100, 12), ObsButton(170, 12), ObsButton(220, 12), ObsButton(270, 12), ObsButton(340, 12)]
obs_buttons4 = [ObsButton(40, 8), ObsButton(52, 8), ObsButton(100, 8), ObsButton(65, 8), ObsButton(280, 8), ObsButton(350, 8)]
obs_buttons5 = [ObsButton(40, 4), ObsButton(70, 4), ObsButton(140, 4), ObsButton(190, 4), ObsButton(240, 4), ObsButton(290, 4), ObsButton(360, 4)]

current_index1 = 0
current_index2 = 0
current_index3 = 0
current_index4 = 0
current_index5 = 0

bad_note_list =[
    Audio ('assets\Bad_note1.wav', autoplay=False),
    Audio ('assets\Bad_note2.wav', autoplay=False),
    Audio ('assets\Bad_note3.wav', autoplay=False),
    Audio ('assets\Bad_note4.wav', autoplay=False),
    Audio ('assets\Bad_note5.wav', autoplay=False),
]

score = 0

full_bar = Healt_Bar(22, 0, 255, 0, 0, length=30)
green_bar = Healt_Bar(22, -.01, 0, 255, 0, length=30)

def stop_music():
    music.stop()

def play_music():
    music.play()

musicintro = Audio('assets\intro.mp3')
music = Audio('assets\slow_ride.mp3', autoplay=False)
invoke(play_music, delay=musicintro.length)
invoke(stop_music, delay=38)

fret = Entity(model='quad', texture='assets\Fret_slow_ride', scale=(60.5, 21),x=60,y=12, z=2)
fret1 = Entity(model='quad', texture='assets\Fret_slow_ride', scale=(60.5, 21),x=120,y=12, z=2)

fret_up = Entity(model='quad', texture='vignette', color=color.white, scale=(62,.5), x=-5,y=21.5)
fret_up1 = Entity(model='quad', texture='vignette', color=color.white, scale=(62,.5), x=54,y=21.5)

fret_down = Entity(model='quad', texture='vignette', color=color.white, scale=(62,.5), x=-5,y=2)
fret_down1 = Entity(model='quad', texture='vignette', color=color.white, scale=(62,.5), x=54,y=2)

background = Entity(model='quad', texture='assets\Background_slow_ride', scale=(60, 32),x=13,y=10, z=3,color=color.rgba(255, 255, 255, 0.5))



B = Button(color=color.rgb(0, 0, 0), scale=(.25, .1), text='ULANG LAGI??', y=1)
B.on_click = reset

score_text = Text(text=f'Score: {score}', position=(-0.2, -0.3), color=color.white, scale=5)

def update_score(points):
    global score
    score += points
    score_text.text = f'Score: {score}'

def toggle_fullscreen():
    window.fullscreen = not window.fullscreen
    

def update():
    global current_index1, current_index2, current_index3, current_index4, current_index5

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
    
    if fret_up.x < -40 :
        fret_up.x = 80
    
    if fret_up1.x < -40 :
        fret_up1.x = 80

    if fret_down.x < -40 :
        fret_down.x = 80
    
    if fret_down1.x < -40 :
        fret_down1.x = 80


    Button1.color = color.rgb(0, 255, 0)
    Button2.color = color.rgb(255, 0, 0)
    Button3.color = color.rgb(255,255,0)
    Button4.color = color.rgb(0, 0, 255)
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
        Button1.color = color.blue
        if Button1.intersects(obs_buttons1[current_index1]).hit:
            Button1.color = color.yellow  
            current_index1 += 1 
            update_score(50)
            if current_index1 >= len(obs_buttons1):
                current_index1 = 0

    if held_keys['s']:
        Button2.color = color.blue
        if Button2.intersects(obs_buttons2[current_index2]).hit:
            Button2.color = color.yellow  
            current_index2 += 1 
            update_score(50)
            if current_index2 >= len(obs_buttons2):
                current_index2 = 0

    if held_keys["l"]:
        Button3.color = color.blue
        if Button3.intersects(obs_buttons3[current_index3]).hit:
            Button3.color = color.yellow  
            current_index3 += 1 
            update_score(50)
            if current_index3 >= len(obs_buttons3):
                current_index3 = 0

    if held_keys[';']:
        Button4.color = color.blue
        if Button4.intersects(obs_buttons4[current_index4]).hit:
            Button4.color = color.yellow  
            current_index4 += 1 
            update_score(50)
            if current_index4 >= len(obs_buttons4):
                current_index4 = 0

    if held_keys['space']:
        Button5.color = color.blue
        if Button5.intersects(obs_buttons5[current_index5]).hit:
            Button5.color = color.yellow  
            current_index5 += 1 
            update_score(50)
            if current_index5 >= len(obs_buttons5):
                current_index5 = 0

def input(key):
    if key == 'f':
        toggle_fullscreen()
    if key == 'escape':
        quit()


    if key == "a" and Button1.intersects(obs_buttons1[current_index1]).hit:
        green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
    if key == "s" and Button2.intersects(obs_buttons2[current_index2]).hit:
        green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
    if key == "l" and Button3.intersects(obs_buttons3[current_index3]).hit:
        green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
    if key == ";" and Button4.intersects(obs_buttons4[current_index4]).hit:
        green_bar.scale_x = min(30, green_bar.scale_x + 0.5)
    if key == "space" and Button5.intersects(obs_buttons5[current_index5]).hit:
        green_bar.scale_x = min(30, green_bar.scale_x + 0.5)

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


app.run()
