from pygame import mixer
from _datetime import datetime
from time import time


def soundplay(ply,stopeer):
    mixer.init()
    mixer.music.load(ply)
    while True:
        mixer.music.play()
        a = input("enter stop for stop")
        if  stopeer == a:
            mixer.music.stop()
            break


def mylog(stopper):
    with open("gr.txt","a") as f:
        f.write(f"{stopper} at {datetime.now() }\n")


if __name__ == '__main__':
    init_water = time()
    init_eye = time()
    init_exercise = time()

    secwtr = 60*60
    seceye = 60*30
    secexercise = 60*45
    while True:
        if time()-init_water>secwtr:
            print("enter 'drank' to stop the alarm")
            soundplay("waterdr.mp3","drank")
            mylog(" drank  water")
            init_water = time()
        elif time() - init_eye > seceye:
            print("enter 'done' to stop the alarm")
            soundplay("eyeexer.mp3","done")
            mylog("done eye exercise ")
            init_eye = time()
        elif time() - init_exercise > secexercise:
            print("enter 'done' to stop the alarm")
            soundplay("physiexcercise.mp3","done")
            mylog("done pysical exercise ")
            init_exercise = time()











