import argparse



def jadge(letters):
    if (letters == ".-"): return "a"
    elif (letters == "-..."): return "b"
    elif (letters == "-.-."): return "c"
    elif (letters == "-.."): return "d"
    elif (letters == "."): return "e"
    elif (letters == "..-."): return "f"
    elif (letters == "--."): return "g"
    elif (letters == "...."): return "h"
    elif (letters == ".."): return "i"
    elif (letters == ".---"): return "j"
    elif (letters == "-.-"): return "k"
    elif (letters == ".-.."): return "l"
    elif (letters == "--"): return "m"
    elif (letters == "-."): return "n"
    elif (letters == "---"): return "o"
    elif (letters == ".--."): return "p"
    elif (letters == "--.-"): return "q"
    elif (letters == ".-."): return "r"
    elif (letters == "..."): return "s"
    elif (letters == "-"): return "t"
    elif (letters == "..-"): return "u"
    elif (letters == "...-"): return "v"
    elif (letters == ".--"): return "w"
    elif (letters == "-..-"): return "x"
    elif (letters == "-.--"): return "y"
    elif (letters == "--.."): return "z"
    elif (letters == "---..."): return ":"
    elif (letters == "-.--.-"): return ")"
    elif (letters == "..--.-"): return "_"


def dec_morse(code, deli):
    codes = code
    d = deli
    tmp = ""
    sentence = ""
    for l in list(codes):
        if(l == d): 
            sentence += jadge(tmp)
            tmp = ""
            continue
        tmp += l
    sentence += jadge(tmp)
    return sentence
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("code", help="morse code")
    parser.add_argument("deli", help="delimiter")
    args = parser.parse_args()
    
    print(dec_morse(args.code, args.deli))
