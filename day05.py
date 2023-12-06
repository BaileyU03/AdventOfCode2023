def part01():
    maps = []
    with open("./files/day05.txt", "r") as f:
        seeds = list(map(int, f.readline().split(":")[1].split()))
        current_map = []
        f.readline()
        for line in f:
            if line.isspace():
                maps.append(current_map)
                current_map = []
            elif not line[0].isalpha():
                current_map.append(list(map(int, line.split())))
        maps.append(current_map)

    updated = seeds.copy()
    for category in maps:
        for i, seed in enumerate(seeds):
            for cat_map in category:
                if cat_map[1] < seed < cat_map[1] + cat_map[2]:
                    updated[i] = cat_map[0] + (seed - cat_map[1])
                    break
        seeds = updated.copy()
    return min(seeds)


def init_seeds(seeds):
    new_seeds = []
    for i in range(0, len(seeds), 2):
        upper = seeds[i] + seeds[i + 1] - 1
        new_seeds.append([seeds[i], upper])
    return new_seeds


def generate_seeds(seeds):
    new_seeds = []
    for i in range(0, len(seeds), 2):
        lower = min(seeds[i], seeds[i + 1])
        upper = max(seeds[i], seeds[i + 1])
        new_seeds.append([lower, upper])
    return new_seeds


def split_seeds(category, seed):
    where_to_split = []
    for cat_map in category:
        lower = cat_map[1]
        upper = cat_map[1] + cat_map[2] - 1
        if lower <= seed[0] <= upper < seed[1]:
            where_to_split.append([upper, upper + 1])
        if seed[0] < lower <= seed[1] < upper:
            where_to_split.append([lower - 1, lower])
        if seed[0] < lower < upper < seed[1]:
            where_to_split.append([lower - 1, lower])
            where_to_split.append([upper, upper + 1])
    where_to_split = list(set(map(tuple, where_to_split)))
    new_seeds = [seed[0]]
    new_seeds += [seed for pair in where_to_split for seed in pair]
    new_seeds.append(seed[1])
    return generate_seeds(new_seeds)


def part02():
    maps = []
    with open("./files/day05.txt", "r") as f:
        seeds = init_seeds(list(map(int, f.readline().split(":")[1].split())))
        current_map = []
        f.readline()
        for line in f:
            if line.isspace():
                maps.append(current_map)
                current_map = []
            elif not line[0].isalpha():
                current_map.append(list(map(int, line.split())))
        maps.append(current_map)

    for category in maps:
        new_seeds = []
        for i, seed in enumerate(seeds):
            new_seeds += split_seeds(category, seed)
        updated = list(new_seeds)
        for i, up_seed in enumerate(new_seeds):
            for cat_map in category:
                if cat_map[1] <= up_seed[0] < cat_map[1] + cat_map[2] - 1:
                    updated[i][0] = cat_map[0] + (up_seed[0] - cat_map[1])
                    updated[i][1] = cat_map[0] + (up_seed[1] - cat_map[1])
                    break
        seeds = list(updated)
    print(seeds)
    return min([seed for pair in seeds for seed in pair])


print(part02())
