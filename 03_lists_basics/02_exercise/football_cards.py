team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

while True:
    cards = input()
    list_of_cards = cards.split()
    game_is_terminated = False

    for card in list_of_cards:
        if card in team_a:
            team_a.remove(card)
        elif card in team_b:
            team_b.remove(card)

        if len(team_a) < 7 or len(team_b) < 7:
            game_is_terminated = True

        if game_is_terminated:
            print(f'Team A - {len(team_a)}'
                  f'Team B - {len(team_b)}'
                  f'Game was terminated')
            break
        else:
            print(f'Team A - {len(team_a)}'
                  f'Team B - {len(team_b)}')
            break
    break
