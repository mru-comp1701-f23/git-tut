def count_12s() -> int:
    """
    Counts the unique ways to sum to 12 using 6-sided dice.
    """
    num_ways = 0
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            if d1 + d2 == 12:
                num_ways += 1
    return num_ways

def main() -> None:
    """
    Program Entry point.
    """
    print(count_12s())

main()