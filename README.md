# Assignment - Python Practice
Write code in `pwm_led.py` and `info_system.py` to complete this assignment.

### `pwm_led.py` (50%)
Introducing PWM. You will learn how PWM control the light strenght of an LED. 
You need to use RPi.GPIO library (`gpiozero` or other GPIO libraries are **NOT** allowed) to realize a slowly blinking LED.
Light up the LED gradually in 2 seconds, then turn it off gradually in 1 seconds.
Repeat this procedure until the program is stopped.

### `info_system.py` (50%)
You will polish your Python programming skills in this exercise.
You will use LED in 4 different colors: GREEN, BLUE, RED, YELLOW and 2 buttons (B1 and B2) to indicate status of the robot.

**Workflow:**

1. Light up LEDs one by one in order: RED for 1 second >> YELLOW for 2 seconds >> BLUE for 3 seconds >> GREEN for 4 seconds >> blink ALL in 2Hz for 2 seconds. Button operations shall not interrupt this procedure. (20%)
2. Slowly blink GREEN use PWM (2 seconds gradually on and 2 seconds gradually off). Press B1, GREEN stays on. Press B1 again, GREEN gets back to PWM blinking mode.
3. Count time consumption of GREEN stays on (GO). DO NOT count GREEN blink (GB) time.
4. If GO takes more than 10 seconds, light up YELLOW (other LED will remain their status). 
5. If GO takes more than 20 seconds, blink RED in 2 Hz for 10 seconds. Then, shutdown the system (pull down all involved GPIOs).
6. If press B1 and B2 together over 3 seconds, turn on BLUE and turn off all other LEDs.
