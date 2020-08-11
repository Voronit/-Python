def main (_file):
    file = open(_file)
    cook_book = {}
    i = True
    for lines in file:
        dish = ""
        if i == True:
            for line in lines:
                if line != "\n":
                    dish += line
                else:
                    cook_book.update({dish: support1(_file, lines)})
                    i = False
        elif lines == "\n":
            i = True
    file.close()
    return cook_book

def support1 (_file, line):
    file = open(_file)
    sup = []
    q = 0
    i = False
    for lines in file:
        if lines == line:
            i = True
        if i == True:
            if q < 2:
                q += 1
            elif lines != "\n":
                sup.append(support2(_file, lines))
            elif lines == "\n":
                q = 0
                i = False
    file.close()
    return sup

def support2 (_file, line):
    file = open (_file)
    sup = {}
    ind = "ingredient_name"
    for lines in file:
        ign = ""
        qua = ""
        mea = ""
        if lines == line:
            for line in lines:
                if  ind == "ingredient_name":
                    if line != "|" and line != " ":
                        ign += line
                    elif line == "|":
                        sup.update({ind: ign})
                        ind = "quantity"
                elif ind == "quantity":
                    if line != "|" and line != " ":
                        qua += line
                    elif line == "|":
                        sup.update({ind: qua})
                        ind = "measure"
                elif ind == "measure":
                    if line != "\n" and line != " ":
                        mea += line
                    if line == lines[-1] and mea != "":
                        sup.update({ind: mea})
    file.close()
    return sup

print (main ("text.txt"))