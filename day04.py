def part01():
    total = 0
    with open("./files/day04.txt", "r") as f:
        for line in f:
            winning, have = process_card(line)
            points = 0
            for number in winning:
                if number in have:
                    points = points * 2 if points else 1
            total += points
    return total


def part02():
    cards = []
    card_count = []
    with open("./files/day04.txt", "r") as f:
        for line in f:
            cards.append(list(process_card(line)))
            card_count.append(1)
    card_pointer = 0
    while card_pointer < len(cards):
        card = cards[card_pointer]
        win_count = get_winning_count(card[0], card[1])
        if win_count:
            for i in range(win_count):
                card_count[card_pointer + i + 1] += card_count[card_pointer]
        card_pointer += 1
    return sum(card_count)



def process_card(card):
    winning = list(map(int, card.split(":")[1].split(" | ")[0].split()))
    have = list(map(int, card.split(":")[1].split(" | ")[1].split()))
    return winning, have


def get_winning_count(winning, have):
    total = 0
    for number in winning:
        if number in have:
            total += 1
    return total


print(part01())
print(part02())
