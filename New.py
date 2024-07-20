def generate_password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, 20):
            if (i + j) == n:
                pairs.append(i)
                pairs.append(j)
    win = pairs
    return win

num = int(input("Введите число от 3 до 20:"))
if num >= 3 and num <= 20:

 win = generate_password(num)
 core = "".join(str(element) for element in win)


print(num, core)

