import sys
import time

import pygame
from typing import Any


class MegaMan:
    pygame.init()
    SIZE = WIDTH, HEIGHT = 1000, 900
    INITIAL_POSITION = [100, 850]

    def __init__(self, **kwargs) -> None:
        self.screen = self.__window_display()
        self.__mega_jump: str = kwargs['mega_jump']
        self.__mega_run: str = kwargs['mega_jump']
        self.__mega_shot: str = kwargs['mega_jump']
        self.__mega_wait: str = kwargs['mega_jump']
        self.__image = pygame.image.load(self.__mega_wait)
        self.__mega_man_rect = self.__image.get_rect()
        self.__image_down = self.__mega_man(self.__mega_wait)
        self.__mega_man_rect_down = self.__image_down.get_rect()
        self.__image_up = self.__mega_man(self.__mega_jump)
        self.__mega_man_rect_up = self.__image_up.get_rect()
        self.__image_right = self.__mega_man(self.__mega_run)
        self.__mega_man_rect_right = self.__image_right.get_rect()
        self.__image_left = self.__mega_man(self.__mega_run)
        self.__mega_man_rect_left = self.__image_left.get_rect()

    @staticmethod
    def __mega_man(image: str) -> pygame.Surface:
        return pygame.image.load(image)

    @staticmethod
    def __update_screen() -> None:
        pygame.display.update()

    def __window_display(self) -> pygame.Surface:
        return pygame.display.set_mode(self.SIZE)

    @staticmethod
    def _window_close(event: Any) -> None:
        if event.type == pygame.QUIT:
            sys.exit(0)

    def __move_right(self, event: Any, screen: pygame.Surface) -> None:
        if event.key == pygame.K_d:
            self.__mega_man_rect.x += 200
            print(self.__mega_man_rect)
            screen.fill((0, 0, 0))
            screen.blit(self.__image, self.__mega_man_rect)
            self.__update_screen()

    def __move_left(self, event: Any, screen: pygame.Surface) -> None:
        if event.key == pygame.K_a:
            self.__mega_man_rect.x -= 200
            screen.fill((0, 0, 0))
            screen.blit(self.__image, self.__mega_man_rect)
            self.__update_screen()

    def __move_up(self, event: Any, screen: pygame.Surface) -> None:
        if event.key == pygame.K_w:
            print(self.__mega_man_rect)
            self.__mega_man_rect.y = self.HEIGHT - 300
            for n in range(230):
                self.__mega_man_rect.y -= 1
                screen.fill((0, 0, 0))
                screen.blit(self.__image, self.__mega_man_rect)
                self.__update_screen()
                #time.sleep(0.01)
            self.__mega_man_rect.y += 200
            screen.fill((0, 0, 0))
            screen.blit(self.__image, self.__mega_man_rect)
            self.__update_screen()

    def __move_down(self, event: Any, screen: pygame.Surface) -> None:
        if event.key == pygame.K_s:
            self.__mega_man_rect.y += 200
            print(self.__mega_man_rect.y)
            screen.fill((0, 0, 0))
            screen.blit(self.__image, self.__mega_man_rect)
            self.__update_screen()

    def _progression(self) -> None:
        while True:
            for event in pygame.event.get():
                self._window_close(event)
                if event.type == pygame.KEYDOWN:
                    self.__move_left(event, self.screen)
                    self.__move_right(event, self.screen)
                    self.__move_up(event, self.screen)
                    self.__move_down(event, self.screen)
            pygame.display.flip()

    def start(self):
        self._progression()


if __name__ == '__main__':
    megaman: MegaMan = MegaMan(
        mega_run='assets/images/mega_run.png',
        mega_jump='assets/images/mega_jump.png',
        mega_shot='assets/images/mega_shot.png',
        mega_wait='assets/images/mega_wait.png'
    )
    megaman.start()
