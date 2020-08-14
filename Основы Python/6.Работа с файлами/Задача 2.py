def get_shop_list_by_dishes (dishs, number):
    i = 0
    main = {}
    while i < len(dishs):
        file = open ("text.txt")
        q = False
        for lines in file:
            if lines == (dishs[i] + "\n"):
                q = True
            elif q == True:
                if len(lines) < 5:
                    continue
                elif lines != "\n":
                    main.update(support1("text.txt", lines, number))
        i += 1
        file.close
    return main

def support1 (_file, _line, number):
    file = open (_file)
    sup1 = {}
    for lines in file:
        if lines == _line:
            ABS = ""
            for line in lines:
                if line != " ":
                    ABS += line
                elif line == " " and ABS != "Запеченный":
                    sup1.update({ABS: support2(_file, _line, number)})
                    break
    file.close
    return sup1

def support2 (_file, _line, number):
    file = open (_file)
    sup2 = {}
    for lines in file:
        i = 0
        ABS = ""
        BAS = ""
        if lines == _line:
            for line in lines:
                if line == " ":
                    i += 1
                elif i == 2:
                    ABS += line
                elif i == 4 and line != lines[-1]:
                    BAS += line
                elif line == lines[-1] and ABS != "":
                    if line != "\n":
                        BAS += line
                    sup2.update({"measure": BAS})
                    sup2.update({"quantity": number*int(ABS)})
    file.close
    return sup2


print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))