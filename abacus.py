background_image_filename = 'frame.gif'

import pygame

from pygame.locals import *
from pygame import mixer
from sys import exit
import os
pygame.init()
screen = pygame.display.set_mode((208, 205), 0, 32)
pygame.display.set_caption("PyAbacus!")
background = pygame.image.load(background_image_filename).convert()
font = pygame.font.SysFont("arial", 12);
BOARD = []
bead_list = []

def init_board():
    for a in range(len(BOARD)):
        pygame.draw.rect(screen, (100,100,100), BOARD[a])
        pygame.image.load("bead.gif")
        if a > 21 and a < 44:
            screen.blit(pygame.image.load("nobead.gif"), (BOARD[a].topleft, BOARD[a].bottomright))
            bead_list.append(0)
        else:
            screen.blit(pygame.image.load("bead.gif"), (BOARD[a].topleft, BOARD[a].bottomright))
            bead_list.append(1)

def draw_rect():
    for y in range(11):
        for x in range(11):
            if y < 3:
                BOARD.append(pygame.Rect(x*17+10,y*17+11,17,17))
            elif y > 4:
                BOARD.append(pygame.Rect(x*17+10,y*17-9,17,17))

def display_board():
    for a in range(len(BOARD)):
        pygame.draw.rect(screen, (100,100,100), BOARD[a])
        pygame.image.load("bead.gif")
        if bead_list[a] == 0:
            screen.blit(pygame.image.load("nobead.gif"), (BOARD[a].topleft, BOARD[a].bottomright))
        elif bead_list[a] == 1:
            screen.blit(pygame.image.load("bead.gif"), (BOARD[a].topleft, BOARD[a].bottomright))
    
def sub(a):
    if bead_list[a] == 1:
        sub(a-11)
    else:
        bead_list[a] = 1
def add(a):
    if bead_list[a] == 1:
        add(a+11)
    else:
        bead_list[a] = 1
def get_count(a):
    if bead_list[a] == 1:
        return get_count(a+11) + 1
    else:
        return 0
def get_total():
    new = ""
    new2 = ""
    new3 = ""
    event_text = []
    event_text2 = []
    event_text3 = []
    for a in range(22,33,1):
        if bead_list[a] == 1:
            event_text.append("5")
            if bead_list[a-11] == 1:
                event_text2.append("5")
            else:
                event_text2.append("0")
        else:
            event_text.append("0")
            event_text2.append("0")        
    event_text.reverse()
    event_text2.reverse()
    for a in range(33,44,1):
        if bead_list[a] == 1:
            event_text3.append(get_count(a))
        else:
            event_text3.append("0")
    event_text3.reverse()
    for i in xrange(len(event_text)):
        new += event_text.pop()
        new2 += event_text2.pop()
        new3 += str(event_text3.pop())
    text = font.render(str(int(new) + int(new2) + int(new3)), True, (255, 255, 255), (0,0,0))
    screen.blit(text, (5,190))

draw_rect()
screen.blit(background, (0,0))                
init_board()
pygame.display.update()
mixer.init(44100)
clickit = mixer.Sound("goclickb.wav")
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            os._exit(1)

        if event.type == MOUSEBUTTONDOWN:
            screen.fill((0,0,0))
            for a in range(len(BOARD)):
                if BOARD[a].collidepoint(pygame.mouse.get_pos()) and bead_list[a] == 1:
                    x, y = pygame.mouse.get_pos()

                    bead_list[a] = 0
                    if a > 10 and a < 23 and (bead_list[a-11] == 0):
                        sub(a-11)
                    elif a > 21 and a < 33:
                        sub(a-11)
                    elif a < 33:
                        add(a+11)
                    elif a > 32 and  a < 44:
                        add(a+11)
                    elif a < 88 and bead_list[a+11] == 0:
                        add(a+11)
                    elif a < 77 and bead_list[a+22] == 0:
                        add(a+11)
                    elif a < 66 and bead_list[a+33] == 0:
                        add(a+11)   
                    elif a < 55 and bead_list[a+44] == 0:
                        add(a+11)   
                    else:
                        sub(a-11)
		    clickit.play()
		    get_total()
	    screen.blit(background, (0,0))                
	    display_board()
	    pygame.display.update()