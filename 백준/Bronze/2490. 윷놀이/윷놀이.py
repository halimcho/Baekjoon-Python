for _ in range(3):
    line = list(map(int, input().split()))
    zero_count = line.count(0)

    if zero_count == 0:
        print('E')  # 모
    elif zero_count == 1:
        print('A')  # 도
    elif zero_count == 2:
        print('B')  # 개
    elif zero_count == 3:
        print('C')  # 걸
    elif zero_count == 4:
        print('D')  # 윷

        