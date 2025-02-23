import pygame
from pygame import font
input_function = ""


def write_to_filef(event, combined_list, text_box_open, screen, font, pygame):
    input_pathname = "pythonatuothing\waypoints.txt"
    input_function = ""
    
    while text_box_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                text_box_open = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_function = "void " + input_function + "(){"
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
                            file.write("}//end\n")
                    
                    for item in combined_list:
                        print(item)
                    print(f"Combined list saved to {input_pathname} under function {input_function}")
                    text_box_open = False
                    print("Combined list:")
                
                elif event.key == pygame.K_BACKSPACE:
                    input_function = input_function[:-1]
                    draw_textt_box(screen, input_function, font)
                else:
                    input_function += event.unicode
                    draw_textt_box(screen, input_function, font)
                
                # Call draw_text_box to draw the text box on the screen
        draw_textt_box(screen, input_function, font)

        

def draw_textt_box(screen, text, font):
    pygame.draw.rect(screen, (0, 0, 0), (10, screen.get_height() - 50, 200, 40))
    pygame.draw.rect(screen, (255, 255, 255), (10, screen.get_height() - 50, 200, 40), 2)
    font = pygame.font.Font(None, 36)
    
    text_surface = font.render(f"name: {text}", True, (255, 0, 0))
    screen.blit(text_surface, (15, screen.get_height() - 50))
    pygame.display.flip()
