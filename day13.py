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
                image.append(list(stripped_line))
        images.append(image)
    total1 = 0
    total2 = 0
    for x, image in enumerate(images):
        found = False
        for h_pointer in range(1, len(image)):
            if is_mirror_here(image, h_pointer):
                total1 += 100 * h_pointer
                found = True
                original_line = ["h", h_pointer]
                break
        if not found:
            t_image = list(zip(*image))
            for h_pointer in range(1, len(t_image)):
                if is_mirror_here(t_image, h_pointer):
                    total1 += h_pointer
                    original_line = ["v", h_pointer]
                    break
        found = False
        for i in range(len(image)):
            for j in range(len(image[0])):
                new_image = [x[:] for x in image]
                new_image[i][j] = "#" if image[i][j] == "." else "."
                for h_pointer in range(1, len(new_image)):
                    if is_mirror_here(new_image, h_pointer) and not (original_line[0] == "h" and original_line[1] == h_pointer):
                        total2 += 100 * h_pointer
                        found = True
                        break
                if found:
                    break
                t_image = list(zip(*new_image))
                for h_pointer in range(1, len(t_image)):
                    if is_mirror_here(t_image, h_pointer) and not (original_line[0] == "v" and original_line[1] == h_pointer):
                        total2 += h_pointer
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return total1, total2


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
