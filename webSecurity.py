import Tkinter as tk
#from tkinter import ttk 


Welcome = ("--------------Welcome to TOR/ VPN Router.:)--------------\n---Starting a GUI console.\n---Author=Krishna Adhikari-K1514289")
Warning = ("\x1b[31;1m\n\nWARNING: BEFORE STARTING \nCLEAR ALL YOUR BROWSING HISTORY \nTO MINIMISE THE RISK OF LOOSING ANONYMITY!!!\n\n\n\x1b[0m")



print Warning
print Welcome

#importing library
import pygame
from pygame.locals import *
import io
import os
import subprocess
import time
#from data import *

import numpy as np
import urllib
import re
import math

pygame.init()

#setting Colour
white = (255,255,255)
black = (0,0,0)
green = (0,200,0)
bright_Green = (0,255,0)
#Setting Background Image and Icons!!!
display_width = 320
display_height = 240

webSecurityDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Web Security')
clock = pygame.time.Clock()

#buttons
def button(msg,x,y,w,h,ic,ac,bt,action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(webSecurityDisplay, ac,(x,y,w,h))
        if click[0]==1 and action !=None:
            action()
    else:
        pygame.draw.rect(webSecurityDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",16)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    webSecurityDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    webSecurityDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def popupmsg(welcome):
	pop = tk.Tk()
	pop.wm_title("!")
	label = ttk.Label(popup, text=msg, font=smallText)
	label.pack(side="top", fill="x",pady=10)
	B1 =ttk.Button(popup, text="Ok", command = popup.destroy)
	B1.pack()
	


backgroundImg = pygame.image.load('page1_320x240.png')
def background(x,y):
	webSecurityDisplay.blit(backgroundImg, (x,y))
x = (display_width * 0.0)
y = (display_height * 0.0)
background(x,y)

internet_tor_32_logo = pygame.image.load("tor.png")
def torlogo(a,b):
	webSecurityDisplay.blit(internet_tor_32_logo, (a,b))
a = (display_width * 0.05)
b = (display_height * 0.27)
torlogo(a,b)

vpn_Logo = pygame.image.load("network_2.png")
def vpnlogo(x,y):
        webSecurityDisplay.blit(vpn_Logo, (x,y))
x = (display_width * 0.65)
y = (display_height * 0.27)
vpnlogo(x,y)



#Variables of (IP)s
def current_Internal_IP():
	print("---The Original IP you are connected to is:") 
	os.system('curl ipinfo.io/ip')


def wlan0_IP():
	wlan = os.system("ifconfig wlan0|grep -Po 't addr:\K[\d.]+'")	
print ("---Your wlan0 IP is:")
print  wlan0_IP()

def eth0():
	eth = os.system("ifconfig eth0|grep -Po 't addr:\K[\d.]+'")
print("---Your eth0 IP is:")
print eth0()

def vpnTnl():
	vpn = (os.system("ifconfig tun0|grep -Po 't addr:\K[\d.]+'"))
print ("---The VPN IP is:")
print vpnTnl()

def Tor_IP():
	tor = (os.system('curl --socks5 127.0.0.1:9050 http://checkip.amazonaws.com/'))
print("---Your TOR IP is:")
print Tor_IP()

#External IP Connected to Internet
external_IP = urllib.urlopen('http://checkip.dyndns.org').read()
pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
ip = re.search(pattern, external_IP).group()

#Font Used
font = pygame.font.Font("coders_crux.ttf", 18)
Curr_Int_IP = font.render(current_Internal_IP(), True, (white))
ext_IP = font.render(ip, True, (white))

def Tor_on():
	os.system('sudo service tor start')
	print("Starting TOR service")

def Tor_off():
        os.system('sudo service tor stop')
        print(" TOR service stopped")

def VPN_on():
        os.system('sudo service openvpn start')
        print(" VPN service started")

def VPN_off():
        os.system('sudo service openvpn stop')
        print(" VPN service stopped")

def write_hostapdConfig(file):
        data = "ctrl_interface="+hostapdConfig['global']['ctrl_interface']+"\n"
        data += "ieee80211n="+hostapdConfig['global']['ieee80211n']+"\n"
        data += "ctrl_interface_group="+hostapdConfig['global']['ctrl_interface_group']+"\n"
        data += "beacon_int="+hostapdConfig['global']['beacon_int']+"\n"
        data += "interface="+hostapdConfig['global']['interface']+"\n"
        data += "ssid="+hostapdConfig['global']['ssid']+"\n"
        data += "hw_mode="+hostapdConfig['global']['hw_mode']+"\n"
        data += "channel="+hostapdConfig['global']['channel']+"\n"
        data += "auth_algs="+hostapdConfig['global']['auth_algs']+"\n"
        data += "wmm_enabled="+hostapdConfig['global']['wmm_enabled']+"\n"
        data += "eap_reauth_period="+hostapdConfig['global']['eap_reauth_period']+"\n"
        data += "macaddr_acl="+hostapdConfig['global']['macaddr_acl']+"\n"
        data += "ignore_broadcast_ssid="+hostapdConfig['global']['ignore_broadcast_ssid']+"\n"
        data += "wpa="+hostapdConfig['global']['wpa']+"\n"
        data += "wpa_passphrase="+hostapdConfig['global']['wpa_passphrase']+"\n"
        data += "wpa_key_mgmt="+hostapdConfig['global']['wpa_key_mgmt']+"\n"
        data += "wpa_pairwise="+hostapdConfig['global']['wpa_pairwise']+"\n"
        data += "rsn_pairwise="+hostapdConfig['global']['rsn_pairwise']+"\n"

        f = open(file, 'wb')
        f.write(data+"\n")
        f.close()


#Starting Main Loop
def main_loop():
	test = False
	while not test:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				test = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				test = True

		#Calling for functions
		webSecurityDisplay.blit(ext_IP, (55,60))
       
#       		TextRect.center = ((display_width/2),(display_height/2))
#        	webSecurityDisplay.blit(TextSurf, TextRect)
        	button("ON",60,160,30,20,bright_Green,green,Tor_on,Tor_IP)
                button("OFF",60,190,30,20,bright_Green,green,Tor_off,Tor_on)
		button("ON",220,190,30,20,bright_Green,green,VPN_on,vpnTnl)	
		button("OFF",255,190,30,20,bright_Green,green,VPN_off,VPN_off)
		pygame.display.update()
		clock.tick(60)

#Loop
main_loop()

#Quit
pygame.quit()
quit()
