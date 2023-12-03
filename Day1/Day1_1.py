with open("Day1/input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        numbers = ""
        for letter in line:
            if letter.isnumeric():
                numbers += letter

        sum += int(numbers[0]) * 10 + int(numbers[-1])

    print(sum)
