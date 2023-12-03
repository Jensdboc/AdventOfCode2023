max_colors = {
            "blue": 14,
            "green": 13,
            "red": 12
            }

with open("Day2/input.txt", "r") as f:
    index = 1
    sum = 0
    for line in f.readlines():
        grabs = line[:-1].split(":")[1].split(";")
        add = True
        for grab in grabs:
            color_dict = {
                "blue": 0,
                "green": 0,
                "red": 0
                }
            colors = grab.split(',')
            for color in colors:
                split_color = color.strip().split(" ")
                color_dict[split_color[1]] += int(split_color[0])
            for key, value in color_dict.items():
                if value > max_colors[key]:
                    add = False
        if add:
            sum += index
        index += 1

    print(sum)
