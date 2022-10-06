from tkinter import CENTER
from pystyle import *
import os, requests, sys, time
import ctypes
import json

def clear():
    os.system("cls")

def setTitle(_str):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")

def design():
    banner = f'''▓█████▄▄▄█████▓ ██░ ██  ██▓ ▄████▄   ▄▄▄       ██▓    
▓█   ▀▓  ██▒ ▓▒▓██░ ██▒▓██▒▒██▀ ▀█  ▒████▄    ▓██▒    
▒███  ▒ ▓██░ ▒░▒██▀▀██░▒██▒▒▓█    ▄ ▒██  ▀█▄  ▒██░    
▒▓█  ▄░ ▓██▓ ░ ░▓█ ░██ ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    
░▒████▒ ▒██▒ ░ ░▓█▒░██▓░██░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒
░░ ▒░ ░ ▒ ░░    ▒ ░░▒░▒░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░
 ░ ░  ░   ░     ▒ ░▒░ ░ ▒ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░
   ░    ░       ░  ░░ ░ ▒ ░░          ░   ▒     ░ ░   
   ░  ░         ░  ░  ░ ░  ░ ░            ░  ░    ░  ░
                           ░                          

            https://discord.gg/asylheim
            https://discord.gg/thestore :)
    '''
    
    xy = print(Colorate.Horizontal(Colors.cyan_to_green, banner))

    return xy


def personalbanner():
    personalbanner = f'''.-=-=-=-=-=-=-=-=-=-=-=-=OOO=-=(_)=-=OOO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
  _______  _______  ______    _______  _______  __    _  _______  ___     
  |       ||       ||    _ |  |       ||       ||  |  | ||   _   ||   |    
  |    _  ||    ___||   | ||  |  _____||   _   ||   |_| ||  |_|  ||   |    
  |   |_| ||   |___ |   |_||_ | |_____ |  | |  ||       ||       ||   |    
  |    ___||    ___||    __  ||_____  ||  |_|  ||  _    ||       ||   |___ 
  |   |    |   |___ |   |  | | _____| ||       || | |   ||   _   ||       |
  |___|    |_______||___|  |_||_______||_______||_|  |__||__| |__||_______|
`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 
    '''

    xx = print(Colorate.Horizontal(Colors.blue_to_cyan, personalbanner))
    return xx

def accountsbanner():
    accountsbanner = f'''.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
  _______  _______  _______  _______  __   __  __    _  _______  _______ 
  |   _   ||       ||       ||       ||  | |  ||  |  | ||       ||       |
  |  |_|  ||       ||       ||   _   ||  | |  ||   |_| ||_     _||  _____|
  |       ||       ||       ||  | |  ||  |_|  ||       |  |   |  | |_____ 
  |       ||      _||      _||  |_|  ||       ||  _    |  |   |  |_____  |
  |   _   ||     |_ |     |_ |       ||       || | |   |  |   |   _____| |
  |__| |__||_______||_______||_______||_______||_|  |__|  |___|  |_______|
`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 
    '''

    xx = print(Colorate.Horizontal(Colors.blue_to_cyan, accountsbanner))
    return xx

def pcbanner():
    pcbanner = f'''.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                             _______  _______ 
                            |       ||       |
                            |    _  ||       |
                            |   |_| ||       |
                            |    ___||      _|
                            |   |    |     |_ 
                            |___|    |_______|
`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 
    '''

    xx = print(Colorate.Horizontal(Colors.blue_to_cyan, pcbanner))
    return xx

def ipbanner():
    ipbanner = f'''.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                               ___   _______ 
                              |   | |       |
                              |   | |    _  |
                              |   | |   |_| |
                              |   | |    ___|
                              |   | |   |    
                              |___| |___|  
`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 
    '''

    xx = print(Colorate.Horizontal(Colors.blue_to_cyan, ipbanner))
    return xx

def screensbanner():
    screensbanner = f'''.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
       _______  _______  ______    _______  _______  __    _  _______ 
       |       ||       ||    _ |  |       ||       ||  |  | ||       |
       |  _____||       ||   | ||  |    ___||    ___||   |_| ||  _____|
       | |_____ |       ||   |_||_ |   |___ |   |___ |       || |_____ 
       |_____  ||      _||    __  ||    ___||    ___||  _    ||_____  |
        _____| ||     |_ |   |  | ||   |___ |   |___ | | |   | _____| |
       |_______||_______||___|  |_||_______||_______||_|  |__||_______|
`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 
    '''

    xx = print(Colorate.Horizontal(Colors.blue_to_cyan, screensbanner))
    return xx


class Ethical:
    def __init__(self):
        os.system("mode 54, 20")
        clear()
        self.author = 'albaner#0001'
        self.version = 1.0
        self.proxies = ''
        self.menu()

    def menu(self):
        design()
        setTitle("[DOX-WRITER] Have fun >< albaner#0001")
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"[Welcome to the Dox-Writer]", 11)))
        print()
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"[if you don't got the INFO just skip]", 5)))
        print()
        time.sleep(3)

        clear()
        os.system("mode 78, 20")
        personalbanner()

        # Personal
        self.vorname = input(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(f"First name > ", 1)))
        self.nachname = input(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(f"Last name > ", 1)))
        self.alter = input(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(f"Age > ", 1)))
        self.geburtsdatum = input(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(f"Birth-Day > ", 1)))

        self.komplettername = self.vorname + " " + self.nachname

        clear()
        personalbanner()
        # Adress
        self.land = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Country > ", 1)))
        self.stadt = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"City > ", 1)))
        self.postleitzahl = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Zip-Code > ", 1)))
        self.straße = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Street > ", 1)))
        self.hausnummer = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Street-Number > ", 1)))

        self.kompletteadresse = self.straße + " " + self.hausnummer + " > " + self.postleitzahl + " " + self.stadt

        # Phone
        clear()
        personalbanner()
        self.Anbieter = input(Colorate.Horizontal(Colors.green_to_yellow, Center.XCenter(f"Phone Host > ", 1)))

        self.nummer = input(Colorate.Horizontal(Colors.green_to_yellow, Center.XCenter(f"Phone-Numer > ", 1)))
        
        self.mailbox = input(Colorate.Horizontal(Colors.green_to_yellow, Center.XCenter(f"MailBox-Code > ", 1)))
        

        self.komplettenummer = self.nummer + " | " + self.Anbieter + " | " + self.mailbox

        clear()
        accountsbanner()
        # Social Media
        self.Mail = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(f"E-Mail > ", 1)))
        self.discord = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(f"Discord Tag > ", 1)))
        self.Tiktok = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(f"Tiktok > ", 1)))
        self.Twitter = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(f"Twitter > ", 1)))
        self.Instagram = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(f"Instagram > ", 1)))
        self.Youtube = input(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(f"Youtube > ", 1)))

        clear()
        pcbanner()
        # PC
        self.hwid = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"HWID > ", 1)))
        self.win_version = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Windows Version > ", 1)))
        self.ProductKey = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Product Key > ", 1)))
        self.PcName = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Pc Name > ", 1)))
        self.HostName = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Host Name > ", 1)))
        self.Antivirus = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Antivirus > ", 1)))
        self.CPU = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"CPU > ", 1)))
        self.RAM = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"RAM > ", 1)))
        self.GPU = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"GPU > ", 1)))
        self.Architectur = input(Colorate.Horizontal(Colors.cyan_to_green, Center.XCenter(f"Architectur > ", 1)))

        # MAC
        self.MAC = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"MAC > ", 1)))
        self.LANIP = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"LAN IP > ", 1)))
        self.WANIP = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"WAN IP > ", 1)))
        self.HostName = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"Host Name > ", 1)))
        self.ASN = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"ASN > ", 1)))
        self.ISP = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"ISP > ", 1)))
        self.Assignemt = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"Assignemt > ", 1)))
        self.Latitude = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"Latitude > ", 1)))
        self.Longitude = input(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(f"Longitude > ", 1)))

        clear()
        screensbanner()
        # Leaks etc.
        print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"If you've a lot of Links then just paste it in Link1, Link2, Link3 ...", 1)))
        self.Face = input(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"Face-Leaks > ", 1)))
        self.family = input(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"Family-Leaks > ", 1)))
        self.Leaks = input(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"ETC > ", 1)))

        self.doxwriter()



    def doxwriter(self):
        doxtext = f'''
                                      ;::::; :;
                                    ;:::::'   :;                                                        https://discord.gg/asylheim
                                  ;:::::;     ;.                                                        https://discord.gg/thestore
                                 ,:::::'       ;           OOO\                                       ______________________________
                                 ::::::;       ;          OOOOO\                                    / \                             \.
                                 ;:::::;       ;         OOOOOOOO                                  |   |    Doxxed by :             |.
                                ,;::::::;     ;'         / OOOOOOO                                  \_ |    Reason :                |.
                               ;:::::::::`. ,,,;.        /  / DOOOOOO                                  |                            |.
                             .';:::::::::::::::::;,     /  /     DOOOO                                 |                            |.
                            ,::::::;::::::;;;;::::;,   /  /        DOOO                                |     Overview :             |.
                           ;`::::::`'::::::;;;::::: ,#/  /          DOOO                               |   - > Personal             |.
                           :`:::::::`;::::::;;::: ;::#  /            DOOO                              |   - > Accounts             |.
                           ::`:::::::`;:::::::: ;::::# /              DOO                              |   - > PC Info              |.
                           `:`:::::::`;:::::: ;::::::#/               DOO                              |   - > IP Info              |.
                            :::`:::::::`;; ;:::::::::##                OO                              |   - > Screens              |.                             
                            ::::`:::::::`;::::::::;:::#                OO                              |   - > Credits              |.
                             `:::::`::::::::::::;'`:;::#                O                              |   _________________________|___                    
                               `:::::`::::::::;' /  / `:#                                              |  /                            /.
                                ::::::`:::::;'  /  /   `#                                              \_/dc__________________________/.





                                                 
                                                                                    >\\\|/<
                                                                                    |_"""_|
                                                                                    (O) (o)          
                                                       .-=-=-=-=-=-=-=-=-=-=-=-=OOO=-=(_)=-=OOO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                                                         _______  _______  ______    _______  _______  __    _  _______  ___     
                                                         |       ||       ||    _ |  |       ||       ||  |  | ||   _   ||   |    
                                                         |    _  ||    ___||   | ||  |  _____||   _   ||   |_| ||  |_|  ||   |    
                                                         |   |_| ||   |___ |   |_||_ | |_____ |  | |  ||       ||       ||   |    
                                                         |    ___||    ___||    __  ||_____  ||  |_|  ||  _    ||       ||   |___ 
                                                         |   |    |   |___ |   |  | | _____| ||       || | |   ||   _   ||       |
                                                         |___|    |_______||___|  |_||_______||_______||_|  |__||__| |__||_______|
                                                       `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'   

                                                   = > Full Name : {self.komplettername}
                                                   
                                                   = > Age       : {self.alter}

                                                   = > Birth-Day : {self.geburtsdatum}
                                                   
                                                   = > Country   : {self.land}

                                                   = > Adress    : {self.kompletteadresse}

                                                   = > Number    : {self.komplettenummer}
 
                                                       .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                                                         _______  _______  _______  _______  __   __  __    _  _______  _______ 
                                                         |   _   ||       ||       ||       ||  | |  ||  |  | ||       ||       |
                                                         |  |_|  ||       ||       ||   _   ||  | |  ||   |_| ||_     _||  _____|
                                                         |       ||       ||       ||  | |  ||  |_|  ||       |  |   |  | |_____ 
                                                         |       ||      _||      _||  |_|  ||       ||  _    |  |   |  |_____  |
                                                         |   _   ||     |_ |     |_ |       ||       || | |   |  |   |   _____| |
                                                         |__| |__||_______||_______||_______||_______||_|  |__|  |___|  |_______|
                                                       `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 

                                                  = > Email   : {self.Mail}
 
                                                  = > Discord : {self.discord}

                                                  = > TikTok  : {self.Tiktok}

                                                  = > Twitter : {self.Twitter}

                                                  = > Insta   : {self.Instagram}

                                                  = > YouTube : {self.Youtube}

                                                       .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                                                                                    _______  _______ 
                                                                                   |       ||       |
                                                                                   |    _  ||       |
                                                                                   |   |_| ||       |
                                                                                   |    ___||      _|
                                                                                   |   |    |     |_ 
                                                                                   |___|    |_______|
                                                       `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 
                                                
                                                  = > HWID        : {self.hwid}

                                                  = > Win Version : {self.win_version}
                         
                                                  = > Product Key : {self.ProductKey}
 
                                                  = > PC Name     : {self.PcName}
 
                                                  = > Host Name   : {self.HostName}

                                                  = > Antivirus   : {self.Antivirus}
                                                
                                                  = > CPU         : {self.CPU}

                                                  = > RAM         : {self.RAM}

                                                  = > GPU         : {self.GPU}
 
                                                  = > Architectur : {self.Architectur}

                                                       .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                                                                                      ___   _______ 
                                                                                     |   | |       |
                                                                                     |   | |    _  |
                                                                                     |   | |   |_| |
                                                                                     |   | |    ___|
                                                                                     |   | |   |    
                                                                                     |___| |___|  
                                                       `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 

                                                   = > MAC Adress : {self.MAC}

                                                   = > LAN IP     : {self.LANIP}

                                                   = > WAN IP     : {self.WANIP}

                                                   = > Host Name  : {self.HostName}

                                                   = > ASN        : {self.ASN}

                                                   = > ISP        : {self.ISP}

                                                   = > Assignment : {self.Assignemt}

                                                   = > Latitude   : {self.Latitude}

                                                   = > Longitude  : {self.Longitude}

                                                       .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                                                              _______  _______  ______    _______  _______  __    _  _______ 
                                                              |       ||       ||    _ |  |       ||       ||  |  | ||       |
                                                              |  _____||       ||   | ||  |    ___||    ___||   |_| ||  _____|
                                                              | |_____ |       ||   |_||_ |   |___ |   |___ |       || |_____ 
                                                              |_____  ||      _||    __  ||    ___||    ___||  _    ||_____  |
                                                               _____| ||     |_ |   |  | ||   |___ |   |___ | | |   | _____| |
                                                              |_______||_______||___|  |_||_______||_______||_|  |__||_______|
                                                       `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 

                                                   = > Face   : {self.Face}

                                                   = > Family : {self.family}

                                                   = > ETC    : {self.Leaks}

                                                       .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
                                                             _______  ______    _______  ______   ___   _______  _______ 
                                                             |       ||    _ |  |       ||      | |   | |       ||       |
                                                             |       ||   | ||  |    ___||  _    ||   | |_     _||  _____|
                                                             |       ||   |_||_ |   |___ | | |   ||   |   |   |  | |_____ 
                                                             |      _||    __  ||    ___|| |_|   ||   |   |   |  |_____  |
                                                             |     |_ |   |  | ||   |___ |       ||   |   |   |   _____| |
                                                             |_______||___|  |_||_______||______| |___|   |___|  |_______|
                                                       `-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' 

                                                                                 * Infos trough *

                                                                                 * Special thanks to * albaner#0001, m0ney#0001, ethischer#7070
                                   _----..................___
 __,,..,-====>       _,.--''------'' |   _____  ______________`''--._
 \      `\   __..--''                |  /::: / /::::::::::::::\      `\
  \       `''                        | /____/ /___ ____ _____::|    .  \
   \      Thanks               ,.... |            `    `     \_|   ( )  |
    `.                       /`     `.\ ,,''`'- ,.----------.._     `   |
      `.                     |        ,'       `               `-.      |
        `-._                 \                                    ``.. /
            `---..............>
        
        '''

        username = self.vorname
        with open(f"{username}DOX.txt", 'w'): pass

        with open(f"{username}DOX.txt", 'w') as yx:
            yx.write(doxtext)

        clear()
        os.system("mode 50, 15")
        thanksbanner = r'''      _______ _                 _        
     |__   __| |               | |       
        | |  | |__   __ _ _ __ | | _____ 
        | |  | '_ \ / _` | '_ \| |/ / __|
        | |  | | | | (_| | | | |   <\__ \
        |_|  |_| |_|\__,_|_| |_|_|\_\___/

            made by albaner#0001
        turkiye Enes27#0001 + Wanted#7777
    supported by m0ney#0001 + ethischer#7070
        '''
        print(Colorate.Horizontal(Colors.red_to_blue, thanksbanner))
        os.system("pause")


Ethical()