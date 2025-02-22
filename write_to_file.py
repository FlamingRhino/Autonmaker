# Description: This file contains the function that writes the combined list to a file.
import pygame
from pygame import font

def write_to_filef(event, combined_list, text_box_open, input_function):
    text_box_open = not text_box_open
    input_pathname = "waypoints.txt"
    
    if text_box_open:
        if event.key == pygame.K_RETURN:
            with open(input_pathname, "r") as file:
                lines = file.readlines()
            
            found_function = False
            with open(input_pathname, "w") as file:
                for line in lines:
                    file.write(line)
                    if input_function in line:
                        found_function = True
                        for item in combined_list:
                            file.write(item + "\n")
                        file.write("\n")
                
                if not found_function:
                    file.write(input_function + "\n")
                    for item in combined_list:
                        file.write(item + "\n")
                    file.write("\n")
            
            for item in combined_list:
                print(item)
            print(f"Combined list saved to {input_pathname}")
            print("Combined list:")
        elif event.key == pygame.K_BACKSPACE:
            input_function = input_function[:-1]
        else:
            input_function += event.unicode
