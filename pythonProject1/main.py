operators = {"plus": "+", "minus": "-", "divided": "/", "over": "/", "times": "*", "multiplied": "*"}
unknown_operators = ["cubed"]
non_math_keyword = ["who"]


def is_num(test_num):
    """
    takes a string input and tests if the string represents a number or a negative number
    """
    neg_test = ""
    if test_num[0] == "-":
        return test_num[1:].isnumeric()
    else:
        return test_num.isnumeric()


def alpha_sieve(word_list):
    alpha_set = []
    for i in word_list:
        neg_test = ""
        if i[0] == "-":
            neg_test = "-"
        alpha_filter = filter(str.isalnum, i)
        ans = neg_test + "".join(alpha_filter)
        alpha_set.append(ans)
    return alpha_set


def op_sieve(words):
    """
    Function to sieve the relevant operators and operants from the list of words
    """
    relevent = []
    for i in words:
        if i in unknown_operators:
            raise ValueError("unknown operation")
        elif i in operators.keys():
            relevent.append(operators[i])
        elif i[0] == "-" and i[1:].isnumeric():
            relevent.append(i)
        elif i.isnumeric():
            relevent.append(i)
    return relevent


def syntax_checks(syntax):
    if len(syntax) == 0:
        raise ValueError("syntax error")
    for nums in range(len(syntax)):
        if nums == 0:
            pass
        else:
            if is_num(syntax[nums]) and is_num(syntax[nums - 1]):
                raise ValueError("syntax error")
            elif not is_num(syntax[nums]) and not is_num(syntax[nums - 1]):
                raise ValueError("syntax error")
    if not is_num(syntax[0]) and not is_num(syntax[-1]):
        raise ValueError("syntax error")
    try:
        eval("".join(syntax))
    except:
        raise ValueError("syntax error")


def answer(question):
    alpha_set = alpha_sieve(question.lower().split())
    if alpha_set[0] in non_math_keyword:
        raise ValueError("unknown operation")
    relevent = op_sieve(alpha_set)
    syntax_checks(relevent)
    while len(relevent) > 3:
        x = "".join(relevent[:3])
        update = [str(eval(x))]
        update.append(relevent[3:])
        relevent = update.copy()
    eval_string = "".join(relevent)
    return eval(eval_string)