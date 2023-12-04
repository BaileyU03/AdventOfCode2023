def part01(cards):
    total = 0
    for line in cards:
        wins = get_winning_count(line)
        total += 2 ** (wins - 1) if wins else 0
    return total


def part02(cards):
    card_count = [1 for _ in cards]
    for card_pointer, card in enumerate(cards):
        win_count = get_winning_count(card)
        if win_count:
            for i in range(win_count):
                card_count[card_pointer + i + 1] += card_count[card_pointer]
    return sum(card_count)


def get_winning_count(card):
    winning, have = process_card(card)
    return sum([1 for number in winning if number in have])


def process_card(card):
    winning = list(map(int, card.split(":")[1].split(" | ")[0].split()))
    have = list(map(int, card.split(":")[1].split(" | ")[1].split()))
    return winning, have


def main():
    cards = []
    with open("./files/day04.txt", "r") as f:
        for line in f:
            cards.append(line)
    return part01(cards), part02(cards)


print(main())
