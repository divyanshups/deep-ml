import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    rng = np.random.default_rng(seed)
    n = data.shape[0]
    seq = rng.permutation(n)
    data = data[seq]
    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)

    return data[:train_end], data[train_end:validation_end], data[validation_end:]