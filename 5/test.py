from unittest import TestCase, main
from number_to_alphabetical_order_string import (
    solver,
    number_to_alphabet,
    number_to_alphabetical_order_string,
    alphabetical_order_string_to_number,
)


class Test(TestCase):
    def test_to_number_to_alphabet(self):
        expected_alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i, expected_alphabet in enumerate(expected_alphabets):
            self.assertEqual(expected_alphabet, number_to_alphabet(i))

    # def test_to_convert_functions(self):
    #     for i in range(1, 1000_000):
    #         self.assertEqual(
    #             i,
    #             alphabetical_order_string_to_number(
    #                 number_to_alphabetical_order_string(i)
    #             ),
    #         )

    def test_to_solver(self):
        self.assertEqual("a c d", solver(iter(["1", "b", "3", "1 2 3"])))
        self.assertEqual(
            "d e h", solver(iter(["5", "g", "b", "f", "a", "c", "3", "1 2 3"]))
        )
        self.assertEqual("z aa", solver(iter(["2", "main", "else", "2", "26 27"])))
        self.assertEqual("f b b e", solver(iter(["1", "d", "4", "5 2 2 4"])))
        self.assertEqual(
            "sky quiz", solver(iter(["1", "welcome", "2", "13155 313248"]))
        )


if __name__ == "__main__":
    main()
