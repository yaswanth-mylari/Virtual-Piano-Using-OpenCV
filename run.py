from pynput.keyboard import Key, Controller
import time
import cv2
import numpy as np 

import random

keyboard = Controller()

def key_q():
    keyboard.press('q')
                #print('a')
    time.sleep(0.05)
    keyboard.release('q')
def key_w():
    keyboard.press('w')
                #print('a')
    time.sleep(0.05)
    keyboard.release('w')

def key_e():
    keyboard.press('e')
                #print('a')
    time.sleep(0.05)
    keyboard.release('e')
def key_r():
    keyboard.press('r')
                #print('a')
    time.sleep(0.05)
    keyboard.release('r')
def key_t():
    keyboard.press('t')
                #print('a')
    time.sleep(0.05)
    keyboard.release('t')
def key_y():
    keyboard.press('y')
                #print('a')
    time.sleep(0.05)
    keyboard.release('y')
def key_u():
    keyboard.press('u')
                #print('a')
    time.sleep(0.05)
    keyboard.release('u')
kamera=cv2.VideoCapture(0)
_,frame1=kamera.read()
frame1=cv2.resize(frame1,(700,700))
g_img1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
_,thresh1=cv2.threshold(g_img1,127,255,cv2.THRESH_BINARY)
#def next_turn():
    #import cv2
while True:
   

        abc,img1=kamera.read()
        img=cv2.resize(img1,(700,700))
        g_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _,thresh=cv2.threshold(g_img,127,255,cv2.THRESH_BINARY)
        img=cv2.rectangle(img,(0,400),(100,400),(0,255,0))
        img=cv2.rectangle(img,(101,400),(200,600),(0,255,0))
        img=cv2.rectangle(img,(201,400),(300,600),(0,255,0))
        img=cv2.rectangle(img,(301,400),(400,600),(0,255,0))
        img=cv2.rectangle(img,(401,400),(500,600),(0,255,0))
        img=cv2.rectangle(img,(501,400),(600,600),(0,255,0))
        img=cv2.rectangle(img,(601,400),(700,600),(0,255,0))
        tre=cv2.bitwise_xor(thresh1,thresh)
        tr1=tre[400:600,0:100]
        tr2=tre[400:600,101:200]
        tr3=tre[400:600,201:300]
        tr4=tre[400:600,301:400]
        tr5=tre[400:600,401:500]
        tr6=tre[400:600,501:600]
        tr7=tre[400:600,601:700]
        #tr8=tre[400:600,301:400]
        s1=np.sum(tr1)
        s2=np.sum(tr2)
        s3=np.sum(tr3)
        s4=np.sum(tr4)
        s5=np.sum(tr5)
        s6=np.sum(tr6)
        s7=np.sum(tr7)
        #s4=np.sum(tr4)
        sum_list=[s1,s2,s3,s4,s5,s6,s7]
        #cv2.imshow('im',img)
        
        
        #label_list=[key_a(),key_d(),key_w(),key_s(),None]
        if np.max(sum_list)>6400:
            if np.argmax(sum_list)==0:
                key_q()
                
            elif np.argmax(sum_list)==1:
                key_w()
            elif np.argmax(sum_list)==2:
                key_e()
            elif np.argmax(sum_list)==3:
                key_r()                
            elif np.argmax(sum_list)==4:
                key_t()              
            elif np.argmax(sum_list)==5:
                key_y()
            elif np.argmax(sum_list)==6:
                key_u()
           
        
        key=cv2.waitKey(200)
        cv2.imshow("orig",img)
        cv2.imshow('tere',tre)
        if key==27:
            break
        
            
                

kamera.release()
cv2.destroyAllWindows()
