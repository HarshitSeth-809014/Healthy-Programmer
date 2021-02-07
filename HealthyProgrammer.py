import datetime
import time
from pygame import mixer


def musicOn(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(30)
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("myLogs.txt", "a") as f:
        f.write(f"{msg} {datetime.datetime.now()}\n")


if __name__ == '__main__':
    init_water = time.time()
    init_eyes = time.time()
    init_exercise = time.time()

    watersecs = 5
    eyesecs = 12
    physecs = 27

    while True:
        if time.time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop alarm: ")
            musicOn("water.mp3", "drank")
            init_water = time.time()
            log_now("Drank water at")
        elif time.time() - init_eyes > eyesecs:
            print("Eye exercise time. Enter 'done eye' to stop alarm: ")
            musicOn("eyes.mp3", "done eye")
            init_eyes = time.time()
            log_now("Done Eye Exercise at")
        elif time.time() - init_exercise > physecs:
            print("Physical Activity time. Enter 'done exercise' to stop alarm: ")
            musicOn("phy.mp3", "done exercise")
            init_exercise = time.time()
            log_now("Done physical exercise at")
