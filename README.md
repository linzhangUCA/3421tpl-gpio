# GPIO Practice

## Requirements:
Please complete the two python scripts prepared in this repository. Verify the required functionalities.
**Note: if any generative AI been used, state in this [document](/README.md) or drop comments in your script.** 

### (40%) [`fade_in_fade_out.py`](/fade_in_fade_out.py)
Repeat the process of gradually increasing and decreasing the brightness of an LED using Raspberry Pi Pico.
- (10%) Ramp up the brightness of the LED in 2 seconds.
- (10%) Ramp down the brightness of the LED in 1 seconds. 
- (20%) Repeat previous two steps **forever**.


### (60%) [`switch_mode.py`](/switch_mode.py)
Make an LED running under two modes. Use a button to switch the mode.
- (12%) **Mode 1**: set the LED to **endlessly** fade in and fade out. Please equally allocate fade-in and fade-out time. Set the frequency to 1/4 Hz.
- (8%) **Mode 2**: set the LED to **constantly on**.
- (20%) Press (and release) the button to switch between the modes. This function is expected to be valid all the time. **DO NOT make it a one-time function.**
- (20%) Mode switching happens **instantaneously**.
    
> **Hint**: an interrupt request could be super helpful.
> You can either start at **Mode 1** or **Mode 2**.
 
## Further Instructions
- You can use the built-in LED or an external LED.
- Solderless breadboard is optional.
- Refer to the wiring diagrams in this [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6).
- For more details on coding Raspberry Pi Pico using Micropython, refer to the official [handbook](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf?_gl=1*1ydsxhc*_ga*NjEyNDE4MjQ3LjE3MjUwNTIzMzE.*_ga_22FD70LWDS*MTcyNTQ4NTEyMy4zLjEuMTcyNTQ4NTIyOC4wLjAuMA..).
