def main():
    seeds = []
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


print(main())

