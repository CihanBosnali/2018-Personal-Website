import cv2
import numpy as np 

def find_thanos(photo_name):

    # This line of code is used to load image
    image = cv2.imread(photo_name)

    # This is a function to convert colorspaces in openCV
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # HSV boundaries for purple.
    lower_bound = np.array([40, 70, 70])
    upper_bound = np.array([180, 255, 255])

    mask = cv2.inRange(image, lower_bound, upper_bound)

    # Show the images to user.
    cv2.imshow("mask", mask)

    # Find how many pixels are in the image
    num_of_pixels = mask.shape[0] * mask.shape[1]

    # Calculate the number of white ones.
    num_of_white = np.sum(mask == 255)

    # Calculate the ratio
    ratio = num_of_white / num_of_pixels

    if ratio > 0.2:
        print("I found someone like Thanos! The probability is", ratio*100, "%")
    else:
        print("No Thanos. The probability is", ratio*100, "%")

    # Stop the code. Wait for user to press space button.
    cv2.waitKey(0)

def run():
    while True:
        photo_name = input("Image path:")

        if photo_name == "":
            break
        else:
            find_thanos(photo_name)
run()
