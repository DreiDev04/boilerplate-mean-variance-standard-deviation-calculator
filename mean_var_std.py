import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    np_list = np.array(list).reshape(3, 3)

    return {
        'mean': [
    np.mean(np_list, axis=0).tolist(),
    np.mean(np_list, axis=1).tolist(),
    np.mean(np_list).tolist()
    ], 
'variance': [
    np.var(np_list, axis=0).tolist(),
    np.var(np_list, axis=1).tolist(),
    np.var(np_list).tolist()
    ]
    }
