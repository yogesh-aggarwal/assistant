import random


def generate():
    return random.choice(["ROCK", "PAPER", "SCISSORS"])


def winDecide(userO, codeO=generate()):
    return (
        True
        if (
            (userO == "PAPER" and codeO == "ROCK")
            or (userO == "SCISSORS" and codeO == "PAPER")
            or (userO == "ROCK" and codeO == "SCISSORS")
        )
        else False
    )
