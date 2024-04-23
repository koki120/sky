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


def quick_sort(array: list, left_index: int, right_index: int) -> None:
    pivot: str = array[(left_index + right_index) // 2]
    left = []
    right = []

    for i in range(left_index, right_index):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])

    if len(left) > 0:
        next_right = left_index + len(left)
        array[next_right + 1] = pivot
        array[left_index:next_right] = left
        quick_sort(array=array, left_index=left_index, right_index=next_right)

    if len(right) > 0:
        next_left = right_index - len(right)
        array[next_left - 1] = pivot
        array[next_left:right_index] = right
        quick_sort(array=array, left_index=next_left, right_index=right_index)


def solver(input_stream: Iterable[str]) -> str:
    reserved_words = []

    result = []

    reserved_word_num = int(next(input_stream))

    for _ in range(reserved_word_num):
        reserved_words.append(
            alphabetical_order_string_to_number(next(input_stream).strip())
        )

    quick_sort(reserved_words, 0, reserved_word_num)

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
