class Hand:
    def __init__(self, line, is_part2):
        split_line = line.split()
        self.cards = list(map(int,
                              list(map(lambda x:
                                       x.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14'),
                                       list(split_line[0])))))
        self.bid = int(split_line[1])
        if is_part2:
            new_cards = list(map(lambda x: 1 if x == 11 else x, self.cards[:]))
            self.cards_to_rank = new_cards
            self.cards_for_type = self.get_best_wildcard_hand(new_cards)
        else:
            self.cards_to_rank = self.cards_for_type = self.cards

    def get_hand_type(self, cards):
        cards_dict_count = list(self.get_cards_as_dict(cards).values())
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

    def get_cards_as_dict(self, cards):
        cards_dict = {}
        for card in cards:
            if card in cards_dict.keys():
                cards_dict[card] += 1
            else:
                cards_dict[card] = 1
        return cards_dict

    def get_best_wildcard_hand(self, cards):
        best_hand = None
        indices = [i for i in range(5) if cards[i] == 1]
        if not indices:
            return cards
        for face in range(2, 15):
            new_cards = cards[:]
            new_cards[indices[0]] = face
            if len(indices) > 1:
                new_cards = self.get_best_wildcard_hand(new_cards)
            if not best_hand:
                best_hand = new_cards
            elif self.get_hand_type(new_cards) < self.get_hand_type(best_hand):
                best_hand = new_cards
        return best_hand

    def __lt__(self, other):
        if self.get_hand_type(self.cards_for_type) != other.get_hand_type(other.cards_for_type):
            return other.get_hand_type(other.cards_for_type) < self.get_hand_type(self.cards_for_type)
        for i in range(5):
            if self.cards_to_rank[i] != other.cards_to_rank[i]:
                return other.cards_to_rank[i] > self.cards_to_rank[i]
        return 0


def main(is_part2):
    hands = []
    with open("./files/day07.txt", "r") as f:
        for line in f:
            hands.append(Hand(line, is_part2))
    hands.sort()
    total = 0
    for i, h in enumerate(hands):
        total += h.bid * (i + 1)
    return total


print(main(False))
print(main(True))
