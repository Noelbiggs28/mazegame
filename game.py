import pygame
from states.gameplay import Gameplay



# initiates with attributes passed in
#calls run from main
#run calls event loop/update/draw
#goes to splash because it was passed in




class Game(object):
    def __init__(self, screen, states, start_state):
        self.done = False  #flips_state when True
        self.screen = screen #gets screen dimensions
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states #absorbs states
        self.state_name = start_state #naming itself from name passed in
        self.state = self.states[self.state_name]

        

    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self):
        current_state = self.state_name
        # resets gameplay state
        if current_state == "GAMEPLAY":
            self.states["GAMEPLAY"] = Gameplay()
        next_state = self.state.next_state #gets this from previous state
        self.state.done = False #resets done condition
        self.state_name = next_state #sets stateindex variable
        persistent = self.state.persist
        self.state = self.states[self.state_name] #calls function for next state from state dictionary
        self.state.startup(persistent)
        self.state.do_once()
        

    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
