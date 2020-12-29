import evdev
import pyautogui

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
    if event.code == evdev.ecodes.KEY_HOMEPAGE and event.value == 1:
        pyautogui.hotkey('shift', 'tab')
        print("Event fired")
