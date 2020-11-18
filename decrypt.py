import subprocess
from pathlib import Path

def DECRYPT(HCAkey,dir):

    HCAkey1 = HCAkey[8:16]
    HCAkey2 = HCAkey[0:8]

    for i in Path(dir).glob("**/*.acb"):
        script = 'acb2wavs ' + str(i) + ' -a ' + HCAkey1 + ' -b ' + HCAkey2 + ' -n wav'
        subprocess.run(script, shell=True)