from ursina import *
import subprocess

app = Ursina()

camera.fov = 100
camera.y = 10
camera.x = 15

twinkle_path = r'C:\Users\Potato\Documents\KODINGAN\Backup Laptop(3)\KODINGAN SEMESTER 4\TUGAS AKHIR\twinkle_little_star.py'

def start_twinkle():
    menu_music.stop()
    print(f"Starting {twinkle_path}")
    try:
        process = subprocess.Popen(['python', twinkle_path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stdout:
            print(f"STDOUT: {stdout}")
        if stderr:
            print(f"STDERR: {stderr}")
    except Exception as e:
        print(f"Error: {e}")
    

def play_outro():
    outro.start()

def play_outro_music():
    outro_music.play()

def menu_music_play():
    menu_music.play()

def toggle_fullscreen():
    window.fullscreen = not window.fullscreen

def tutorial():
    tutor.enabled=True
    back_button.enabled=True
    tutor_button.enabled =True
    main_menu1.enabled = False
    main_menu2.enabled = False
    main_menu3.enabled = False
    
def songL():
    song_list.enabled=True
    back_button.enabled=True
    main_menu1.enabled = False
    main_menu2.enabled = False
    main_menu3.enabled = False

main_menu1 = Button(text='Mulai Permainan', position=(0, 0.1), color=color.black, scale=(.5, .1), enabled=False, on_click= songL)
main_menu2 = Button(text='Tutorial', position=(0, 0), color=color.black, scale=(.5, .1), enabled=False, on_click=tutorial)
main_menu3 = Button(text='Menghentikan Permainan', position=(0, -.1), color=color.black, scale=(.5, .1), enabled=False,on_click=quit)

song_list = Button(text='Twinkle Twinkle Little Star', position=(0, 0), color=color.black, scale=(.5, .1), enabled=False, on_click=start_twinkle)

def menu():
    menu_music.play
    main_menu1.enabled = True
    main_menu2.enabled = True
    main_menu3.enabled = True
    tutor.enabled=False
    back_button.enabled=False
    tutor_button.enabled =False
    song_list.enabled = False

def quit():
    quit()


tutor = Text(color=color.white,text="Guitar Hero merupakan game Rthym yang dimana cara bermainnya yaitu menekan tombol yang ada dan harus berirama\n\n sesuai dengan tombol yang ada dilayar \n\n\n Tekan Tombol A untuk yang pertama \n\n Tekan Tombol S untuk Yang Kedua \n\n Tekan Tombol L untuk Tombol Yang Ketiga \n\n Tekan Tombol ; Untuk Tombol Yang Keempat \n\n Tekan Tombol SPACE Untuk TOmbol Yang Kelima\n\n\n\n\n Jika anda mnekan tombol dengan benar maka darah akan bertambah\n\n\n dan jika anda salah menekan tombol maka darah anda akan berkurang\n\n\nTekan Tombol F Untuk FULLSCREEN!!!",position=(-.8,0.4),enabled=False )
tutor_button = Entity(model='quad', texture='assets/tutor.png',scale=(20,10),position=(28,15),enabled=False )
back_button = Button(text='Kembali ke Menu', position=(0, -0.4), color=color.black, scale=(.5, .1), enabled=False, on_click=menu)


intro = Animation('assets/INTRO', scale=(60, 32), x=15, y=10, z=3, loop=False)
outro_music = Audio('assets/Electric.mp3', autoplay=False)
outro = Animation('assets/OUTRO', scale=(60, 32), x=15, y=10, z=3, loop=False, autoplay=False)

menu_music = Audio('assets/menu_ost.mp3', autoplay=False,loop=False)
background = Entity(model='quad', texture='assets/menu.png', scale=(60, 32), x=13, y=10, color=color.rgba(255, 255, 255, 0.5),enabled=False)

def bg():
    background.enabled=True

invoke(bg, delay=10)

invoke(play_outro, delay=5)
invoke(play_outro_music, delay=5)

invoke(menu_music_play, delay=10)

invoke(menu, delay=10)

def update():
    pass

def input(key):
    if key == 'f':
        toggle_fullscreen()

    if key == 'escape':
        quit()

app.run()
