import pygame
class High_Scores():
    def __init__(self, screen_rect=False):
        self.high_scores = self.load_high_scores('high_scores.txt')
        self.screen_rect = screen_rect

    # Load high scores from a file (if any)
    @staticmethod
    def load_high_scores(file_path):
        high_scores_list = []
        with open(file_path, 'r') as file:
            for line in file:
                name, score = line.strip().split(',')
                high_scores_list.append((name, int(score)))
        return high_scores_list

    # Save high scores to a file
    @staticmethod
    def save_high_scores(file_path, list_of_scores):
        list_of_scores.sort(key=lambda x: x[1], reverse=True)
        list_of_scores = list_of_scores[:5]
        with open(file_path, 'w') as file:
            for name, score in list_of_scores:
                file.write(f"{name},{score}\n")

        return list_of_scores

    def draw(self, surface):
        color = pygame.Color("grey")
        # rect = (x,y,width, height)
        rect = (self.screen_rect.centerx+100, 200, 200, 350)
        pygame.draw.rect(surface, color, rect, width=0)
        color = pygame.Color("blue")
        font = pygame.font.Font(None, 24)
        title_text = font.render(f"High Scores", True, color)
        surface.blit(title_text, title_text.get_rect(center=(self.screen_rect.centerx+200, 250)))
        font = pygame.font.Font(None, 20)
        for index in range(len(self.high_scores)):
            text_render = font.render(f"{self.high_scores[index][0]}: {self.high_scores[index][1]}", True, color)
            text_position = text_render.get_rect(center=(self.screen_rect.centerx+200, 300 + (index * 50)))
            surface.blit(text_render, text_position)

