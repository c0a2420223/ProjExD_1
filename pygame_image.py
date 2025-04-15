import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton_img = pg.image.load("fig/3.png") #練習1
    koukaton_img = pg.transform.flip(koukaton_img,True,False) #練習2
    bg_hanten_img=pg.transform.flip(bg_img,True,False) #練習8
    kk_rct=koukaton_img.get_rect()
    kk_rct.center=300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(+1,0)
        x=tmr%3200
        screen.blit(bg_img, [-x, 0]) #練習6
        screen.blit(bg_hanten_img, [-x+1600,0]) #練習7
        
        screen.blit(bg_img,[-x+3200,0])
        
        screen.blit(koukaton_img,kk_rct)
        pg.display.update()
        
        
        tmr += 1        
        clock.tick(200) #練習4
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()