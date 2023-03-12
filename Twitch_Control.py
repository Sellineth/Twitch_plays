#   CODE MADE BY SELLINETH INSPIRED BY DOUGDOUG
#   THIS CODE IF FREE TO USE AND SHARE AS LONG AS YOU GIVE CREDIT

##########################################################

TWITCH_CHANNEL = input("Please type your channel name: ") # Replace this with your Twitch username. Must be all lowercase.

##########################################################

import keyboard
import time
import TwitchPlays_Connection
import pydirectinput
import pyautogui
import vgamepad as vg                      #only needed if playing with controller otherwise leave it with " # " on the start of the line
import concurrent.futures
from TwitchPlays_KeyCodes import *

#import pyttsx3
#import speech_recognition as sr
import random
#import importlib.util

gamepad = vg.VX360Gamepad()              #only needed if playing with controller otherwise leave it with " # " on the start of the line
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

### CONTROLLER KEYS ###

def CONTROLLER_TRIGGERS_SHOULDER(msg,
                    left_trigger,release_left_trigger,
                    right_trigger,hold_right_trigger,release_right_trigger,
                    right_shoulder,left_shoulder):

        ################################################## TRIGGERS ##################################################

        if msg in left_trigger:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)

        if msg in release_left_trigger:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in right_trigger:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.2)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in hold_right_trigger:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in release_right_trigger:
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()


        ################################################## SHOULDERS ##################################################

        if msg in right_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in left_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

def CONTROLLER_BUTTONS(msg,f5_,f9_,
                    button_a,double_a_,hold_a_1sec,button_b,hold_b_1sec,button_x,button_y,
                    back_,start_):

        ################################################## F KEYS ##################################################

        if msg in f5_:
                HoldAndReleaseKey(F5, 0.1)

        if msg in f9_:
                HoldAndReleaseKey(F9, 0.1)

        ################################################## A B X Y ##################################################

        if msg in button_a:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in double_a_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.4)
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in hold_a_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in button_b:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in hold_b_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in button_x :
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in button_y:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        ################################################## START BACK ##################################################

        if msg in back_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()

        if msg in start_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()

def CONTROLLER_DPADS(msg,d_pad_up_,d_pad_down_,d_pad_left_,d_pad_right_):

        ################################################## D PADS ##################################################

        if msg in d_pad_up_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in d_pad_down_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg  in d_pad_left_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg  in d_pad_right_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

def CONTROLLER_ANALOGS(msg,
                    right_analog_up,right_analog_down,right_analog_left,right_analog_right,
                    left_analog_up,left_analog_down,left_analog_left,left_analog_right,
                    auto_walk,stop_walking,
                    l3_,r3_):

        ################################################## RIGHT ANALOG ##################################################

        if msg in right_analog_up:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_down:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_left:
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_right:
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## LEFT ANALOG ##################################################

        if msg in left_analog_up:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_down:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_left:
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_right:
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## AUTO WALK ##################################################

        if msg in auto_walk:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in stop_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## L3 R3 ##################################################

        if msg in l3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        if msg in r3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()

###   GENERIC CONTROLLER   ###

def GENERIC_CONTROLLER(message):

    ############################################################
    f5_ = ["quicksave", "quick save", "save", "f5"]
    f9_ = ["quickload" "quick sload", "load", "f9"]

    right_analog_up = ["lookup", "lup", "look up"]
    right_analog_down = ["lookdown", "ldown", "look down"]
    right_analog_left = ["lookleft", "lleft", "look left", "turnleft"]
    right_analog_right = ["lookright", "lright", "look right", "turnright"]

    left_analog_up = ["forward"]
    left_analog_down = ["backwards"]
    left_analog_left = ["left"]
    left_analog_right = ["right"]

    auto_walk = ["auto walk", "walk"]
    stop_walking = ["stop walking", "stop running"]

    button_a = ["accept", "activate", "a"]
    hold_a_1sec = ["hold a"]
    button_b = ["return", "back", "b"]
    hold_b_1sec = ["hold b"]
    button_x = ["reload", "x"]
    button_y = ["y"]

    left_trigger = ["aim", "left trigger", "lt"]
    release_left_trigger = ["freeaim", "free aim", "faim", "release left trigger", "rlt"]
    right_trigger = ["shoot", "attack", "right trigger", "rt"]

    right_shoulder = ["right shoulder", "rb"]
    left_shoulder = ["left shoulder", "lb"]

    d_pad_up_ = ["dup", "dpadup", "d pad up"]
    d_pad_down_ = ["dup", "dpaddown", "d pad down"]
    d_pad_left_ = ["dleft", "dpadleft", "d pad left"]
    d_pad_right_ = ["dright", "dpadright", "d pad right"]

    l3_ = ["l3"]
    r3_ = ["r3"]

    back_ = ["select"]
    start_ = ["pause", "start"]
    ############################################################
    
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        ################################################## F KEYS ##################################################

        if msg in f5_:
                HoldAndReleaseKey(F5, 0.1)

        if msg in f9_:
                HoldAndReleaseKey(F9, 0.1)

        ################################################## RIGHT ANALOG ##################################################

        if msg in right_analog_up:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_down:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_left:
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_right:
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## LEFT ANALOG ##################################################

        if msg in left_analog_up:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_down:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_left:
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_right:
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## AUTO WALK ##################################################

        if msg in auto_walk:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in stop_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## L3 R3 ##################################################

        if msg in l3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        if msg in r3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()

        ################################################## A B X Y ##################################################

        if msg in button_a:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in hold_a_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in button_b:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in hold_b_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in button_x :
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in button_y:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        ################################################## TRIGGERS ##################################################

        if msg in left_trigger:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)

        if msg in release_left_trigger:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in right_trigger:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.2)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        ################################################## SHOULDERS ##################################################

        if msg in right_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in left_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        ################################################## D PADS ##################################################

        if msg in d_pad_up_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in d_pad_down_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg  in d_pad_left_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg  in d_pad_right_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        ################################################## START BACK ##################################################

        if msg in start_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()

        if msg in back_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))

###   GTAVBLOCK   ###

def GTAVBLOCK(msg):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg == "left":
            HoldAndReleaseKey(A, 2)

        # If the chat message is "right", then hold down the D key for 2 seconds
        if msg == "right":
            HoldAndReleaseKey(D, 2)

        # If message is "drive", then permanently hold down the W key
        if msg == "drive":
            ReleaseKey(S)  # release brake key first
            HoldKey(W)  # start permanently driving

        # If message is "reverse", then permanently hold down the S key
        if msg == "reverse":
            ReleaseKey(W)  # release drive key first
            HoldKey(S)  # start permanently reversing

        # Release both the "drive" and "reverse" keys
        if msg == "stop":
            ReleaseKey(W)
            ReleaseKey(S)

        # Press the spacebar for 0.7 seconds
        if msg == "brake":
            HoldAndReleaseKey(SPACE, 0.7)

        # Press the left mouse button down for 1 second, then release it
        if msg == "shoot":
            pydirectinput.mouseDown(button="left")
            time.sleep(1)
            pydirectinput.mouseUp(button="left")

    except Exception as e:
        print("Encountered exception: " + str(e))

###   MORROWINDKEYBOARD   ###

def MORROWINDKEYBOARD(message):

    ############################################################
    f1_ = ["quick key menu", "quick menu", "f1"]
    f5_ = ["quicksave", "quick save", "save", "f5"]
    f9_ = ["quickload" "quick sload", "load", "f9"]


    esc_key = ["pause", "esc"]
    tab_key = ["tab", "toggle view", "1st person", "3rd person"]

    mouse_move_up = ["lookup", "lup", "look up"]
    mouse_move_down = ["lookdown", "ldown", "look down"]
    mouse_move_left = ["lookleft", "lleft", "look left", "turnleft"]
    mouse_move_right = ["lookright", "lright", "look right", "turnright"]

    w_key = ["forward"]
    s_key = ["backwards"]
    a_key = ["left"]
    d_key = ["right"]

    auto_walk = ["auto walk", "walk"]
    stop_walking = ["stop walking", "stop running"]

    e_key = ["activate", "open", "interact", "talk", "e"]
    f_key = ["ready weapon", "prepare weapon", "f"]
    r_key = ["ready magic", "prepare magic", "r"]
    j_key = ["journal", "j"]
    t_key = ["rest", "wait", "t"]

    shift_key = ["shift"]
    hold_shift_key = ["hold shift", "run"]
    ctrl_key = ["sneak", "ctrl"]
    space_key = ["space", "jump"]
    caps_key = ["toggle run", "toggle walk", "caps", "caps lock"]

    open_braket = ["previous weapon", "["]
    close_braket = ["next weapon", "]"]
    equals_key = ["next spell", "="]
    hyphen_key = ["previous spell", "-"]

    number_0 = ["0"]
    number_1 = ["1"]
    number_2 = ["2"]
    number_3 = ["3"]
    number_4 = ["4"]
    number_5 = ["5"]
    number_6 = ["6"]
    number_7 = ["7"]
    number_8 = ["8"]
    number_9 = ["9"]

    ############################################################

    add_500g = ["#add gold"]
    add_burden_pot = ["#add burden pot", "#add burden potion"]
    add_feather_pot = ["#add feather pot", "#add feather potion"]
    add_fire_shield_port = ["#add fire shield pot", "#add fire shield potion"]
    add_frost_shield_pot = ["#add frost pot", "#add frost potion"]
    add_jump_pot = ["#add jump pot", "#add jump potion"]
    add_levitate_pot = ["#add levitate pot", "#add levitate potion"]
    add_lightning_shield_pot = ["#add lightning shield pot", "#add lightining shield potion"]
    add_slow_fall_pot = ["#add slow fall pot", "#add slow fall potion"]
    add_swift_swim_pot = ["#add swift swim pot", "#add swift swim potion"]
    add_water_breathing_pot = ["#add water breathing pot", "#dd water breathing potion"]
    add_water_walking_pot = ["#add water walking pot", "#add water walking potion"]
    
    add_chamaleon_pot = ["#add chameleon pot", "#add chameleon potion"]
    add_invisibility_pot = ["#add invisibility pot", "#add invisibility potion"]
    add_light_pot = ["#add light pot", "#add light potion"]
    add_night_eye_pot = ["#add night eye pot", "#add night eye potion"]
    add_paralyze_pot = ["#add paralyze pot", "#add paralyze potion"]
    add_silence_pot = ["#add silence pot", "#add silence potion"]
    
    add_almsivi_intervention_pot = ["#add almsivi intervention pot", "#add almsivi intervention potion"]
    add_detect_animal_pot = ["#add detect animal pot", "#add detect animal potion"]
    add_detect_enchantment_pot = ["#add detect enchantment pot", "#add detect enchantment potion"]
    add_detect_key_pot = ["#add detect key pot", "#add detect key potion"]
    add_dispel_pot = ["#add dispel pot", "#add dispel potion"]
    add_mark_pot = ["#add mark pot", "#add mark potion"]
    add_recall_pot = ["#add recall pot", "#add recall potion"]
    add_reflect_pot = ["#add reflect pot", "#add reflect potion"]
    add_spell_absorption_pot = ["#add spell absorption  pot", "#add spell a bsorption  potion"]
    add_telekinesis_pot = ["#add telekinesis pot", "#add telekinesis potion"]
    
    add_cure_blight_disease_pot = ["#add cure blight disease pot", "#add cure blight disease potion"]
    add_cure_common_disease_pot = ["#add cure common disease pot", "#add cure common disease potion"]
    add_cure_paralyzation_pot = ["#add cure paralyzation pot", "#add cure paralyzation potion"]
    add_cure_poison_pot = ["#add cure poison pot", "#add cure poison potion"]
    add_fortify_attack_pot = ["#add fortify attack pot", "#add fortify attack potion"]
    add_fortify_fatigue_pot = ["#add fortify fatigue pot", "#add fortify fatigue potion"]
    add_fortify_health_pot = ["#add fortify health pot", "#add fortify health potion"]
    add_fortify_magicka_pot = ["#add fortify magicka pot", "#add fortify magicka potion"]
    add_resist_common_disease_pot = ["#add resist common disease pot", "#add resist common disease potion"]
    add_resist_fire_pot = ["#add resist fire pot", "#add resist fire potion"]
    add_resist_frost_pot = ["#add resist frost pot", "#add resist frost potion"]
    add_resist_magicka_pot = ["#add resist magicka pot", "#add resist magicka potion"]
    add_resist_poison_pot = ["#add resist poison pot", "#add resist poison potion"]
    add_resist_shock_pot = ["#add resist shock pot", "#add resist shock potion"]
    add_restore_fatigue_pot = ["#add restore fatigue pot", "#add restore fatigue potion"]
    add_restore_health_pot = ["#add restore health pot", "#add restore health potion"]
    add_restore_magicka_pot = ["#add restore magicka pot", "#add restore magicka potion"]

    add_ancient_dagoth_brandy = ["#add Ancient Dagoth Brandy"]
    add_cyrodiilic_brandy = ["#add Cyrodiilic Brandy"]
    add_flin = ["#add Flin"]
    add_greef = ["#add Greef"]
    add_mazte = ["#add Mazte"]
    add_shein = ["#add Shein"]
    add_skooma = ["#add Skooma"]
    add_sujamma = ["#add Sujamma"]
    add_sintage_brandy = ["#add Vintage Brandy"]

    alit_ = ["#spawn_alit", "#spawn alit"]
    ancestor_ghost = ["s#pawn ancestor ghost", "#spawn ghost"]
    ancestor_guardian = ["#spawn ancestor guardian", "#spawn guardian"]
    ascended_sleeper = ["#spawn ascended sleeper"]
    ash_ghoul = ["#spawn ash ghoul"]
    ash_slave = ["#spawn ash slave"]
    ash_vampire = ["#spawn vampire"]
    ash_zombie = ["#spawn  ash zombie"]
    bonelord = ["#spawn  bonelord"]
    bonewalker = ["#spawn bonewalker"]
    centurion_sphere = ["#spawn centurion sphere"]
    centurion_spider = ["#spawn centurion spider"]
    clannfear = ["#spawn clannfear"]
    cliff_racer = ["#spawn cliff racer"]
    corprus_stalker = ["#spawn corprus stalker"]
    daedroth = ["#spawn daedroth"]
    dremora = ["#spawn dremora"]
    dreugh = ["#spawn dreugh"]
    dwarven_ghost = ["#spawn dwarven ghost"]
    atronach_fire = ["#spawn atronach fire"]
    atronach_frost = ["#spawn atronach frost"]
    golden_saint = ["#spawn golden saint"]
    bonewalker_Greater = ["#spawn bonewalker greater"]
    guar_ = ["#spawn guar"]
    hunger_ = ["#spawn hunger"]
    kagouti_ = ["#spawn kagouti"]
    kwama_forager = ["#spawn kwama forager"]
    kwama_queen = ["#spawn Kwama Queen"]
    kwama_warrior = ["#spawn Kwama"]
    kwama_worker = ["#spawn kwama worker"]
    mudcrab_ = ["#spawn mudcrab"]
    netch_ = ["#spawn netch"]
    nix_hound = ["#spawn nix hound", "#spawn nix-hound"]
    ogrim_ = ["#spawn ogrim"]
    rat_ = ["#spawn Rat"]
    scamp_ = ["#spawn scamp"]
    scrib_ = ["#spawn scrib"]
    shalk_ = ["#spawn shalk"]
    skeleton_ = ["#spawn skeleton"]
    slaughterfish_ = ["#spawn slaughterfish"]
    centurion_steam = ["#spawn centurion steam", "#spawn centurion"]
    atronach_storm = ["#spawn atronach_storm"]
    winged_twilight = ["#spawn winged twilight"]

    ############################################################

    add_burden_pot_ = ["p_burden_b", "p_burden_c", "p_burden_s", "p_burden_q", "p_burden_e"]
    add_feather_pot_ = ["p_feather_b", "p_feather_c", "p_feather_q", "p_feather_e"]
    add_fire_shield_port_ = ["p_fire_shield_b", "p_fire_shield_c", "p_fire_shield_s", "p_fire_shield_q", "p_fire_shield_e"]
    add_frost_shield_pot_ = ["p_frost_shield_b", "p_frost_shield_c", "p_frost_shield_s", "p_frost_shield_q", "p_frost_shield_e"]
    add_jump_pot_ = ["p_jump_b", "p_jump_c", "p_jump_s", "p_jump_q", "p_jump_e"]
    add_levitate_pot_ = ["p_levitation_b", "p_levitation_c", "p_levitation_s", "P_Levitation_Q", "p_levitation_e"]
    add_lightning_shield_pot_ = ["p_lightning shield_b", "p_lightning shield_c", "p_lightning shield_s", "p_lightning shield_q", "p_lightning shield_e"]
    add_slow_fall_pot_ = ["p_slowfall_s", "p_drain_agility_q", "p_drain_endurance_q"]
    add_swift_swim_pot_ = ["p_swift_swim_b", "p_swift_swim_c", "p_swift_swim_q", "p_swift_swim_e", "p_drain_intelligence_q", "p_drain_personality_q"]
    add_water_breathing_pot_ = ["p_water_breathing_s"]
    add_water_walking_pot_ = ["p_water_walking_s"]

    add_chamaleon_pot_ = ["p_chameleon_b", "p_chameleon_c", "p_chameleon_s", "p_chameleon_q", "p_chameleon_e"]
    add_invisibility_pot_ = ["p_invisibility_b", "p_invisibility_c", "p_invisibility_s", "p_invisibility_q", "p_invisibility_e"]
    add_light_pot_ = ["p_light_b", "p_light_c", "p_light_s", "p_light_q", "p_light_e"]
    add_night_eye_pot_ = ["p_night-eye_b", "p_night-eye_c", "p_night-eye_s", "p_night-eye_q", "p_night-eye_e"]
    add_paralyze_pot_ = ["p_paralyze_b", "p_paralyze_c", "p_paralyze_s", "p_paralyze_q", "p_paralyze_e"]
    add_silence_pot_ = ["p_silence_b", "p_silence_c", "p_silence_s", "p_silence_q", "p_silence_e"]

    add_almsivi_intervention_pot_ = ["p_almsivi_intervention_s"]
    add_detect_animal_pot_ = ["p_detect_creatures_s"]
    add_detect_enchantment_pot_ = ["p_detect_enchantment_s"]
    add_detect_key_pot_ = ["p_detect_key_s"]
    add_dispel_pot_ = ["p_dispel_s"]
    add_mark_pot_ = ["p_mark_s"]
    add_recall_pot_ = ["p_recall_s"]
    add_reflect_pot_ = ["p_reflection_b", "p_reflection_c", "p_reflection_s", "p_reflection_q", "p_reflection_e"]
    add_spell_absorption_pot_ = ["p_spell_absorption_b", "p_spell_absorption_c", "p_spell_absorption_s", "p_spell_absorption_q", "p_spell_absorption_e"]
    add_telekinesis_pot_ = ["p_telekinesis_s"]

    add_cure_blight_disease_pot_ = ["p_cure_blight_s"]
    add_cure_common_disease_pot_ = ["p_cure_common_s", "p_drain_luck_q", "p_drain_strength_q", "p_drain willpower_q"]
    add_cure_paralyzation_pot_ = ["p_cure_paralyzation_s"]
    add_cure_poison_pot_ = ["p_cure_poison_s", "p_drain_magicka_q", "p_drain_speed_q"]
    add_fortify_attack_pot_ = ["p_fortify_attack_e"]
    add_fortify_fatigue_pot_ = ["p_fortify_fatigue_b", "p_fortify_fatigue_c", "p_fortify_fatigue_s", "p_fortify_fatigue_q", "p_fortify_fatigue_e"]
    add_fortify_health_pot_ = ["p_fortify_health_b", "p_fortify_health_c", "p_fortify_health_s", "p_fortify_health_q", "p_fortify_health_e"]
    add_fortify_magicka_pot_ = ["p_fortify_magicka_b", "p_fortify_magicka_c", "p_fortify_magicka_s", "p_fortify_magicka_q", "p_fortify_magicka_e"]
    add_resist_common_disease_pot_ = ["p_disease_resistance_b", "p_disease_resistance_c", "p_disease_resistance_s", "p_disease_resistance_q", "p_disease_resistance_e"]
    add_resist_fire_pot_ = ["p_fire_resistance_b", "p_fire_resistance_c", "p_fire resistance_s", "p_fire_resistance_q", "p_fire_resistance_e"]
    add_resist_frost_pot_ = ["p_frost_resistance_b", "p_frost_resistance_c", "p_frost_resistance_s", "p_frost_resistance_q", "p_frost_resistance_e"]
    add_resist_magicka_pot_ = ["p_magicka_resistance_b", "p_magicka_resistance_c", "p_magicka_resistance_s", "p_magicka_resistance_q", "p_magicka_resistance_e"]
    add_resist_poison_pot_ = ["p_poison_resistance_b", "p_poison_resistance_c", "p_poison_resistance_s", "p_poison_resistance_q", "p_poison_resistance_e"]
    add_resist_shock_pot_ = ["p_shock_resistance_b", "p_shock_resistance_c", "p_shock_resistance_s", "p_shock_resistance_q", "p_shock_resistance_e"]
    add_restore_fatigue_pot_ = ["p_restore_fatigue_b", "p_restore_fatigue_c", "p_restore_fatigue_s", "p_restore_fatigue_q", "p_restore_fatigue_e"]
    add_restore_health_pot_ = ["p_restore_health_b", "p_restore_health_c", "p_restore_health_s", "p_restore_health_q", "p_restore_health_e"]
    add_restore_magicka_pot_ = ["p_restore_magicka_b", "p_restore_magicka_c", "p_restore_magicka_s", "p_restore_magicka_q", "p_restore_magicka_e"]

    add_ancient_dagoth_brandy_ = ["potion_ancient_brandy"]
    add_cyrodiilic_brandy_ = ["potion_cyro_brandy_01"]
    add_flin_ = ["Potion_Cyro_Whiskey_01"]
    add_greef_ = ["potion_comberry_brandy_01"]
    add_azte_ = ["Potion_Local_Brew_01"]
    add_shein_ = ["potion_comberry_wine_01"]
    add_skooma_ = ["potion_skooma_01"]
    add_sujamma_ = ["potion_local_liquor_01"]
    add_sintage_brandy_ = ["p_vintagecomberrybrandy1"]

    alit_variants = ["alit", "alit_blighted", "alit_diseased"]
    ancestor_ghost_variant = ["ancestor_ghost", "ancestor_mg_wisewoman", "ancestor_ghost_vabdas", "gateway_haunt"]
    ancestor_guardian_variant = ["ancestor_guardian_fgdd", "ancestor_guardian_heler"]
    ascended_sleeper_variant = ["ascended_sleeper", "dagoth fandril", "dagoth felmis", "dagoth garel", "dagoth goral", "dagoth_hlevul", "dagoth irvyn", "dagoth irvyn", "dagoth malan", "dagoth molos", "dagoth rather", "dagoth tanis", "dagoth tanis", "dagoth ulen", "dagoth uvil", "dagoth vaner"]
    ash_ghoul_variant = ["ash_ghoul", "dagoth aladus", "dagoth baler", "dagoth daynil", "dagoth delnus", "dagoth drals", "dagoth draven", "dagoth elam", "dagoth fals", "dagoth fovon", "dagoth galmis", "dagoth girer", "dagoth ienas", "dagoth mendras", "dagoth mulis", "ash_ghoul_mulyn", "dagoth muthes", "dagoth nilor", "dagoth ralas", "dagoth_soler", "ash_ghoul_fgr"]
    ash_slave_variant = ["ash_slave"]
    ash_vampire_variant = ["dagoth araynys", "dagoth gilvoth", "dagoth odros", "dagoth tureynul", "dagoth uthol", "dagoth vemyn"]
    ash_zombie_variant = ["ash_zombie"]
    bonelord_variant = ["bonelord"]
    bonewalker_variant = ["bonewalker", "bonewalker_weak", "Bonewalker_Greater"]
    centurion_sphere_variant = ["centurion_sphere", "centurion_sphere_bbot1", "centurion_sphere_bbot5", "centurion_sphere_bbot6", "centurion_sphere_hts2", "centurion_sphere_hts2", "centurion_sphere_nchur", "centurion_sphere_summon"]
    centurion_spider_variant = ["centurion_spider"]
    clannfear_variant = ["clannfear"]
    cliff_racer_variant = ["cliff racer", "cliff racer_blighted", "cliff racer_diseased"]
    corprus_stalker_variant = ["corprus_stalker"]
    daedroth_variant = ["daedroth", "daedroth_fg_nchur", "deadroth_menta_unique"]
    dremora_variant = ["dremora", "dremora_ttmg", "dremora_ttmg", "dremora_ttpc", "dremora_special_Fyr"]
    dreugh_variant = ["dreugh", "dreugh_koal"]
    dwarven_ghost_variant = ["dwarven ghost", "Dahrk Mezalf", "dwarven ghost_radac"]
    atronach_fire_variant = ["atronach_fire"]
    atronach_frost_variant = ["atronach_frost", "atronach_frost_gwai_uni"]
    golden_saint_variant = ["golden saint", "golden saint_staada"]
    bonewalker_Greater_variant = ["Bonewalker_Greater"]
    guar_variant = ["guar", "guar_feral", "guar_pack", "guar_hrmudcrabnest", "guar_pack_tarvyn_unique", "guar_rollie_unique", "guar_white_unique", "guar_llovyn_unique", "guar_rollie_unique", "guar_white_unique"]
    hunger_variant = ["hunger", "hunger_audenian", "hunger_az_01", "hunger_az_02", "hunger_az_02", "hunger_fghl"]
    kagouti_variant = ["kagouti", "kagouti_blighted", "kagouti_diseased", "kagouti_mating"]
    kwama_forager_variant = ["kwama forager", "kwama forager blighted", "kwama forager"]
    kwama_queen_variant = ["Kwama Queen"]
    kwama_warrior_variant = ["Kwama Warrior", "kwama_warrior_blighted"]
    kwama_worker_variant = ["kwama worker", "kwama worker diseased"]
    mudcrab_variant = ["mudcrab", "mudcrab_unique"]
    netch_variant = ["netch_betty", "netch_betty_ranched", "netch_betty_ilgn", "netch_bull", "netch_bull_ranched", "netch_bull_ilgn", "Netch_Giant_UNIQUE"]
    nix_hound_variant = ["nix-hound", "nix-hound blighted"]
    ogrim_variant = ["ogrim", "ogrim_az", "ogrim titan"]
    rat_variant = ["Rat", "rat_blighted", "rat_cave_fgrh", "rat_cave_hhte1", "rat_cave_hhte2", "rat_diseased", "rat_telvanni_unique", "rat_telvanni_unique_2", "rat_pack_rerla"]
    scamp_variant = ["scamp", "lustidrike", "scamp_creeper"]
    scrib_variant = ["scrib"]
    shalk_variant = ["shalk"]
    skeleton_variant = ["skeleton_vemynal", "worm lord"]
    slaughterfish_variant = ["slaughterfish", "slaughterfish_hr_sfavd", "Slaughterfish_Small"]
    centurion_steam_variant = ["centurion_steam", "centurion_Mudan_unique"]
    atronach_storm_variant = ["atronach_storm", "atronach_storm_az", "atronach_storm_summon", "atronach_storm_ttmk"]
    winged_twilight_variant = ["winged twilight", "winged_twilight_grunda"]

    ############################################################

    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg in f1_:
            HoldAndReleaseKey(F1, 0.1)

        if msg in f5_:
            HoldAndReleaseKey(F5, 0.1)

        if msg in f9_:
            HoldAndReleaseKey(F9, 0.1)

        if msg in mouse_move_left:
            pydirectinput.moveRel(-2000,0, relative=True)

        if msg in mouse_move_right:
            pydirectinput.moveRel(2000,0, relative=True)

        if msg in mouse_move_down:
            pydirectinput.moveRel(0, 300, relative=True)

        if msg in mouse_move_up:
            pydirectinput.moveRel(0, -300, relative=True)

        if msg in esc_key:
            HoldAndReleaseKey(ESC, 0.1)

        if msg in tab_key:
            HoldAndReleaseKey(TAB, 0.1)

        if msg in w_key:
            HoldAndReleaseKey(W, 10)

        if msg in s_key:
            HoldAndReleaseKey(S, 10)

        if msg in a_key:
            HoldAndReleaseKey(A, 10)

        if msg in d_key:
            HoldAndReleaseKey(D, 10)

        if msg in auto_walk:
            HoldAndReleaseKey(Q, 0.1)

        if msg in stop_walking:
            HoldAndReleaseKey(Q, 0.1)

        if msg in e_key:
            HoldAndReleaseKey(E, 0.1)

        if msg in f_key:
            HoldAndReleaseKey(F, 0.1)

        if msg in r_key:
            HoldAndReleaseKey(R, 0.1)

        if msg in j_key:
            HoldAndReleaseKey(J, 0.1)

        if msg in t_key:
            HoldAndReleaseKey(T, 0.1)

        if msg in shift_key:
            HoldAndReleaseKey(LEFT_SHIFT, 0.1)

        if msg in hold_shift_key:
            HoldAndReleaseKey(LEFT_SHIFT, 10)

        if msg in ctrl_key:
            HoldAndReleaseKey(LEFT_CONTROL, 0.1)

        if msg in space_key:
            HoldAndReleaseKey(SPACE, 0.3)

        if msg in caps_key:
            HoldAndReleaseKey(CAPSLOCK, 0.1)

        if msg in open_braket:
            HoldAndReleaseKey(LEFT_BRACKET, 0.1)

        if msg in close_braket:
            HoldAndReleaseKey(RIGHT_BRACKET, 0.1)

        if msg in equals_key:
            HoldAndReleaseKey(EQUALS, 0.1)

        if msg in hyphen_key:
            HoldAndReleaseKey(MINUS, 0.1)

        #########################   SHORTCUTS   #########################

        if msg in number_0:
            HoldAndReleaseKey(ZERO, 0.1)

        if msg in number_1:
            HoldAndReleaseKey(ONE, 0.1)

        if msg in number_2:
            HoldAndReleaseKey(TWO, 0.1)

        if msg in number_3:
            HoldAndReleaseKey(THREE, 0.1)

        if msg in number_4:
            HoldAndReleaseKey(FOUR, 0.1)

        if msg in number_5:
            HoldAndReleaseKey(FIVE, 0.1)

        if msg in number_6:
            HoldAndReleaseKey(SIX, 0.1)

        if msg in number_7:
            HoldAndReleaseKey(SEVEN, 0.1)

        if msg in number_8:
            HoldAndReleaseKey(EIGHT, 0.1)

        if msg in number_9:
            HoldAndReleaseKey(NINE, 0.1)

        #########################   ADD ITEMS   #########################

        if msg == isinstance(add_500g, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write('player->AddItem "Gold_001" 500')
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_burden_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_burden_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_feather_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_feather_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_fire_shield_port, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_fire_shield_port_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_frost_shield_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_frost_shield_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_jump_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_jump_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_levitate_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_levitate_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_lightning_shield_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_lightning_shield_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_slow_fall_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_slow_fall_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_swift_swim_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_swift_swim_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_water_breathing_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_water_breathing_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_water_walking_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_water_walking_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_chamaleon_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_chamaleon_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_invisibility_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_invisibility_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_invisibility_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_invisibility_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_light_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_light_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_night_eye_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_night_eye_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_paralyze_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_silence_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_silence_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_almsivi_intervention_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_almsivi_intervention_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_detect_animal_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_detect_animal_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_detect_enchantment_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_detect_enchantment_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_detect_key_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_detect_key_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_dispel_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_dispel_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_mark_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_mark_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_recall_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_recall_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_reflect_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_reflect_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_spell_absorption_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_spell_absorption_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_telekinesis_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_telekinesis_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_cure_blight_disease_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_cure_blight_disease_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_cure_common_disease_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_cure_common_disease_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_cure_paralyzation_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_cure_paralyzation_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_cure_poison_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_cure_poison_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_fortify_attack_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_fortify_attack_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_fortify_fatigue_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_fortify_fatigue_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_fortify_health_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_fortify_health_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_fortify_magicka_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_fortify_magicka_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_resist_common_disease_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_resist_common_disease_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_resist_fire_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_resist_fire_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_resist_frost_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_resist_frost_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_resist_magicka_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_resist_magicka_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_resist_poison_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_resist_poison_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_resist_shock_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_resist_shock_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_restore_fatigue_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_restore_fatigue_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_restore_health_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_restore_health_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_restore_magicka_pot, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_restore_magicka_pot_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_ancient_dagoth_brandy, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_ancient_dagoth_brandy_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_cyrodiilic_brandy, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_cyrodiilic_brandy_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_flin, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_flin_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_greef, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_greef_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_mazte, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_mazte_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_shein, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_shein_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_skooma, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_skooma_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_sujamma, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_sujamma_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(add_sintage_brandy, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("player->AddItem " + random.choice(add_sintage_brandy_) + " 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        #########################   SPAWN STUFF   #########################

        if msg == isinstance(alit_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write("PlaceAtPC " + random.choice(alitvariants) +" 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ancestor_ghost, list) :
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ancestor_ghost_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ancestor_guardian, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ancestor_guardian_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ascended_sleeper, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ascended_sleeper_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ash_ghoul, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ash_ghoul_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ash_slave, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ash_slave_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ash_vampire, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ash_vampire_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ash_zombie, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ash_zombie_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(bonelord, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(bonelord_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(bonewalker, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(bonewalker_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(centurion_sphere, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(centurion_sphere_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(centurion_spider, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(centurion_spider_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(clannfear, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(clannfear_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(cliff_racer, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(cliff_racer_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(corprus_stalker, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(corprus_stalker_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(daedroth, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(daedroth_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(dremora, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(dremora_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(dreugh, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(dreugh_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(dwarven_ghost, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(dwarven_ghost_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(atronach_fire, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(atronach_fire_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(atronach_frost, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(atronach_frost_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(golden_saint, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(golden_saint_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(bonewalker_Greater, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(bonewalker_Greater_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(guar_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(guar_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(hunger_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(hunger_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(kagouti_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(kagouti_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(kwama_forager, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(kwama_forager_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(kwama_queen, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(kwama_queen_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(kwama_warrior, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(kwama_warrior_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(kwama_worker, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(kwama_worker_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(mudcrab_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(mudcrab_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(netch_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(netch_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(nix_hound, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(nix_hound_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(ogrim_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(ogrim_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(rat_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(rat_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(scamp_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(scamp_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(scrib_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(scrib_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(shalk_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(shalk_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(skeleton_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(skeleton_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(slaughterfish_, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(slaughterfish_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(centurion_steam, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(centurion_steam_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(atronach_storm, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(atronach_storm_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

        if msg == isinstance(winged_twilight, list):
            HoldAndReleaseKey(TILDE, 0.1)
            time.sleep(0.2)
            keyboard.write(f"PlaceAtPC {random.choice(winged_twilight_variant)} 1,5, 1")
            time.sleep(0.1)
            HoldAndReleaseKey(ENTER, 0.1)
            time.sleep(0.1)
            HoldAndReleaseKey(TILDE, 0.1)

    except Exception as e:
        print("Encountered exception: " + str(e))

###   SKYRIMBLOCKKEYBOARD   ###

def SKYRIMBLOCKKEYBOARD(message):

    ############################################################
    f5_ = ["quicksave", "quick save", "save", "f5"]
    f9_ = ["quickload" "quick sload", "load", "f9"]

    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg == "left":
            HoldAndReleaseKey(0x1E, 5)

        if msg == "right":
            HoldAndReleaseKey(0x20, 5)

        if msg == "forward":
            HoldAndReleaseKey(0x11, 5)

        if msg == "backwards":
            HoldAndReleaseKey(0x1F, 5)

        if msg == "shout":
            HoldAndReleaseKey(0x2C, 2)

        if msg == "sneak":
            HoldAndReleaseKey(0x1D, 10)

        if msg == "jump":
            HoldAndReleaseKey(0x39, 2)

        if msg == "fire":
            HoldAndReleaseKey(0x4F, 0.5)

        if msg == "frost":
            HoldAndReleaseKey(0x50, 0.5)

        if msg == "whirlwind":
            HoldAndReleaseKey(0x51, 0.5)

        if msg == "force":
            HoldAndReleaseKey(0x4B, 0.5)

        if msg == "dragonrend":
            HoldAndReleaseKey(0x4C, 0.5)

        if msg == "lookleft":
            pydirectinput.moveRel(-300,0, relative=True)

        if msg == "lookright":
            pydirectinput.moveRel(300,0, relative=True)

        if msg == "lookdown":
            pydirectinput.moveRel(0,3000, relative=True)

        if msg == "lookup":
            pydirectinput.moveRel(0,300, relative=True)

    except Exception as e:
        print("Encountered exception: " + str(e))

###   SKYRIMBLOCKCONTROLER   ###

def SKYRIMBLOCKCONTROLER(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg == "left":
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.reset()

        if msg == "right":
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.reset()

        if msg == "forward":
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.reset()

        if msg == "backwards":
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.reset()

        if msg == "shout":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(2)
            gamepad.reset()

        if msg == "sneak":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.5)
            gamepad.reset()

        if msg == "jump":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(2)
            gamepad.reset()

        if msg == "lookleft":
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        if msg == "lookright":
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        if msg == "lookdown":
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        if msg == "lookup":
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

    except Exception as e:
        print("Encountered exception: " + str(e))

###   FALLOUT4LOCKKEYBOARD   ###

def FALLOUT4LOCKKEYBOARD(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg == "left":
            HoldAndReleaseKey(A, 5)

        if msg == "right":
            HoldAndReleaseKey(D, 5)

        if msg == "forward":
            HoldAndReleaseKey(W, 5)

        if msg == "back":
            HoldAndReleaseKey(S, 5)

        if msg == "sneak":
            HoldAndReleaseKey(LEFT_CONTROL, 0.5)

        if msg == "jump":
            HoldAndReleaseKey(SPACE, 2)

        if msg == "shoot":
            pydirectinput.mouseDown(button=left)
            time.sleep(0.3)
            pydirectinput.mouseUp(button=left)

        if msg == "aim":
            timewait = 30
            while timewait > 0:
                pydirectinput.mouseDown(button=right)
                if msg == "freeaim":
                    pydirectinput.mouseUp(button=right)
                    break
                else:
                    timewait -=1
                    time.sleep(1)
            time.sleep(5)
            pydirectinput.mouseUp(button=right)

        if msg == "lookleft" or msg== "lleft":
            pydirectinput.moveRel(-300,0, relative=True)

        if msg == "lookright" or msg== "lright":
            pydirectinput.moveRel(300,0, relative=True)

        if msg == "lookdown" or msg == "ldown":
            pydirectinput.moveRel(0,3000, relative=True)

        if msg == "lookup" or msg == "lup":
            pydirectinput.moveRel(0,300, relative=True)

    except Exception as e:
        print("Encountered exception: " + str(e))

###   FALLOUT4BLOCKCONTROLER   ###

def FALLOUT4BLOCKCONTROLER(message):

    ############################################################
    f5_ = ["quicksave", "quick save", "save", "f5"]
    f9_ = ["quickload" "quick sload", "load", "f9"]

    right_analog_up = ["lookup", "lup", "look up"]
    right_analog_down = ["lookdown", "ldown", "look down"]
    right_analog_left = ["lookleft", "lleft", "look left", "turnleft"]
    right_analog_right = ["lookright", "lright", "look right", "turnright"]

    left_analog_up = ["forward"]
    left_analog_down = ["backwards"]
    left_analog_left = ["left"]
    left_analog_right = ["right"]

    auto_walk = ["auto walk", "walk"]
    stop_walking = ["stop walking", "stop running"]

    button_a = ["accept", "activate", "loot", "a"]
    hold_a_1sec = ["hold a"]
    button_b = ["return", "back", "pipbot", "b"]
    hold_b_1sec = ["flash light", "light", "hold b"]
    button_x = ["reload", "transfer", "takeall", "take all", "x"]
    button_y = ["jump", "y"]

    left_trigger = ["aim", "block", "left trigger", "lt"]
    release_left_trigger = ["freeaim", "free aim", "faim", "release left trigger", "rlt"]
    right_trigger = ["shoot", "attack", "right trigger", "rt"]

    right_shoulder = ["strongattack", "strong attack", "melee", "right shoulder", "rb"]
    left_shoulder = ["vats", "left shoulder", "lb"]

    d_pad_up_ = ["dup", "dpadup", "d pad up"]
    d_pad_down_ = ["dup", "dpaddown", "d pad down"]
    d_pad_left_ = ["dleft", "dpadleft", "d pad left"]
    d_pad_right_ = ["dright", "dpadright", "d pad right"]

    l3_ = ["sprint", "run", "running", "l3"]
    r3_ = ["sneak", "hide", "crouch""r3"]

    back_ = ["select", "1st person", "3rd  person"]
    start_ = ["pause", "start"]
    ############################################################
    
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        ################################################## F KEYS ##################################################

        if msg in f5_:
                HoldAndReleaseKey(F5, 0.1)

        if msg in f9_:
                HoldAndReleaseKey(F9, 0.1)

        ################################################## RIGHT ANALOG ##################################################

        if msg in right_analog_up:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_down:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_left:
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_right:
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## LEFT ANALOG ##################################################

        if msg in left_analog_up:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_down:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_left:
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_right:
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## AUTO WALK ##################################################

        if msg in auto_walk:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in stop_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## L3 R3 ##################################################

        if msg in l3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        if msg in r3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()

        ################################################## A B X Y ##################################################

        if msg in button_a:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in hold_a_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in button_b:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in hold_b_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in button_x :
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in button_y:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        ################################################## TRIGGERS ##################################################

        if msg in left_trigger:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)

        if msg in release_left_trigger:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in right_trigger:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.2)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        ################################################## SHOULDERS ##################################################

        if msg in right_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in left_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        ################################################## D PADS ##################################################

        if msg in d_pad_up_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in d_pad_down_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg  in d_pad_left_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg  in d_pad_right_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        ################################################## START BACK ##################################################

        if msg in start_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()

        if msg in back_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))

'''def FALLOUT4BLOCKCONTROLER_old(message):
    ############################################################
    save_ = ["quicksave", "quick save", "save"]
    load_ = ["quickload" "quick sload", "load"]
    faim_ = ["freeaim", "free aim", "faim"]
    melee_ = ["strongattack", "strong attack", "melee"]
    jump_ = ["jump", "y"]
    button_b = ["return", "b", "pipboy"]
    dup_ = ["dup", "dpadup", "d pad up"]
    ddown_ = ["dup", "dpaddown", "d pad down"]
    dleft_ = ["dleft", "dpadleft", "d pad left"]
    dright_ = ["dright", "dpadright", "d pad right"]
    button_a = ["loot", "accept", "a", "activate"]
    button_x = ["reload", "transfer", "takeall", "take all", "x"]
    turn_left = ["lookleft", "lleft", "look left", "turnleft"]
    turn_right = ["lookright", "lright", "look right", "turnright"]
    look_down = ["lookdown", "ldown", "look down"]
    look_up = ["lookup", "lup", "look up"]
    sprint_ = ["sprint", "run", "running"]
    sneak_ = ["sneak", "hide", "crouch"]
    aim_ = ["aim", "block"]
    attack_ = ["shoot", "attack"]
    flash_light = ["flash light", "light"]
    select_ = ["select", "1st person", "3rd  person"]
    pause_ = ["pause", "main menu"]
    ############################################################
    
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg in save_:
                HoldAndReleaseKey(F5, 0.1)

        if msg in load_:
                HoldAndReleaseKey(F9, 0.1)

        if "left" in msg:
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if "right" in msg:
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if "forward" in msg:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if "backwards" in msg:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in attack_:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.2)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in aim_:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)

        if msg in faim_:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if "vats" in msg:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        if msg in melee_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in jump_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        if msg in button_b:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in flash_light:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in dup_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in ddown_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg  in dleft_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg  in dright_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        if msg in button_a:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in button_x :
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in turn_left:
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in turn_right:
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in look_down:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in look_up:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if "walk" in msg:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if "stop walking" in msg:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in sprint_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        if msg in sneak_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()

        if msg in pause_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()

        if msg in select_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))
'''

###   DARKESTDUNGEONBLOCKCONTOLLER   ###

def DARKESTDUNGEONBLOCKCONTOLLER(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg == "left":
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "right":
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "forward":
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "backwards":
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "lookleft" or msg == "lleft" or msg == "look left" or msg == "turnleft":
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "lookright" or msg == "lright" or msg == "look right" or msg == "turnright":
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "lookdown" or msg == "ldown" or msg == "look down":
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "lookup" or msg == "lup" or msg == "look up":
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg == "rt":
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg == "releasert" or msg == "release rt":
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg == "lt":
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg == "releaselt" or msg == "release lt":
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg == "l3":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()

        if msg == "lb":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        if msg == "rb":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg == "y":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.reset()

        if msg == "b":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg == "a":
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg == "x":
            gamepzd.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg == "dup" or msg == "dpadup":
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg == "ddown" or msg == "dpaddown":
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg == "dleft" or msg == "dpadleft":
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg == "dright" or msg == "dpadright":
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))

###   TERRARIABLOCKKEYBOAR   ###

def TERRARIABLOCKKEYBOAR(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg == "left":
            HoldAndReleaseKey(A, 5)

        if msg == "right":
            HoldAndReleaseKey(D, 5)

        if msg == "up":
            HoldAndReleaseKey(W, 5)

        if msg == "down":
            HoldAndReleaseKey(S, 5)

        if msg == "jump":
            HoldAndReleaseKey(SPACE, 0.3)

        if msg == "grapple":
            HoldAndReleaseKey(E, 0.1)

        if msg == "auto select" or msg == "autoselect":
            HoldAndReleaseKey(LEFT_SHIFT, 0.1)

        if msg == "smartcursor" or msg == "smartcursor":
            HoldAndReleaseKey(LEFT_CONTROL, 0.1)

        if msg == "aquickmount" or msg == "quick mount" or msg == "mount":
            HoldAndReleaseKey(R, 0.1)

        if msg == "aquickheal" or msg == "quick heal" or msg == "heal":
            HoldAndReleaseKey(H, 0.1)

        if msg == "aquickmana" or msg == "quick mana" or msg == "mana":
            HoldAndReleaseKey(J, 0.1)

        if msg == "aquickbuff" or msg == "quick buff" or msg == "buff":
            HoldAndReleaseKey(B, 0.1)

        if msg == "throw" or msg == "discard":
            HoldAndReleaseKey(T, 0.1)

        if msg == "inventory":
            HoldAndReleaseKey(ESC, 0.1)

        if msg == "chat":
            HoldAndReleaseKey(ENTER, 0.1)

        if msg == "zoom in" or msg == "zoomin" or msg == "zoom+" or msg == "zoom +":
            HoldKey(RIGHT_SHIFT)
            HoldAndReleaseKey(NUMPAD_PLUS, 0.5)
            ReleaseKey(RIGHT_SHIFT)

        if msg == "zoom out" or msg == "zoomout" or msg == "zoom-" or msg == "zoom -":
            HoldKey(RIGHT_SHIFT)
            HoldAndReleaseKey(NUMPAD_MINUS, 0.5)
            ReleaseKey(RIGHT_SHIFT)

        if msg == "zoom in map" or msg == "zoominmap" or msg == "zoom+map" or msg == "zoom + map":
            HoldAndReleaseKey(NUMPAD_PLUS, 0.5)

        if msg == "zoom out map" or msg == "zoomoutmap" or msg == "zoom-map" or msg == "zoom - map":
            HoldAndReleaseKey(NUMPAD_MINUS, 0.5)

        if msg == "map":
            HoldAndReleaseKey(M, 0.5)

        if msg == "changemap" or msg == "change map" or msg == "change map style" or msg == "map style" or msg == "changemapstyle" or msg == "mapstyle":
            HoldAndReleaseKey(TAB, 0.5)

        if msg == "use" or msg == "attack":
            pydirectinput.mouseDown(button="left")
            time.sleep(0.1)
            pydirectinput.mouseUp(button="left")

        if msg == "interact" or msg == "open" or msg == "activate":
            pydirectinput.mouseDown(button="right")
            time.sleep(0.1)
            pydirectinput.mouseUp(button="right")

        if msg == "mouse wheel +" or msg == "mousewheel+" or msg == "mousewheelup" or msg == "mouse wheel up":
            HoldAndReleaseKey(MOUSE_WHEEL_UP, 0.5)

        if msg == "mouse wheel -" or msg == "mousewheel-" or msg == "mousewheeldown" or msg == "mouse wheel down":
            HoldAndReleaseKey(MOUSE_WHEELDOWN, 0.5)

        if msg == "1" or msg == "hotbar1" or msg == "hot bar 1" or msg == "item1" or msg == "item 1":
            HoldAndReleaseKey(1, 0.1)

        if msg == "2" or msg == "hotbar2" or msg == "hot bar 2" or msg == "item2" or msg == "item 2":
            HoldAndReleaseKey(2, 0.1)

        if msg == "3" or msg == "hotbar3" or msg == "hot bar 3" or msg == "item3" or msg == "item 3":
            HoldAndReleaseKey(3, 0.1)

        if msg == "4" or msg == "hotbar4" or msg == "hot bar 4" or msg == "item4" or msg == "item 4":
            HoldAndReleaseKey(4, 0.1)

        if msg == "5" or msg == "hotbar5" or msg == "hot bar 5" or msg == "item5" or msg == "item 5":
            HoldAndReleaseKey(5, 0.1)

        if msg == "6" or msg == "hotbar6" or msg == "hot bar 6" or msg == "item6" or msg == "item 6":
            HoldAndReleaseKey(6, 0.1)

        if msg == "7" or msg == "hotbar7" or msg == "hot bar 7" or msg == "item7" or msg == "item 7":
            HoldAndReleaseKey(7, 0.1)

        if msg == "8" or msg == "hotbar8" or msg == "hot bar 8" or msg == "item8" or msg == "item 8":
            HoldAndReleaseKey(8, 0.1)

        if msg == "9" or msg == "hotbar9" or msg == "hot bar 9" or msg == "item9" or msg == "item 9":
            HoldAndReleaseKey(9, 0.1)

        if msg == "0" or msg == "hotbar0" or msg == "hot bar 0" or msg == "item0" or msg == "item 0":
            HoldAndReleaseKey(0, 0.1)

        if msg == "hud" or msg == "togglehud" or msg == "toggle hud":
            HoldAndReleaseKey(F11, 0.1)

        if msg == "lookleft":
            pydirectinput.moveRel(-300,0, relative=True)

        if msg == "lookright":
            pydirectinput.moveRel(300,0, relative=True)

        if msg == "lookdown":
            pydirectinput.moveRel(0,3000, relative=True)

        if msg == "lookup":
            pydirectinput.moveRel(0, 300, relative=True)

    except Exception as e:
        print("Encountered exception: " + str(e))

###   CYBERPUNK2077BLOCKKEYBOARD   ###

def CYBERPUNK2077BLOCKKEYBOARD(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        if msg == "quicksave" or msg == "quick save" or msg == "save":
            HoldAndReleaseKey(F5, 0.1)

        if msg == "quickload" or msg == "quick sload" or msg == "load":
            HoldAndReleaseKey(F9, 0.1)

        ################################################       MOVEMENT        #################################################

        if msg == "left" or msg == "a":
            HoldAndReleaseKey(A, 5)

        if msg == "right" or msg == "d":
            HoldAndReleaseKey(D, 5)

        if msg == "forward" or msg == "w":
            HoldAndReleaseKey(W, 5)

        if msg == "back" or msg == "s":
            HoldAndReleaseKey(S, 5)

        ################################################       CAMERA          #################################################

        if msg =="lookleft" or msg =="lleft":
            pydirectinput.moveRel(-300, 0, relative=True)

        if msg == "lookright" or msg == "lright":
            pydirectinput.moveRel(300, 0, relative=True)

        if msg == "lookdown" or msg == "ldown":
            pydirectinput.moveRel(0, 3000, relative=True)

        if msg == "lookup" or msg == "lup":
            pydirectinput.moveRel(0, 300, relative=True)

        ################################################       MOUSE          #################################################

        if msg == "shoot" or msg == "cannon" or msg == "right click" or msg == "rightclick":
            pydirectinput.mouseDown(button=left)
        time.sleep(0.1)
        pydirectinput.mouseUp(button=left)

        if msg == "aim":
            timewait = 30
        while timewait > 0:
            pydirectinput.mouseDown(button=right)
            if msg == "freeaim" or msg == "free aim" or msg == "faim":
                pydirectinput.mouseUp(button=right)
                break
            else:
                timewait -= 1
                time.sleep(1)
        time.sleep(5)
        pydirectinput.mouseUp(button=right)
        if msg == "launcher" or msg == "left click" or msg == "leftclick":
            pydirectinput.mouseDown(button=right)
            time.sleep(0.1)
            pydirectinput.mouseUp(button=right)

        if msg == "zoom in" or msg == "zoomin" or msg == "next weapon" or msg == "nextweapon" or msg == "mousewheelup" or msg == "mouse wheel up" or msg == "mousewheel up":
            pydirectinput.mouseDown(button=MOUSE_WHEEL_UP)
            time.sleep(0.5)
            pydirectinput.mouseDown(button=MOUSE_WHEEL_UP)

        if msg == "zoom out" or msg == "zoomout" or msg == "previous weapon" or msg == "preveiousweapon" or msg == "mousewheeldown" or msg == "mouse wheel down" or msg == "mousewheel down":
            pydirectinput.mouseDown(button=MOUSE_WHEEL_DOWN)
            time.sleep(0.5)
            pydirectinput.mouseDown(button=MOUSE_WHEEL_DOWN)

        if msg == "tag" or msg == "use gadget" or msg == "usegadget" or msg == "gadget" or msg == "reverse camera" or msg == "reversecamera" or msg == "middlemouse" or msg == "middle mouse":
            pydirectinput.mouseDown(button=MIDDLE_MOUSE)
            time.sleep(0.1)
            pydirectinput.mouseDown(button=MIDDLE_MOUSE)

            ##############################################       SPECIAL KEYS        ###############################################

        if msg == "pause braindance" or msg == "pausebraindance":
            HoldAndReleaseKey(SPACE, 0.1)

        if msg == "jump" or msg == "space":
            HoldAndReleaseKey(SPACE, 0.5)

        if msg == "handbreak" or msg == "hand break":
            HoldAndReleaseKey(SPACE, 5)

        if msg == "changebraindancelayer" or msg == "changebraindancelayer" or msg == "leftshift" or msg == "left shift":
            HoldAndReleaseKey(LEFT_SHIFT, 0.1)

        if msg == "sprint":
            HoldAndReleaseKey(RIGHT_SHIFT, 5)

        if msg == "analysis mode" or msg == "analysismode" or msg == "tab":
            HoldAndReleaseKey(TAB, 0.1)

        if msg == "scan" or msg =="holdtab":
            HoldAndReleaseKey(TAB, 5)

        if msg == "cycle weapon" or msg == "cycleweapon" or msg == "cycle lights" or msg == "cyclelights" or msg == "alt":
            HoldAndReleaseKey(LEFT_ALT, 0.1)

        if msg == "horn" or msg == "smokescreen" or msg == "ctrl":
            HoldAndReleaseKey(LEFT_CONTROL, 1)

        if msg == "smokescreen":
            HoldAndReleaseKey(LEFT_CONTROL, 0.1)

        ##############################################       NORMAL KEYS         ###############################################

        if msg == "fastforward braindance" or msg == "fastforwardbraindance" or msg == "cyberware systems" or msg == "cyberwaresystems" or msg == "e":
            HoldAndReleaseKey(E, 0.1)

        if msg == "quick attack" or msg == "quickattack" or msg == "cycle camera" or msg == "cyclecamera" or msg == "q":
            HoldAndReleaseKey(Q, 0.1)

        if msg == "rewind braindance" or msg == "rewindbraindance":
            HoldAndReleaseKey(Q, 5)

        if msg == "restart braindance" or msg == "restartbraindance" or msg == "reload" or msg == "radio" or msg =="r":
            HoldAndReleaseKey(R, 0.1)

        if msg == "exit braindance" or msg == "exitbraindance" or msg == "use consumable" or msg == "useconsumable" or msg == "use item" or msg == "useitem" or msg == "x":
            HoldAndReleaseKey(X, 0.1)

        if msg == "open phone" or msg == "openphone" or msg == "t":
            HoldAndReleaseKey(T, 0.1)

        if msg == "open notifications" or msg == "opennotifications" or msg == "quickhack details" or msg == "quickhackdetails" or msg == "z":
            HoldAndReleaseKey(Z, 0.1)

        if msg == "open photo mode" or msg == "openphotomode" or msg == "n":
            HoldAndReleaseKey(N, 0.1)

        if msg == "exit vehicle" or msg == "exitvehicle" or msg == "f":
            HoldAndReleaseKey(F, 0.1)

        if msg == "call vehicle" or msg == "callvehicle" or msg == "v":
            HoldAndReleaseKey(V, 0.1)

        if msg == "draw weapon" or msg == "drawweapon" or msg == "withdraw weapon" or msg == "withdrawweapon" or msg == "b":
            HoldAndReleaseKey(B, 0.5)

        ################################################       NUMBERS         #################################################

        if msg == "1" or msg == "first weapon" or msg == "firstweapon" or msg == "previous item" or msg == "previousitem":
            HoldAndReleaseKey(NUMPAD_1, 0.1)

        if msg == "2" or msg == "second weapon":
            HoldAndReleaseKey(NUMPAD_2, 0.1)

        if msg == "3" or msg == "third weapon" or msg == "thirdweapon" or msg == "next item" or msg == "nextitem":
            HoldAndReleaseKey(NUMPAD_3, 0.1)

        if msg == "4" or msg == "fists" or msg == "melee":
            HoldAndReleaseKey(NUMPAD_4, 0.1)

        ##################################################       DRIVING       #################################################

        if msg == "drive":
            HoldKey(W)

        if msg == "stop":
            ReleaseKey(W)

        if msg == "drive back" or msg == "driveback":
            HoldKey(S)

        if msg == "stop":
            ReleaseKey(S)

    except Exception as e:
        print("Encountered exception: " + str(e))

###   CYBERPUNK2077BLOCKCONTROLER   ###

def CYBERPUNK2077BLOCKCONTROLER(message):

    ###############################################       LISTS TO CALL       ############################################

    save_ = (["save", "quick save", "quicksave"])
    load_ = (["load", "quick load", "quickload"])
    dpadup_ = (["dpadup", "dpad up", "zoom in", "zoomin", "use item", "useitem", "heal"])
    dpaddown_ = (["dpaddown", "zoom out", "zoomout"])
    dpadleft_ = (["left dpad", "dpad left", "dleft", "flashlight", "dpadleft", "nitifications", "text", "message"])
    call_car = (["call car", "callcar", "call vehicle", "callvehicle"])
    garage_ = (["garage", "car list", "carlist", "vahicle list", "vahiclelist"])
    aim_ = (["aim", "hold left trigger", "holdlefttrigger", "hleft trigger", "hlefttrigger", "left trigger", "lefttrigger"])
    faim_ = (["free aim", "freeaim", "faim"])
    shoot_ = (["shoot", "right trigger", "righttrigger", "rt"])
    holdrb_ = (["hold rb", "holdrb", "hrb", "aim grenade", "aimgrenade"])
    releaserb_ = (["release rb", "release rb", "release grenade", "releasegrenade"])
    quickrb_ = (["quick rb", "rb", "grenade", "quick grenade", "throw grenade", "throwgrenade"])
    holdlb_ = (["scan mode", "scanmode", "hold lb", "hold lb", "hlb"])
    a_button = (["loot", "click", "jump", "a"])
    x_button = (["reload", "select", "confirm"])
    y_button = (["draw", "draw weapon", "drawweapon", "draw gun", "draw gun"])
    double_y = (["holster", "holster weapon", "holsterweapon", "holster gun", "holstergun", "double y", "doubley"])
    quick_menu = (["quick access menu", "quickaccessmenu", "quick menu", "quickmenu", "weapon wheel", "weaponwheel", "hold y", "holdy", "hy"])
    b_button = (["return", "sneak", "stand", "b"])
    photo_mode = (["photo mode", "photomode", "r3+l3", "l3+r3"])
    stop_driving = (["stop driving", "stopdriving", "release accelerator", "disable autopilot"])
    autopilot_ = (["autopilot", "auto pilot", "start driving", "startdriving", "drive", "accelerate", "accelerator"])
    leave_car = (["leave car", "leavecar", "dismount"])
    stop_walking = (["stop waling", "stopwalking", "stop running", "stoprunning"])
    start_walking = (["start walking", "startwalking", "walk"])
    run_ = (["run", "start running", "startrunning"])

    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        ###############################################    START OF THE COMMANDS   ###########################################

        if ("test" in msg):
            print("it's working")

        if msg in save_:
            HoldAndReleaseKey(F5, 0.1)

        if msg in load_:
            HoldAndReleaseKey(F9, 0.1)

        ################################################       MOVEMENT        #################################################

        if ("left" in msg):
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("right" in msg):
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("forward" in msg):
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("backwards" in msg):
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################       CAMERA          #################################################

        if ("look left" in msg):
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("look right" in msg):
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("look down" in msg):
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("look up" in msg):
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################       D PADS          #################################################

        if msg in dpadup_:
            gamepad.press_button(button=vb.vb.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.vb.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in dpaddown_:
        #if ("dpaddown" in msg) or ("zoom out" in msg):
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if ("phone" in msg):
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg in dpadleft_:
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg in call_car:
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        if msg in garage_:
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        ################################################       TRIGGERS        #################################################

        if msg in aim_:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(10)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in faim_:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in shoot_:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.1)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if ("block" in msg):
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        ################################################       BUMPERS         #################################################

        if msg in holdrb_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(10)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in releaserb_:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in quickrb_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if ("quick scan" in msg):
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        if msg in holdlb_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(30)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        ################################################       A X Y B         #################################################

        if msg in a_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in x_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in y_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()

        if msg in double_y:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()

        if msg in quick_menu:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(5)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()

        if msg in b_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        ###################################################       R3/L3       ##################################################

        if msg in photo_mode:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        ###################################################       DRIVE       ##################################################

        if msg in stop_driving:
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in autopilot_:
            gamepad.left_trigger_float(value_float=0.0)
            gamepad.right_trigger_float(value_float=0.5)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(10)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if ("break" in msg):
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(2)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if ("reverse" in msg):
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.left_trigger_float(value_float=0.5)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(10)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in leave_car:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        ###################################################       WALK        ##################################################

        if msg in stop_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in start_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in run_:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(1)
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))

###   DRAKENGARD 3   ###

def DRAKENGARD3(message):

    ###############################################       LISTS TO CALL       ############################################

    save_ = (["save", "quick save", "quicksave"])
    #! load_ = (["load", "quick load", "quickload"])
    dpadup_ = (["dpadup", "dpad up", "combo list", "combolist"])
    dpaddown_ = (["dpaddown", "dpad down", "item list", "itemlist"])
    #! dpadleft_ = (["left dpad", "dpad left", "dleft", "flashlight", "dpadleft", "nitifications", "text", "message"])
    quickrb_ = (["quick rb", "rb", "dash", "dodge"])
    quicklb_ = (["quicklrb", "lrb", "lock-on", "lock on", "lock camera", "lockcamera", "lockon"])
    a_button = (["jump", "a"])
    x_button = (["reload", "select", "confirm"])
    y_button = (["draw", "draw weapon", "drawweapon", "draw gun", "draw gun"])
    double_y = (["holster", "holster weapon", "holsterweapon", "holster gun", "holstergun", "double y", "doubley"])
    b_button = (["return", "b"])
    hold_b = (["shield", "hb"])
    stop_walking = (["stop waling", "stopwalking", "stop"])
    start_walking = (["start walking", "startwalking", "walk"])
    rising_spinslash = (["rising spinslash", "risingspinslash", "rising spin slash", "risingspin slash"])
    forward_spinslash = (["forward spinslash", "forwardspinslash", "forward spin slash", "forwardspin slash"])
    maximum_spinslash = (["maximum spinslash", "maximumspinslash", "maximum spin slash", "maximumspin slash"])
    aerial_3hit = (["aerial 3 hit", "aerial3hit", "aerial 3hit", "aerial3 hit"])
    r3 = (["reset camera", "resetcamera", "camera reset", "camerareset"])
    l3 = (["change minimap", "changeminimap", "change mini map", "changemini map"])
    start_(["start"])
    select_ = (["back", "select"])
    pause_emulation = (["pause emulation", "pauseemulaion", "pause emulator", "pauseemulator"])

    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        ###############################################    START OF THE COMMANDS   ###########################################

        if ("test" in msg):
            print("it's working")

        if msg in save_:
            HoldAndReleaseKey(F5, 0.1)

        if msg in load_:
            HoldAndReleaseKey(F9, 0.1)

        ################################################       MOVEMENT        #################################################

        if ("left" in msg):
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("right" in msg):
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("forward" in msg):
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("backwards" in msg):
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################       CAMERA          #################################################

        if ("look left" in msg):
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("look right" in msg):
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("look down" in msg):
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if ("look up" in msg):
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################       D PADS          #################################################

        if msg in dpadup_:
            gamepad.press_button(button=vb.vb.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.vb.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in dpaddown_:
        #if ("dpaddown" in msg) or ("zoom out" in msg):
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if ("phone" in msg):
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg in dpadleft_:
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg in call_car:
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        if msg in garage_:
            gamepad.press_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vb.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        ################################################       TRIGGERS        #################################################

        if msg in aim_:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(10)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in faim_:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in shoot_:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.1)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if ("block" in msg):
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        ################################################       BUMPERS         #################################################

        if msg in holdrb_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(10)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in releaserb_:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in quickrb_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if ("quick scan" in msg):
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        if msg in holdlb_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(30)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        ################################################       A X Y B         #################################################

        if msg in a_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in x_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in y_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()

        if msg in double_y:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()

        if msg in quick_menu:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(5)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()

        if msg in b_button:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        ###################################################       R3/L3       ##################################################

        if msg in photo_mode:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        ###################################################       DRIVE       ##################################################

        if msg in stop_driving:
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in autopilot_:
            gamepad.left_trigger_float(value_float=0.0)
            gamepad.right_trigger_float(value_float=0.5)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(10)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if ("break" in msg):
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(2)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if ("reverse" in msg):
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.left_trigger_float(value_float=0.5)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(10)
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in leave_car:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        ###################################################       WALK        ##################################################

        if msg in stop_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in start_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in run_:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(1)
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))

###   DYING LIGHT   ###

def DYINGLIGHT(message):

    ############################################################
    f5_ = ["quicksave", "quick save", "save", "f5"]
    f9_ = ["quickload" "quick sload", "load", "f9"]

    right_analog_up = ["lookup", "lup", "look up"]
    right_analog_down = ["lookdown", "ldown", "look down"]
    right_analog_left = ["lookleft", "lleft", "look left", "turnleft"]
    right_analog_right = ["lookright", "lright", "look right", "turnright"]

    left_analog_up = ["forward"]
    left_analog_down = ["backwards"]
    left_analog_left = ["left"]
    left_analog_right = ["right"]

    auto_walk = ["auto walk", "walk"]
    stop_walking = ["stop walking", "stop running"]

    button_a = ["accept", "activate", "survival sense", "sense", "a"]
    hold_a_1sec = ["use consumable", "hold a"]
    button_b = ["return", "crouch", "b"]
    hold_a_1sec = []
    button_x = ["reload", "use", "x"]
    button_y = ["repair", "look back", "y"]

    left_trigger = ["use equipament", "equipament", "left trigger", "lt"]
    release_left_trigger = ["release left trigger", "rlt"]
    right_trigger = ["shoot", "attack", "right trigger", "rt"]

    right_shoulder = ["jump", "right shoulder", "rb"]
    left_shoulder = ["kick", "left shoulder", "lb"]

    d_pad_up_ = ["dup", "dpadup", "d pad up", "flashlight", "flash light"]
    d_pad_down_ = ["dup", "dpaddown", "d pad down", "heal"]
    d_pad_left_ = ["dleft", "dpadleft", "d pad left", "equipament"]
    d_pad_right_ = ["dright", "dpadright", "d pad right", "weapons", "weapon"]

    l3_ = ["sprint", "run", "l3"]
    r3_ = ["aim", "r3"]

    back_ = ["select", "main menu", "back"]
    start_ = ["pause", "start", "player menu", "menu"]
    ############################################################
    
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        ################################################## F KEYS ##################################################

        if msg in f5_:
                HoldAndReleaseKey(F5, 0.1)

        if msg in f9_:
                HoldAndReleaseKey(F9, 0.1)

        ################################################## RIGHT ANALOG ##################################################

        if msg in right_analog_up:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_down:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_left:
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_right:
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## LEFT ANALOG ##################################################

        if msg in left_analog_up:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_down:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_left:
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_right:
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## AUTO WALK ##################################################

        if msg in auto_walk:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in stop_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## L3 R3 ##################################################

        if msg in l3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        if msg in r3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()

        ################################################## A B X Y ##################################################

        if msg in button_a:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in hold_a_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in button_b:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in hold_b_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in button_x :
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in button_y:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        ################################################## TRIGGERS ##################################################

        if msg in left_trigger:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)

        if msg in release_left_trigger:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in right_trigger:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.2)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        ################################################## SHOULDERS ##################################################

        if msg in right_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in left_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        ################################################## D PADS ##################################################

        if msg in d_pad_up_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in d_pad_down_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg  in d_pad_left_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg  in d_pad_right_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        ################################################## START BACK ##################################################

        if msg in start_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()

        if msg in back_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))

###   NIER AUTOMATA CONTROLLER   ###

def NIERAUTOMATACONTROLLER(message):

    ############################################################
    f5_ = ["quicksave", "quick save", "save", "f5"]
    f9_ = ["quickload" "quick sload", "load", "f9"]

    right_analog_up = ["lookup", "lup", "look up"]
    right_analog_down = ["lookdown", "ldown", "look down"]
    right_analog_left = ["lookleft", "lleft", "look left", "turnleft"]
    right_analog_right = ["lookright", "lright", "look right", "turnright"]

    left_analog_up = ["forward"]
    left_analog_down = ["backwards"]
    left_analog_left = ["left"]
    left_analog_right = ["right"]

    auto_walk = ["auto walk", "walk"]
    stop_walking = ["stop walking", "stop running"]

    button_a = ["accept", "activate", "a"]
    hold_a_1sec = ["hold a"]
    button_b = ["return", "back", "b", "use"]
    hold_b_1sec = ["hold b"]
    button_x = ["x", "fast attack", "attack"]
    button_y = ["y", "strong attack"]

    left_trigger = ["aim", "left trigger", "lt", "lock cam"]
    release_left_trigger = ["freeaim", "free aim", "faim", "release left trigger", "rlt"]
    right_trigger = ["shoot", "attack", "right trigger", "rt", "dodge", "run"]

    right_shoulder = ["right shoulder", "rb"]
    left_shoulder = ["left shoulder", "lb"]

    d_pad_up_ = ["dup", "dpadup", "d pad up"]
    d_pad_down_ = ["dup", "dpaddown", "d pad down"]
    d_pad_left_ = ["dleft", "dpadleft", "d pad left"]
    d_pad_right_ = ["dright", "dpadright", "d pad right"]

    l3_ = ["l3"]
    r3_ = ["r3"]

    back_ = ["select"]
    start_ = ["pause", "start"]
    ############################################################
    
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        ################################################## F KEYS ##################################################

        if msg in f5_:
                HoldAndReleaseKey(F5, 0.1)

        if msg in f9_:
                HoldAndReleaseKey(F9, 0.1)

        ################################################## RIGHT ANALOG ##################################################

        if msg in right_analog_up:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_down:
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_left:
            gamepad.right_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=-0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in right_analog_right:
            gamepad.right_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(0.5)
            gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## LEFT ANALOG ##################################################

        if msg in left_analog_up:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_down:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=-1.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_left:
            gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in left_analog_right:
            gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()
            time.sleep(5)
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## AUTO WALK ##################################################

        if msg in auto_walk:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=1.0)  # values between -1.0 and 1.0
            gamepad.update()

        if msg in stop_walking:
            gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)  # values between -1.0 and 1.0
            gamepad.update()

        ################################################## L3 R3 ##################################################

        if msg in l3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            gamepad.update()

        if msg in r3_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            gamepad.update()

        ################################################## A B X Y ##################################################

        if msg in button_a:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in hold_a_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
            time.sleep(2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        if msg in button_b:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in hold_b_1sec:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()
            time.sleep(1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            gamepad.update()

        if msg in button_x :
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            gamepad.update()

        if msg in button_y:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            gamepad.update()
            time.sleep(1)
            gamepad.reset()

        ################################################## TRIGGERS ##################################################

        if msg in left_trigger:
            gamepad.left_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(30)

        if msg in release_left_trigger:
            gamepad.left_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        if msg in right_trigger:
            gamepad.right_trigger_float(value_float=1.0)  # value between 0.0 and 1.0
            gamepad.update()
            time.sleep(0.2)
            gamepad.right_trigger_float(value_float=0.0)  # value between 0.0 and 1.0
            gamepad.update()

        ################################################## SHOULDERS ##################################################

        if msg in right_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        if msg in left_shoulder:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()
            time.sleep(0.2)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        ################################################## D PADS ##################################################

        if msg in d_pad_up_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_UP)
            gamepad.update()

        if msg in d_pad_down_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad.update()

        if msg  in d_pad_left_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad.update()

        if msg  in d_pad_right_:
            gamepad.press_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad.update()

        ################################################## START BACK ##################################################

        if msg in start_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            gamepad.update()

        if msg in back_:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()
            time.sleep(0.1)
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            gamepad.update()

    except Exception as e:
        print("Encountered exception: " + str(e))

###   DRAGON'S DOGMA CONTROLLER   ###

def DRAGONSDOGMA_CONTROLLER(message):

    ############################################################

    f5_ = ["quicksave", "quick save", "save", "f5"]
    f9_ = ["quickcheckpoint" "quick checkpoint", "checkpoint", "f9"]

    right_analog_up = ["lookup", "lup", "look up"]
    right_analog_down = ["lookdown", "ldown", "look down"]
    right_analog_left = ["lookleft", "lleft", "look left", "turnleft"]
    right_analog_right = ["lookright", "lright", "look right", "turnright"]

    left_analog_up = ["forward"]
    left_analog_down = ["backwards"]
    left_analog_left = ["left"]
    left_analog_right = ["right"]

    auto_walk = ["auto walk", "walk"]
    stop_walking = ["stop walking", "stop running"]

    button_a = ["jump", "a"]
    hold_a_1sec = ["hold a"]
    double_a_ = ["double jump", "aa", "2a"]
    button_b = ["return", "back", "b", "action", "help", "examine"]
    hold_b_1sec = ["hold b"]
    button_x = ["light attack", "x"]
    button_y = ["y", "heavy attack"]

    left_trigger = ["draw", "sheathe", "left trigger", "lt"]
    release_left_trigger = ["release left trigger", "rlt"]
    right_trigger = ["grab", "cling", "fire arrow", "shoot", "right trigger", "rt"]
    hold_right_trigger = ["hold rt", "hold right trigger", "hrt"]
    release_right_trigger = ["release rt", "release right trigger"]

    right_shoulder = ["right shoulder", "rb"]
    left_shoulder = ["left shoulder", "lb"]

    d_pad_up_ = ["go", "dup", "dpadup", "d pad up"]
    d_pad_down_ = ["come", "dup", "dpaddown", "d pad down"]
    d_pad_left_ = ["help", "dleft", "dpadleft", "d pad left"]
    d_pad_right_ = ["help", "dright", "dpadright", "d pad right"]

    l3_ = ["l3"]
    r3_ = ["r3"]

    back_ = ["select", "inventory"]
    start_ = ["pause", "start"]
    ############################################################
    
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print(username + " said : " + msg)

        CONTROLLER_TRIGGERS_SHOULDER(msg,left_trigger,release_left_trigger,right_trigger,hold_right_trigger,release_right_trigger,right_shoulder,left_shoulder);
        CONTROLLER_BUTTONS(msg,f5_,f9_,button_a,double_a_,hold_a_1sec,button_b,hold_b_1sec,button_x,button_y,back_,start_);
        CONTROLLER_DPADS(msg,d_pad_up_,d_pad_down_,d_pad_left_,d_pad_right_);
        CONTROLLER_ANALOGS(msg,right_analog_up,right_analog_down,right_analog_left,right_analog_right,left_analog_up,left_analog_down,left_analog_left,left_analog_right,auto_walk,stop_walking,l3_,r3_);

    except Exception as e:
        print("Encountered exception: " + str(e))


########################################################################################################################
# MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
# This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
# A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch.
# A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
# You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
MESSAGE_RATE = 0.5
# MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages.
# e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
# This is helpful for games where too many inputs at once can actually hinder the gameplay.
# Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
MAX_QUEUE_LENGTH = 50
MAX_WORKERS = 100 # Maximum number of threads you can process at a time

last_time = time.time()
message_queue = []
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
active_tasks = []
pyautogui.FAILSAFE = False

########################################################################################################################

t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_CHANNEL);

active_tasks = [t for t in active_tasks if not t.done()]

####################################    GAME LIST AND KEYWORD TO CALL THEM
generic_c = ["generic", "generic controller", "genericcontroller"]
morrowind_k = ["morrowind keyboard", "morrowindkeyboard", "tes3", "tesiii"]
skyrim_k = ["skyrim keyboard", "skyrim key board"]
skyrim_c = ["skyrim controller", "skyrim"]
fallout4_k = ["fallout 4 keyboard", "fallout 4 key board", "fallout4 keyboard", "fallout4 key board"]
fallout4_c = ["fallout4 controller", "fallout4controller", "fallout 4 controller", "fallout 4", "fallout4", "fo4"]
dd1_c = ["darkest dungeon controller", "darkestdungeoncontroller", "darkest dungeon", "dd"]
terraria_k = ["terraria keyboard", "terrariakeyboard", "terraria"]
cp77_k = ["cyber punk 2077 keyboard", "cyberpunkkeyboard", "cyber punk keyboard"]
cp77_c = ["cyber punk 2077 controller", "cyberpunkcontroller", "cyber punk controller", "cyber punk", "cyberpunk", "cyber punk 2077", "cyberpunk2077", "cyberpunk77", "cyber punk 77"]
drakengard_3 = ["drakengard3", "drakengard 3"]
drying_light_c = ["dying light", "dying light controller", "dyinglight", "dyinglightcontroller"]
nier_automata_c = ["nier", "nier automata", "nier automata controller", "nierautomata", "nierautomatacontroller"]
dragons_dogma_c = ["ddda", "dragons dogma", "dragons dogma dark arisen", "dragons dogma controler", "ddda controller"]
####################################

print ("GENERIC CONTROLLER",
       "\nMORROWIND KEYBOARD",
       "\nSKYRIM KEYBOARD",
       "\nSKYRIM CONTROLLER",
       "\nFALLOUT4 KEYBOARD",
       "\nFALLOUT4 CONTROLLER",
       "\nDARKEST DUNGEON CONTOLLER",
       "\nTERRARIA KEYBOARD",
       "\nCYBER PUNK 2077 KEYBOARD",
       "\nCYBER PUNK 2077 CONTROLLER",
       "\nNIER AUTOMATA CONTROLLER",
       "\nDRAGON'S DOGMA: DARK ARISEN")
while True:
    game_input = input("pleaset select your game: \n")
    game = game_input.lower()
    try:

        if game in generic_c:
            print("loading generic controller code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)

            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(GENERIC_CONTROLLER, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in morrowind_k:
            print("loading Morrowind Keyboard code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)

            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(MORROWINDKEYBOARD, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in skyrim_k:
            print("loading skyrim keyboard code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)

            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(SKYRIMBLOCKKEYBOARD, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in skyrim_c:
            print("loading skyrim controller code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(SKYRIMBLOCKCONTROLER, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in fallout4_k:
            print("loading fallout 4 keyboard code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(FALLOUT4LOCKKEYBOARD, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in fallout4_c:
            print("loading fallout 4 controller code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(FALLOUT4BLOCKCONTROLER, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in dd1_c:
            print("loading darkest dungeon controller code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(DARKESTDUNGEONBLOCKCONTOLLER, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in terraria_k:
            print("loading terraria keyboard code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(TERRARIABLOCKKEYBOAR, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in cp77_k:
            print("loading cyberpunk 2077 keyboard code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(CYBERPUNK2077BLOCKKEYBOARD, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in cp77_c:
            print("loading cyberpunk 2077 controller code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(CYBERPUNK2077BLOCKCONTROLER, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in drakengard_3:
            print("loading drakengard 3 code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(DRAKENGARD3, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in drying_light_c:
            print("loading Drying Light code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(DYINGLIGHT, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in nier_automata_c:
            print("loading Nier Automata code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(NIERAUTOMATACONTROLLER, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

        if game in dragons_dogma_c:
            print("loading Dragon's dogma code")
            for i in range(10,-1,-1):
                print (" Starting in ", i, " ", end="\r")
                time.sleep(1)
            while True:
                #Check for new messages
                new_messages = t.twitch_receive_messages();
                if new_messages:
                    message_queue += new_messages; # New messages are added to the back of the queue
                    message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

                messages_to_handle = []
                if not message_queue:
                    # No messages in the queue
                    last_time = time.time()
                else:
                    # Determine how many messages we should handle now
                    r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
                    n = int(r * len(message_queue))
                    if n > 0:
                        # Pop the messages we want off the front of the queue
                        messages_to_handle = message_queue[0:n]
                        del message_queue[0:n]
                        last_time = time.time();

                # If user presses Shift+Backspace, automatically end the program
                if keyboard.is_pressed('shift+backspace'):
                    exit()

                if not messages_to_handle:
                    continue
                else:
                    for message in messages_to_handle:
                        if len(active_tasks) <= MAX_WORKERS:
                            active_tasks.append(thread_pool.submit(DRAGONSDOGMA_CONTROLLER, message))
                        else:
                            print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

    except:
        pass
    print("game not found, please try again")
