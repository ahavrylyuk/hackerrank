def safe_pawns(pawns):
    matrix = [None] * 8
    for i in range(8):
        matrix[i] = [0] * 8
    for pawn in pawns:
        x, y = list(pawn)
        matrix[8 - int(y)][ord(x) - ord('a')] = 1
    safe = 0
    for i in range(7):
        for j in range(8):
            if matrix[i][j] == 1:
                if (j > 0 and matrix[i+1][j-1]) or (j < 7 and matrix[i+1][j+1] == 1):
                    safe += 1
    return safe

assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
assert safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}) == 7
assert safe_pawns({"a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"}) == 7
