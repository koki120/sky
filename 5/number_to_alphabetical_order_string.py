from typing import Iterable
import bisect
import sys


def number_to_alphabet(num: int) -> str:
    return chr(ord("a") + num)


def alphabetical_order_string_to_number(chars: str) -> int:
    result = 0
    for i, char in enumerate(chars[::-1]):
        result += 26**i * (ord(char) - 96)
    return result


def number_to_alphabetical_order_string(num: int) -> str:
    quotient = num
    response = []
    while True:
        quotient, remainder = divmod(quotient - 1, 26)
        response.append(number_to_alphabet(remainder))
        if quotient == 0:
            break
    response.reverse()
    return "".join(response)


def solver(input_stream: Iterable[str]) -> str:
    reserved_words = []

    result = []

    reserved_word_num = int(next(input_stream))

    for _ in range(reserved_word_num):
        reserved_words.append(
            alphabetical_order_string_to_number(next(input_stream).strip())
        )

    reserved_words.sort()

    # Nの数が書かれている行は飛ばす。
    next(input_stream)

    n_list = [int(num) for num in str(next(input_stream)).split()]

    for n in n_list:
        current_skip = bisect.bisect_right(reserved_words, n)
        while (
            next_skip := bisect.bisect_right(reserved_words, n + current_skip)
        ) != current_skip:
            current_skip = next_skip

        result.append(number_to_alphabetical_order_string(n + current_skip))

    return " ".join(result)


if __name__ == "__main__":
    print(solver(sys.stdin))
