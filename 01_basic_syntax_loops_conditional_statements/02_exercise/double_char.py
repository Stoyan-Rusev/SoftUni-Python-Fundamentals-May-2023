word = input()
while word != "End":
    if word == "SoftUni":
        word = input()
        continue
    double_char_word = ''
    for ch in word:
        double_char_word += ch * 2
    print(double_char_word)
    word = input()
