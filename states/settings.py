
import pygame
from .base import BaseState


class Settings(BaseState):
    def __init__(self):
        super(Settings, self).__init__()
        self.active_index = None
        self.options = [
            {"text": "Multiple Choice", "checked": True},
            {"text": "Sounds", "checked": True},
            {"text": "Menu"}
        ]
        self.next_state = "MENU"


    def render_text(self, index):
        option = self.options[index]
        color = pygame.Color("white")
        if "hovered" in option and option["hovered"]:
            color = pygame.Color("red")
        elif index == self.active_index:
            color = pygame.Color("red")
        return self.font.render(option["text"], True, color)

    def handle_hover(self, mouse_pos):
        for option in self.options:
            text_position = self.get_text_position(self.render_text(self.options.index(option)), self.options.index(option))
            if text_position.collidepoint(mouse_pos):
                option["hovered"] = True
            else:
                option["hovered"] = False

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0], self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self, index):
        if index == 0:
            self.options[0]["checked"] = not self.options[0]["checked"]
        elif index == 1:
            self.options[1]["checked"] = not self.options[1]["checked"]
        elif index == 2:
            self.persist['multiple_choice'] = self.options[0]["checked"]
            self.persist['sound'] = self.options[1]["checked"]
            self.done = True

    def handle_click(self, mouse_pos):
        for index, option in enumerate(self.options):
            text_position = self.get_text_position(self.render_text(index), index)
            if text_position.collidepoint(mouse_pos):
                self.handle_action(index)
                break


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print(self.persist['profile'])
        elif event.type == pygame.MOUSEBUTTONUP:
            self.handle_click(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEMOTION:
            self.handle_hover(pygame.mouse.get_pos())

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            text_position = self.get_text_position(text_render, index)
            surface.blit(text_render, self.get_text_position(text_render, index))

            if "checked" in option:
                checkbox_rect = pygame.Rect(text_position.left - 30, text_position.centery - 10, 20, 20)
                if option["checked"]:
                    pygame.draw.rect(surface, pygame.Color("green"), checkbox_rect)
                elif option["checked"] == False:
                    pygame.draw.rect(surface, pygame.Color("red"), checkbox_rect)
                pygame.draw.rect(surface, pygame.Color("white"), checkbox_rect, 2)

