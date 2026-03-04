import numpy as np
import struct


def delta_encode(input_file, output_file):
    with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
        prev = np.zeros(6, dtype=np.int64)
        while True:
            bytes_read = f_in.read(48)
            if not bytes_read:
                break
            current = np.array(struct.unpack("6q", bytes_read))
            delta = current - prev
            f_out.write(struct.pack("6q", *delta))
            prev = current
