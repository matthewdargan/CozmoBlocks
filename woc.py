import pygame

'''
@class WOC
@author - Wizards of Coz
'''

class WOC:
    def __init__(self):
        pygame.init()
        self._exit_flag = False

    @property
    def exit_flag(self):
        if (self._exit_flag == True):
            return True
        for event in pygame.event.get():
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_ESCAPE):
                    print("EXIT")
                    return True
        return False

    @exit_flag.setter
    def exit_flag(self, value):
        print("Setting exit flag");
        self._exit_flag = True;