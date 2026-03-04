import gzip
import lzma
import zstandard as zstd
import time
import os


def compress_file(method, filename):
    start = time.time()

    if method == "gzip":
        out = filename + ".gz"
        with open(filename, "rb") as f_in, gzip.open(out, "wb") as f_out:
            f_out.writelines(f_in)

    elif method == "lzma":
        out = filename + ".xz"
        with open(filename, "rb") as f_in, lzma.open(out, "wb") as f_out:
            f_out.write(f_in.read())

    elif method == "zstd":
        out = filename + ".zst"
        cctx = zstd.ZstdCompressor()
        with open(filename, "rb") as f_in, open(out, "wb") as f_out:
            f_out.write(cctx.compress(f_in.read()))

    elapsed = time.time() - start
    return out, elapsed



def decompress_file(method, filename):
    start = time.time()

    if method == "gzip":
        with gzip.open(filename, "rb") as f:
            f.read()

    elif method == "lzma":
        with lzma.open(filename, "rb") as f:
            f.read()

    elif method == "zstd":
        dctx = zstd.ZstdDecompressor()
        with open(filename, "rb") as f:
            dctx.decompress(f.read())

    return time.time() - start
  
