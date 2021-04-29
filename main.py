ranges = []
starts = []
ends = []

def calc():
    maxOverlap = 0
    currentOverlap = 0

    starts.sort()
    ends.sort()
    i = 0
    j = 0
    m = len(starts)
    n = len(ends)
    start = starts[0]
    end = ends[0]
    while i < m and j < n:
        if starts[i] <= ends[j]:
            currentOverlap += 1
            if (currentOverlap >= maxOverlap):
                start = starts[i]
                end = ends[j]
            maxOverlap = max(maxOverlap, currentOverlap)

            i += 1

        else:
            currentOverlap -= 1
            end = ends[j]
            j += 1

    return [maxOverlap, [start, end]]

def main():
    loop(step)


def getNumber(text):
    number = int(input(text))
    if number < 0 or number > 100:
        print("Incorrect value. Should be in range [0,100]")
        return getNumber(text)
    return number


def getNumbers():
    x = getNumber("Enter the first number:")
    y = getNumber("Enter the second number:")
    return [x, y]


def printResult(res):
    print(res)


def step():
    [x, y] = getNumbers()
    if x <= y:
        ranges.append([x, y])
        starts.append(x)
        ends.append(y)
    else:
        ranges.append([y, x])
        starts.append(y)
        ends.append(x)
    result = calc()
    printResult(result)


def loop(cb):
    while True:
        cb()


main()
