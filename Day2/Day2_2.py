with open("Day2/input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        color_dict = {
            "blue": 0,
            "green": 0,
            "red": 0
            }
        grabs = line[:-1].split(":")[1].split(";")
        for grab in grabs:
            colors = grab.split(',')
            for color in colors:
                split_color = color.strip().split(" ")
                if color_dict[split_color[1]] < int(split_color[0]):
                    color_dict[split_color[1]] = int(split_color[0])
        product = 1
        for value in color_dict.values():
            product *= value
        sum += product

    print(sum)
