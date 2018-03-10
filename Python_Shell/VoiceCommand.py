import speech_recognition as sr
import RPi.GPIO as GPIO
import time
import pigpio

# Set key words for car operations
KEY_WORD_1 = "stop"
KEY_WORD_2 = "go"
KEY_WORD_3 = "turn left"
KEY_WORD_4 = "turn right"

r = sr.Recognizer()
m = sr.Microphone()

#Set push button to stop voice control mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)


#Set LEDs to react with voice rerecognition mode
RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24
pi = pigpio.pi()
pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(RED_PIN, 0)
pi.set_PWM_dutycycle(RED_PIN, 0)
        


try:
    
    # Set threshold
    print("Test envirenment noise...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    
    # Voice recognition
    print("Start voice recognition")
    while True:
        
##        # Set button
##        button = GPIO.input(18)
##        if (button == False):
##            print("End voice control")
##            pi.set_PWM_dutycycle(RED_PIN, 0)
##            pi.set_PWM_dutycycle(RED_PIN, 0)
##            pi.set_PWM_dutycycle(RED_PIN, 0)
##            time.sleep(0.2)
##            break
        
        pi.set_PWM_dutycycle(RED_PIN, 255)
        pi.set_PWM_dutycycle(RED_PIN, 0)
        pi.set_PWM_dutycycle(RED_PIN, 0)
        print("Say the commands!")
        with m as source: audio = r.listen(source)
        
        print("Got it! Now to recognize it...")
        pi.set_PWM_dutycycle(RED_PIN, 0)
        pi.set_PWM_dutycycle(RED_PIN, 255)
        pi.set_PWM_dutycycle(RED_PIN, 0)
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            print("You said {}".format(value))
            if (KEY_WORD_1 in r.recognize_google(audio)) == True:
                
                print("******The Car stops******")
                
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 255)
                time.sleep(2)
            elif (KEY_WORD_2 in r.recognize_google(audio)) == True:
                
                print("******The Car moves******")
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 255)
                time.sleep(2)
            elif (KEY_WORD_3 in r.recognize_google(audio)) == True:
                
                print("******The Car turns left******")
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 255)
                time.sleep(2)
            elif (KEY_WORD_4 in r.recognize_google(audio)) == True:
                
                print("******The Car turns right******")
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 0)
                pi.set_PWM_dutycycle(RED_PIN, 255)
                time.sleep(2)
         
        except sr.UnknownValueError:
            print("Oops! Can't recognize it...")
        except sr.RequestError as e:
            print("Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass