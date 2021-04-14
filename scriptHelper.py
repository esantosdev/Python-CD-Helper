#!/usr/bin/python3
from platform import system as platform_name
from os import system
import ctypes
import time
import tkinter
import tkinter.messagebox
import sys



platforms_dictionary = {
    "Windows": {                              #
                "open" : 'ctypes.windll.WINMM.mciSendStringW(u"open L: type CDAudio alias L_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set L_drive door open", None, 0, None)',
                "close": 'ctypes.windll.WINMM.mciSendStringW(u"open L: type CDAudio alias L_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set L_drive door closed", None, 0, None)'
               },
    "Darwin":  {
                "open" : 'system("drutil tray open")',
                "close": 'system("drutil tray closed")'
               },
    "Linux":   {
                "open" : 'system("eject cdrom")',
                "close": 'system("eject -t cdrom")'
               },
    "NetBSD":  {
                "open" : 'system("eject cd")',
                "close": 'system("eject -t cd")'
               },
    "FreeBSD": {
                "open" : 'system("sudo cdcontrol eject")',
                "close": 'system("sudo cdcontrol close")'
               }
}

print(platform_name())

if platform_name() in platforms_dictionary:
    print("Abrindo")
    exec(platforms_dictionary[platform_name()]["open"])
    time.sleep(1.5)
    print("Fechando")
    time.sleep(0.5)
    exec(platforms_dictionary[platform_name()]["close"])
else:
    print("S.O não suportado")
