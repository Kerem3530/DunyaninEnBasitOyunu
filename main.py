import pgzrun

hiz = 10
mod = "menü"
WIDTH = 1000
HEIGHT = 700
TITLE = "Dünyanın En Kolay Oyunu"
FPS = 30

Oyuncu = Actor("oyuncu", (500, 150))
Arkaplan = Actor("arkaplan")
Hikaye = Actor("hikaye", (500, 250))
Oyna = Actor("oyna", (500, 320))
s2Engel1 = Rect((80, 270), (760, 30))
s2Engel2 = Rect((180, 360), (760, 30))
s1Engel = Rect((80, 270), (760, 30))
s3Engel1 = Rect((80, 270), (760, 30))
s3Engel2 = Rect((180, 370), (760, 30))
s3Engel3 = Rect((80, 470), (760, 30))
s4Engel1 = Rect((80, 270), (760, 30))
s4Engel2 = Rect((180, 370), (760, 30))
s4Engel3 = Rect((80, 470), (760, 30))
s5Engel1 = Rect((80, 270), (760, 30))
s5Engel2 = Rect((180, 370), (760, 30))
s5Engel3 = Rect((80, 470), (760, 30))
GeriDon = Actor("geridön", (500, 650))
Hedef = Actor("hedef", (500, 500))
Seviye1 = Actor("seviyebir", (200, 350))
Seviye2 = Actor("seviyeiki", (350, 350))
Seviye3 = Actor("seviyeüç", (500, 350))
Seviye4 = Actor("seviyedört", (650, 350))
Seviye5 = Actor("seviyebeş", (800, 350))

s2Engeller = [s2Engel1, s2Engel2]
s3Engeller = [s3Engel1, s3Engel2, s3Engel3]
s4Engeller = [s4Engel1, s4Engel2, s4Engel3]
s5Engeller = [s5Engel1, s5Engel2, s5Engel3]

def reset_player():
    Oyuncu.topleft = (500, 150)

def draw():
    screen.clear()
    
    if mod == "hikaye":
        Arkaplan.draw()
        GeriDon.draw()
        screen.draw.text("Hikaye Mikaye Yoh \n Ben Anlamam", fontsize=50, color="white", topleft=(450, 120))

    elif mod == "menü":
        Arkaplan.draw()
        Hikaye.draw()
        Oyna.draw()
        screen.draw.text("Dünyanın En Kolay Oyunu", fontsize=50, color="white", topleft=(280, 120))

    elif mod == "s1":
        Arkaplan.draw()
        Oyuncu.draw()
        GeriDon.draw()
        Hedef.draw()
        screen.draw.filled_rect(s1Engel, 'red')

    elif mod == "s2":
        Arkaplan.draw()
        Oyuncu.draw()
        GeriDon.draw()
        Hedef.topleft = (500, 520)
        Hedef.draw()
        for i in s2Engeller:
            screen.draw.filled_rect(i, "red")

    elif mod == "s3":
        Arkaplan.draw()
        Oyuncu.draw()
        GeriDon.draw()
        Hedef.topleft = (500, 520)
        Hedef.draw()
        for i in s3Engeller:
            screen.draw.filled_rect(i, "red")

    elif mod == "s4":
        Arkaplan.draw()
        Oyuncu.draw()
        GeriDon.draw()
        Hedef.topleft = (500, 520)
        Hedef.draw()
        for i in s4Engeller:
            screen.draw.filled_rect(i, "red")

    elif mod == "s5":
        Arkaplan.draw()
        Oyuncu.draw()
        GeriDon.draw()
        Hedef.topleft = (500, 520)
        Hedef.draw()
        for i in s5Engeller:
            screen.draw.filled_rect(i, "red")

    elif mod == "seviyeler":
        Arkaplan.draw()
        GeriDon.draw()
        Seviye1.draw()
        Seviye2.draw()
        Seviye3.draw()
        Seviye4.draw()
        Seviye5.draw()

def update():
    global mod
    global Oyuncu
    global hiz

    if keyboard.up or keyboard.w:
        if Oyuncu.y > 140:
            Oyuncu.y -= hiz

    if keyboard.down or keyboard.s:
        if Oyuncu.y < 550:
            Oyuncu.y += hiz

    if keyboard.right or keyboard.d:
        if Oyuncu.x < 910:
            Oyuncu.x += hiz

    if keyboard.left or keyboard.a:
        if Oyuncu.x > 90:
            Oyuncu.x -= hiz

    if mod == "s1":
        if Oyuncu.colliderect(s1Engel):
            reset_player()
        
        if Oyuncu.colliderect(Hedef):
            mod = "seviyeler"
            reset_player()

    if mod == "s2":
        if Oyuncu.collidelist(s2Engeller) != -1:
            reset_player()
        
        if Oyuncu.colliderect(Hedef):
            mod = "seviyeler"
            reset_player()

    if mod == "s3":
        if Oyuncu.collidelist(s3Engeller) != -1:
            reset_player()
        
        if Oyuncu.colliderect(Hedef):
            mod = "seviyeler"
            reset_player()

    if mod == "s4":
        if Oyuncu.collidelist(s4Engeller) != -1:
            reset_player()

        if s4Engel1.x < 160:
            s4Engel1.x += 3
        else:
            s4Engel1.x = 80

        if Oyuncu.colliderect(Hedef):
            mod = "seviyeler"
            reset_player()

    if mod == "s5":
        if Oyuncu.collidelist(s5Engeller) != -1:
            reset_player()

        if s5Engel1.x < 160:
            s5Engel1.x += 3
        else:
            s5Engel1.x = 80

        if s5Engel3.x < 160:
            s5Engel3.x += 3
        else:
            s5Engel3.x = 80

        if s5Engel2.x > 80:
            s5Engel2.x -= 3
        else:
            s5Engel2.x = 180

        if Oyuncu.colliderect(Hedef):
            mod = "seviyeler"
            reset_player()

def on_mouse_down(pos):
    global mod
    if mod == "menü":

        if Oyna.collidepoint(pos):
            mod = "seviyeler"

        elif Hikaye.collidepoint(pos):
            mod = "hikaye"

    elif GeriDon.collidepoint(pos):
        mod = "menü"

    elif mod == "seviyeler":
        if Seviye1.collidepoint(pos):
            mod = "s1"
            reset_player()

        if Seviye2.collidepoint(pos):
            mod = "s2"
            reset_player()

        if Seviye3.collidepoint(pos):
            mod = "s3"
            reset_player()

        if Seviye4.collidepoint(pos):
            mod = "s4"
            reset_player()

        if Seviye5.collidepoint(pos):
            mod = "s5"
            reset_player()

pgzrun.go()
