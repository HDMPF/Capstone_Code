import pygame
import time
import pigpio
import math
import wave
import random
import contextlib
import struct
import soundfile as sf

# Set LEDs pin
RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24


def set_LEDs(pin, intensity):
    set_PWM_dutycycle(pin, intensity)


def get_random_number():
    return random.randint(0, 255)


def get_length(audio_file):
    with contextlib.closing(wave.open(audiofile,'r')) as file:
        return file.getnframes() / float(file.getframerate())


def get_amplitude(audio_file):
    data, fs = sf.read(audio_file)
    return data, fs

#    waveFile = wave.open(audio_file, 'r')
#    length = waveFile.getnframes()
#    for i in range(0,length):
#        waveData = waveFile.readframes(1)
#        data = struct.unpack("<h", waveData)
#        print(int(data[0]))


def get_amplitude_in_second(data, length):
    return math.floor(len(data)/length)

audiofile = "MissionImpossible.wav"
pi = pigpio.pi()
pygame.mixer.init()
pygame.mixer.music.load(audiofile)
pygame.mixer.music.play()

length = get_length(audiofile)
print("The the length of music is " + str(length)+ " seconds")
data, fs = get_amplitude(audiofile)
print(len(data))
#print(data)
print(fs)

#print(max(map(max,data)))
#print(min(map(min,data)))
##for i in range(len(data)):
##    print(abs(data[i,0]) * 255)
##    print(abs(data[i,1]) * 255)
##    i += 441
    

i = 0
while pygame.mixer.music.get_busy() == True:
    
    intens_left = abs(data[i,0]) * 255
    intens_right = abs(data[i,1]) * 255
    intens_mid = (abs(data[i,0]) + abs(data[i,1]))/2 * 255
    print(intens_left)
    print(intens_right)
    print(intens_mid)

    pi.set_PWM_dutycycle(RED_PIN, intens_left)
    pi.set_PWM_dutycycle(GREEN_PIN, intens_right)
    pi.set_PWM_dutycycle(BLUE_PIN, intens_mid)
    
    i += 4410
    time.sleep(0.1)
    
    # i += 44100
    #time.sleep(1)
    
    #i += 441
    #time.sleep(0.01)
    continue

#while pygame.mixer.music.get_busy() == True:
#    pi.set_PWM_dutycycle(RED_PIN, random.randint(0, 255))
#    pi.set_PWM_dutycycle(GREEN_PIN, random.randint(0, 255))
#    pi.set_PWM_dutycycle(BLUE_PIN, random.randint(0, 255))
#    continue

pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(GREEN_PIN, 0)
pi.set_PWM_dutycycle(BLUE_PIN, 0)
time.sleep(0.5)


