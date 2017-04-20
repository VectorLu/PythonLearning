def pascal_triangle(max):
    n = 0
    line = [1]
    while len(line) < max:
        yield(line)
        next_line = []
        for i in range(len(line)+1):
            if i == 0 or i == len(line):
                next_line.append(1)
            else:
                next_line.append(line[i-1] + line[i])
        line = next_line


for line in pascal_triangle(10):
    print(line)
