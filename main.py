#packeges :
import turtle, time, sys
from random import choice
from pygame import mixer
mixer.init()

# Set screen :
from screen_funcs import wn

# Make and set all the cards :
from card_class import cards, shuffle_button, reset_button, space_card, get_best

#Set music :
mixer.music.load('bg_music.wav')
mixer.music.play(-1)

#Set starting time :
time_0 = time.time()

#Shuffles the cards :
def shuffle() -> None:
    global time_0
    time_0 = time.time()

    for _ in range(5000):
        available_vecs = [(space_card.pos[0] + 100, space_card.pos[1]), (space_card.pos[0] - 100, space_card.pos[1]), (space_card.pos[0], space_card.pos[1] + 100), (space_card.pos[0], space_card.pos[1] - 100)]
        available_cards = []
        for card in cards:
            available_cards.append(card) if card.pos in available_vecs else None

        chosen_card = choice(available_cards)
        chosen_card.switch(shuffled = True)

    # Updating
    for card in cards:
        if card.pos == card.right_pos:
            card.shape(card.image_paths[1])
            card.image_phase = 2
        else:
            card.shape(card.image_paths[0])
            card.image_phase = 1
    space_card.reset()
    wn.update()

#Reset best score
def reset_best():
    with open("bests.txt", 'w') as f:
        f.write(f"time:99999\n")
        f.write(f"moves:99999\n")
    best_turtle.clear()
    best_turtle.write(f"BEST TIME: {get_best()[0]}s\nBEST MOVES: {int(get_best()[1])}\n1. Press with the mouse on the tile that you want to move.\n2. Left button shuffles the game.\n3. Right button resets your best scores.\nMade by: Itay Shinderman", font=('arial', 20, 'bold'), align='center')

#Escape function :
def ESCAPE() -> None:
    global run
    run = False

#Start
shuffle()
space_card.change_check_game(True)
wn.update()

#Event keys :
wn.listen()
shuffle_button.onclick(lambda x, y: shuffle())
reset_button.onclick(lambda x, y: reset_best())
wn.onkey(ESCAPE, "Escape")

#Best time writer
best_turtle = turtle.Turtle()
best_turtle.ht()
best_turtle.pu()
best_turtle.goto(0, -400)
best_turtle.write(f"BEST TIME: {get_best()[0]}s\nBEST MOVES: {int(get_best()[1])}\n1. Press with the mouse on the tile that you want to move.\n2. Left button shuffles the game.\n3. Right button resets your best scores.\nMade by: Itay Shinderman", font=('arial', 20, 'bold'), align='center')

#Information loop :
run = True
while run:
    try:
        game_time = time.time() - time_0
        turtle.clear()
        turtle.write(f"TIME: {game_time: .3f}s   MOVES: {space_card.get_moves()}", font=('arial', 20, 'bold'), align='center')
        if space_card.get_check() == False:
            space_card.write_best_score(game_time)
            shuffle()
            best_turtle.clear()
            best_turtle.write(f"BEST TIME: {get_best()[0]}s\nBEST MOVES: {int(get_best()[1])}\n1. Press with the mouse on the tile that you want to move.\n2. Left button shuffles the game.\n3.\nRight button resets your best scores. Made by: Itay Shinderman", font=('arial', 20, 'bold'), align='center')
            space_card.change_check_game(True)
    except:
        sys.exit()