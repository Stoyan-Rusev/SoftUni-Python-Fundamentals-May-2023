def loading_bar(percents: int) -> str:
    loaded_parts_out_of_ten = percents // 10
    loading_bar_string = f"[{loaded_parts_out_of_ten * '%'}{(10 - loaded_parts_out_of_ten) * '.'}]"

    if percents == 100:
        return f"100% Complete!\n{loading_bar_string}"

    return f"{percents}% {loading_bar_string}\nStill loading..."


loaded_percents = int(input())
print(loading_bar(loaded_percents))
