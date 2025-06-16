<img src=media/pysmirfduino.png width=600>

This repository provides an example of fast bidirectional communication between
an Arduino-compatible microcontroller (MCU) using
[BlueSMiRF v2](https://www.sparkfun.com/sparkfun-bluesmirf-v2.html)
and a Python program running on a desktop or laptop computer.   

Instructions:

1. [Connect](media/wiring2.jpg) the BlueSMiRF to your MCU:

  * BlueSMiRF GND to MCU GND
  * BlueSMiRF 3V3-5V to MCU 5V
  * BlueSMiRF RXI to MCU TX1
  * BlueSMiRF TXO to MCU RX1

2. Power the MCU.  The BlueSMiRF will start blinking and
   can immediately be paired with the Bluetooth on your
   computer (no need to press the BlueSMiRF's pairing 
   button).  Before accepting the pairing request,note the BlueSMiRF's
   [address](media/pairing2.png) for the next step.

3. Change the [address](https://github.com/simondlevy/pysmirfduino/blob/main/python/bluesmirf.py#L25)
   in the Python program to the address you just noted.

4. Flash the Arduino [sketch](arduino/arduino.ino) onto your MCU.

5. Run the Python program.  You should see the lower-case letters of the
   alphabet scrolling by very quickly.

6. Open the Serial Monitor in the Arduino IDE.  You should see the upper-case
   letters of the alphabet scrolling by very quickly.

