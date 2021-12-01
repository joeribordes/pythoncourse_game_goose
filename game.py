

from typing import Optional, Tuple
import random

class Game:
    
    def __init__(self, player1: str, player2: str) -> None:
        self.player1 = player1  # Save player1 data in self.player1
        self.player2 = player2
        self.player1_space = 0
        self.player2_space = 0
        self.turn = 0

    def get_player1_name(self) -> str:
        "Returns the name of Player 1 as a string."
        return self.player1
    
    def get_player2_name(self) -> str:
        "Returns the name of Player 2 as a string."
        return self.player2
    
    def get_player1_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 1 is currently on"""
        return self.player1_space
    
    def get_player2_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 2 is currently on"""
        return self.player2_space
        
    def get_current_player(self) -> str:
        """Returns the name of the current player."""
        if self.turn%2 == 0:
            return self.player1
        else:
            return self.player2
    
    def roll_dice(self) -> None:
        """Updates the game in-place by rolling dice."""
        dice_numbers = (random.randint(1, 6), random.randint(1, 6))
        if self.turn%2 ==0:
            self.player1_space = self.get_player1_space() + sum(dice_numbers)
        else:
            self.player2_space = self.get_player2_space() + sum(dice_numbers)
        self.turn = self.turn + 1

    def get_last_dice_roll(self) -> Optional[Tuple[int, int]]:
        """Returns either None or a pair of die rolls, like (2, 6)"""
        # if self.roll_dice():
        #     dice_numbers = (random.randint(1, 6), random.randint(1, 6))
        #     return dice_numbers
        # else:
        #     return None
        
    def is_over(self) -> bool:
        """Returns True if game is over."""
        if self.player1_space >= 63 | self.player2_space >= 63:
            return True
        else:
            return False
    
    def get_winner(self) -> Optional[str]:
        """Returns None (if the game is not over) or the name of the winner"""
        if self.player1_space >= 63:
            return self.get_player1_name()
        else:
            return self.get_player2_name()

        # elif self.player2_space == 63:
        #     return self.get_player2_name()
    
    
    