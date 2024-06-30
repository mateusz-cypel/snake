from enum import auto, Enum
from typing import List

import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_p

from pattern.observer import Observer, Subject


class JoystickAction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    PAUSE = auto()
    NOTHING = auto()


class JoystickInputHandler:
    """Class connects pygame control handling and joystick actions"""
    _current_joystick_action: JoystickAction = JoystickAction.NOTHING

    def read(self) -> None:
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self._current_joystick_action = JoystickAction.UP
        elif pressed_keys[K_DOWN]:
            self._current_joystick_action = JoystickAction.DOWN
        elif pressed_keys[K_LEFT]:
            self._current_joystick_action = JoystickAction.LEFT
        elif pressed_keys[K_RIGHT]:
            self._current_joystick_action = JoystickAction.RIGHT
        elif pressed_keys[K_p]:
            self._current_joystick_action = JoystickAction.PAUSE
        else:
            self._current_joystick_action = JoystickAction.NOTHING

    @property
    def current_joystick_action(self) -> JoystickAction:
        return self._current_joystick_action


class JoystickInputHandlerSubjectWrapper(Subject):
    """Subject class for triggering related observers to handle joystick actions"""
    _observers: List[Observer] = []

    def __init__(self, joystick_input_handler: JoystickInputHandler):
        self._joystick_input_handler = joystick_input_handler

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    @property
    def current_joystick_action(self) -> JoystickAction:
        return self._joystick_input_handler.current_joystick_action

    def read(self):
        self._joystick_input_handler.read()
        self.notify()
