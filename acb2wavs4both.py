import os
import gui
import decrypt
import configparser

### Loading Settings ###
os.chdir(os.path.dirname(os.path.abspath(__file__)))
config_ini = configparser.ConfigParser()
config_ini.read('settings.ini', encoding='utf-8')
read_default = config_ini['DEFAULT']
tmps = []

for i in range(0,3):
    tmp = read_default['line'+str(i)]
    tmps.append(tmp)

if str(tmps[0]) == "GUI" :
    HCAkey,dir  = gui.GUI()
    decrypt.DECRYPT(HCAkey,dir)
else :
    HCAkey = str(tmps[1])
    dir = str(tmps[2])
    decrypt.DECRYPT(HCAkey,dir)