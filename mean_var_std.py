import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    np_list = np.array(list).reshape(3, 3)

    return {
        "mean": [
            np.mean(np_list, axis=0).tolist(),
            np.mean(np_list, axis=1).tolist(),
            np.mean(np_list).tolist(),
        ],
        "variance": [
            np.var(np_list, axis=0).tolist(),
            np.var(np_list, axis=1).tolist(),
            np.var(np_list).tolist(),
        ],
        "standard deviation" : [
            np.std(np_list, axis=0).tolist(),
            np.std(np_list, axis=1).tolist(),
            np.std(np_list).tolist(),
        ],
        "min": [
            np.min(np_list, axis=0).tolist(),
            np.min(np_list, axis=1).tolist(),
            np.min(np_list).tolist(),
        ],
        "max": [
            np.max(np_list, axis=0).tolist(),
            np.max(np_list, axis=1).tolist(),
            np.max(np_list).tolist(),
        ],
        "sum": [
            np.sum(np_list, axis=0).tolist(),
            np.sum(np_list, axis=1).tolist(),
            np.sum(np_list).tolist(),
        ],
    }
