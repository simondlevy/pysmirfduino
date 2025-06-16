<img src=media/pysmirfduino.png width=600>

This repository provides an example of fast bidirecitonal communication between
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
   button).  Note the BlueSMiRF's [address](media/pairing2.png) for the
   next step.
