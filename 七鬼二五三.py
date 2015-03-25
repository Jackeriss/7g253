#!/usr/bin/env python
# -*- coding: gbk -*-

# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Time of release:2014/4/12

"""
    Author:  Jackeriss	
    Email:  i@jackeriss.com
    Site:  http://www.jackeriss.com
    Blog:  http://blog.csdn.net/jackeriss
"""

import os, pygame, random, webbrowser
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode([1360,690])
pygame.display.set_caption("七鬼二五三")
screen.fill([0,70,130])
pygame.mixer.init()
win_sound=pygame.mixer.Sound("Sounds/win.wav")
lose_sound=pygame.mixer.Sound("Sounds/lose.wav")
cp_sound=pygame.mixer.Sound("Sounds/cp.ogg")
click1=pygame.mixer.Sound("Sounds/click1.wav")
click2=pygame.mixer.Sound("Sounds/click2.wav")
pass_by=pygame.mixer.Sound("Sounds/pass_by.wav")
perror=pygame.mixer.Sound("Sounds/Error.ogg")
buyao1=pygame.mixer.Sound("Sounds/buyao1.wav")
buyao2=pygame.mixer.Sound("Sounds/buyao2.wav")
buyao3=pygame.mixer.Sound("Sounds/buyao3.wav")
buyao4=pygame.mixer.Sound("Sounds/buyao4.wav")
wbuyao1=pygame.mixer.Sound("Sounds/wbuyao1.wav")
wbuyao2=pygame.mixer.Sound("Sounds/wbuyao2.wav")
wbuyao3=pygame.mixer.Sound("Sounds/wbuyao3.wav")
wbuyao4=pygame.mixer.Sound("Sounds/wbuyao4.wav")
dani1=pygame.mixer.Sound("Sounds/dani1.wav")
dani2=pygame.mixer.Sound("Sounds/dani2.wav")
dani3=pygame.mixer.Sound("Sounds/dani3.wav")
wdani1=pygame.mixer.Sound("Sounds/wdani1.wav")
wdani2=pygame.mixer.Sound("Sounds/wdani2.wav")
wdani3=pygame.mixer.Sound("Sounds/wdani3.wav")
pchat1=pygame.mixer.Sound("Sounds/Fight.ogg")
pchat2=pygame.mixer.Sound("Sounds/Sorry.ogg")
pchat3=pygame.mixer.Sound("Sounds/Good.ogg")
pchat4=pygame.mixer.Sound("Sounds/Greetings.ogg")
pchat5=pygame.mixer.Sound("Sounds/Hurry.ogg")
pchat6=pygame.mixer.Sound("Sounds/Thanks.ogg")
pchat7=pygame.mixer.Sound("Sounds/Oops.ogg")
cchat1=pygame.mixer.Sound("Sounds/wFight.ogg")
cchat2=pygame.mixer.Sound("Sounds/wSorry.ogg")
cchat3=pygame.mixer.Sound("Sounds/wGood.ogg")
cchat4=pygame.mixer.Sound("Sounds/wGreetings.ogg")
cchat5=pygame.mixer.Sound("Sounds/wHurry.ogg")
cchat6=pygame.mixer.Sound("Sounds/wThanks.ogg")
cchat7=pygame.mixer.Sound("Sounds/wOops.ogg")
pthink1=pygame.mixer.Sound("Sounds/Thinking1.ogg")
pthink2=pygame.mixer.Sound("Sounds/Thinking2.ogg")
pthink3=pygame.mixer.Sound("Sounds/Thinking3.ogg")
buyao=[buyao1,buyao2,buyao3,buyao4]
wbuyao=[wbuyao1,wbuyao2,wbuyao3,wbuyao4]
dani=[dani1,dani2,dani3]
wdani=[wdani1,wdani2,wdani3]
p_hand_cover=pygame.image.load("Images/p_hand_cover.png")
c_hand_cover=pygame.image.load("Images/c_hand_cover.png")
p_chat_cover1=pygame.image.load("Images/p_chat_cover1.png")
p_chat_cover2=pygame.image.load("Images/p_chat_cover2.png")
choice_cover=pygame.image.load("Images/choice_cover.png")
p_kou_cover=pygame.image.load("Images/p_kou_cover.png")
c_kou_cover=pygame.image.load("Images/c_kou_cover.png")
firework_cover1_0=pygame.image.load("Images/firework_cover1_0.png")
firework_cover1_1=pygame.image.load("Images/firework_cover1_1.png")
firework_cover1_2=pygame.image.load("Images/firework_cover1_2.png")
firework_cover1_3=pygame.image.load("Images/firework_cover1_3.png")
firework_cover1_4=pygame.image.load("Images/firework_cover1_4.png")
firework_cover1_5=pygame.image.load("Images/firework_cover1_5.png")
firework_cover1_6=pygame.image.load("Images/firework_cover1_6.png")
firework_cover1_7=pygame.image.load("Images/firework_cover1_7.png")
firework_cover2_0=pygame.image.load("Images/firework_cover2_0.png")
firework_cover2_1=pygame.image.load("Images/firework_cover2_1.png")
firework_cover2_2=pygame.image.load("Images/firework_cover2_2.png")
firework_cover2_3=pygame.image.load("Images/firework_cover2_3.png")
firework_cover2_4=pygame.image.load("Images/firework_cover2_4.png")
firework_cover2_5=pygame.image.load("Images/firework_cover2_5.png")
firework_cover2_6=pygame.image.load("Images/firework_cover2_6.png")
firework_cover2_7=pygame.image.load("Images/firework_cover2_7.png")
firework_cover3_0=pygame.image.load("Images/firework_cover3_0.png")
firework_cover3_1=pygame.image.load("Images/firework_cover3_1.png")
firework_cover3_2=pygame.image.load("Images/firework_cover3_2.png")
firework_cover3_3=pygame.image.load("Images/firework_cover3_3.png")
firework_cover3_4=pygame.image.load("Images/firework_cover3_4.png")
firework_cover3_5=pygame.image.load("Images/firework_cover3_5.png")
firework_cover3_6=pygame.image.load("Images/firework_cover3_6.png")
firework_cover3_7=pygame.image.load("Images/firework_cover3_7.png")
firework_cover4_0=pygame.image.load("Images/firework_cover4_0.png")
firework_cover4_1=pygame.image.load("Images/firework_cover4_1.png")
firework_cover4_2=pygame.image.load("Images/firework_cover4_2.png")
firework_cover4_3=pygame.image.load("Images/firework_cover4_3.png")
firework_cover4_4=pygame.image.load("Images/firework_cover4_4.png")
firework_cover4_5=pygame.image.load("Images/firework_cover4_5.png")
firework_cover4_6=pygame.image.load("Images/firework_cover4_6.png")
firework_cover4_7=pygame.image.load("Images/firework_cover4_7.png")
firework_cover1=[firework_cover1_1,firework_cover1_2,firework_cover1_3,firework_cover1_4,firework_cover1_5,firework_cover1_6,firework_cover1_7]
firework_cover2=[firework_cover2_1,firework_cover2_2,firework_cover2_3,firework_cover2_4,firework_cover2_5,firework_cover2_6,firework_cover2_7]
firework_cover3=[firework_cover3_1,firework_cover3_2,firework_cover3_3,firework_cover3_4,firework_cover3_5,firework_cover3_6,firework_cover3_7]
firework_cover4=[firework_cover4_1,firework_cover4_2,firework_cover4_3,firework_cover4_4,firework_cover4_5,firework_cover4_6,firework_cover4_7]
background=pygame.image.load("Images/background.png")
dark=pygame.image.load("Images/dark.png")
cp=pygame.image.load("Images/cp.png")
kp=pygame.image.load("Images/kp.png")
Tishi=pygame.image.load("Images/Tishi.png")
Pjq=pygame.image.load("Images/Pjq.png")
Cjq=pygame.image.load("Images/Cjq.png")
Pgx=pygame.image.load("Images/Pgx.png")
Cgx=pygame.image.load("Images/Cgx.png")
pj=pygame.image.load("Images/pj.png")
firework_L1=pygame.image.load("Images/firework_L1.png")
firework_L2=pygame.image.load("Images/firework_L2.png")
firework_L3=pygame.image.load("Images/firework_L3.png")
firework_L4=pygame.image.load("Images/firework_L4.png")
firework_L5=pygame.image.load("Images/firework_L5.png")
firework_L6=pygame.image.load("Images/firework_L6.png")
firework_L7=pygame.image.load("Images/firework_L7.png")
firework_L8=pygame.image.load("Images/firework_L8.png")
firework_L9=pygame.image.load("Images/firework_L9.png")
firework_L10=pygame.image.load("Images/firework_L10.png")
firework_L11=pygame.image.load("Images/firework_L11.png")
firework_L12=pygame.image.load("Images/firework_L12.png")
firework_L13=pygame.image.load("Images/firework_L13.png")
firework_L14=pygame.image.load("Images/firework_L14.png")
firework_L15=pygame.image.load("Images/firework_L15.png")
firework_L16=pygame.image.load("Images/firework_L16.png")
firework_L17=pygame.image.load("Images/firework_L17.png")
firework_L18=pygame.image.load("Images/firework_L18.png")
firework_L19=pygame.image.load("Images/firework_L19.png")
firework_L20=pygame.image.load("Images/firework_L20.png")
firework_L21=pygame.image.load("Images/firework_L21.png")
firework_R1=pygame.image.load("Images/firework_R1.png")
firework_R2=pygame.image.load("Images/firework_R2.png")
firework_R3=pygame.image.load("Images/firework_R3.png")
firework_R4=pygame.image.load("Images/firework_R4.png")
firework_R5=pygame.image.load("Images/firework_R5.png")
firework_R6=pygame.image.load("Images/firework_R6.png")
firework_R7=pygame.image.load("Images/firework_R7.png")
firework_R8=pygame.image.load("Images/firework_R8.png")
firework_R9=pygame.image.load("Images/firework_R9.png")
firework_R10=pygame.image.load("Images/firework_R10.png")
firework_R11=pygame.image.load("Images/firework_R11.png")
firework_R12=pygame.image.load("Images/firework_R12.png")
firework_R13=pygame.image.load("Images/firework_R13.png")
firework_R14=pygame.image.load("Images/firework_R14.png")
firework_R15=pygame.image.load("Images/firework_R15.png")
firework_R16=pygame.image.load("Images/firework_R16.png")
firework_R17=pygame.image.load("Images/firework_R17.png")
firework_R18=pygame.image.load("Images/firework_R18.png")
firework_R19=pygame.image.load("Images/firework_R19.png")
firework_R20=pygame.image.load("Images/firework_R20.png")
firework_R21=pygame.image.load("Images/firework_R21.png")
firework_L=[firework_L1,firework_L2,firework_L3,firework_L4,firework_L5,firework_L6,firework_L7,firework_L8,firework_L9,firework_L10,firework_L11,firework_L12,firework_L13,firework_L14,firework_L15,firework_L16,firework_L17,firework_L18,firework_L19,firework_L20,firework_L21]
firework_R=[firework_R1,firework_R2,firework_R3,firework_R4,firework_R5,firework_R6,firework_R7,firework_R8,firework_R9,firework_R10,firework_R11,firework_R12,firework_R13,firework_R14,firework_R15,firework_R16,firework_R17,firework_R18,firework_R19,firework_R20,firework_R21]
win_image=pygame.image.load("Images/win.png")
lose_image0=pygame.image.load("Images/lose0.png")
lose_image1=pygame.image.load("Images/lose1.png")
lose_image2=pygame.image.load("Images/lose2.png")
lose_image3=pygame.image.load("Images/lose3.png")
lose_image4=pygame.image.load("Images/lose4.png")
lose_image5=pygame.image.load("Images/lose5.png")
win_continue=pygame.image.load("Images/win_continue.png")
win_continue2=pygame.image.load("Images/win_continue2.png")
lose_continue=pygame.image.load("Images/lose_continue.png")
lose_continue2=pygame.image.load("Images/lose_continue2.png")
chat=pygame.image.load("Images/chat.png")
chat0=pygame.image.load("Images/chat0.png")
choice0=pygame.image.load("Images/choice0.png")
choice1=pygame.image.load("Images/choice1.png")
choice2=pygame.image.load("Images/choice2.png")
choice3=pygame.image.load("Images/choice3.png")
choice4=pygame.image.load("Images/choice4.png")
choice5=pygame.image.load("Images/choice5.png")
choice6=pygame.image.load("Images/choice6.png")
choice=[choice1,choice2,choice3,choice4,choice5,choice6]
setting_button=pygame.image.load("Images/setting_button.png")
setting_button2=pygame.image.load("Images/setting_button2.png")
setting1=pygame.image.load("Images/setting1.png")
setting2=pygame.image.load("Images/setting2.png")
setting3=pygame.image.load("Images/setting3.png")
control_1=pygame.image.load("Images/control_1.png")
control_2=pygame.image.load("Images/control_2.png")
manu1=pygame.image.load("Images/manu1.png")
manu2=pygame.image.load("Images/manu2.png")
manu3=pygame.image.load("Images/manu3.png")
manu4=pygame.image.load("Images/manu4.png")
manu_A=pygame.image.load("Images/manu_A.png")
manu_B=pygame.image.load("Images/manu_B.png")
manu_C=pygame.image.load("Images/manu_C.png")
manu_D=pygame.image.load("Images/manu_D.png")
web=pygame.image.load("Images/web.png")
left2=pygame.image.load("Images/left2.png")
right2=pygame.image.load("Images/right2.png")
help_b=pygame.image.load("Images/help_b.png")
about_b=pygame.image.load("Images/about_b.png")
continue_b=pygame.image.load("Images/continue_b.png")
help1=pygame.image.load("Images/help1.png")
help2=pygame.image.load("Images/help2.png")
help3=pygame.image.load("Images/help3.png")
help4=pygame.image.load("Images/help4.png")
help5=pygame.image.load("Images/help5.png")
about1=pygame.image.load("Images/about1.png")
about2=pygame.image.load("Images/about2.png")
about3=pygame.image.load("Images/about3.png")
about4=pygame.image.load("Images/about4.png")
about5=pygame.image.load("Images/about5.png")
pchat_image1_1=pygame.image.load("Images/Fight1.png")
pchat_image1_2=pygame.image.load("Images/Fight2.png")
pchat_image1_3=pygame.image.load("Images/Fight3.png")
pchat_image1_4=pygame.image.load("Images/Fight4.png")
pchat_image1_5=pygame.image.load("Images/Fight5.png")
pchat_image2_1=pygame.image.load("Images/Sorry1.png")
pchat_image2_2=pygame.image.load("Images/Sorry2.png")
pchat_image2_3=pygame.image.load("Images/Sorry3.png")
pchat_image2_4=pygame.image.load("Images/Sorry4.png")
pchat_image2_5=pygame.image.load("Images/Sorry5.png")
pchat_image3_1=pygame.image.load("Images/Good1.png")
pchat_image3_2=pygame.image.load("Images/Good2.png")
pchat_image3_3=pygame.image.load("Images/Good3.png")
pchat_image3_4=pygame.image.load("Images/Good4.png")
pchat_image3_5=pygame.image.load("Images/Good5.png")
pchat_image4_1=pygame.image.load("Images/Greetings1.png")
pchat_image4_2=pygame.image.load("Images/Greetings2.png")
pchat_image4_3=pygame.image.load("Images/Greetings3.png")
pchat_image4_4=pygame.image.load("Images/Greetings4.png")
pchat_image4_5=pygame.image.load("Images/Greetings5.png")
pchat_image5_1=pygame.image.load("Images/Hurry1.png")
pchat_image5_2=pygame.image.load("Images/Hurry2.png")
pchat_image5_3=pygame.image.load("Images/Hurry3.png")
pchat_image5_4=pygame.image.load("Images/Hurry4.png")
pchat_image5_5=pygame.image.load("Images/Hurry5.png")
pchat_image6_1=pygame.image.load("Images/Thanks1.png")
pchat_image6_2=pygame.image.load("Images/Thanks2.png")
pchat_image6_3=pygame.image.load("Images/Thanks3.png")
pchat_image6_4=pygame.image.load("Images/Thanks4.png")
pchat_image6_5=pygame.image.load("Images/Thanks5.png")
pchat_image7_1=pygame.image.load("Images/Oops1.png")
pchat_image7_2=pygame.image.load("Images/Oops2.png")
pchat_image7_3=pygame.image.load("Images/Oops3.png")
pchat_image7_4=pygame.image.load("Images/Oops4.png")
pchat_image7_5=pygame.image.load("Images/Oops5.png")
cchat_image1_1=pygame.image.load("Images/wFight1.png")
cchat_image1_2=pygame.image.load("Images/wFight2.png")
cchat_image1_3=pygame.image.load("Images/wFight3.png")
cchat_image1_4=pygame.image.load("Images/wFight4.png")
cchat_image1_5=pygame.image.load("Images/wFight5.png")
cchat_image2_1=pygame.image.load("Images/wSorry1.png")
cchat_image2_2=pygame.image.load("Images/wSorry2.png")
cchat_image2_3=pygame.image.load("Images/wSorry3.png")
cchat_image2_4=pygame.image.load("Images/wSorry4.png")
cchat_image2_5=pygame.image.load("Images/wSorry5.png")
cchat_image3_1=pygame.image.load("Images/wGood1.png")
cchat_image3_2=pygame.image.load("Images/wGood2.png")
cchat_image3_3=pygame.image.load("Images/wGood3.png")
cchat_image3_4=pygame.image.load("Images/wGood4.png")
cchat_image3_5=pygame.image.load("Images/wGood5.png")
cchat_image4_1=pygame.image.load("Images/wGreetings1.png")
cchat_image4_2=pygame.image.load("Images/wGreetings2.png")
cchat_image4_3=pygame.image.load("Images/wGreetings3.png")
cchat_image4_4=pygame.image.load("Images/wGreetings4.png")
cchat_image4_5=pygame.image.load("Images/wGreetings5.png")
cchat_image5_1=pygame.image.load("Images/wHurry1.png")
cchat_image5_2=pygame.image.load("Images/wHurry2.png")
cchat_image5_3=pygame.image.load("Images/wHurry3.png")
cchat_image5_4=pygame.image.load("Images/wHurry4.png")
cchat_image5_5=pygame.image.load("Images/wHurry5.png")
cchat_image6_1=pygame.image.load("Images/wThanks1.png")
cchat_image6_2=pygame.image.load("Images/wThanks2.png")
cchat_image6_3=pygame.image.load("Images/wThanks3.png")
cchat_image6_4=pygame.image.load("Images/wThanks4.png")
cchat_image6_5=pygame.image.load("Images/wThanks5.png")
cchat_image7_1=pygame.image.load("Images/wOops1.png")
cchat_image7_2=pygame.image.load("Images/wOops2.png")
cchat_image7_3=pygame.image.load("Images/wOops3.png")
cchat_image7_4=pygame.image.load("Images/wOops4.png")
cchat_image7_5=pygame.image.load("Images/wOops5.png")
back_left_1=pygame.image.load("Images/left_1.png")
back_left_2=pygame.image.load("Images/left_2.png")
back_left_3=pygame.image.load("Images/left_3.png")
back_right_1=pygame.image.load("Images/right_1.png")
back_right_2=pygame.image.load("Images/right_2.png")
back_right_3=pygame.image.load("Images/right_3.png")
back_both_1=pygame.image.load("Images/both_1.png")
back_both_2=pygame.image.load("Images/both_2.png")
back_both_3=pygame.image.load("Images/both_3.png")
back0=pygame.image.load("Images/back0.png")
back1=pygame.image.load("Images/back1.png")
back2=pygame.image.load("Images/back2.png")
back3=pygame.image.load("Images/back3.png")
back4=pygame.image.load("Images/back4.png")
back5=pygame.image.load("Images/back5.png")
back6=pygame.image.load("Images/back6.png")
set0_1=pygame.image.load("Images/set0_1.png")
set0_2=pygame.image.load("Images/set0_2.png")
set0_3=pygame.image.load("Images/set0_3.png")
set1_1=pygame.image.load("Images/set1_1.png")
set1_2=pygame.image.load("Images/set1_2.png")
set1_3=pygame.image.load("Images/set1_3.png")
set2_1=pygame.image.load("Images/set2_1.png")
set2_2=pygame.image.load("Images/set2_2.png")
set2_3=pygame.image.load("Images/set2_3.png")
set3_1=pygame.image.load("Images/set3_1.png")
set3_2=pygame.image.load("Images/set3_2.png")
set3_3=pygame.image.load("Images/set3_3.png")
set4_1=pygame.image.load("Images/set4_1.png")
set4_2=pygame.image.load("Images/set4_2.png")
set4_3=pygame.image.load("Images/set4_3.png")
set5_1=pygame.image.load("Images/set5_1.png")
set5_2=pygame.image.load("Images/set5_2.png")
set5_3=pygame.image.load("Images/set5_3.png")
set6_1=pygame.image.load("Images/set6_1.png")
set6_2=pygame.image.load("Images/set6_2.png")
set6_3=pygame.image.load("Images/set6_3.png")
pthink_image1_1=pygame.image.load("Images/Thinking1_1.png")
pthink_image1_2=pygame.image.load("Images/Thinking1_2.png")
pthink_image1_3=pygame.image.load("Images/Thinking1_3.png")
pthink_image1_4=pygame.image.load("Images/Thinking1_4.png")
pthink_image1_5=pygame.image.load("Images/Thinking1_5.png")
pthink_image2_1=pygame.image.load("Images/Thinking2_1.png")
pthink_image2_2=pygame.image.load("Images/Thinking2_2.png")
pthink_image2_3=pygame.image.load("Images/Thinking2_3.png")
pthink_image2_4=pygame.image.load("Images/Thinking2_4.png")
pthink_image2_5=pygame.image.load("Images/Thinking2_5.png")
pthink_image3_1=pygame.image.load("Images/Thinking3_1.png")
pthink_image3_2=pygame.image.load("Images/Thinking3_2.png")
pthink_image3_3=pygame.image.load("Images/Thinking3_3.png")
pthink_image3_4=pygame.image.load("Images/Thinking3_4.png")
pthink_image3_5=pygame.image.load("Images/Thinking3_5.png")
back=[back0,back1,back2,back3,back4,back5,back6]
set_back_1=[set0_1,set1_1,set2_1,set3_1,set4_1,set5_1,set6_1]
set_back_2=[set0_2,set1_2,set2_2,set3_2,set4_2,set5_2,set6_2]
set_back_3=[set0_3,set1_3,set2_3,set3_3,set4_3,set5_3,set6_3]
end_sound=[win_sound,lose_sound]
back_gl=pygame.image.load("Images/back_gl.png")
channel1 = pygame.mixer.Channel(1)#p_card&c_card
channel2 = pygame.mixer.Channel(2)#p_chat
channel3 = pygame.mixer.Channel(3)#c_chat
channel4 = pygame.mixer.Channel(4)#Tishi
channel5 = pygame.mixer.Channel(5)#end_sound&button_press
channel6 = pygame.mixer.Channel(6)#p_thinking
channel7 = pygame.mixer.Channel(7)#cp&button_pass

##########################################################################################################################################
#Card Class
##########################################################################################################################################
class Card:
    def __init__(self,card_id):
        self.id=card_id

        if self.id==1:
            self.value=1
            self.image=pygame.image.load("Images/1.png")
            self.sound=pygame.mixer.Sound("Sounds/1.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w1.wav")            
        elif self.id==2:
            self.value=23
            self.image=pygame.image.load("Images/2.png")
            self.sound=pygame.mixer.Sound("Sounds/2.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w2.wav")
        elif self.id==3:
            self.value=19
            self.image=pygame.image.load("Images/3.png")
            self.sound=pygame.mixer.Sound("Sounds/3.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w3.wav")
        elif self.id==4:
            self.value=3
            self.image=pygame.image.load("Images/4.png")
            self.sound=pygame.mixer.Sound("Sounds/4.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w4.wav")
        elif self.id==5:
            self.value=21
            self.image=pygame.image.load("Images/5.png")
            self.sound=pygame.mixer.Sound("Sounds/5.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w5.wav")
        elif self.id==6:
            self.value=5
            self.image=pygame.image.load("Images/6.png")
            self.sound=pygame.mixer.Sound("Sounds/6.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w6.wav")
        elif self.id==7:
            self.value=27
            self.image=pygame.image.load("Images/7.png")
            self.sound=pygame.mixer.Sound("Sounds/7.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w7.wav")
        elif self.id==8:
            self.value=7
            self.image=pygame.image.load("Images/8.png")
            self.sound=pygame.mixer.Sound("Sounds/8.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w8.wav")
        elif self.id==9:
            self.value=9
            self.image=pygame.image.load("Images/9.png")
            self.sound=pygame.mixer.Sound("Sounds/9.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w9.wav")
        elif self.id==10:
            self.value=11
            self.image=pygame.image.load("Images/10.png")
            self.sound=pygame.mixer.Sound("Sounds/10.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w10.wav")
        elif self.id==11:
            self.value=13
            self.image=pygame.image.load("Images/11.png")
            self.sound=pygame.mixer.Sound("Sounds/11.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w11.wav")
        elif self.id==12:
            self.value=15
            self.image=pygame.image.load("Images/12.png")
            self.sound=pygame.mixer.Sound("Sounds/12.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w12.wav")
        elif self.id==13:
            self.value=17
            self.image=pygame.image.load("Images/13.png")
            self.sound=pygame.mixer.Sound("Sounds/13.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w13.wav")
        elif self.id==14:
            self.value=2
            self.image=pygame.image.load("Images/14.png")
            self.sound=pygame.mixer.Sound("Sounds/1.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w1.wav")
        elif self.id==15:
            self.value=24
            self.image=pygame.image.load("Images/15.png")
            self.sound=pygame.mixer.Sound("Sounds/2.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w2.wav")
        elif self.id==16:
            self.value=20
            self.image=pygame.image.load("Images/16.png")
            self.sound=pygame.mixer.Sound("Sounds/3.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w3.wav")
        elif self.id==17:
            self.value=4
            self.image=pygame.image.load("Images/17.png")
            self.sound=pygame.mixer.Sound("Sounds/4.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w4.wav")
        elif self.id==18:
            self.value=22
            self.image=pygame.image.load("Images/18.png")
            self.sound=pygame.mixer.Sound("Sounds/5.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w5.wav")
        elif self.id==19:
            self.value=6
            self.image=pygame.image.load("Images/19.png")
            self.sound=pygame.mixer.Sound("Sounds/6.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w6.wav")
        elif self.id==20:
            self.value=28
            self.image=pygame.image.load("Images/20.png")
            self.sound=pygame.mixer.Sound("Sounds/7.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w7.wav")
        elif self.id==21:
            self.value=8
            self.image=pygame.image.load("Images/21.png")
            self.sound=pygame.mixer.Sound("Sounds/8.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w8.wav")
        elif self.id==22:
            self.value=10
            self.image=pygame.image.load("Images/22.png")
            self.sound=pygame.mixer.Sound("Sounds/9.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w9.wav")
        elif self.id==23:
            self.value=12
            self.image=pygame.image.load("Images/23.png")
            self.sound=pygame.mixer.Sound("Sounds/10.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w10.wav")
        elif self.id==24:
            self.value=14
            self.image=pygame.image.load("Images/24.png")
            self.sound=pygame.mixer.Sound("Sounds/11.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w11.wav")
        elif self.id==25:
            self.value=16
            self.image=pygame.image.load("Images/25.png")
            self.sound=pygame.mixer.Sound("Sounds/12.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w12.wav")
        elif self.id==26:
            self.value=18
            self.image=pygame.image.load("Images/26.png")
            self.sound=pygame.mixer.Sound("Sounds/13.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w13.wav")
        elif self.id==27:
            self.value=1
            self.image=pygame.image.load("Images/27.png")
            self.sound=pygame.mixer.Sound("Sounds/1.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w1.wav")
        elif self.id==28:
            self.value=23
            self.image=pygame.image.load("Images/28.png")
            self.sound=pygame.mixer.Sound("Sounds/2.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w2.wav")
        elif self.id==29:
            self.value=19
            self.image=pygame.image.load("Images/29.png")
            self.sound=pygame.mixer.Sound("Sounds/3.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w3.wav")
        elif self.id==30:
            self.value=3
            self.image=pygame.image.load("Images/30.png")
            self.sound=pygame.mixer.Sound("Sounds/4.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w4.wav")
        elif self.id==31:
            self.value=21
            self.image=pygame.image.load("Images/31.png")
            self.sound=pygame.mixer.Sound("Sounds/5.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w5.wav")
        elif self.id==32:
            self.value=5
            self.image=pygame.image.load("Images/32.png")
            self.sound=pygame.mixer.Sound("Sounds/6.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w6.wav")
        elif self.id==33:
            self.value=27
            self.image=pygame.image.load("Images/33.png")
            self.sound=pygame.mixer.Sound("Sounds/7.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w7.wav")
        elif self.id==34:
            self.value=7
            self.image=pygame.image.load("Images/34.png")
            self.sound=pygame.mixer.Sound("Sounds/8.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w8.wav")
        elif self.id==35:
            self.value=9
            self.image=pygame.image.load("Images/35.png")
            self.sound=pygame.mixer.Sound("Sounds/9.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w9.wav")
        elif self.id==36:
            self.value=11
            self.image=pygame.image.load("Images/36.png")
            self.sound=pygame.mixer.Sound("Sounds/10.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w10.wav")
        elif self.id==37:
            self.value=13
            self.image=pygame.image.load("Images/37.png")
            self.sound=pygame.mixer.Sound("Sounds/11.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w11.wav")
        elif self.id==38:
            self.value=15
            self.image=pygame.image.load("Images/38.png")
            self.sound=pygame.mixer.Sound("Sounds/12.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w12.wav")
        elif self.id==39:
            self.value=17
            self.image=pygame.image.load("Images/39.png")
            self.sound=pygame.mixer.Sound("Sounds/13.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w13.wav")
        elif self.id==40:
            self.value=2
            self.image=pygame.image.load("Images/40.png")
            self.sound=pygame.mixer.Sound("Sounds/1.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w1.wav")
        elif self.id==41:
            self.value=24
            self.image=pygame.image.load("Images/41.png")
            self.sound=pygame.mixer.Sound("Sounds/2.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w2.wav")
        elif self.id==42:
            self.value=20
            self.image=pygame.image.load("Images/42.png")
            self.sound=pygame.mixer.Sound("Sounds/3.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w3.wav")
        elif self.id==43:
            self.value=4
            self.image=pygame.image.load("Images/43.png")
            self.sound=pygame.mixer.Sound("Sounds/4.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w4.wav")
        elif self.id==44:
            self.value=22
            self.image=pygame.image.load("Images/44.png")
            self.sound=pygame.mixer.Sound("Sounds/5.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w5.wav")
        elif self.id==45:
            self.value=6
            self.image=pygame.image.load("Images/45.png")
            self.sound=pygame.mixer.Sound("Sounds/6.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w6.wav")
        elif self.id==46:
            self.value=28
            self.image=pygame.image.load("Images/46.png")
            self.sound=pygame.mixer.Sound("Sounds/7.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w7.wav")
        elif self.id==47:
            self.value=8
            self.image=pygame.image.load("Images/47.png")
            self.sound=pygame.mixer.Sound("Sounds/8.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w8.wav")
        elif self.id==48:
            self.value=10
            self.image=pygame.image.load("Images/48.png")
            self.sound=pygame.mixer.Sound("Sounds/9.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w9.wav")
        elif self.id==49:
            self.value=12
            self.image=pygame.image.load("Images/49.png")
            self.sound=pygame.mixer.Sound("Sounds/10.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w10.wav")
        elif self.id==50:
            self.value=14
            self.image=pygame.image.load("Images/50.png")
            self.sound=pygame.mixer.Sound("Sounds/11.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w11.wav")
        elif self.id==51:
            self.value=16
            self.image=pygame.image.load("Images/51.png")
            self.sound=pygame.mixer.Sound("Sounds/12.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w12.wav")
        elif self.id==52:
            self.value=18
            self.image=pygame.image.load("Images/52.png")
            self.sound=pygame.mixer.Sound("Sounds/13.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w13.wav")
        elif self.id==53:
            self.value=25
            self.image=pygame.image.load("Images/53.png")
            self.sound=pygame.mixer.Sound("Sounds/14.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w14.wav")
        elif self.id==54:
            self.value=26
            self.image=pygame.image.load("Images/54.png")
            self.sound=pygame.mixer.Sound("Sounds/15.wav")
            self.sound2=pygame.mixer.Sound("Sounds/w15.wav")
            
#####################################################################################################################################
#Control Spirit Class
#####################################################################################################################################    
class MyControlClass(pygame.sprite.Sprite):
    def __init__(self, location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/control_3.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
############################################################################################################################################
#Function : Initialization
############################################################################################################################################
def init_cards():
    global deck, p_hand, c_hand, up_card, nc_kou, np_kou, c_kou, p_kou
    deck = []
    nc_kou=np_kou=0
    c_kou=[]
    p_kou=[]
    for pear in range(2):
        for card_id in range(1, 55):
            next = Card(card_id)
            deck.append(next)
    p_hand = []
    for cards in range(0, 5):
        card = random.choice(deck)
        p_hand.append(card)
        deck.remove(card)    
    c_hand = []    
    for cards in range(0, 5):
        card = random.choice(deck)
        c_hand.append(card)
        deck.remove(card)

######################################################################################################################################################
#Function : Blit p_hand
######################################################################################################################################################
def blit_p():
    screen.blit(p_hand_cover,[347,478])
    if np_hand==5:
        screen.blit(p_hand_sorted[0].image,[357,490])
        screen.blit(p_hand_sorted[1].image,[492,490])
        screen.blit(p_hand_sorted[2].image,[627,490])
        screen.blit(p_hand_sorted[3].image,[762,490])
        screen.blit(p_hand_sorted[4].image,[897,490])
    elif np_hand==4:
        screen.blit(p_hand_sorted[0].image,[425,490])
        screen.blit(p_hand_sorted[1].image,[560,490])
        screen.blit(p_hand_sorted[2].image,[695,490])
        screen.blit(p_hand_sorted[3].image,[830,490])
    elif np_hand==3:
        screen.blit(p_hand_sorted[0].image,[492,490])
        screen.blit(p_hand_sorted[1].image,[627,490])
        screen.blit(p_hand_sorted[2].image,[762,490])
    elif np_hand==2:
        screen.blit(p_hand_sorted[0].image,[560,490])
        screen.blit(p_hand_sorted[1].image,[695,490])
    elif np_hand==1:
        screen.blit(p_hand_sorted[0].image,[627,490])

######################################################################################################################################################
#Function : Blit c_hand
######################################################################################################################################################
def blit_c():
    screen.blit(c_hand_cover,[357,30])
    if nc_hand==5:
        screen.blit(back[back_id],[357,30])
        screen.blit(back[back_id],[492,30])
        screen.blit(back[back_id],[627,30])
        screen.blit(back[back_id],[762,30])
        screen.blit(back[back_id],[897,30])
    elif nc_hand==4:
        screen.blit(back[back_id],[425,30])
        screen.blit(back[back_id],[560,30])
        screen.blit(back[back_id],[695,30])
        screen.blit(back[back_id],[830,30])
    elif nc_hand==3:
        screen.blit(back[back_id],[492,30])
        screen.blit(back[back_id],[627,30])
        screen.blit(back[back_id],[762,30])
    elif nc_hand==2:
        screen.blit(back[back_id],[560,30])
        screen.blit(back[back_id],[695,30])
    elif nc_hand==1:
        screen.blit(back[back_id],[627,30])

######################################################################################################################################################
#Function : Blit P_Chat
######################################################################################################################################################
def blit_p_chat():
    screen.blit(p_chat_cover1,[790,250])
    screen.blit(p_chat_cover2,[820,250])
    screen.blit(p_chat[0],[801,322])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_chat_cover1,[790,250])
    screen.blit(p_chat_cover2,[820,250])
    screen.blit(p_chat[1],[794,297])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_chat_cover1,[790,250])
    screen.blit(p_chat_cover2,[820,250])
    screen.blit(p_chat[2],[786,270])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_chat_cover1,[790,250])
    screen.blit(p_chat_cover2,[820,250])
    screen.blit(p_chat[3],[783,259])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_chat_cover1,[790,250])
    screen.blit(p_chat_cover2,[820,250])
    screen.blit(p_chat[4],[780,250])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_chat_cover1,[790,250])
    screen.blit(p_chat_cover2,[820,250])
    screen.blit(p_chat[3],[783,259])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_chat_cover1,[790,250])
    screen.blit(p_chat_cover2,[820,250])
    screen.blit(p_chat[2],[786,270])
    
######################################################################################################################################################
#Function : Blit C_Chat
######################################################################################################################################################
def blit_c_chat():
    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
    screen.blit(c_chat[0],[450,204])
    pygame.display.flip()
    pygame.time.delay(40)
    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
    screen.blit(c_chat[1],[408,202])
    pygame.display.flip()
    pygame.time.delay(40)
    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
    screen.blit(c_chat[2],[387,201])
    pygame.display.flip()
    pygame.time.delay(40)
    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
    screen.blit(c_chat[3],[370,200])
    pygame.display.flip()
    pygame.time.delay(40)
    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
    screen.blit(c_chat[4],[360,200])
    pygame.display.flip()
    pygame.time.delay(40)
    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
    screen.blit(c_chat[3],[370,200])
    pygame.display.flip()
    pygame.time.delay(40)
    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
    screen.blit(c_chat[2],[387,201])

######################################################################################################################################################
#Function : Blit P_kou
######################################################################################################################################################
def blit_p_kou():
    screen.blit(back[back_id],[1100,260])
    p_x_str="x"
    p_x_font = pygame.font.Font("Fonts/FORTE.TTF",70)
    p_x_surf = p_x_font.render(p_x_str, 1, (255, 255, 255))
    p_x_surf_s = p_x_font.render(p_x_str, 1, (150, 150, 150))
    screen.blit(p_x_surf_s, [1217, 342])
    screen.blit(p_x_surf_s, [1216, 341])
    screen.blit(p_x_surf, [1215, 340])
    pkou_str = "%i" % np_kou
    npkou_font1 = pygame.font.Font("Fonts/FORTE.TTF",50)
    npkou_surf1 = npkou_font1.render(pkou_str, 1, (255, 255, 255))
    npkou_surf_s1 = npkou_font1.render(pkou_str, 1, (150, 150, 150))
    screen.blit(npkou_surf_s1, [1257, 360])
    screen.blit(npkou_surf_s1, [1256, 359])
    screen.blit(npkou_surf1, [1255, 358])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_kou_cover,[1255,322])
    npkou_font2 = pygame.font.Font("Fonts/FORTE.TTF",60)
    npkou_surf2 = npkou_font2.render(pkou_str, 1, (255, 255, 255))
    npkou_surf_s2 = npkou_font2.render(pkou_str, 1, (150, 150, 150))
    screen.blit(npkou_surf_s2, [1257, 350])
    screen.blit(npkou_surf_s2, [1256, 349])
    screen.blit(npkou_surf2, [1255, 348])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_kou_cover,[1255,322])
    npkou_font3 = pygame.font.Font("Fonts/FORTE.TTF",70)
    npkou_surf3 = npkou_font3.render(pkou_str, 1, (255, 255, 255))
    npkou_surf_s3 = npkou_font3.render(pkou_str, 1, (150, 150, 150))
    screen.blit(npkou_surf_s3, [1257, 342])
    screen.blit(npkou_surf_s3, [1256, 341])
    screen.blit(npkou_surf3, [1255, 340])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_kou_cover,[1255,322])
    npkou_font4 = pygame.font.Font("Fonts/FORTE.TTF",80)
    npkou_surf4 = npkou_font4.render(pkou_str, 1, (255, 255, 255))
    npkou_surf_s4 = npkou_font4.render(pkou_str, 1, (150, 150, 150))
    screen.blit(npkou_surf_s4, [1257, 334])
    screen.blit(npkou_surf_s4, [1256, 333])
    screen.blit(npkou_surf4, [1255, 332])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_kou_cover,[1255,322])
    npkou_font5 = pygame.font.Font("Fonts/FORTE.TTF",90)
    npkou_surf5 = npkou_font5.render(pkou_str, 1, (255, 255, 255))
    npkou_surf_s5 = npkou_font5.render(pkou_str, 1, (150, 150, 150))
    screen.blit(npkou_surf_s5, [1257, 324])
    screen.blit(npkou_surf_s5, [1256, 323])
    screen.blit(npkou_surf5, [1255, 322])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_kou_cover,[1255,322])
    npkou_font4 = pygame.font.Font("Fonts/FORTE.TTF",80)
    npkou_surf4 = npkou_font4.render(pkou_str, 1, (255, 255, 255))
    npkou_surf_s4 = npkou_font4.render(pkou_str, 1, (150, 150, 150))
    screen.blit(npkou_surf_s4, [1257, 334])
    screen.blit(npkou_surf_s4, [1256, 333])
    screen.blit(npkou_surf4, [1255, 332])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(p_kou_cover,[1255,322])
    npkou_font3 = pygame.font.Font("Fonts/FORTE.TTF",70)
    npkou_surf3 = npkou_font3.render(pkou_str, 1, (255, 255, 255))
    npkou_surf_s3 = npkou_font3.render(pkou_str, 1, (150, 150, 150))
    screen.blit(npkou_surf_s3, [1257, 342])
    screen.blit(npkou_surf_s3, [1256, 341])
    screen.blit(npkou_surf3, [1255, 340])
    pygame.display.flip()

######################################################################################################################################################
#Function : Blit C_kou
######################################################################################################################################################   
def blit_c_kou():
    screen.blit(back[back_id],[140,260])
    c_x_str="x"
    c_x_font = pygame.font.Font("Fonts/FORTE.TTF",70)
    c_x_surf = c_x_font.render(c_x_str, 1, (255, 255, 255))
    c_x_surf_s = c_x_font.render(c_x_str, 1, (150, 150, 150))
    screen.blit(c_x_surf_s, [257, 342])
    screen.blit(c_x_surf_s, [256, 341])
    screen.blit(c_x_surf, [255, 340])
    ckou_str = "%i" % nc_kou
    nckou_font1 = pygame.font.Font("Fonts/FORTE.TTF",50)
    nckou_surf1 = nckou_font1.render(ckou_str, 1, (255, 255, 255))
    nckou_surf_s1 = nckou_font1.render(ckou_str, 1, (150, 150, 150))
    screen.blit(nckou_surf_s1, [297, 360])
    screen.blit(nckou_surf_s1, [296, 359])
    screen.blit(nckou_surf1, [295, 358])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(c_kou_cover,[295,322])
    nckou_font2 = pygame.font.Font("Fonts/FORTE.TTF",60)
    nckou_surf2 = nckou_font2.render(ckou_str, 1, (255, 255, 255))
    nckou_surf_s2 = nckou_font2.render(ckou_str, 1, (150, 150, 150))
    screen.blit(nckou_surf_s2, [297, 350])
    screen.blit(nckou_surf_s2, [296, 349])
    screen.blit(nckou_surf2, [295, 348])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(c_kou_cover,[295,322])
    nckou_font3 = pygame.font.Font("Fonts/FORTE.TTF",70)
    nckou_surf3 = nckou_font3.render(ckou_str, 1, (255, 255, 255))
    nckou_surf_s3 = nckou_font3.render(ckou_str, 1, (150, 150, 150))
    screen.blit(nckou_surf_s3, [297, 342])
    screen.blit(nckou_surf_s3, [296, 341])
    screen.blit(nckou_surf3, [295, 340])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(c_kou_cover,[295,322])
    nckou_font4 = pygame.font.Font("Fonts/FORTE.TTF",80)
    nckou_surf4 = nckou_font4.render(ckou_str, 1, (255, 255, 255))
    nckou_surf_s4 = nckou_font4.render(ckou_str, 1, (150, 150, 150))
    screen.blit(nckou_surf_s4, [297, 334])
    screen.blit(nckou_surf_s4, [296, 333])
    screen.blit(nckou_surf4, [295, 332])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(c_kou_cover,[295,322])
    nckou_font5 = pygame.font.Font("Fonts/FORTE.TTF",90)
    nckou_surf5 = nckou_font5.render(ckou_str, 1, (255, 255, 255))
    nckou_surf_s5 = nckou_font5.render(ckou_str, 1, (150, 150, 150))
    screen.blit(nckou_surf_s5, [297, 324])
    screen.blit(nckou_surf_s5, [296, 323])
    screen.blit(nckou_surf5, [295, 322])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(c_kou_cover,[295,322])
    nckou_font4 = pygame.font.Font("Fonts/FORTE.TTF",80)
    nckou_surf4 = nckou_font4.render(ckou_str, 1, (255, 255, 255))
    nckou_surf_s4 = nckou_font4.render(ckou_str, 1, (150, 150, 150))
    screen.blit(nckou_surf_s4, [297, 334])
    screen.blit(nckou_surf_s4, [296, 333])
    screen.blit(nckou_surf4, [295, 332])
    pygame.display.flip()
    pygame.time.delay(40)
    screen.blit(c_kou_cover,[295,322])
    nckou_font3 = pygame.font.Font("Fonts/FORTE.TTF",70)
    nckou_surf3 = nckou_font3.render(ckou_str, 1, (255, 255, 255))
    nckou_surf_s3 = nckou_font3.render(ckou_str, 1, (150, 150, 150))
    screen.blit(nckou_surf_s3, [297, 342])
    screen.blit(nckou_surf_s3, [296, 341])
    screen.blit(nckou_surf3, [295, 340])
    pygame.display.flip()

#################################################################################################################################################################
#Funtion : Player Turn
#################################################################################################################################################################
def player_turn():
    global deck, p_hand,np_hand, p_blocked, up_card, over, p_kou, np_kou, pkou,ckou, c_hand, nc_kou, p_first_play, win, p_kua,back_id,p_hand_sorted,p_chat,c_chat,chatting
    p_hand1 = p_hand[:]
    p_hand_sorted = []
    np_hand=0
    for card in p_hand:
        np_hand=np_hand+1

    for i in range(1,np_hand+1):
        card1 = p_hand1[0]
        for card in p_hand1:
            if card1.value <= card.value:
                card1 = card
        p_hand_sorted.append(card1)
        p_hand1.remove(card1)
    blit_p()
    pygame.display.flip()

    
    if not p_first_play and not c_first_play:
        pygame.time.set_timer(pygame.USEREVENT,4000)
    pygame.time.set_timer(pygame.USEREVENT+1,15000)
    pygame.time.set_timer(pygame.USEREVENT+2,30000)
    pygame.time.set_timer(pygame.USEREVENT+6,20000)
    pygame.time.set_timer(pygame.USEREVENT+7,35000)
    selected=False
    gonnachat=False
    p_done=False
    p_kua=False
    cchatted=False
    churry1=False
    churry2=False
    thought1=False
    thought2=False
    count_in=0
    while not p_done:
        choose=False
        move=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEMOTION:
                m_pos = pygame.mouse.get_pos()
                move=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            pos = pygame.mouse.get_pos()
                            choose=True
            elif event.type == pygame.USEREVENT:
                if chatting==False and random.randint(0,5)==0:
                    cchat_id=random.randint(0,2)
                    if cchat_id==0:
                        channel3.play(cchat1)
                        c_chat=[cchat_image1_1,cchat_image1_2,cchat_image1_3,cchat_image1_4,cchat_image1_5]
                        blit_c_chat()
                    elif cchat_id==1:
                        channel3.play(cchat2)
                        c_chat=[cchat_image2_1,cchat_image2_2,cchat_image2_3,cchat_image2_4,cchat_image2_5]
                        blit_c_chat()
                    elif cchat_id==2:
                        channel3.play(cchat4)
                        c_chat=[cchat_image4_1,cchat_image4_2,cchat_image4_3,cchat_image4_4,cchat_image4_5]
                        blit_c_chat()
                    elif cchat_id==3:
                        channel3.play(cchat7)
                        c_chat=[cchat_image7_1,cchat_image7_2,cchat_image7_3,cchat_image7_4,cchat_image7_5]
                        blit_c_chat()
                    pygame.time.set_timer(pygame.USEREVENT+4,3000)
                pygame.time.set_timer(pygame.USEREVENT,0)
            elif event.type == pygame.USEREVENT+1:
                if random.randint(0,3)==0:
                    channel3.play(cchat5)
                    c_chat=[cchat_image5_1,cchat_image5_2,cchat_image5_3,cchat_image5_4,cchat_image5_5]
                    blit_c_chat()
                    pygame.time.set_timer(pygame.USEREVENT+4,3000)
                pygame.time.set_timer(pygame.USEREVENT+1,0)
            elif event.type == pygame.USEREVENT+2:
                if random.randint(0,1)==0:
                    channel3.play(cchat5)
                    c_chat=[cchat_image5_1,cchat_image5_2,cchat_image5_3,cchat_image5_4,cchat_image5_5]
                    blit_c_chat()
                    pygame.time.set_timer(pygame.USEREVENT+4,3000)
                pygame.time.set_timer(pygame.USEREVENT+2,0)
            elif event.type == pygame.USEREVENT+3:
                screen.blit(p_chat_cover1,[790,250])
                screen.blit(p_chat_cover2,[820,250])
                pygame.time.set_timer(pygame.USEREVENT+3,0)
            elif event.type == pygame.USEREVENT+4:
                pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                pygame.time.set_timer(pygame.USEREVENT+4,0)
            elif event.type == pygame.USEREVENT+5:
                pygame.draw.rect(screen,[0,70,130],[520,393,305,25])
                pygame.time.set_timer(pygame.USEREVENT+5,0)
            elif event.type == pygame.USEREVENT+6:
                think_id=random.randint(0,1)
                if think_id==0:
                    channel6.play(pthink1)
                    p_chat=[pthink_image1_1,pthink_image1_2,pthink_image1_3,pthink_image1_4,pthink_image1_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                elif think_id==1:
                    channel6.play(pthink2)
                    p_chat=[pthink_image2_1,pthink_image2_2,pthink_image2_3,pthink_image2_4,pthink_image2_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                pygame.time.set_timer(pygame.USEREVENT+6,0)
            elif event.type == pygame.USEREVENT+7:
                channel6.play(pthink3)
                p_chat=[pthink_image3_1,pthink_image3_2,pthink_image3_3,pthink_image3_4,pthink_image3_5]
                blit_p_chat()
                pygame.time.set_timer(pygame.USEREVENT+3,3000)
                pygame.time.set_timer(pygame.USEREVENT+7,0)
            pygame.display.flip()
        if move==True:
            if m_pos[0]>20 and m_pos[0]<65 and m_pos[1]>642 and m_pos[1]<670:
                screen.blit(setting_button2,[20,642])
                count_in+=1
            else:
                screen.blit(setting_button,[20,642])
                count_in=0
            pygame.display.flip()
            if count_in==1:
                channel7.play(pass_by)
        if choose==True:
            if gonnachat==True:
                for i in range(5,1,-1):
                    screen.blit(choice_cover,[1083,451])
                    screen.blit(choice[i],[1083,451])                    
                    pygame.display.flip()
                    pygame.time.delay(20)
                screen.blit(choice_cover,[1083,451])
                screen.blit(choice1,[1083,451])
                for i in range(0,4):
                    screen.blit(chat0,[1150,525])
                    pygame.display.flip()
                    pygame.time.delay(20)
                screen.blit(chat,[1150,525])
                pygame.display.flip()
                gonnachat=False
                if (pos[0]-1189)**2+(pos[1]-564)**2<=1521:
                    channel2.play(pchat4)
                    p_chat=[pchat_image4_1,pchat_image4_2,pchat_image4_3,pchat_image4_4,pchat_image4_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                    pygame.time.set_timer(pygame.USEREVENT+6,0)
                    pygame.time.set_timer(pygame.USEREVENT+7,0)
                elif (pos[0]-1189)**2+(pos[1]-486)**2<=1521:
                    channel2.play(pchat5)
                    p_chat=[pchat_image5_1,pchat_image5_2,pchat_image5_3,pchat_image5_4,pchat_image5_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                    pygame.time.set_timer(pygame.USEREVENT+6,0)
                    pygame.time.set_timer(pygame.USEREVENT+7,0)
                elif (pos[0]-1189)**2+(pos[1]-642)**2<=1521:
                    channel2.play(pchat2)
                    p_chat=[pchat_image2_1,pchat_image2_2,pchat_image2_3,pchat_image2_4,pchat_image2_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                    pygame.time.set_timer(pygame.USEREVENT+6,0)
                    pygame.time.set_timer(pygame.USEREVENT+7,0)
                elif (pos[0]-1121)**2+(pos[1]-603)**2<=1521:
                    channel2.play(pchat6)
                    p_chat=[pchat_image6_1,pchat_image6_2,pchat_image6_3,pchat_image6_4,pchat_image6_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                    pygame.time.set_timer(pygame.USEREVENT+6,0)
                    pygame.time.set_timer(pygame.USEREVENT+7,0)
                elif (pos[0]-1121)**2+(pos[1]-525)**2<=1521:
                    channel2.play(pchat3)
                    p_chat=[pchat_image3_1,pchat_image3_2,pchat_image3_3,pchat_image3_4,pchat_image3_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                    pygame.time.set_timer(pygame.USEREVENT+6,0)
                    pygame.time.set_timer(pygame.USEREVENT+7,0)
                    p_kua=True
                elif (pos[0]-1257)**2+(pos[1]-603)**2<=1521:
                    channel2.play(pchat7)
                    p_chat=[pchat_image7_1,pchat_image7_2,pchat_image7_3,pchat_image7_4,pchat_image7_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                    pygame.time.set_timer(pygame.USEREVENT+6,0)
                    pygame.time.set_timer(pygame.USEREVENT+7,0)
                elif (pos[0]-1257)**2+(pos[1]-525)**2<=1521:
                    channel2.play(pchat1)
                    p_chat=[pchat_image1_1,pchat_image1_2,pchat_image1_3,pchat_image1_4,pchat_image1_5]
                    blit_p_chat()
                    pygame.time.set_timer(pygame.USEREVENT+3,3000)
                    pygame.time.set_timer(pygame.USEREVENT+6,0)
                    pygame.time.set_timer(pygame.USEREVENT+7,0)
            else:
                if(pos[0]-1189)**2+(pos[1]-564)**2<=1521:
                    for i in range(0,4):
                        screen.blit(choice0,[1083,451])
                        pygame.display.flip()
                        pygame.time.delay(20)
                    for i in range(0,6):
                        screen.blit(choice_cover,[1083,451])
                        screen.blit(choice[i],[1083,451])                    
                        pygame.display.flip()
                        pygame.time.delay(20)
                    pygame.display.flip()
                    gonnachat=True
            if pos[0]>20 and pos[0]<65 and pos[1]>642 and pos[1]<670:
                channel5.play(click1)
                screen.blit(manu1,[585,223])
                pygame.display.flip()
                pygame.time.delay(20)
                screen.blit(manu2,[580,217])
                pygame.display.flip()
                pygame.time.delay(20)
                screen.blit(manu3,[570,203])
                pygame.display.flip()
                pygame.time.delay(20)
                screen.blit(manu4,[555,183])
                pygame.display.flip()          
                setted1=False
                count_in=0
                while not setted1:
                    choose=False
                    move=False
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            exit()
                        elif event.type == pygame.MOUSEMOTION:
                            m_pos = pygame.mouse.get_pos()
                            move=True
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            pressed_array = pygame.mouse.get_pressed()
                            for index in range(len(pressed_array)):
                                if pressed_array[index]:
                                    if index == 0:
                                        pos = pygame.mouse.get_pos()
                                        choose=True
                    if move==True:
                        if m_pos[0]>615 and m_pos[0]<748 and m_pos[1]>239 and m_pos[1]<274:
                            screen.blit(manu_A,[590,233])
                            count_in+=1
                        elif m_pos[0]>615 and m_pos[0]<748 and m_pos[1]>317 and m_pos[1]<352:
                            screen.blit(manu_B,[590,314])
                            count_in+=1
                        elif m_pos[0]>615 and m_pos[0]<748 and m_pos[1]>367 and m_pos[1]<402:
                            screen.blit(manu_C,[591,363])
                            count_in+=1
                        elif m_pos[0]>615 and m_pos[0]<748 and m_pos[1]>447 and m_pos[1]<482:
                            screen.blit(manu_D,[590,442])
                            count_in+=1
                        else:
                            count_in=0
                            screen.blit(manu4,[555,183])
                        pygame.display.flip()
                        if count_in==1:
                            channel7.play(pass_by)
                    if choose==True:
                        if pos[0]>615 and pos[0]<748 and pos[1]>239 and pos[1]<274:
                            channel5.play(click2)
                            over+=1
                            win=3
                            setted1=True
                            p_done=True
                            pygame.draw.rect(screen,[0,70,130],[555,183,249,344])
                            pygame.draw.rect(screen,[0,70,130],[520,390,305,28])
                        elif pos[0]>615 and pos[0]<748 and pos[1]>317 and pos[1]<352:
                            channel5.play(click2)
                            screen.blit(setting1,[463,95])
                            screen.blit(control_1,[int((control1.rect.left-680)*5/6.0)+680,345-int((345-control1.rect.top)*5/6.0)])
                            screen.blit(control_1,[int((control2.rect.left-680)*5/6.0)+680,345-int((345-control2.rect.top)*5/6.0)])
                            screen.blit(set_back_1[back_id],[644,413])
                            if back_id==0:
                                screen.blit(back_right_1,[596,535])
                            elif back_id==6:
                                screen.blit(back_left_1,[596,535])
                            else:
                                screen.blit(back_both_1,[596,535])
                            pygame.display.flip()
                            pygame.time.delay(40)
                            screen.blit(setting2,[442,70])
                            screen.blit(control_2,[int((control1.rect.left-680)*11/12.0)+680,345-int((345-control1.rect.top)*11/12.0)])
                            screen.blit(control_2,[int((control2.rect.left-680)*11/12.0)+680,345-int((345-control2.rect.top)*11/12.0)])
                            screen.blit(set_back_2[back_id],[641,420])
                            if back_id==0:
                                screen.blit(back_right_2,[588,554])
                            elif back_id==6:
                                screen.blit(back_left_2,[588,554])
                            else:
                                screen.blit(back_both_2,[588,554])
                            pygame.display.flip()
                            pygame.time.delay(40)
                            setted2=0
                            held_down1=0
                            held_down2=0
                            right_in=0
                            left_in=0
                            help_in=0
                            about_in=0
                            while not setted2:
                                choose=False
                                move=False
                                screen.blit(setting3,[420,45])
                                screen.blit(control1.image,control1.rect)
                                screen.blit(control2.image,control2.rect)
                                screen.blit(set_back_3[back_id],[637,426])
                                if back_id==0:
                                    screen.blit(back_right_3,[580,573])
                                    if right_in>0:
                                        screen.blit(right2,[740,575])
                                elif back_id==6:
                                    screen.blit(back_left_3,[580,573])
                                    if left_in>0:
                                        screen.blit(left2,[592,575])
                                else:
                                    screen.blit(back_both_3,[580,573])
                                    if right_in>0:
                                        screen.blit(right2,[740,575])
                                    if left_in>0:
                                        screen.blit(left2,[592,575])
                                if help_in>0:
                                    screen.blit(help_b,[532,312])
                                elif about_in>0:
                                    screen.blit(about_b,[689,310])
                                pygame.display.flip()
                                pygame.mixer.music.set_volume((control1.rect.left-691)/3.0/90.0)
                                channel1.set_volume((control2.rect.left-691)/3.0/90.0)
                                channel2.set_volume((control2.rect.left-691)/3.0/90.0)
                                channel3.set_volume((control2.rect.left-691)/3.0/90.0)
                                channel4.set_volume((control2.rect.left-691)/3.0/90.0) 
                                channel5.set_volume((control1.rect.left-691)/90.0)
                                channel6.set_volume((control2.rect.left-691)/3.0/90.0)
                                channel7.set_volume((control1.rect.left-691)/3.0/90.0)
                                for event in pygame.event.get():
                                    if event.type==pygame.QUIT:
                                        exit()
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        held_down1 = False
                                        held_down2 = False
                                    elif event.type == pygame.MOUSEMOTION:
                                        m_pos = pygame.mouse.get_pos()
                                        move=True
                                        if held_down1:
                                            control1.rect.left = event.pos[0]
                                            if control1.rect.left < 691:
                                                control1.rect.left= 691
                                            if control1.rect.left > 781:
                                                control1.rect.left = 781
                                        elif held_down2:
                                            control2.rect.left = event.pos[0]
                                            if control2.rect.left < 691:
                                                control2.rect.left= 691
                                            if control2.rect.left > 781:
                                                control2.rect.left = 781
                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                        pressed_array = pygame.mouse.get_pressed()
                                        for index in range(len(pressed_array)):
                                            if pressed_array[index]:
                                                if index == 0:
                                                    pos = pygame.mouse.get_pos()
                                                    choose=True
                                if move==True:
                                    if m_pos[0]>742 and m_pos[0]<770 and m_pos[1]>578 and m_pos[1]<598:
                                        right_in+=1
                                    else:
                                        right_in=0
                                    if m_pos[0]>596 and m_pos[0]<624 and m_pos[1]>578 and m_pos[1]<598:
                                        left_in+=1
                                    else:
                                        left_in=0
                                    if m_pos[0]>556 and m_pos[0]<647 and m_pos[1]>319 and m_pos[1]<342:
                                        help_in+=1
                                    else:
                                        help_in=0
                                    if m_pos[0]>711 and m_pos[0]<802 and m_pos[1]>319 and m_pos[1]<342:
                                        about_in+=1
                                    else:
                                        about_in=0
                                    if (back_id!=6 and right_in==1) or (back_id!=0 and left_in==1) or help_in==1 or about_in==1:
                                        channel7.play(pass_by)
                                if choose==True:
                                    if pos[0]>control1.rect.left and pos[0]<control1.rect.right and pos[1]>control1.rect.top and pos[1]<control1.rect.bottom:
                                        held_down1=True
                                    if pos[0]>control2.rect.left and pos[0]<control2.rect.right and pos[1]>control2.rect.top and pos[1]<control2.rect.bottom:
                                        held_down2=True
                                    if back_id==0:
                                        if pos[0]>742 and pos[0]<770 and pos[1]>578 and pos[1]<598:
                                            channel5.play(click2)
                                            back_id+=1
                                            screen.blit(set_back_3[back_id],[637,426])
                                            if back_id==6:
                                                screen.blit(back_left_3,[580,573])
                                            else:
                                                screen.blit(back_both_3,[580,573])
                                            pygame.display.flip()
                                            
                                    elif back_id==6:
                                        if pos[0]>596 and pos[0]<624 and pos[1]>578 and pos[1]<598:
                                            channel5.play(click2)
                                            back_id-=1
                                            screen.blit(set_back_3[back_id],[637,426])
                                            if back_id==0:
                                                screen.blit(back_right_3,[580,573])
                                            else:
                                                screen.blit(back_both_3,[580,573])
                                            pygame.display.flip()
                                    else:
                                        if pos[0]>742 and pos[0]<770 and pos[1]>578 and pos[1]<598:
                                            channel5.play(click2)
                                            back_id+=1
                                            screen.blit(set_back_3[back_id],[637,426])
                                            if back_id==6:
                                                screen.blit(back_left_3,[580,573])
                                            else:
                                                screen.blit(back_both_3,[580,573])
                                            pygame.display.flip()
                                        if pos[0]>596 and pos[0]<624 and pos[1]>578 and pos[1]<598:
                                            channel5.play(click2)
                                            back_id-=1
                                            screen.blit(set_back_3[back_id],[637,426])
                                            if back_id==0:
                                                screen.blit(back_right_3,[580,573])
                                            else:
                                                screen.blit(back_both_3,[580,573])
                                            pygame.display.flip() 
                                    if pos[0]>556 and pos[0]<647 and pos[1]>319 and pos[1]<342:
                                        channel5.play(click2)
                                        pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                                        screen.blit(help1,[415,178])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(help2,[400,167])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(help3,[389,160])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(help4,[380,154])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(help5,[375,151])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        pygame.draw.rect(screen,[0,70,130],[375,151,610,420])
                                        blit_p()
                                        if p_first_play:
                                            screen.blit(c_hand_cover,[357,30])
                                            screen.blit(back[back_id],[357,30])
                                            screen.blit(back[back_id],[492,30])
                                            screen.blit(back[back_id],[627,30])
                                            screen.blit(back[back_id],[762,30])
                                            screen.blit(back[back_id],[897,30])
                                        else:
                                            blit_c()
                                        screen.blit(setting3,[420,45])
                                        screen.blit(control1.image,control1.rect)
                                        screen.blit(control2.image,control2.rect)
                                        screen.blit(set_back_3[back_id],[637,426])
                                        if back_id==0:
                                            screen.blit(back_right_3,[580,573])
                                        elif back_id==6:
                                            screen.blit(back_left_3,[580,573])
                                        else:
                                            screen.blit(back_both_3,[580,573])
                                        screen.blit(help4,[380,154])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        pygame.draw.rect(screen,[0,70,130],[380,154,600,413])
                                        blit_p()
                                        if p_first_play:
                                            screen.blit(c_hand_cover,[357,30])
                                            screen.blit(back[back_id],[357,30])
                                            screen.blit(back[back_id],[492,30])
                                            screen.blit(back[back_id],[627,30])
                                            screen.blit(back[back_id],[762,30])
                                            screen.blit(back[back_id],[897,30])
                                        else:
                                            blit_c()
                                        screen.blit(setting3,[420,45])
                                        screen.blit(control1.image,control1.rect)
                                        screen.blit(control2.image,control2.rect)
                                        screen.blit(set_back_3[back_id],[637,426])
                                        if back_id==0:
                                            screen.blit(back_right_3,[580,573])
                                        elif back_id==6:
                                            screen.blit(back_left_3,[580,573])
                                        else:
                                            screen.blit(back_both_3,[580,573])
                                        screen.blit(help3,[389,160])
                                        pygame.display.flip()
                                        setted3=False
                                        count_in=0
                                        while not setted3:
                                            choose=False
                                            for event in pygame.event.get():
                                                if event.type==pygame.QUIT:
                                                    exit()
                                                elif event.type == pygame.MOUSEMOTION:
                                                    m_pos = pygame.mouse.get_pos()
                                                    move=True
                                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                                    pressed_array = pygame.mouse.get_pressed()
                                                    for index in range(len(pressed_array)):
                                                        if pressed_array[index]:
                                                            if index == 0:
                                                                pos = pygame.mouse.get_pos()
                                                                choose=True
                                            if move==True:
                                                if m_pos[0]>786 and m_pos[0]<891 and m_pos[1]>484 and m_pos[1]<510:
                                                    screen.blit(continue_b,[763,474])
                                                    count_in+=1
                                                else:
                                                    screen.blit(help3,[389,160])
                                                    count_in=0
                                                pygame.display.flip()
                                                if count_in==1:
                                                    channel7.play(pass_by)
                                            if choose==True:
                                                if pos[0]>786 and pos[0]<891 and pos[1]>484 and pos[1]<510:
                                                    channel5.play(click2)
                                                    pygame.draw.rect(screen,[0,70,130],[389,184,582,377])
                                                    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                                                    pygame.draw.rect(screen,[0,70,130],[790,250,30,150])
                                                    pygame.draw.rect(screen,[0,70,130],[820,250,265,172])
                                                    blit_p()
                                                    if selected==True:
                                                        screen.blit(back_gl,gl_pos)
                                                        screen.blit(selected_card.image,sl_pos)
                                                    screen.blit(setting3,[420,45])
                                                    pygame.display.flip()
                                                    setted3=True
                                                elif not(pos[0]>389 and pos[0]<971 and pos[1]>160 and pos[1]<561):
                                                    channel5.play(click1)
                                                    pygame.draw.rect(screen,[0,70,130],[389,184,582,377])
                                                    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                                                    pygame.draw.rect(screen,[0,70,130],[790,250,30,150])
                                                    pygame.draw.rect(screen,[0,70,130],[820,250,265,172])
                                                    blit_p()
                                                    if selected==True:
                                                        screen.blit(back_gl,gl_pos)
                                                        screen.blit(selected_card.image,sl_pos)
                                                    screen.blit(setting3,[420,45])
                                                    pygame.display.flip()
                                                    setted3=True
                                    elif pos[0]>711 and pos[0]<802 and pos[1]>319 and pos[1]<342:
                                        channel5.play(click2)
                                        pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                                        screen.blit(about1,[415,178])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(about2,[400,167])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(about3,[389,160])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(about4,[380,154])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        screen.blit(about5,[375,151])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        pygame.draw.rect(screen,[0,70,130],[375,151,610,420])
                                        blit_p()
                                        if p_first_play:
                                            screen.blit(c_hand_cover,[357,30])
                                            screen.blit(back[back_id],[357,30])
                                            screen.blit(back[back_id],[492,30])
                                            screen.blit(back[back_id],[627,30])
                                            screen.blit(back[back_id],[762,30])
                                            screen.blit(back[back_id],[897,30])
                                        else:
                                            blit_c()
                                        screen.blit(setting3,[420,45])
                                        screen.blit(control1.image,control1.rect)
                                        screen.blit(control2.image,control2.rect)
                                        screen.blit(set_back_3[back_id],[637,426])
                                        if back_id==0:
                                            screen.blit(back_right_3,[580,573])
                                        elif back_id==6:
                                            screen.blit(back_left_3,[580,573])
                                        else:
                                            screen.blit(back_both_3,[580,573])
                                        screen.blit(about4,[380,154])
                                        pygame.display.flip()
                                        pygame.time.delay(30)
                                        pygame.draw.rect(screen,[0,70,130],[380,154,600,413])
                                        blit_p()
                                        if p_first_play:
                                            screen.blit(c_hand_cover,[357,30])
                                            screen.blit(back[back_id],[357,30])
                                            screen.blit(back[back_id],[492,30])
                                            screen.blit(back[back_id],[627,30])
                                            screen.blit(back[back_id],[762,30])
                                            screen.blit(back[back_id],[897,30])
                                        else:
                                            blit_c()
                                        screen.blit(setting3,[420,45])
                                        screen.blit(control1.image,control1.rect)
                                        screen.blit(control2.image,control2.rect)
                                        screen.blit(set_back_3[back_id],[637,426])
                                        if back_id==0:
                                            screen.blit(back_right_3,[580,573])
                                        elif back_id==6:
                                            screen.blit(back_left_3,[580,573])
                                        else:
                                            screen.blit(back_both_3,[580,573])
                                        screen.blit(about3,[389,160])
                                        pygame.display.flip()
                                        setted4=False
                                        while not setted4:
                                            choose=False
                                            move=False
                                            for event in pygame.event.get():
                                                if event.type==pygame.QUIT:
                                                    exit()
                                                elif event.type == pygame.MOUSEMOTION:
                                                    m_pos = pygame.mouse.get_pos()
                                                    move=True    
                                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                                    pressed_array = pygame.mouse.get_pressed()
                                                    for index in range(len(pressed_array)):
                                                        if pressed_array[index]:
                                                            if index == 0:
                                                                pos = pygame.mouse.get_pos()
                                                                choose=True
                                            if move==True:
                                                if m_pos[0]>489 and m_pos[0]<879 and m_pos[1]>480 and m_pos[1]<504:
                                                    screen.blit(web,[475,475])
                                                else:
                                                    screen.blit(about3,[389,160])
                                                pygame.display.flip()
                                            if choose==True:
                                                if not(pos[0]>389 and pos[0]<971 and pos[1]>160 and pos[1]<561):
                                                    channel5.play(click1)
                                                    pygame.draw.rect(screen,[0,70,130],[389,184,582,377])
                                                    pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                                                    pygame.draw.rect(screen,[0,70,130],[790,250,30,150])
                                                    pygame.draw.rect(screen,[0,70,130],[820,250,265,172])
                                                    blit_p()
                                                    if selected==True:
                                                        screen.blit(back_gl,gl_pos)
                                                        screen.blit(selected_card.image,sl_pos)
                                                    screen.blit(setting3,[420,45])
                                                    pygame.display.flip()
                                                    setted4=True
                                                elif pos[0]>489 and pos[0]<879 and pos[1]>480 and pos[1]<504:
                                                    webbrowser.open_new_tab("http://blog.csdn.net/jackeriss/article/details/23531155")
                                                elif pos[0]>513 and pos[0]<664 and pos[1]>391 and pos[1]<440:
                                                    webbrowser.open_new_tab("https://www.python.org/")
                                                elif pos[0]>699 and pos[0]<869 and pos[1]>391 and pos[1]<440:
                                                    webbrowser.open_new_tab("http://www.pygame.org/")
                                    elif not (pos[0]>420 and pos[0]<939 and pos[1]>45 and pos[1]<645):
                                        channel5.play(click1)
                                        pygame.draw.rect(screen,[0,70,130],[420,45,519,600])
                                        pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                                        pygame.draw.rect(screen,[0,70,130],[790,250,30,150])
                                        pygame.draw.rect(screen,[0,70,130],[820,250,265,172])
                                        if p_first_play:
                                            screen.blit(c_hand_cover,[357,30])
                                            screen.blit(back[back_id],[357,30])
                                            screen.blit(back[back_id],[492,30])
                                            screen.blit(back[back_id],[627,30])
                                            screen.blit(back[back_id],[762,30])
                                            screen.blit(back[back_id],[897,30])
                                        else:
                                            blit_c()
                                        blit_p()
                                        if selected==True:
                                            screen.blit(back_gl,gl_pos)
                                            screen.blit(selected_card.image,sl_pos)
                                        if np_kou>0:
                                            screen.blit(back[back_id],[1100,260])
                                        if nc_kou>0:
                                            screen.blit(back[back_id],[140,260])
                                        screen.blit(manu1,[585,223])
                                        pygame.display.flip()
                                        pygame.time.delay(20)
                                        screen.blit(manu2,[580,217])
                                        pygame.display.flip()
                                        pygame.time.delay(20)
                                        screen.blit(manu3,[570,203])
                                        pygame.display.flip()
                                        pygame.time.delay(20)
                                        screen.blit(manu4,[555,183])  
                                        pygame.display.flip()
                                        setted2=True
                                volume_file= open("Settings/volume.txt","w")
                                volume_file.write("%i,%i" % (control1.rect.left,control2.rect.left))
                                volume_file.close
                                back_file= open("Settings/back.txt","w")
                                back_file.write("%i" % back_id)
                                back_file.close
                        elif pos[0]>615 and pos[0]<748 and pos[1]>367 and pos[1]<402:
                            channel5.play(click2)
                            pygame.time.delay(800)
                            exit()
                        elif pos[0]>615 and pos[0]<748 and pos[1]>447 and pos[1]<482:
                            channel5.play(click2)
                            pygame.draw.rect(screen,[0,70,130],[555,184,249,344])
                            pygame.draw.rect(screen,[0,70,130],[520,390,305,28])
                            pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                            pygame.draw.rect(screen,[0,70,130],[790,250,30,150])
                            pygame.draw.rect(screen,[0,70,130],[820,250,265,172])
                            if not p_first_play:
                                screen.blit(up_card.image, [627,220])
                            blit_p()
                            if selected==True:
                                screen.blit(back_gl,gl_pos)
                                screen.blit(selected_card.image,sl_pos)
                            pygame.display.flip()
                            setted1=True
                        elif not(pos[0]>555 and pos[0]<804 and pos[1]>190 and pos[1]<534):
                            channel5.play(click1)
                            pygame.draw.rect(screen,[0,70,130],[555,184,249,344])
                            pygame.draw.rect(screen,[0,70,130],[520,390,305,28])
                            pygame.draw.rect(screen,[0,70,130],[360,200,252,185])
                            pygame.draw.rect(screen,[0,70,130],[790,250,30,150])
                            pygame.draw.rect(screen,[0,70,130],[820,250,265,172])
                            if not p_first_play:
                                screen.blit(up_card.image, [627,220])
                            blit_p()
                            if selected==True:
                                screen.blit(back_gl,gl_pos)
                                screen.blit(selected_card.image,sl_pos)
                            pygame.display.flip()
                            setted1=True
            if np_hand==5:
                if pos[0]>357 and pos[0]<462 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[0]
                    sl_pos=[357,490]
                    gl_pos=[346,478]
                    selected=True
                elif pos[0]>492 and pos[0]<597 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[1]
                    sl_pos=[492,490]
                    gl_pos=[481,478]
                    selected=True
                elif pos[0]>627 and pos[0]<732 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[2]
                    sl_pos=[627,490]
                    gl_pos=[616,478]
                    selected=True
                elif pos[0]>762 and pos[0]<867 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[3]
                    sl_pos=[762,490]
                    gl_pos=[751,478]
                    selected=True
                elif pos[0]>897 and pos[0]<1002 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[4]
                    sl_pos=[897,490]
                    gl_pos=[886,478]
                    selected=True
            elif np_hand==4:
                if pos[0]>425 and pos[0]<530 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[0]
                    sl_pos=[425,490]
                    gl_pos=[414,478]
                    selected=True
                elif pos[0]>560 and pos[0]<665 and pos[1]>490and pos[1]<640:
                    selected_card=p_hand_sorted[1]
                    sl_pos=[560,490]
                    gl_pos=[549,478]
                    selected=True
                elif pos[0]>695 and pos[0]<800 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[2]
                    sl_pos=[695,490]
                    gl_pos=[684,478]
                    selected=True
                elif pos[0]>830 and pos[0]<935 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[3]
                    sl_pos=[830,490]
                    gl_pos=[819,478]
                    selected=True
            elif np_hand==3:
                if pos[0]>492 and pos[0]<597 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[0]
                    sl_pos=[492,490]
                    gl_pos=[481,478]
                    selected=True
                elif pos[0]>627 and pos[0]<732 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[1]
                    sl_pos=[627,490]
                    gl_pos=[616,478]
                    selected=True
                elif pos[0]>762 and pos[0]<867 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[2]
                    sl_pos=[762,490]
                    gl_pos=[751,478]
                    selected=True
            elif np_hand==2:
                if pos[0]>560 and pos[0]<665 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[0]
                    sl_pos=[560,490]
                    gl_pos=[549,478]
                    selected=True
                elif pos[0]>695 and pos[0]<800 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[1]
                    sl_pos=[695,490]
                    gl_pos=[684,478]
                    selected=True
            elif np_hand==1:
                if pos[0]>627 and pos[0]<732 and pos[1]>490 and pos[1]<640:
                    selected_card=p_hand_sorted[0]
                    sl_pos=[627,490]
                    gl_pos=[616,478]
                    selected=True
            else:
                selected=False
            if selected==True:
                blit_p()
                screen.blit(back_gl,gl_pos)
                screen.blit(selected_card.image,sl_pos)
                screen.blit(cp,[560,430])
                screen.blit(kp,[710,430])
                pygame.display.flip()
                pchu=False
                if pos[0]>560 and pos[0]<650 and pos[1]>430 and pos[1]<467:
                    pygame.draw.rect(screen,[0,70,130],[560,430,240,37])
                    blit_p()
                    pygame.display.flip()                 
                    pkou=False
                    pchu=True
                    if p_first_play==True:
                        p_first_play=False
                        p_done=True
                        up_card=selected_card
                        p_hand.remove(selected_card)
                        screen.blit(up_card.image, [627,220])
                        pygame.display.flip()
                        channel1.play(up_card.sound)
                        channel7.play(cp_sound)
                        if len(deck)>0:
                            card=random.choice(deck)
                            p_hand.append(card)
                            deck.remove(card)
                        else:
                            p_blocked+=1
                            if len(p_hand)==0:
                                for card in c_hand:
                                    c_kou.append(card)
                                blit_c_kou()
                                over+=1
                    else:
                        if ckou==True:
                            up_card.value=0
                        if selected_card.value>up_card.value:
                            p_done=True
                            p_hand.remove(selected_card)
                            if up_card.value%2==1 and selected_card.value==(up_card.value+1):
                                Dani=random.choice(dani)
                                channel1.play(Dani)
                            else:
                                channel1.play(selected_card.sound)
                            channel7.play(cp_sound)
                            up_card=selected_card
                            screen.blit(up_card.image, [627,220])
                            pygame.display.flip()                        
                            if len(deck)>0:
                                card=random.choice(deck)
                                p_hand.append(card)
                                deck.remove(card)
                            else:
                                p_blocked+=1
                                if len(p_hand)==0:
                                    for card in c_hand:
                                        c_kou.append(card)
                                        nc_kou=nc_kou+1
                                    blit_c_kou()
                                    over+=1
                        else:
                            channel4.play(perror)
                            screen.blit(Tishi,[520,390])
                            pygame.display.flip()
                            pygame.time.set_timer(pygame.USEREVENT+5,3000)
                            selected=False
                            p_done=False
                            
                elif pos[0]>710 and pos[0]<800 and pos[1]>430 and pos[1]<467:
                    pygame.draw.rect(screen,[0,70,130],[560,430,240,37])
                    blit_p()
                    pygame.display.flip()  
                    pkou=True
                    pchu=True
                    p_done=True
                    p_hand.remove(selected_card)
                    np_kou=np_kou+1
                    p_kou.append(selected_card)
                    BuYao=random.choice(buyao)
                    channel1.play(BuYao)
                    if np_kou>0:
                        blit_p_kou()
                    if len(deck)>0:
                        card=random.choice(deck)
                        p_hand.append(card)
                        deck.remove(card)
                    else:
                        p_blocked+=1
                        if len(p_hand)==0:
                            for card in c_hand:
                                c_kou.append(card)
                                nc_kou=nc_kou+1
                            blit_c_kou()
                            over+=1
              
    p_hand1 = p_hand[:]
    p_hand_sorted = []
    np_hand=0
    for card in p_hand:
        np_hand=np_hand+1
    for i in range(1,np_hand+1):
        card1 = p_hand1[0]
        for card in p_hand1:
            if card1.value <= card.value:
                card1 = card
        p_hand_sorted.append(card1)
        p_hand1.remove(card1)
        
    blit_p()
    pygame.display.flip()
    if np_hand==5:
        if (p_hand_sorted[0].value==27 and p_hand_sorted[1].value==25 and p_hand_sorted[2].value==23 and p_hand_sorted[3].value==21 and p_hand_sorted[4].value==19)or(p_hand_sorted[0].value==28 and p_hand_sorted[1].value==26 and p_hand_sorted[2].value==24 and p_hand_sorted[3].value==22 and p_hand_sorted[4].value==20):
            over+=1
            win=1
    length=random.randint(0,2)
    if length==0:
        pygame.time.delay(1000)
    elif length==1:
        pygame.time.delay(2000)
    elif length==2:
        pygame.time.delay(3000)
        
############################################################################################################################################
#Function : Computer Turn
############################################################################################################################################
def computer_turn():
    global c_hand, deck, up_card, over, c_blocked, c_kou, nc_kou, pkou,ckou, p_hand, np_kou, c_first_play, win, p_kua, nc_hand,c_chat,chatting
    c_hand1 = c_hand[:]
    c_hand_sorted = []
    nc_hand=0
    suit_cards=[]
    ckou=False
    chatting=False
    for card in c_hand:
        nc_hand=nc_hand+1
    for i in range(1,nc_hand+1):
        card1 = c_hand1[0]
        for card in c_hand1:
            if card1.value <= card.value:
                card1 = card
        c_hand_sorted.append(card1)
        c_hand1.remove(card1)
    blit_c()
    pygame.display.flip()
    
    if pkou==True:
        best_play = c_hand[0]
        for card in c_hand:
            if card.value < best_play.value:
                best_play = card
        c_hand.remove(best_play)
        up_card = best_play
        screen.blit(up_card.image, [627,220])
        pygame.display.flip()
        channel1.play(up_card.sound2)
        channel7.play(cp_sound)
        if len(deck) >0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
        else:
            c_blocked+=1
            if len(c_hand)==0:
                for card in p_hand:
                    p_kou.append(card)
                    np_kou=np_kou+1
                blit_p_kou()
                over+=1
    elif c_first_play==True:
        c_first_play=False
        best_play = c_hand[0]
        for card in c_hand:
            if card.value < best_play.value:
                best_play = card
        c_hand.remove(best_play)
        up_card = best_play
        screen.blit(up_card.image, [627,220])
        pygame.display.flip()
        channel1.play(up_card.sound2)
        channel7.play(cp_sound)
        if len(deck) >0:
            next_card = random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
        else:
            c_blocked+=1
            if len(c_hand)==0:
                for card in p_hand:
                    p_kou.append(card)
                    np_kou=np_kou+1
                blit_p_kou()
                over+=1
    else:
        if (up_card.value==27 or up_card.value==28) and random.randint(0,4)==0:
            chatting=True
            channel3.play(cchat3)
            c_chat=[cchat_image3_1,cchat_image3_2,cchat_image3_3,cchat_image3_4,cchat_image3_5]
            blit_c_chat()
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.time.set_timer(pygame.USEREVENT+4,3000)
        elif (up_card.value==25 or up_card.value==26) and random.randint(0,6)==0:
            chatting=True
            channel3.play(cchat3)
            c_chat=[cchat_image3_1,cchat_image3_2,cchat_image3_3,cchat_image3_4,cchat_image3_5]
            blit_c_chat()
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.time.set_timer(pygame.USEREVENT+4,3000)
        if p_kua==True and random.randint(0,3)==0:
            chatting=True
            channel3.play(cchat6)
            c_chat=[cchat_image6_1,cchat_image6_2,cchat_image6_3,cchat_image6_4,cchat_image6_5]
            blit_c_chat()
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.time.set_timer(pygame.USEREVENT+4,3000)
        for card in c_hand:
            if card.value>up_card.value:
                suit_cards.append(card)
        if len(suit_cards) > 0:
            best_play = suit_cards[0]
            for card in suit_cards:
                if card.value < best_play.value:
                    best_play = card
            c_hand.remove(best_play)
            if up_card.value%2==1 and best_play.value==(up_card.value+1):
                wDani=random.choice(wdani)
                channel1.play(wDani)
            else:
                channel1.play(best_play.sound2)
            channel7.play(cp_sound)
            up_card = best_play
            screen.blit(up_card.image, [627,220])
            pygame.display.flip()
            if len(deck) >0:
                next_card = random.choice(deck)
                c_hand.append(next_card)
                deck.remove(next_card)
            else:
                c_blocked+=1
                if len(c_hand)==0:
                    for card in p_hand:
                        p_kou.append(card)
                        np_kou=np_kou+1
                    blit_p_kou()                        
                    over+=1
        else:
            if len(c_hand)>0:
                selected_card=c_hand[0]
                for card in c_hand:
                    if card.value<selected_card.value:
                        selected_card=card
                c_hand.remove(selected_card)
                nc_kou=nc_kou+1
                c_kou.append(selected_card)
                WBuYao=random.choice(wbuyao)
                channel1.play(WBuYao)
                blit_c_kou()
                ckou=True
                if len(deck) >0:
                    next_card = random.choice(deck)
                    c_hand.append(next_card)
                    deck.remove(next_card)
                else:
                    c_blocked+=1
            else:
                for card in p_hand:
                    p_kou.append(card)
                    np_kou=np_kou+1
                blit_p_kou()
                over+=1
    c_hand1 = c_hand[:]
    c_hand_sorted = []
    nc_hand=0
    suit_cards=[]
    for card in c_hand:
        nc_hand=nc_hand+1
    for i in range(1,nc_hand+1):
        card1 = c_hand1[0]
        for card in c_hand1:
            if card1.value <= card.value:
                card1 = card
        c_hand_sorted.append(card1)
        c_hand1.remove(card1)
    blit_c()
    pygame.display.flip()
    if nc_hand==5:
        if (c_hand_sorted[0].value==27 and c_hand_sorted[1].value==25 and c_hand_sorted[2].value==23 and c_hand_sorted[3].value==21 and c_hand_sorted[4].value==19)or(c_hand_sorted[0].value==28 and c_hand_sorted[1].value==26 and c_hand_sorted[2].value==24 and c_hand_sorted[3].value==22 and c_hand_sorted[4].value==20):
            over+=1
            win=2
            
############################################################################################################################################
#Main Loop
############################################################################################################################################
p_total=c_total=0
game_time=1
volume_file = open("Settings/volume.txt", "r")
volumes = volume_file.readline()
volume_list = volumes.split(',')
volume_file.close
back_file=open("Settings/back.txt","r")
back_id=int(back_file.readline())
back_file.close
control1=MyControlClass([int(volume_list[0]),150])
control2=MyControlClass([int(volume_list[1]),202])
while 1:
    game_done=False
    c_blocked=0
    p_blocked=0
    Blocked=False
    over=0
    win=0
    init_cards()
    n=random.randint(0,1)
    if n==0:
        p_first_play=True
        c_first_play=False
    else:
        p_first_play=False
        c_first_play=True
    pkou=False
    ckou=False
    pygame.mixer.music.load("Sounds/background.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume((control1.rect.left-691)/3.0/90.0)
    channel1.set_volume((control2.rect.left-691)/3.0/90.0)
    channel2.set_volume((control2.rect.left-691)/3.0/90.0)
    channel3.set_volume((control2.rect.left-691)/3.0/90.0)
    channel4.set_volume((control2.rect.left-691)/3.0/90.0)
    channel5.set_volume((control1.rect.left-691)/90.0)
    channel6.set_volume((control2.rect.left-691)/3.0/90.0)
    channel7.set_volume((control1.rect.left-691)/3.0/90.0)
    screen.blit(background,[0,0])
    js_str = "Round  %i"% game_time
    js_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 50)
    js_surf = js_font.render(js_str, 1, (255, 255, 255))
    js_surf_s = js_font.render(js_str, 1, (150, 150, 150))
    jf_str = "You     Computer"
    jf_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 20)
    jf_surf = jf_font.render(jf_str, 1, (255, 255, 255))
    jf_surf_s = jf_font.render(jf_str, 1, (150, 150, 150))
    bf1_str = "%i"%p_total
    bf1_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 40)
    bf1_surf = bf1_font.render(bf1_str, 1, (255, 255, 255))
    bf1_surf_s = bf1_font.render(bf1_str, 1, (150, 150, 150))
    bf2_str = "%i"%c_total
    bf2_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 40)
    bf2_surf = bf2_font.render(bf2_str, 1, (255, 255, 255))
    bf2_surf_s = bf2_font.render(bf2_str, 1, (150, 150, 150))
    you_str = "You"
    you_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 50)
    you_surf = you_font.render(you_str, 1, (255, 255, 255))
    you_surf_s = you_font.render(you_str, 1, (150, 150, 150))
    computer_str = "Computer"
    computer_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 45)
    computer_surf = computer_font.render(computer_str, 1, (255, 255, 255))
    computer_surf_s = computer_font.render(computer_str, 1, (150, 150, 150))
    screen.blit(js_surf_s, [17, 7])
    screen.blit(js_surf_s, [16, 6])
    screen.blit(js_surf, [15, 5])
    screen.blit(jf_surf_s, [1191, 6])
    screen.blit(jf_surf, [1190, 5])
    screen.blit(bf1_surf_s, [1197, 42])
    screen.blit(bf1_surf_s, [1196, 41])
    screen.blit(bf1_surf, [1195, 40])
    screen.blit(bf2_surf_s, [1287, 42])
    screen.blit(bf2_surf_s, [1286, 41])
    screen.blit(bf2_surf, [1285, 40])
    screen.blit(you_surf_s, [1097, 187])
    screen.blit(you_surf_s, [1096, 186])
    screen.blit(you_surf, [1095, 185])
    screen.blit(computer_surf_s, [92, 182])
    screen.blit(computer_surf_s, [91, 181])
    screen.blit(computer_surf, [90, 180])    
    screen.blit(back[back_id],[357,30])
    screen.blit(back[back_id],[492,30])
    screen.blit(back[back_id],[627,30])
    screen.blit(back[back_id],[762,30])
    screen.blit(back[back_id],[897,30])
    screen.blit(chat,[1150,525])
    screen.blit(setting_button,[20,642])
    while not game_done:
        if over>=1:
            game_done=True
        else:
            if n==0:
                player_turn()
                if c_blocked+p_blocked >= 1:
                    Blocked=True
                if over>=1:
                    game_done=True
                if not game_done:
                    computer_turn()
                    if c_blocked+p_blocked >= 1:
                        Blocked=True
                    if over>=1:
                        game_done=True
            else:
                computer_turn()
                if c_blocked+p_blocked >= 1:
                    Blocked=True
                if over>=1:
                    game_done=True
                if not game_done:
                    player_turn()
                    if c_blocked+p_blocked>=1:
                        Blocked=True
                    if over>=1:
                        game_done=True

        if game_done:
            no_card=False
            game_time+=1
            if win==1:
                winner_id=0
                screen.blit(Pjq, [440,650])
            elif win==2:
                winner_id=1
                screen.blit(Cjq, [390,650])
            elif win==3:
                winner_id=1
            else:
                no_card=True
                pygame.draw.rect(screen,[0,70,130],[347,478,666,172])
                pygame.draw.rect(screen,[0,70,130],[357,30,645,170])
                if np_kou<nc_kou:
                    winner_id=0
                elif np_kou>nc_kou:
                    winner_id=1         
                else:
                    c_kou_p=p_kou_p=0
                    for card in c_kou:
                        c_kou_p+=card.value
                    for card in p_kou:
                        p_kou_p+=card.value
                    if c_kou_p>p_kou_p:
                        winner_id=0
                        screen.blit(Pgx, [406,650])
                        Pgx_str = "%i" % np_kou
                        Pgx_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 20)
                        Pgx_surf = Pgx_font.render(Pgx_str, 1, (255, 242, 52))
                        width=Pgx_surf.get_width()
                        screen.blit(Pgx_surf, [562-width/2,650])
                    elif c_kou_p<p_kou_p:
                        winner_id=1
                        screen.blit(Cgx, [383,650])
                        Cgx_str = "%i" % np_kou
                        Cgx_font = pygame.font.Font("Fonts/JOKERMAN.TTF", 20)
                        Cgx_surf = Cgx_font.render(Cgx_str, 1, (255, 242, 52))
                        width=Cgx_surf.get_width()
                        screen.blit(Cgx_surf, [540-width/2,650])
                    else:
                        winner_id=0 
                        screen.blit(pj, [480,650])
            pygame.mixer.music.stop()
            channel5.play(end_sound[winner_id])
            if winner_id==0:
                for i in range(1,51):
                    screen.blit(dark, [0,0])
                    pygame.display.flip()  
                if np_kou>0 and nc_kou>0:                 
                    for j in range(0,5):
                        screen.blit(firework_cover1[back_id],[1000,88])
                        screen.blit(firework_L[j],[1000,88])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    for j in range(0,16):
                        screen.blit(firework_cover1[back_id],[1000,88])
                        screen.blit(firework_L[j+5],[1000,88])
                        screen.blit(firework_cover2[back_id],[40,117])
                        screen.blit(firework_R[j],[40,117])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover1[back_id],[1000,88])
                    for j in range(0,5):
                        screen.blit(firework_cover2[back_id],[40,117])
                        screen.blit(firework_R[j+16],[40,117])
                        screen.blit(firework_cover3[back_id],[1096,105])
                        screen.blit(firework_L[j],[1096,105])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover2[back_id],[40,117])
                    for j in range(0,16):
                        screen.blit(firework_cover3[back_id],[1096,105])
                        screen.blit(firework_L[j+5],[1096,105])
                        screen.blit(firework_cover4[back_id],[102,65])
                        screen.blit(firework_R[j],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover3[back_id],[1096,105]) 
                    for j in range(0,5):
                        screen.blit(firework_cover4[back_id],[102,65])
                        screen.blit(firework_L[j+16],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover4[back_id],[102,65])
                    screen.blit(win_image,[310,160])
                    for i in range(0,2):                   
                        for j in range(0,5):
                            screen.blit(firework_cover1[back_id],[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j],[1000,88])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        for j in range(0,16):
                            screen.blit(firework_cover1[back_id],[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+5],[1000,88])
                            screen.blit(firework_cover2[back_id],[40,117])
                            screen.blit(firework_R[j],[40,117])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover1[back_id],[1000,88])
                        screen.blit(win_image,[310,160])
                        for j in range(0,5):
                            screen.blit(firework_cover2[back_id],[40,117])
                            screen.blit(firework_R[j+16],[40,117])
                            screen.blit(firework_cover3[back_id],[1096,105])
                            screen.blit(firework_L[j],[1096,105])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover2[back_id],[40,117])
                        for j in range(0,16):
                            screen.blit(firework_cover3[back_id],[1096,105])
                            screen.blit(firework_L[j+5],[1096,105])
                            screen.blit(firework_cover4[back_id],[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_R[j],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover3[back_id],[1096,105]) 
                        for j in range(0,5):
                            screen.blit(firework_cover4[back_id],[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+16],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover4[back_id],[102,65])
                        screen.blit(win_image,[310,160])
                        screen.blit(win_continue, [596,490])
                elif np_kou>0 and nc_kou==0:               
                    for j in range(0,5):
                        screen.blit(firework_cover1[back_id],[1000,88])
                        screen.blit(firework_L[j],[1000,88])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    for j in range(0,16):
                        screen.blit(firework_cover1[back_id],[1000,88])
                        screen.blit(firework_L[j+5],[1000,88])
                        screen.blit(firework_cover2_0,[40,117])
                        screen.blit(firework_R[j],[40,117])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover1[back_id],[1000,88])
                    for j in range(0,5):
                        screen.blit(firework_cover2_0,[40,117])
                        screen.blit(firework_R[j+16],[40,117])
                        screen.blit(firework_cover3[back_id],[1096,105])
                        screen.blit(firework_L[j],[1096,105])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover2_0,[40,117])
                    for j in range(0,16):
                        screen.blit(firework_cover3[back_id],[1096,105])
                        screen.blit(firework_L[j+5],[1096,105])
                        screen.blit(firework_cover4_0,[102,65])
                        screen.blit(firework_R[j],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover3[back_id],[1096,105]) 
                    for j in range(0,5):
                        screen.blit(firework_cover4_0,[102,65])
                        screen.blit(firework_L[j+16],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover4_0,[102,65])
                    screen.blit(win_image,[310,160])
                    for i in range(0,2):                   
                        for j in range(0,5):
                            screen.blit(firework_cover1[back_id],[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j],[1000,88])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        for j in range(0,16):
                            screen.blit(firework_cover1[back_id],[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+5],[1000,88])
                            screen.blit(firework_cover2_0,[40,117])
                            screen.blit(firework_R[j],[40,117])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover1[back_id],[1000,88])
                        screen.blit(win_image,[310,160])
                        for j in range(0,5):
                            screen.blit(firework_cover2_0,[40,117])
                            screen.blit(firework_R[j+16],[40,117])
                            screen.blit(firework_cover3[back_id],[1096,105])
                            screen.blit(firework_L[j],[1096,105])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover2_0,[40,117])
                        for j in range(0,16):
                            screen.blit(firework_cover3[back_id],[1096,105])
                            screen.blit(firework_L[j+5],[1096,105])
                            screen.blit(firework_cover4_0,[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_R[j],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover3[back_id],[1096,105]) 
                        for j in range(0,5):
                            screen.blit(firework_cover4_0,[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+16],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover4_0,[102,65])
                        screen.blit(win_image,[310,160])
                        screen.blit(win_continue, [596,490])
                elif np_kou==0 and nc_kou>0:                
                    for j in range(0,5):
                        screen.blit(firework_cover1_0,[1000,88])
                        screen.blit(firework_L[j],[1000,88])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    for j in range(0,16):
                        screen.blit(firework_cover1_0,[1000,88])
                        screen.blit(firework_L[j+5],[1000,88])
                        screen.blit(firework_cover2[back_id],[40,117])
                        screen.blit(firework_R[j],[40,117])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover1_0,[1000,88])
                    for j in range(0,5):
                        screen.blit(firework_cover2[back_id],[40,117])
                        screen.blit(firework_R[j+16],[40,117])
                        screen.blit(firework_cover3_0,[1096,105])
                        screen.blit(firework_L[j],[1096,105])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover2[back_id],[40,117])
                    for j in range(0,16):
                        screen.blit(firework_cover3_0,[1096,105])
                        screen.blit(firework_L[j+5],[1096,105])
                        screen.blit(firework_cover4[back_id],[102,65])
                        screen.blit(firework_R[j],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover3_0,[1096,105]) 
                    for j in range(0,5):
                        screen.blit(firework_cover4[back_id],[102,65])
                        screen.blit(firework_L[j+16],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover4[back_id],[102,65])
                    screen.blit(win_image,[310,160])
                    for i in range(0,2):                   
                        for j in range(0,5):
                            screen.blit(firework_cover1_0,[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j],[1000,88])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        for j in range(0,16):
                            screen.blit(firework_cover1_0,[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+5],[1000,88])
                            screen.blit(firework_cover2[back_id],[40,117])
                            screen.blit(firework_R[j],[40,117])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover1_0,[1000,88])
                        screen.blit(win_image,[310,160])
                        for j in range(0,5):
                            screen.blit(firework_cover2[back_id],[40,117])
                            screen.blit(firework_R[j+16],[40,117])
                            screen.blit(firework_cover3_0,[1096,105])
                            screen.blit(firework_L[j],[1096,105])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover2[back_id],[40,117])
                        for j in range(0,16):
                            screen.blit(firework_cover3_0,[1096,105])
                            screen.blit(firework_L[j+5],[1096,105])
                            screen.blit(firework_cover4[back_id],[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_R[j],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover3_0,[1096,105]) 
                        for j in range(0,5):
                            screen.blit(firework_cover4[back_id],[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+16],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover4[back_id],[102,65])
                        screen.blit(win_image,[310,160])
                        screen.blit(win_continue, [596,490])
                elif np_kou==0 and nc_kou==0:                
                    for j in range(0,5):
                        screen.blit(firework_cover1_0,[1000,88])
                        screen.blit(firework_L[j],[1000,88])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    for j in range(0,16):
                        screen.blit(firework_cover1_0,[1000,88])
                        screen.blit(firework_L[j+5],[1000,88])
                        screen.blit(firework_cover2_0,[40,117])
                        screen.blit(firework_R[j],[40,117])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover1_0,[1000,88])
                    for j in range(0,5):
                        screen.blit(firework_cover2_0,[40,117])
                        screen.blit(firework_R[j+16],[40,117])
                        screen.blit(firework_cover3_0,[1096,105])
                        screen.blit(firework_L[j],[1096,105])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover2_0,[40,117])
                    for j in range(0,16):
                        screen.blit(firework_cover3_0,[1096,105])
                        screen.blit(firework_L[j+5],[1096,105])
                        screen.blit(firework_cover4_0,[102,65])
                        screen.blit(firework_R[j],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover3_0,[1096,105]) 
                    for j in range(0,5):
                        screen.blit(firework_cover4_0,[102,65])
                        screen.blit(firework_L[j+16],[102,65])
                        pygame.display.flip()
                        pygame.time.delay(40)
                    screen.blit(firework_cover4_0,[102,65])
                    screen.blit(win_image,[310,160])
                    for i in range(0,2):                   
                        for j in range(0,5):
                            screen.blit(firework_cover1_0,[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j],[1000,88])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        for j in range(0,16):
                            screen.blit(firework_cover1_0,[1000,88])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+5],[1000,88])
                            screen.blit(firework_cover2_0,[40,117])
                            screen.blit(firework_R[j],[40,117])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover1_0,[1000,88])
                        screen.blit(win_image,[310,160])
                        for j in range(0,5):
                            screen.blit(firework_cover2_0,[40,117])
                            screen.blit(firework_R[j+16],[40,117])
                            screen.blit(firework_cover3_0,[1096,105])
                            screen.blit(firework_L[j],[1096,105])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover2_0,[40,117])
                        for j in range(0,16):
                            screen.blit(firework_cover3_0,[1096,105])
                            screen.blit(firework_L[j+5],[1096,105])
                            screen.blit(firework_cover4_0,[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_R[j],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover3_0,[1096,105]) 
                        for j in range(0,5):
                            screen.blit(firework_cover4_0,[102,65])
                            screen.blit(win_image,[310,160])
                            screen.blit(firework_L[j+16],[102,65])
                            pygame.display.flip()
                            pygame.time.delay(40)
                        screen.blit(firework_cover4_0,[102,65])
                        screen.blit(win_image,[310,160])
                        screen.blit(win_continue, [596,490])
            elif winner_id==1:
                for i in range(1,11):
                    screen.blit(dark, [0,0])
                    pygame.display.flip()
                    pygame.time.delay(5)
                for i in range(1,41):
                    screen.blit(dark, [0,0])
                    screen.blit(lose_image0, [310,160])
                    pygame.display.flip()
                    pygame.time.delay(5)
                for i in range(1,101):
                    screen.blit(lose_image0, [310,160])
                    pygame.display.flip()
                    pygame.time.delay(3)
                screen.blit(lose_image1, [310,160])
                pygame.display.flip()
                pygame.time.delay(50)
                screen.blit(lose_image2, [310,160])
                pygame.display.flip()
                pygame.time.delay(50)
                screen.blit(lose_image3, [310,160])
                pygame.display.flip()
                pygame.time.delay(50)
                screen.blit(lose_image4, [310,160])
                pygame.display.flip()
                pygame.time.delay(50)
                screen.blit(lose_image5, [310,160])
                pygame.display.flip()
                pygame.time.delay(1000)
                screen.blit(lose_continue, [596,490])                   
            pygame.display.flip()
            if winner_id==0:
                p_total+=1
            elif winner_id==1:
                c_total+=1
    go_on=False
    while not go_on:
        choose=False
        move=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEMOTION:
                m_pos = pygame.mouse.get_pos()
                move=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            pos = pygame.mouse.get_pos()
                            choose=True
        if move==True:
            if m_pos[0]>596 and m_pos[0]<762 and m_pos[1]>490 and m_pos[1]<539:
                if winner_id==0:
                    screen.blit(win_continue2, [596,490])
                    pygame.display.flip()
                elif winner_id==1:
                    screen.blit(lose_continue2, [596,490])
                    pygame.display.flip()
            else:
                if winner_id==0:
                    screen.blit(win_continue, [596,490])
                    pygame.display.flip()
                elif winner_id==1:
                    screen.blit(lose_continue, [596,490])
                    pygame.display.flip()
        if choose==True:
            if pos[0]>596 and pos[0]<762 and pos[1]>490 and pos[1]<539:
                go_on=True
                pygame.draw.rect(screen,[0,70,130],[0,0,1360,690],0)
