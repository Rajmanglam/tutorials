# Assume that a programmer works at the office from 9-5 pm. We have to take care
# of his health and remind him three things,
#
# To drink a total of 3.5-liter water after some time interval between 9-5 pm.
# To do eye exercise after every 30 minutes.
# To perform physical activity after every 45 minutes.

# For Water, the user should enter “Drank”
# For Eye Exercise, the user should enter “EyDone”
# For Physical Exercise, the user should enter “ExDone”

# You will have to manage the clashes between the reminders. Such that no two
# reminders play at the same time.
# Use pygame module to play audio.

#SOLUTION

from pygame import mixer
from time import time
from datetime import datetime

def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def logger(msg):
    with open('log.txt','a') as f:
        f.write(f'{msg}{datetime.now()}')


if __name__=='__main__':
    init_water = time()
    init_exercise = time()
    init_eyes = time()
    water_secs = 4
    eye_secs = 6
    exer_secs = 8

    while True:
        if time() - init_water > water_secs:
            print(f'water drinking time. enter "drank" to stop music')
            music('water.mp3', 'drank')
            init_water = time()
            logger('\nwater drank at')

        if time() - init_eyes > eye_secs:
            print(f'eyes exercise time. enter "eydone" to stop music')
            music('eye exercise.mp3', 'eydone')
            init_eyes =time()
            logger('\neyes exercise done at')

        if time() - init_exercise > exer_secs:
            print(f'exercise time. enter "done" to stop music ')
            music('exercise.mp3', 'done')
            init_exercise =time()
            logger('\nexercise done at')