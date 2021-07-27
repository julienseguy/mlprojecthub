from termcolor import colored

def try_me():

    return "Hello my name is Julien"


def who_am_i():

    name = try_me()

    # cannot be tested since the function returns None implicitly
    print(colored(name, "blue"))
