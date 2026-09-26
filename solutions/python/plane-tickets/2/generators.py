"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    seat_letters = ['A', 'B', 'C', 'D']
    for letter in range(number):
        yield seat_letters[letter % 4]
        


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    row = 1
    seat_letters = ['A', 'B', 'C', 'D']
    for i in range(number):
        if row == 13:
            row += 1
        yield f"{row}{seat_letters[i % 4]}"
        if (i + 1) % 4 == 0:
            row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_assignments = {}
    seat_generator = generate_seats(len(passengers))
    for passenger in passengers:
        seat_assignments[passenger] = next(seat_generator)
    return seat_assignments


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        ticket_code = f"{seat}{flight_id}".ljust(12, '0')
        yield ticket_code
