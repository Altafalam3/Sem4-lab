def moving_average(sequence, window_size):
    moving_averages = []
    for i in range(len(sequence) - window_size + 1):
        sum = 0
        for j in range(i, i + window_size):
            sum += sequence[j]
        moving_averages.append(sum/window_size)
    return moving_averages

sequence = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
window_size = 3

result = moving_average(sequence, window_size)
print(result)
