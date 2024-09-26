dict_sides_members = {}

data = input().split()
while data[0] != 'Lumpawaroo':
    side, action, member = data[0], data[1], data[2]
    if action == '|':
        if member not in dict_sides_members.values():
            if side not in dict_sides_members.keys():
                dict_sides_members[side] = [member]
            elif side in dict_sides_members.keys():
                dict_sides_members[side].append(member)

    elif action == '->':
        if member not in dict_sides_members.values():
            if side not in dict_sides_members.keys():
                dict_sides_members[side] = [member]
            elif side in dict_sides_members.keys():
                dict_sides_members[side].append(member)

        elif member in dict_sides_members.values():
            member_changing_side = ''
            member_new_side = ''
            for current_side, current_members_list in dict_sides_members:
                if member not in current_members_list:
                    member_new_side = current_side
            for current_side, current_members_list in dict_sides_members:
                if member in current_members_list:
                    member_changing_side = current_members_list.pop(member)
            dict_sides_members[member_new_side] = member_changing_side
        print(f"{member} joins the {side} side!")
    print(dict_sides_members)
    data = input().split()
