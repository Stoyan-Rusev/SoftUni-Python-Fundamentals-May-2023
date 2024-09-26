elements = input().split()
stash_dict = {}
for i in range(0, len(elements), 2):
    stash_dict[elements[i]] = int(elements[i + 1])

searched_products = input().split()
for current_product in searched_products:
    if current_product in stash_dict.keys():
        print(f"We have {stash_dict[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")
