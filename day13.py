def main():
    images = []
    with open("./files/day13.txt", "r") as f:
        image = []
        for line in f:
            stripped_line = line.replace("\n", "")
            if len(stripped_line) == 0:
                images.append(image)
                image = []
            else:
                image.append(stripped_line)
        images.append(image)
    total = 0
    for image in images:
        found = False
        for h_pointer in range(1, len(image)):
            if is_mirror_here(image, h_pointer):
                total += 100 * h_pointer
                found = True
                break
        if found:
            continue
        t_image = list(zip(*image))
        for h_pointer in range(1, len(t_image)):
            if is_mirror_here(t_image, h_pointer):
                total += h_pointer
                break
    return total


def is_mirror_here(image, h_pointer):
    if h_pointer <= len(image) // 2:
        top = image[:h_pointer]
        bottom = image[h_pointer:(2 * h_pointer)]
    else:
        top = image[(2 * h_pointer - len(image)):h_pointer]
        bottom = image[h_pointer:]
    bottom.reverse()
    return top == bottom


print(main())
