import pygame
import sys

# player = o, computer = x


class Square(pygame.sprite.Sprite):
    def __init__(self, position: int, state: str):
        super().__init__()
        self.position = position
        self.state = state
        self.image = pygame.image.load("graphics/test_square.png").convert_alpha()
        x_pos = ((self.position-1) % 3) * 200
        y_pos = 400 - ((self.position-1) // 3) * 200
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_lmb = pygame.mouse.get_pressed()[0]
        if mouse_lmb:
            if self.state != "x" and self.state != "o":
                if self.rect.collidepoint(mouse_pos):
                    self.state = "o"
                    return True
                else:
                    return False

    def change_state(self):
        if self.state == "x":
            self.image = pygame.image.load("graphics/x.png").convert_alpha()
        elif self.state == "o":
            self.image = pygame.image.load("graphics/o.png").convert_alpha()
        else:
            self.image = pygame.image.load("graphics/test_square.png").convert_alpha()

    def win_checking(self):
        win_states = \
        [
            # vertical:
            (1,4,7), (2,5,8), (3,6,9),
            # horizontal:
            (1,2,3), (4,5,6), (7,8,9),
            # diagonal:
            (1,5,9), (3,5,7)
        ]
        pass

    def update(self):
        self.clicked()
        self.change_state()
        self.win_checking()


class Computer:
    def check_board(self, square_group):
        self.square_group = square_group
        self.square_group_list = self.square_group.sprites()
        self.x_count = 0
        self.o_count = 0
        for sq in self.square_group_list:
            if sq.state == "x":
                self.x_count += 1
            if sq.state == "o":
                self.o_count += 1

    def place_a_cross(self, game_state):
        if game_state == 4:
            pass
            # if self.square_group_list[8-1].state == "o":
            #     if self.o_count == 1:
            #         self.square_group_list[1-1].state = "x"
            #     if self.o_count == 2:
            #         if self.square_group_list[4-1].state == "o":
            #             self.square_group_list[3-1].state = "x"
            #         elif self.square_group_list[4-1].state == "o":
            #             self.square_group_list[4-1].state = "x"
            #             print("computer win1")
            #     if self.o_count == 3:
            #         if self.square_group_list[5-1].state == "o":
            #             self.square_group_list[2-1].state = "x"
            #             print("computer win2")
            #         else:
            #             self.square_group_list[5-1].state = "x"
            #             print("computer win3")
            #
            # elif self.square_group_list[4-1].state == "o":
            #     if self.o_count == 1:
            #         self.square_group_list[9-1].state = "x"
            #     if self.o_count == 2:
            #         if self.square_group_list[8-1].state == "o":
            #             self.square_group_list[3-1].state = "x"
            #         else:
            #             self.square_group_list[8-1].state = "x"
            #             print("computer win4")
            #     if self.o_count == 3:
            #         if self.square_group_list[5-1].state == "o":
            #             self.square_group_list[6-1].state = "x"
            #             print("computer win5")
            #         else:
            #             self.square_group_list[5-1].state = "x"
            #             print("computer win6")

            # elif self.o_count == 1 and self.square_group_list[4-1].state == "o":
            #     pass
            # elif self.o_count == 1 and self.square_group_list[9-1].state == "o":
            #     pass
            # elif self.o_count == 1 and self.square_group_list[1-1].state == "o":
            #     pass
            # elif self.o_count == 1 and self.square_group_list[6-1].state == "o":
            #     pass
            # elif self.o_count == 1 and self.square_group_list[2-1].state == "o":
            #     pass
            # elif self.o_count == 1 and self.square_group_list[3-1].state == "o":
            #     pass
            # elif self.o_count == 1 and self.square_group_list[5-1].state == "o":
            #     pass




def main():
    pygame.init()
    main_screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    game_state = 0

    board_surf = pygame.image.load("graphics/board.jpg").convert_alpha()
    go_first_button = pygame.image.load("graphics/go_first.png").convert_alpha()
    go_first_button_rect = go_first_button.get_rect(center=(300, 200))
    go_second_button = pygame.image.load("graphics/go_second.png").convert_alpha()
    go_second_button_rect = go_second_button.get_rect(center=(300, 400))

    computer = Computer()

    cross_surf = pygame.image.load("graphics/x.png").convert_alpha()
    circle_surf = pygame.image.load("graphics/o.png").convert_alpha()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_state == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if go_first_button_rect.collidepoint(event.pos):
                        game_state = 1
                    elif go_second_button_rect.collidepoint(event.pos):
                        game_state = 2

        main_screen.blit(board_surf, (0, 0))
        if game_state == 0:
            main_screen.blit(go_first_button, go_first_button_rect)
            main_screen.blit(go_second_button, go_second_button_rect)
        elif game_state == 1:
            square_group = pygame.sprite.Group()
            for i in range(1, 9+1):
                square_group.add(Square(i, ""))
            game_state = 3
        elif game_state == 2:
            square_group = pygame.sprite.Group()
            for i in range(1, 9+1):
                if i == 7: square_group.add(Square(i, "x"))
                else:      square_group.add(Square(i, ""))
            game_state = 4
        elif game_state == 3:
            square_group.draw(main_screen)
            square_group.update()
        elif game_state == 4:
            square_group.draw(main_screen)
            square_group.update()
            # 7 already has "x"
            computer.check_board(square_group)
            computer.place_a_cross(game_state)







        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
