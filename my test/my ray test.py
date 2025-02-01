import ray
import time
import numpy as np

# Initialize Ray
ray.init()


@ray.remote
def compute():
    time.sleep(1)
    return np.random.rand(4000, 4000)


futures = [compute.remote() for _ in range(10)]

results = ray.get(futures)

ray.shutdown()
