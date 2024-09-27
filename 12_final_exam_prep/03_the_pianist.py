def adding(pieces_dict: dict, parameters: list):
    new_piece = parameters[0]
    new_composer = parameters[1]
    new_key = parameters[2]

    if new_piece not in pieces_dict:
        pieces_dict[new_piece] = {"Composer": new_composer,
                                  "Key": new_key}
        print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
    else:
        print(f"{new_piece} is already in the collection!")


def removing(pieces_dict: dict, parameters: list):
    piece_to_remove = parameters[0]
    if piece_to_remove in pieces_dict.keys():
        del pieces_dict[piece_to_remove]
        print(f"Successfully removed {piece_to_remove}!")
    else:
        print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")


def changing_key(pieces_dict: dict, parameters: list):
    piece_to_edit = parameters[0]
    new_key = parameters[1]

    if piece_to_edit in pieces_dict.keys():
        pieces_dict[piece_to_edit]["Key"] = new_key
        print(f"Changed the key of {piece_to_edit} to {new_key}!")
    else:
        print(f"Invalid operation! {piece_to_edit} does not exist in the collection.")


initial_number_of_pieces = int(input())
initial_composers_dict = {}

for num in range(initial_number_of_pieces):
    initial_data = input().split("|")
    piece = initial_data[0]
    composer = initial_data[1]
    key = initial_data[2]
    initial_composers_dict[piece] = {"Composer": composer,
                                     "Key": key}

command = input()
while command != "Stop":
    command = command.split("|")
    action, *params = command
    if action == "Add":
        adding(initial_composers_dict, params)
    elif action == "Remove":
        removing(initial_composers_dict, params)
    elif action == "ChangeKey":
        changing_key(initial_composers_dict, params)
    command = input()

for current_piece, current_values in initial_composers_dict.items():
    print(f"{current_piece} -> Composer: {current_values['Composer']}, Key: {current_values['Key']}")
