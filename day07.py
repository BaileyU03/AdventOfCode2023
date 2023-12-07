class Hand:
    def __init__(self, line):
        split_line = line.split()
        self.cards = list(map(int,
                              list(map(lambda x:
                                       x.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14'), list(split_line[0])))))
        self.bid = int(split_line[1])

    def get_hand_type(self):
        cards_dict_count = list(self.get_cards_as_dict().values())
        cards_dict_count.sort()
        if cards_dict_count == [5]:
            return 0
        if cards_dict_count == [1, 4]:
            return 1
        if cards_dict_count == [2, 3]:
            return 2
        if cards_dict_count == [1, 1, 3]:
            return 3
        if cards_dict_count == [1, 2, 2]:
            return 4
        if cards_dict_count == [1, 1, 1, 2]:
            return 5
        return 6

    def get_cards_as_dict(self):
        cards_dict = {}
        for card in self.cards:
            if card in cards_dict.keys():
                cards_dict[card] += 1
            else:
                cards_dict[card] = 1
        return cards_dict

    def __lt__(self, other):
        if self.get_hand_type() != other.get_hand_type():
            return other.get_hand_type() < self.get_hand_type()
        for i in range(5):
            if self.cards[i] != other.cards[i]:
                return other.cards[i] > self.cards[i]
        return 0


def main():
    hands = []
    with open("./files/day07.txt", "r") as f:
        for line in f:
            hands.append(Hand(line))
    hands.sort()
    for hand in hands:
        print(hand.cards)
    total = 0
    for i, h in enumerate(hands):
        total += h.bid * (i + 1)
    return total


print(main())
