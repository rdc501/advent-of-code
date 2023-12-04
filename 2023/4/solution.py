from collections import namedtuple


def parse_row(row):
    row = row.split(':')[1]
    sections = row.split('|')

    winning_numbers =  [int(number) for number in sections[0].split(' ') if number != '']
    numbers = [int(number) for number in sections[1].split(' ') if number != '']

    return winning_numbers, numbers


def get_matching_numbers(winning_numbers, numbers):
    return [number for number in numbers if number in winning_numbers]


def get_score(matching_numbers):
    match len(matching_numbers):
        case 0:
            return 0
        case 1:
            return 1

    return pow(2, len(matching_numbers) - 1)

def get_cards(all_matching_numbers):
    Result = namedtuple("Result", "winning_numbers amount")
    cards = [Result(winning_numbers, 1) for winning_numbers in all_matching_numbers]

    index = 0
    while index < len(all_matching_numbers):
        cards_won = len(all_matching_numbers[index])
        amount_to_add = cards[index].amount

        if cards_won > 0:
            cards_added = 1
            while cards_added <= cards_won:
                card = cards[index + cards_added]
                cards[index + cards_added] = Result(card.winning_numbers, card.amount + amount_to_add)
                cards_added += 1
        index += 1

    return cards

def get_total_cards(cards):
    amounts = [card.amount for card in cards]
    return sum(amounts)




file = open("input.txt", "r")
file_lines = file.readlines()

all_matching_numbers = [get_matching_numbers(*parse_row(row)) for row in file_lines]
scores = [get_score(matching_numbers) for matching_numbers in all_matching_numbers]

print(sum(scores))
print(get_total_cards(get_cards(all_matching_numbers)))