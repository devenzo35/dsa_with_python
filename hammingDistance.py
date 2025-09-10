# Hamming distance

text1 = "patitoswaaaaaat5"
text2 = "paratosaaaaaaaaa"

# Correct Result: 3


def hammingDistance(text1: str, text2: str) -> int:
    """Function to calculate the Hamming distance between two strings, strings should be the same
    length.

    Args:
        text1 (str): first text to be compared.
        text2 (str): second text to be compared.

    Raises:
        ValueError: if the two strings are not the same length.

    Returns:
        int: The distance calculated between the two strings
    """

    if len(text1) != len(text2):
        raise ValueError("Both strings should be the same length")

    # distance = 0

    # for idx, elem in enumerate(text1):
    #     if elem != text2[idx]:
    #         distance += 1

    # * using sum() instead of a explicit for loop

    return sum(elem1 != elem2 for elem1, elem2 in zip(text1, text2))


print(hammingDistance(text1, text2))
