from solution import get_hand_types, calculate_winnings


def test_get_hand_types():
    hands = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
A8342 12
AAAAA 433
34QQQ 682
32QQQ 685
JJJJJ 785
4QQ44 124
44474 625"""

    # hands = "JJJJJ 785"

    expected = {
        'five': ["JJJJJ 785", "AAAAA 433"],
        'four': ["44474 625", "T55J5 684", "QQQJA 483", "KTJJT 220"],
        'full_house': ["4QQ44 124"],
        'three': ["32QQQ 685", "34QQQ 682"],
        'two_pair': ["KK677 28"],
        'one_pair': ["32T3K 765"],
        'highest_card': ["A8342 12"]
    }

    actual = get_hand_types(hands.splitlines())

    modified = {
        'five': [hand.original for hand in actual['five']],
        'four': [hand.original for hand in actual['four']],
        'full_house': [hand.original for hand in actual['full_house']],
        'three': [hand.original for hand in actual['three']],
        'two_pair': [hand.original for hand in actual['two_pair']],
        'one_pair': [hand.original for hand in actual['one_pair']],
        'highest_card': [hand.original for hand in actual['highest_card']]
    }

    assert modified == expected


def test_calculate_winnings():
    hands = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

    hand_types = get_hand_types(hands.splitlines())

    assert calculate_winnings(hand_types) == 5905