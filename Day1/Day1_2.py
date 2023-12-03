number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("Day1/input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        origline = line
        numbers = ""
        for key, value in number_dict.items():
            # Put the typed number before and after the replaced number
            # This allows overlapping numbers to be checked aswell
            # twone => two + one
            line = line.replace(key, key + value + key)
        for letter in line:
            if letter.isnumeric():
                numbers += letter

        sum += int(numbers[0]) * 10 + int(numbers[-1])

    print(sum)
