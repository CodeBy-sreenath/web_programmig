def magic_square(n: int):
    """
    Returns an n x n magic square (list of lists).
    Supports:
      - Odd n  (Siamese / De la Loubère method)
      - Doubly even n (n % 4 == 0) (complement pattern)
    Raises:
      - ValueError for n == 2 or unsupported singly-even n (n % 2 == 0 and n % 4 != 0)
    """
    if n < 1:
        raise ValueError("Order n must be >= 1")
    if n == 1:
        return [[1]]
    if n == 2:
        raise ValueError("No normal magic square exists for n = 2.")
    if n % 2 == 1:
        return _magic_square_odd(n)
    if n % 4 == 0:
        return _magic_square_doubly_even(n)
    # singly even (n = 4k + 2) not implemented here
    raise ValueError("Singly-even order (n = 4k+2) not implemented in this snippet.")

def _magic_square_odd(n: int):
    # Siamese method
    square = [[0]*n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n*n + 1):
        square[i][j] = num
        ni, nj = (i - 1) % n, (j + 1) % n
        if square[ni][nj]:
            i = (i + 1) % n
        else:
            i, j = ni, nj
    return square

def _magic_square_doubly_even(n: int):
    # Fill 1..n^2 then complement specific cells
    square = [[i*n + j + 1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            # Keep cells where i%4 == j%4 or (i%4 + j%4) == 3; complement the rest
            if not ((i % 4 == j % 4) or ((i % 4 + j % 4) == 3)):
                square[i][j] = n*n + 1 - square[i][j]
    return square

def magic_constant(n: int) -> int:
    return n * (n*n + 1) // 2

def print_square(square):
    n = len(square)
    width = len(str(n*n))
    for row in square:
        print(" ".join(f"{v:>{width}}" for v in row))

# ---------- Demo ----------
if __name__ == "__main__":
    for N in (3, 4, 5, 8):  # change or add Ns as you like (avoid 2 and 6/10/14 here)
        try:
            ms = magic_square(N)
            print(f"\nMagic square (n={N}), M = {magic_constant(N)}")
            print_square(ms)
        except ValueError as e:
            print(f"\n(n={N}) -> {e}")
