"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    return list((number, number + 1, number + 2))


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    for item in rounds:
        if item == number:
            return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    sum_hand = sum(hand)
    if len(hand) == 0:
        return None
    return sum_hand/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    if len(hand) % 2 == 0:
        pass
    else:
        mid_hand_card = hand[-((int(len(hand)/ 2)) + 1)]
        average_first_last_number = (hand[0] + hand[-1]) / 2
        if mid_hand_card == card_average(hand) or average_first_last_number == card_average(hand):
            return True
        return False
    


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    even_indexed_cards = hand[::2]
    odd_indexed_cards = hand[1::2]

    avg_even = card_average(even_indexed_cards)
    avg_odd = card_average(odd_indexed_cards)

    return avg_even == avg_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] > 10:
        hand[-1] = hand[-1] * 2
    return hand
