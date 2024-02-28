
import os
import pygame



class Display_csv:
    @staticmethod
    def display_csv_options(path, surface, font):
        folder_path = path  # profiles
        csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
        if not csv_files:
            print("No CSV files found in the current folder.")
            return None

        selected_file = None
        option_texts = []
        option_rects = []

        for i, file in enumerate(csv_files):
            option_text = font.render(f"{i+1}. {file[:-4]}", True, pygame.Color("white"))
            option_texts.append(option_text)
            option_rect = option_text.get_rect(center=(surface.get_width() // 2, 200 + (i+1) * 50))
            option_rects.append(option_rect)

        while not selected_file:
            for i, option_text in enumerate(option_texts):
                option_rect = option_rects[i]
                if option_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(surface, pygame.Color("red"), option_rect)
                else:
                    pygame.draw.rect(surface, pygame.Color("black"), option_rect)
                surface.blit(option_text, option_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, option_rect in enumerate(option_rects):
                        if option_rect.collidepoint(mouse_pos):
                            selected_file = os.path.join(folder_path, csv_files[i])

        return selected_file
