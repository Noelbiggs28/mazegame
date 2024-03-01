import pygame
from states.gameplay import Gameplay



# initiates with attributes passed in
#calls run from main
#run calls event loop/update/draw
#starts on splash because it was passed in




class Game(object):
    def __init__(self, screen, states, start_state):
        self.done = False  #stays in state while this is false
        self.screen = screen #gets screen dimensions
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states #absorbs initialized states passed in
        self.state_name = start_state #making string of state passed in 
        self.state = self.states[self.state_name] #sets state equal to state passed in that you want to run

        

    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event) #performs current states get_event function

    #performs these functions when self.done == True
    def flip_state(self):
        current_state = self.state_name
        # resets gameplay state, initialized a new Gameplay object.
        if current_state == "GAMEPLAY":
            self.states["GAMEPLAY"] = Gameplay()
        next_state = self.state.next_state #gets this from current state
        self.state.done = False #resets done condition
        self.state_name = next_state #sets stateindex variable
        persistent = self.state.persist #store persistant data in current state
        self.state = self.states[self.state_name] #changes current state to next state
        self.state.startup(persistent) #loads persistant data from 2 lines up into new state.
        # perform any actions for state you only want run once upon switching to the state
        # actions that cannot be performed on init because they depend on persistant data
        # such as question/profile selection.
        self.state.do_once() 
        

    def update(self, dt):
        if self.state.quit: #closes pygame
            self.done = True
        elif self.state.done: #closes state to open another
            self.flip_state()
        self.state.update(dt) #perfoms current states update function

    def draw(self):
        self.state.draw(self.screen) #performs current states draw function


    # the game loop. get inputs updates game and draws continuously. 
    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
