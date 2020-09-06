def validation(string):
    stage = [False, False, False, False]
    parts = []
    ret = {}
    string = string.replace(" ", "", 100)

    x_index = None
    equ_index = None

    try:
        x_index = string.index("x")
        stage[0] = True
        equ_index = string.index("=")
        stage[1] = True
        parts.append(string[equ_index + 1:x_index])
        parts.append(string[x_index + 1:])
        temp = int(parts[0])
        stage[2] = True
        temp = int(parts[1])
        if temp != 0:
            stage[3] = True
    except TypeError:
        pass
    except IndexError:
        pass
    except ValueError:
        pass

    for i in stage:
        if not i:
            return False

    ret["equ"] = string
    ret["m"] = int(parts[0])
    ret["b"] = int(parts[1])

    return ret


def hit(equation, position):
    if validation(equation) and type(position) is tuple:
        dic = validation(equation)
        y = dic["m"] * position[0] + dic["b"]
        if y == position[1]:
            print('Hit!!!')
        else:
            print("Didn't hit")
    else:
        print("The Equation is invalid!")


hit("y = 2x - 5", (1, -3))
