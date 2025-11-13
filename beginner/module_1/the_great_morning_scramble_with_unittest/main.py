'''The Great Morning Scramble!'''

# from custom_error import MyCustomError
from scr.game import Game
from scr.game_data import Game_data
from data.data_store import locations_and_outcomes

if __name__ == "__main__":
    locations = Game_data(locations_and_outcomes)
    my_game = Game(locations)
    my_game.run_game()
