# Stadia Xbox Mapper

Hook the Xbox button on Xbox One gamepads to open Stadia's in-game menu rather than doing nothing.

## Requirements

Get xpadneo here: https://atar-axis.github.io/xpadneo/

Install all python dependencies:
```
pip3 install pyautogui evdev
```

Launch it:
```
python3 xbox_map_service.py
```

## Behaviour

| Keycombo                                 	| Action                             	|
|------------------------------------------	|------------------------------------	|
| Hold L and R stick down for 0.25 seconds 	| Take screenshot                    	|
| Hold L and R stick down for 1 second     	| Record last 30 seconds of gameplay 	|
| Hold L and R stick down for 2 seconds    	| Exit game                          	|
| Press Xbox button                        	| Open Stadia's in-game menu bar     	|