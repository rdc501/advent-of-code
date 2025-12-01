def get_hand_types(hands):
    hand_types = {
        'five': [],
        'four': [],
        'full_house': [],
        'three': [],
        'two_pair': [],
        'one_pair': [],
        'highest_card': []
    }

    for hand_string in hands:
        hand = Hand(hand_string)

        if hand.highest_number_of_cards() == 5:
            hand_types['five'].append(hand)
            continue
        if hand.highest_number_of_cards() == 4:
            hand_types['four'].append(hand)
            continue
        if hand.highest_number_of_cards() == 3 and hand.second_highest_number_of_cards() == 2:
            hand_types['full_house'].append(hand)
            continue
        if hand.highest_number_of_cards() == 3:
            hand_types['three'].append(hand)
            continue
        if hand.highest_number_of_cards() == 2 and hand.second_highest_number_of_cards() == 2:
            hand_types['two_pair'].append(hand)
            continue
        if hand.highest_number_of_cards() == 2:
            hand_types['one_pair'].append(hand)
            continue

        hand_types['highest_card'].append(hand)

    def sort_by_first_card(hand):
        return hand.cards_value()

    for key, value in hand_types.items():
        value.sort(key=sort_by_first_card)

    return hand_types

def calculate_winnings(hand_types):
    ranking = 1
    total = 0
    hand_lists = list(hand_types.items())
    hand_lists.reverse()

    for hand_list in hand_lists:
        for hand in hand_list[1]:
            total += ranking * int(hand.original[6:])
            ranking += 1

    return total

class Hand():
    def __init__(self, input):
        self.original = input

        self.card_counts = {}
        cards = input.split(' ')[0]
        self.bid = int(input.split(' ')[1])

        for card in cards:
            self.card_counts[card] = self.card_counts.get(card, 0) + 1

    def highest_number_of_cards(self):
        def fu(e):
            return e[1]

        z = [item for item in self.card_counts.items() if item[0] != 'J']
        z.sort(key=fu, reverse=True)

        if len(z) != 0:
            return z[0][1] + self.number_of_jokers()
        else:
            return 5

    def second_highest_number_of_cards(self):
        def fu(e):
            return e[1]

        z = [item for item in self.card_counts.items() if item[0] != 'J']
        z.sort(key=fu, reverse=True)
        return z[1][1]

    def number_of_jokers(self):
        return self.card_counts.get('J', 0)

    def cards_value(self):
        card_types = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        result = ''
        for card in self.original[:5]:
            result += str(card_types.index(card)).zfill(2)
        return int(result)





if __name__ == "__main__":
    file = open("input.txt", "r")
    file_lines = file.readlines()

    hand_types = get_hand_types(file_lines)
    winnings = calculate_winnings(hand_types)
    print(winnings)
