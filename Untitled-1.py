import cv2 as cv
import numpy as np
import pyautogui

# Load the image you want to check for matches
img = cv2.imread('dum562mqgzja1.png')

# Define the threshold for image similarity
threshold = 0.8

# Define the number of times to check the screen before pressing Page Up
num_checks = 9
check_count = 0

# Define the number of times D has been pressed
d_press_count = 0

# Start an infinite loop to continuously check the screen
while True:
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array and convert it to grayscale
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Compare the two images using template matching with normalized cross-correlation
    res = cv2.matchTemplate(screenshot, img, cv2.TM_CCOEFF_NORMED)
    match = np.max(res)

    # If the images are not close enough, simulate key presses
    if match < threshold:
        pyautogui.press('d')
        d_press_count += 1

        # If D has been pressed 9 times, press Page Up and reset the D count
        if d_press_count >= 9:
            pyautogui.press('pageup')
            d_press_count = 0

    # If the images match closely, reset the D count
    else:
        d_press_count = 0

    # Increment the check count
    check_count += 1

    # If the check count reaches the specified number, break out of the loop
    if check_count >= num_checks:
        break
