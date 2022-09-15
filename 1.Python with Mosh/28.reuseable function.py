def emoji_converter(string):
    emojis = {
        ":)": "😀",
        ":(": "😞",
        "love": "💗"
    }
    output = " "
    for emoji in string:
        output = output + emojis.get(emoji, emoji) + " "
    return output


string = input("-> type hre : ")
string = string.split(" ")
message = emoji_converter(string)
print(message)
