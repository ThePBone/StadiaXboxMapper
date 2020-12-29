import evdev
import pyautogui
import time

leftStickDown = False
rightStickDown = False

bothDownStartTime = -1


def processStickDownTime(seconds):
    if seconds > 2:
        pyautogui.hotkey("esc")
    elif seconds > 1:
        pyautogui.keyDown('f12')
        time.sleep(1)
        pyautogui.keyUp('f12')
    elif seconds > 0.25:
        pyautogui.hotkey("f12")


def checkState():
    global bothDownStartTime
    if leftStickDown and rightStickDown:
        if bothDownStartTime < 0:
            print("Both sticks held down")
            bothDownStartTime = time.time()
    elif bothDownStartTime > 0:
        diff = time.time() - bothDownStartTime
        bothDownStartTime = -1
        processStickDownTime(diff)
        print("Held down for", round(diff, 2), "seconds")


dev = None
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if device.name == "Xbox Wireless Controller":
        print("Selected device:", device.path, device.name, device.phys)
        dev = device
        break

if dev is None:
    print("No supported device found")
    exit(1)

for event in dev.read_loop():
    if event.code == 317:
        leftStickDown = event.value
    elif event.code == 318:
        rightStickDown = event.value
    elif event.code == evdev.ecodes.KEY_HOMEPAGE and event.value == 1:
        pyautogui.hotkey('shift', 'tab')
        print("Xbox button pressed")

    checkState()
