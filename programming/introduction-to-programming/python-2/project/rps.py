#!/usr/bin/env python3

import random
import math

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round. The game ends when one Player
# has a score difference of 3.

moves = ['rock', 'paper', 'scissors']


# The Player class is the parent class for all of the Players
# in this game. It contains the basic functionality for all Players.
class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.score = 0
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        pass

    def move(self):
        return self.my_move


class BasicPlayer(Player):
    def move(self):
        return "rock"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = input(f"{self.name}, enter your move (rock, paper, scissors): ")
        while move not in moves:
            move = input(f"{self.name}, invalid move. "
                         "Enter your move (rock, paper, or scissors): ")
        return move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        return moves[(moves.index(self.my_move) + 1) % len(moves)]

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"{self.p1.name}: {move1}  {self.p2.name}: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print(f"{self.p1.name} wins the round!")
            self.p1.score += 1
        elif beats(move2, move1):
            print(f"{self.p2.name} wins the round!")
            self.p2.score += 1
        else:
            print(f"{self.p1.name} & {self.p2.name} tie!")
        print(f"Score: {self.p1.name}: {self.p1.score}  "
              f"{self.p2.name}: {self.p2.score}")

    def play_game(self):
        print("Game Start!")
        round = 0
        # Play until one player has a score difference of 3
        while math.fabs(self.p1.score - self.p2.score) < 3 and round < 100:
            round += 1
            print(f"\nRound {round}:")
            self.play_round()
        print(f"\nFinal Score: {self.p1.name}: {self.p1.score}  "
              f"{self.p2.name}: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print(f"{self.p1.name} wins the game!")
        elif self.p1.score < self.p2.score:
            print(f"{self.p2.name} wins the game!")
        else:
            print("It's a tie!")
        print("\nGame Over!")


if __name__ == '__main__':
    modes = [HumanPlayer, RandomPlayer, ReflectPlayer,
             CyclePlayer, BasicPlayer]
    # Get player names and modes
    try:
        print("Welcome to Rock, Paper, Scissors!")
        print("This is a game between two players. "
              "First to 3 points difference wins! "
              "Maximum of 100 rounds.")
        print("Choose your players:")
        p1_name = input("Enter Player 1 name: ")
        if p1_name == "":
            p1_name = "Player 1"
        p2_name = input("Enter Player 2 name: ")
        if p2_name == "":
            p2_name = "Player 2"
        print("Choose Player modes:")
        p1_mode = modes[int(input("Choose Player 1 (0: Human, 1: "
                                  "Random, 2: Reflect, 3: Cycle,: "
                                  "4: Basic): "))]
        p2_mode = modes[int(input("Choose Player 2 (0: Human, 1: "
                                  "Random, 2: Reflect, 3: Cycle,: "
                                  "4: Basic): "))]
        game = Game(p1_mode(p1_name), p2_mode(p2_name))
    except (ValueError, IndexError):
        print("Invalid input. Defaulting to Human vs Random.")
        game = Game(HumanPlayer(p1_name), RandomPlayer(p2_name))
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting.")
        exit()
    # Create players and start game
    try:
        game.play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting.")
        exit()
