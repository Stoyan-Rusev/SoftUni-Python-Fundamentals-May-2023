def sorting_tasks():
    notes_list = []
    while True:
        note = input()
        if note == "End":
            break
        notes_list.append(note)

    sorted_notes = sorted(notes_list, key=lambda x: int(x.split('-')[0]))
    result_sorted_notes = [note.split('-')[1] for note in sorted_notes]
    return result_sorted_notes


print(sorting_tasks())
