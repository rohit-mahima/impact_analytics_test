class InvalidType(Exception):
    """Exception to Check Invalid data type"""
    pass


def attendance_probability(days: int) -> str:
    """ Calculates attendance probability for
    attending ceremony using the Number of days """
    try:
        if not isinstance(days, int):
            raise InvalidType("Invalid days type")

        valid_attendance = [0] * (days + 1)
        missing_possibility = [0] * (days + 1)

        # Base cases for the total possibilities
        valid_attendance[0] = 1
        if days >= 1:
            valid_attendance[1] = 2
        if days >= 2:
            valid_attendance[2] = 4
        if days >= 3:
            valid_attendance[3] = 8
        if days >= 4:
            valid_attendance[4] = 15

        # Base cases for the missing possibilities
        missing_possibility[0] = 0
        if days >= 1:
            missing_possibility[1] = 1
        if days >= 2:
            missing_possibility[2] = 2
        if days >= 3:
            missing_possibility[3] = 4
        if days >= 4:
            missing_possibility[4] = 7

        # Compute values using the recurrence relations
        for i in range(5, days + 1):
            valid_attendance[i] = 2 * valid_attendance[i - 1] - valid_attendance[i - 5]
            missing_possibility[i] = valid_attendance[i - 1] - valid_attendance[i - 5]

        # The probability is the number of sequences missing the last day divided by total sequences
        return f"{missing_possibility[days]} / {valid_attendance[days]}"
    except Exception as e:
        return e


if __name__ == '__main__':
    print(attendance_probability(4))  # Output: ?
    print(attendance_probability(5))  # Output: 14/29
    print(attendance_probability(6))  # Output: ?
    print(attendance_probability(10))  # Output:372/773
    print(attendance_probability(11))  # Output:?
    print(attendance_probability('11'))
