"""
Here is the fast card maker class ~ Not a generator!
"""

import turtle
from screen_funcs import wn

check_game = False
class card(turtle.Turtle):
    def __init__(self, pos=(0, 0), image_paths=None):
        super().__init__()
        self.pu()
        self.right_pos = pos
        self.pos = pos
        self.goto(pos)
        self.image_paths = image_paths
        self.image_phase = 0
        if (self.image_paths != None):
            for image_path in self.image_paths:
                wn.register_shape(image_path)

            self.shape(self.image_paths[0])
        self.onclick(lambda x, y: self.switch())

    def switch(self, shuffled = False) -> None:
        global moves, check_game
        motion_positions = [(space_card.pos[0] + 100, space_card.pos[1]), (space_card.pos[0] - 100, space_card.pos[1]),
                            (space_card.pos[0], space_card.pos[1] + 100), (space_card.pos[0], space_card.pos[1] - 100)]
        if (self.pos in motion_positions):
            self.pos, space_card.pos = space_card.pos, self.pos
            self.goto(self.pos)
            space_card.goto(space_card.pos)
            moves += 1

            for card in cards:
                if card.pos == card.right_pos:
                    card.shape(card.image_paths[1])
                    card.image_phase = 2
                else:
                    card.shape(card.image_paths[0])
                    card.image_phase = 1
            if not shuffled:
                wn.update()
            if check_game == True:
                if (len([card.image_phase for card in cards if card.image_phase == 2]) == len(cards)):
                    decision = wn.numinput("YOU WON", "Go Get A Better Time!", 0, minval=0, maxval=0)
                    if decision == 0:
                        check_game = False
                    else:
                        turtle.bye()
                    wn.listen()

    def get_check(self):
        global check_game
        return check_game

    def change_check_game(self, decition):
        global check_game
        check_game = decition

    def write_best_score(self, game_time):
        global moves
        best_scores = get_best()
        with open("bests.txt", 'w') as f:
            if best_scores[0] > game_time:
                f.write(f"time:{game_time: .3f}\n")
            else:
                f.write(f"time:{best_scores[0]: .3f}\n")

            if best_scores[1] > moves:
                f.write(f"moves:{int(moves)}\n")
            else:
                f.write(f"moves:{int(best_scores[1])}\n")

    def get_moves(self):
        global moves
        return moves

    def reset(self):
        global moves
        moves = 0

#Get best scores
def get_best() -> list:
    with open("bests.txt", 'r') as f:
      best_scores = []
      for line in f:
        score = line.split(':')[1]
        if ("\n" in score):
            score = score[0:-1]
        best_scores.append(float(score))
    return best_scores


# Creating 2d vectors (16 2d vectors for places where the cards will be) :
vecs = [(x, y) for y in range(150, -250, -100) for x in range(-150, 250, 100)]

# The sprites :
card_image_paths = [["images/number1.gif", "images/number1_green.gif"],
                    ["images/number2.gif", "images/number2_green.gif"],
                    ["images/number3.gif", "images/number3_green.gif"],
                    ["images/number4.gif", "images/number4_green.gif"],
                    ["images/number5.gif", "images/number5_green.gif"],
                    ["images/number6.gif", "images/number6_green.gif"],
                    ["images/number7.gif", "images/number7_green.gif"],
                    ["images/number8.gif", "images/number8_green.gif"],
                    ["images/number9.gif", "images/number9_green.gif"],
                    ["images/number10.gif", "images/number10_green.gif"],
                    ["images/number11.gif", "images/number11_green.gif"],
                    ["images/number12.gif", "images/number12_green.gif"],
                    ["images/number13.gif", "images/number13_green.gif"],
                    ["images/number14.gif", "images/number14_green.gif"],
                    ["images/number15.gif", "images/number15_green.gif"]]

# List with all the created cards :
cards = [card(pos=vec, image_paths=image_paths) for vec, image_paths in zip(vecs, card_image_paths)]

# Shuffle button card on screen :
shuffle_button = card(pos=(-250, 250), image_paths=["images/shuffle_button.gif", "images/space_button.gif"])
shuffle_button.onclick(None)

# Reset scores button:
reset_button = card(pos=(250, 250), image_paths=["images/reset_score.gif", "images/space_button.gif"])
reset_button.onclick(None)

# Space card
space_card = card(pos=(150, -150), image_paths=["images/space.gif", "images/space_button.gif"])
space_card.onclick(None)

# Moves
moves = 0

