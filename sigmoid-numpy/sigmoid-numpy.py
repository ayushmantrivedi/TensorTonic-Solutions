import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x_arr = np.asarray(x)
    result = 1.0/(1.0 +np.exp(-x_arr))
    if x_arr.ndim == 0:
        return float(result)
    return result.astype(float)    