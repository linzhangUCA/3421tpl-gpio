"""
Use LED in 4 different colors: GREEN, BLUE, RED, YELLOW and 2 buttons (B1 and B2) to indicate status of the robot.
Workflow:
1. Light up LEDs one by one in order: RED for 1 second >> YELLOW for 2 seconds >> BLUE for 3 seconds >> GREEN for 4 seconds >> blink ALL in 2Hz for 2 seconds.
2. Slowly blink GREEN use PWM (2 seconds gradually on and 2 seconds gradually off). Press B1, GREEN stays on. Press B1 again, GREEN gets back to PWM blinking mode.
3. Count time consumption of GREEN stays on (GO). DO NOT count GREEN blink (GB) time.
4. If GO takes more than 10 seconds, light up YELLOW (other LED will remain their status). 
5. If GO takes more than 20 seconds, blink RED in 2 Hz for 10 seconds. Then, shutdown the system (pull down all involved GPIOs).
6. If press B1 and B2 together over 3 seconds, turn on BLUE and turn off all other LEDs.
"""

#### Write your code below ####
import time
from gpiozero import LED, Button 
