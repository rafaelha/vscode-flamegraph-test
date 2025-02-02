import numpy as np
import matplotlib.pyplot as plt
import qutip

def main():
    n = 300
    for _ in range(10):
        matrix = np.random.rand(4000, 4000)
        np.matmul(matrix[:n, :n], matrix[:n, :n])



if __name__ == "__main__":
    main()
    import time
    # time.sleep(1000)
