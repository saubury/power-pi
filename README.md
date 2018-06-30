# Power Pi
**Home power consumption monitoring using a Raspberry Pi**

## Hardware Sensors
Our electrical power board has a red LED that pulses each time 1Wh of energy is consumed.   The LED will flash fast or slow, depending on the load being drawn from the network. 


### Raspberry Pi with an analogue sensor
We can use a _light dependant resistor_ (also known as an _LDR_ or _photoresistor_) to sense the pulse of light from our power meter without directly connecting to any of the mains powered circuits.  We can therefore count every 1000 pulses the meter is equivilent to measure each kWh used.  

 Unlike the Arduino, the Raspberry Pi's GPIO pins are unable to measure resistance and can only sense if the voltage supplied to them is above a certain voltage (approximately 2 volts). The circuit at [Raspberry Pi LDR GPIO circuit](http://www.instructables.com/id/Raspberry-Pi-GPIO-Circuits-Using-an-LDR-Analogue-S/) shows a very simple circuit using only an _LDR_ and 1uF capacitor.


