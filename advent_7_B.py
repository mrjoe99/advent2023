import os
import numpy as np

ABSOLUTE_PATH = os.path.dirname(__file__)
DAY = os.path.basename(__file__).split('_')[1].split(".")[0]

label_str = { # "label strength"
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}
type_strength = {
    "high_card": 1,
    "one_pair": 2,
    "two_pair": 3,
    "three_of_a_kind": 4,
    "full_house": 5,
    "four_of_a_kind": 6,
    "five_of_a_kind": 7
}

def get_input(file):
    input = []

    with open(file, 'r') as infile:
        for line in infile:
            hand, bid = line.strip("\n").split(" ")
            input.append([hand, int(bid)])

    return input

def classify_hands(hands):
    classifications = {}

    for x, hand in enumerate(hands):
        count = {}
        jokers = 0

        for letter in hand[0]:
            if letter == 'J':
                jokers += 1

            if letter not in count.keys():
                count[letter] = 1
            else:
                count[letter] += 1

        rank = determine_type(count, jokers)
        
        if rank not in classifications.keys():
            classifications[rank] = []

        classifications[rank].append(hands[x])

    return classifications
    
def determine_type(count, jokers):
    length = len(count) - jokers
    if length < 1:
        length = 1

    if length == 1:
        return type_strength["five_of_a_kind"]
    
    elif length == 2:
        for card_type in count:
            if count[card_type] == 4:
                return type_strength["four_of_a_kind"]
            elif count[card_type] == 3:
                return type_strength["full_house"]
            
    elif length == 3:
        for card_type in count:
            if count[card_type] == 3:
                return type_strength["three_of_a_kind"]
        return type_strength["two_pair"]
    
    elif length == 4:
        return type_strength["one_pair"]
    
    elif length == 5:
        return type_strength["high_card"]

def sort_hands(hands):
    converted = {}

    for group in hands:
        for hand in hands[group]:
            if group not in converted.keys():
                converted[group] = []

            converted[group].append(convert_labels(hand))

    for group in converted:
        temp = np.array(converted[group])
        converted[group] = (temp[np.lexsort(temp[:,::-1].T)]).tolist()

    return converted

def convert_labels(hand):
    conversion = []
    
    for card in hand[0]:
        conversion.append(label_str[card])
    
    return conversion

def assign_ranks(sorted_hands):
    ranked_hands = []
    rank = 1

    for x in range(1, 8):
        if x in sorted_hands.keys():
            for hand in sorted_hands[x]:
                ranked_hands.append(hand)
    
    return ranked_hands

def attach_bids(hands, ranked_hands):
    translated = []

    for hand_type in hands:
        for hand in hands[hand_type]:
            temp = []

            for card in hand[0]:
                temp.append(label_str[card])
        
            translated.append([temp, hand[1]])

    hands_and_bids = []

    for x, hand in enumerate(ranked_hands):
        for bid in translated:
            if hand == bid[0]:
                hands_and_bids.append([ranked_hands[x], bid[1]])

    return hands_and_bids

def calculate_winnings(hands):
    winnings = 0

    for x, hand in enumerate(hands):
        winnings += (x + 1) * hand[1]
    
    return winnings


if __name__ == '__main__':
    file = f'{ABSOLUTE_PATH}/advent_data_{DAY}.txt'
    #file = f'{ABSOLUTE_PATH}/example_advent_data_{DAY}.txt'

    hands = get_input(file)
    hands = classify_hands(hands)
    sorted_hands = sort_hands(hands)
    ranked_hands = assign_ranks(sorted_hands)
    ranked_hands = attach_bids(hands, ranked_hands)
    
    print(f"ANSWER: {calculate_winnings(ranked_hands)}")
    print(f"\n[COMPLETE] {__file__}")

    # 220560961, too low