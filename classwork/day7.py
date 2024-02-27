# TOH
# Recursion
# Difficult as helll!!!


# Normal TOH

# def toh(n, start, end, other):
#     if n == 1:
#         print(f"Move Disk 1 from {start} to {end}")
#         return

#     toh(n-1, start, other, end)
#     print(f"Move Disk {n} from {start} to {end}")
#     toh(n-1, other, end, start)


# Twisted TOH

# def toh(n, start, end, other):
#     if n == 1:
#         print(f"Move Disk 1 from {start} to {other}")
#         print(f"Move Disk 1 from {other} to {end}")
#         return

#     toh(n-1, start, end, other)
#     print(f"Move Disk {n} from {start} to {other}")
#     toh(n-1, end, start, other)
#     print(f"Move Disk {n} from {other} to {end}")
#     toh(n-1, start, end, other)


# toh(3, "A", "C", "B")


# ----------------Have to study this --------------------------
# def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
#     if n == 0:
#         return
#     TowerOfHanoi(n-1, from_rod, to_rod, aux_rod)
#     print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
#     TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# # Driver code
# N = 3

# # A, C, B are the name of rods
# TowerOfHanoi(N, 'A', 'C', 'B')
