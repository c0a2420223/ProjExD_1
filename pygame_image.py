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
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0]) #練習6
        screen.blit(bg_hanten_img, [1600,0]) #練習7
        screen.blit(koukaton_img,[300,200]) #練習2
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習4
    


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()