def sliding_window(sequence, window_size):
    if window_size <= 0:
        raise ValueError("window_size must be positive")
    for i in range(len(sequence) - window_size + 1):
        yield sequence[i:i + window_size]

data = [1, 2, 3, 4, 5]
for window in sliding_window(data, 3):
    print(window)
