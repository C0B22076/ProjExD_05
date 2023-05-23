import pygame as pg
import sys
import time
import random

white = (255,255,255)
black = (0,0,0)
green = (0,150,0)
red = (255,0,0)
blue = (0,0,255)
light_blue = (147,251,253)
width = 1600
hight = 900

def check_bound(area: pg.Rect, obj: pg.Rect) -> tuple[bool, bool]:
    
    yoko, tate = True, True
    if obj.left < area.left or area.right < obj.right:  # 横方向のはみ出し判定
        yoko = False
    if obj.top < area.top or area.bottom < obj.bottom:  # 縦方向のはみ出し判定
        tate = False
    return yoko, tate

class playerlect_1:

    _delta = {
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
    }
    

    def __init__(self, xy: tuple[int,int]): 
        self._img = pg.transform.rotozoom(pg.image.load(f"ex05/fig/redpad.png"),0, 2.0)
        self._rct = self._img.get_rect()
        self._rct.center = xy


    def update(self,key_lst: list[bool], screen: pg.Surface):
        for k,mv in __class__._delta.items():
            if key_lst[k]:
                self._rct.move_ip(mv)
        if check_bound(screen.get_rect(), self._rct) != (True, True):
            for k, mv in __class__._delta.items():
                if key_lst[k]:
                    self._rct.move_ip(-mv[0], -mv[1])
        screen.blit(self._img,self._rct)


def main():
    pg.display.set_caption("Air-hockey")
    screen = pg.display.set_mode((1600,900))
    pl1 = playerlect_1((width-300,hight/2))
    clock = pg.time.Clock()

    pk_img = pg.Surface((20,20))
    pg.draw.circle(pk_img, (255, 0, 0), (10, 10), 10)
    pk_img.set_colorkey((0, 0, 0))
    pk_rct = pk_img.get_rect()
    x, y = random.randint(0, 1600), random.randint(0, 900)
    pk_rct.center = x, y
    vx, vy = +1, +1



    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


        screen.fill((0,0,0))
        pg.draw.line(screen, blue,(0,0), (screen.get_width()/2 - 5,0) ,20)
        pg.draw.line(screen, blue,(0,screen.get_height()), (screen.get_width()/2 - 5,screen.get_height()) ,20)
        pg.draw.line(screen, red, (screen.get_width()/2+5,0), (screen.get_width() ,0) ,20)
        pg.draw.line(screen, red, (screen.get_width()/2 + 5,screen.get_height()) , (screen.get_width(),screen.get_height()) ,20)
        pg.draw.line(screen,white,(width/2,0),(width/2,hight),5)
            
        yoko, tate = check_bound(screen.get_rect(), pk_rct)
        if not yoko:  # 横方向にはみ出ていたら
            vx *= -1
        if not tate:  # 縦方向にはみ出ていたら
            vy *= -1
        
        # ボールとの衝突判定
        
        if pl1._rct.colliderect(pk_rct):
            vx *= -1
            vy *= -1
            

        pk_rct.move_ip(vx, vy)
        screen.blit(pk_img, pk_rct)
    
        key_lst = pg.key.get_pressed()
        pl1.update(key_lst,screen)
        


        pg.display.update()
        clock.tick(1000)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()