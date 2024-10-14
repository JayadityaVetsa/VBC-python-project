import pyautogui
import time

def click_next_button(image_path):
    # Wait for 2 seconds before starting to give you time to open the application window
    time.sleep(2)
    
    while True:
        try:
            # Attempt to locate the "Next" button using the image with lower confidence if needed
            button_location = pyautogui.locateOnScreen(image_path, confidence=0.7)

            if button_location:
                # Get the center of the button location
                button_center = pyautogui.center(button_location)
                
                # Move to the center of the button and click
                pyautogui.moveTo(button_center.x, button_center.y, duration=0.3)
                pyautogui.click()
                
                print("Clicked the 'Next' button.")
                
                # Optional: wait for a short time before the next iteration
                time.sleep(2)
            else:
                print("Button not found, trying again...")
                time.sleep(1)
                
        except pyautogui.ImageNotFoundException:
            print("Button image not found, make sure the image is correct.")
            break
        except KeyboardInterrupt:
            print("Script stopped by user.")
            break

# Give 5 seconds to switch to the correct screen before the script starts
time.sleep(5)

# Make sure the image file is accurate and matches the button on the screen
click_next_button('next_button_image.png')
