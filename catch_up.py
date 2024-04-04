from pygame import *

#создай окно игры

window = display.set_mode((700, 500))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'),(700, 500))
window.blit(background,(0, 0))



sprut1x = 150
sprut2x = 250
sprut1y = 150
sprut2y = 90

sprut1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprut2 = transform.scale(image.load('sprite2.png'), (100, 100))

clock = time.Clock()
speed = 5

   

gamenotover = True
while gamenotover:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and sprut1y > 5:
        sprut1y -= speed
    if keys_pressed[K_DOWN] and sprut1y < 395:
        sprut1y += speed
    if keys_pressed[K_LEFT] and sprut1x > 5:
        sprut1x -= speed
    if keys_pressed[K_RIGHT] and sprut1x < 595: 
        sprut1x += speed
    if keys_pressed[K_w] and sprut2y > 5:
        sprut2y -= speed
    if keys_pressed[K_s] and sprut2y < 395:
        sprut2y += speed
    if keys_pressed[K_a] and sprut2x > 5:
        sprut2x -= speed
    if keys_pressed[K_d] and sprut2x < 595: 
        sprut2x += speed
    


    window.blit(background,(0, 0))
    window.blit(sprut1, (sprut1x, sprut1y))
    window.blit(sprut2, (sprut2x, sprut2y))
    clock.tick(60)



    for e in event.get():
        if e.type == QUIT:
            gamenotover = False

    display.update()
    


#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»