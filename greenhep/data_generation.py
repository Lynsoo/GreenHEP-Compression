import numpy as np
import struct
from .config import NUM_EVENTS, SCALE_FACTOR

def generate_event():
    px = np.random.normal(0, 1)
    py = np.random.normal(0, 1)
    pz = np.random.normal(5, 1)
    mass = 0.938
    energy = np.sqrt(px**2 + py**2 + pz**2 + mass**2)
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2*np.pi)
    return np.array([px, py, pz, energy, theta, phi], dtype=np.float64)

def generate_dataset(filename):
    with open(filename, "wb") as f:
        for _ in range(NUM_EVENTS):
            event = generate_event()
            scaled = (event * SCALE_FACTOR).astype(np.int64)
            f.write(struct.pack("6q", *scaled))
