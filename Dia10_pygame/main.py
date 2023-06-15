import pygame
import random
import math
from pygame import mixer

pygame.init()

pantalla = pygame.display.set_mode((800,600))

#titulo e icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("nave.png")
pygame.display.set_icon(icono)

#imagen de fondo
fondo = pygame.image.load("galaxia.jpg")


#agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#Variables del Jugador
limite = 460
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 100
jugador_y = 520
jugador_x_cambio = 0

#puntaje
puntaje = 0
fuente = pygame.font.Font('DePixelBreit.ttf', 32)
texto_x = 10
texto_y = 10


#funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))


#texto final del juego
fuente_final =  pygame.font.Font('DePixelBreit.ttf', 64)

#funcion para el texto final
def texto_final():
    mi_fuente_final = fuente_final.render("Juego terminado", True, (255, 0 , 0))
    pantalla.blit(mi_fuente_final, (60, 200))
#Variables del Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 10
velocidad_enemigo = .8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(e*70)
    enemigo_y.append(0)
    enemigo_x_cambio.append(velocidad_enemigo)
    enemigo_y_cambio.append(32)

# img_enemigo = pygame.image.load("enemigo.png")
# enemigo_x = 0
# enemigo_y = 0
# enemigo_x_cambio = 0.3
# enemigo_y_cambio = 64

#Variables del bala
img_bala = pygame.image.load("laser.jpg")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1.3
bala_visible = False


#funcion de jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))

#funcion de enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x,y))

#funcion de bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 28,y - 25))

#detectar cuando hay colisiones
def hay_colision (x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 50:
        return True
    else:
        return False


se_ejecuta = True
while se_ejecuta:
    # #rgb de la pantalle
    # pantalla.fill((205, 144 , 228))
    #cargar imagen de fondo
    pantalla.blit(fondo, (0,0))
    for evento in pygame.event.get():
        #evento para cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #evento para presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5

            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        #evento para soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar ubicación Juegador
    jugador_x += jugador_x_cambio
    #mantener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #modificar ubicación Enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] > limite:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]
        #mantener dentro de bordes Enmigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = velocidad_enemigo
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -velocidad_enemigo
            enemigo_y[e] += enemigo_y_cambio[e]
        #colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = 0
            enemigo_y[e] = 0

        enemigo(enemigo_x[e], enemigo_y[e], e)


    #movimiento bala
    if bala_y <= -64:
        bala_visible = False
        bala_y = 500

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio




    jugador(jugador_x, jugador_y)

    #mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    #actualizar
    pygame.display.update()