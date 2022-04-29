import random


class Card:
    
    def __init__(self, card: str, value: int):
        '''Pass card: A♠, value: 1.'''
        self.card = card
        self.value = value

    def get_card(self):
        '''Print 3d:) card!'''
        for i in range(11):
            if i == 0 or i == 10:
                print('-------------')
            elif i == 1:
                print(f'| {self.card[0]}         |')
            elif i == 9:
                print(f'|         {self.card[0]} |')
            elif i == 5:
                print(f'|     {self.card[1]}     |')
            else:
                print('|           |')

class DeckCards:
    
    suit = ('♠', '♣', '♥', '♦')
    num = ('A', '2', '3', '4', '5', '6', 
             '7', '8', '9', 'T', 'J', 'Q', 'K')
    
    def __init__(self, value_cards, amount_deck=1):
        '''Pass amount of decks and value cards.'''
        self.stand_value = value_cards
        self.amount_deck = amount_deck
        self.deck = []
        self.burn_deck = []
        self.__init_deck_cards()
    
    def __init_deck_cards(self):
        for deck in range(self.amount_deck):
            for s in self.suit:
                for n in range(len(self.num)):
                    card = Card(self.num[n] + s, self.stand_value[n])
                    self.deck.append(card)
                
    def shuffle_deck(self):
        shuffle_deck = random.shuffle(self.deck)
        print('Shuffle deck finished!')
        
    def pick_one_card(self):
        card = self.deck.pop()
        self.burn_deck.append(card)
        card.get_card()
        return card.value
        
    def print_burn_deck(self):
        for card in self.burn_deck:
            print(card.get_value())
    
    def __len__(self):
        '''Return amount of cards in deck.'''
        return len(self.deck)
    
    
stand_value = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

deck = DeckCards(stand_value)
deck.shuffle_deck()
deck.print_burn_deck()
print(deck.pick_one_card())



