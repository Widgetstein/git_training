

def give_me_a_hello():
    print("Git says hi")


def give_me_a_goodbye():
    raise NotImplementedError("please create a message that says goodbye")




if __name__ == "__main__":
    print(
        "the program starts here"
    )
    give_me_a_hello()

    give_me_a_goodbye()