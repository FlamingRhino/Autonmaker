import pygame

def read_functions_from_file(filepath):
    functions = {}
    current_function = None
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("void"):
                current_function = line.split()[1].strip("()")
                functions[current_function] = []
            elif current_function:
                functions[current_function].append(line)
    return functions

def display_function_menu(screen, font, functions):
    menu_open = True
    selected_function = None
    while menu_open:
        screen.fill((0, 0, 0))
        y_offset = 50
        for function_name in functions.keys():
            text_surface = font.render(function_name, True, (255, 255, 255))
            screen.blit(text_surface, (50, y_offset))
            y_offset += 40

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_open = False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_open = False
                elif event.key == pygame.K_RETURN:
                    selected_function = function_name
                    menu_open = False

        pygame.display.flip()
    return selected_function
