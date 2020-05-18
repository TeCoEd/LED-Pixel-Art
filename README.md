# LED-Pixel-Art
A simple Python program that pulls out RGB values from a 10 x 10 pxel JPEG image and then writes them to an LED display.

<img src="https://camo.githubusercontent.com/c8a9d4f1653d599167ef09852550c6810a7306bc/68747470733a2f2f7777772e6b6f2d66692e636f6d2f696d672f676974687562627574746f6e5f736d2e737667" alt="ko-fi" data-canonical-src="https://www.ko-fi.com/img/githubbutton_sm.svg" style="max-width:100%;">

![](images/LEDs.png)

I built a 10 x 10 LED board then used Python to display JPEGSs in real time.  The LEDs are GRB so the program code has to covert them into the 
correct RGB order first.

Uses the Pimoroni UnicornHAT Python library to drive the LEDs

Install libs:
* sudo pip3 install pil (pre installed on Pi)
* curl -sS https://get.pimoroni.com/unicornhat | bash 

More build details here: https://www.tecoed.co.uk/led-board.html

YouTube - https://www.youtube.com/watch?v=IQs2gBY1vNs&feature=youtu.be

Hackster.io 

