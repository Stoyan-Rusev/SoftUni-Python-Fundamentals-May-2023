deck = input().split()
number_of_shuffles = int(input())
middle_of_deck = len(deck) // 2

for shuffle in range(number_of_shuffles):
    new_deck = []
    first_half = deck[:middle_of_deck]
    second_half = deck[middle_of_deck:]

    for deck_index in range(middle_of_deck):
        new_deck.append(first_half[deck_index])
        new_deck.append(second_half[deck_index])

    deck = new_deck

print(deck)
