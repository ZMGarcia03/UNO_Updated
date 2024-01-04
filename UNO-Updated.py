import random

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return f"{self.color.capitalize()} {self.number}"

class Deck:
    def __init__(self):
        self.cards = []
        for color in ['red', 'green', 'blue', 'yellow']:
            for number in range(1, 10):
                self.cards.append(Card(color, number))
                self.cards.append(Card(color, number))
                if number < 8:
                    self.cards.append(Card(color, number + 2))
                    self.cards.append(Card(color, number + 2))
        self.cards.append(Card('red', 'skip'))
        self.cards.append(Card('green', 'skip'))
        self.cards.append(Card('blue', 'skip'))
        self.cards.append(Card('yellow', 'skip'))
        self.cards.append(Card('red', 'reverse'))
        self.cards.append(Card('green', 'reverse'))
        self.cards.append(Card('blue', 'reverse'))
        self.cards.append(Card('yellow', 'reverse'))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = [[] for _ in range(num_players)]
        self.deck = Deck()
        self.deck.shuffle()
        self.turn = 0
        self.direction = 1

    def deal_cards(self):
        for player in range(self.num_players):
            self.players[player] = self.deck.deal(7)

    def play_card(self, card):
        current_card = self.players[self.turn].pop(0)
        if card.color != current_card.color and card.number != current_card.number:
            print("You cannot play that card.")
            return False
        else:
            print(f"Player {self.turn + 1} played {card}")
            return True

    def start_game(self):
        self.deal_cards()
        while True:
            current_player = self.turn % self.num_players
            print(f"\nPlayer {current_player + 1}'s turn")
            print(f"Current card: {self.players[self.turn][0]}")
            card_to_play = input("Enter the card number to play or type 'pass': ").strip()
            if card_to_play.lower() == 'pass':
                self.turn += self.direction
            else:
                try:
                    card_number = int(card_to_play)
                    if 1 <= card_number <= 9:
                        for card in self.players[current_player]:
                            if card.number == card_number:
                                self.turn += self.direction
                                break
                    elif card_number == 10:
                        self.direction *= -1
                        self.turn += self.direction
                    else:
                        print("Invalid card number.")
                except ValueError:
                    print("Invalid input.")

game = Game(4)
game.start_game()
