def magic_square(square):
    # Check that the square has 3 rows and 3 columns
    if len(square) != 3 or any(len(row) != 3 for row in square):
        return False

    # Check that the square contains the numbers 1 through 9 exactly
    nums = set(num for row in square for num in row)
    if nums != set(range(1, 10)):
        return False

    # Calculate the sum of the first row
    total = sum(square[0])

    # Check the sum of each row
    for row in square:
        if sum(row) != total:
            return False

    # Check the sum of each column
    for col in range(3):
        if sum(square[row][col] for row in range(3)) != total:
            return False

    # Check the sum of each diagonal
    if square[0][0] + square[1][1] + square[2][2] != total:
        return False
    if square[0][2] + square[1][1] + square[2][0] != total:
        return False

    # If all checks pass, return True
    return True


def main():
    # Example Lo Shu Magic Square
    shu_square = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]

    if magic_square(shu_square):
        print("The given square is a Lo Shu Magic Square.")
    else:
        print("The given square is not a Lo Shu Magic Square.")


if __name__ == "__main__":
    main()
