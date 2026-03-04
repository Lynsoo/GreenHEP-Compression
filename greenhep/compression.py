import gzip
import lzma
import zstandard as zstd
import time


def compress_file(method, filename):
    start = time.time()

    if method == "gzip":
        out = filename + ".gz"
        with open(filename, "rb") as f_in, gzip.open(out, "wb") as f_out:
            for chunk in iter(lambda: f_in.read(1024 * 1024), b''):
                f_out.write(chunk)

    elif method == "lzma":
        out = filename + ".xz"
        with open(filename, "rb") as f_in, lzma.open(out, "wb") as f_out:
            # Process the file in chunks
            for chunk in iter(lambda: f_in.read(1024 * 1024), b''):
                f_out.write(chunk)

    elif method == "zstd":
        out = filename + ".zst"
        cctx = zstd.ZstdCompressor()
        with open(filename, "rb") as f_in, open(out, "wb") as f_out:
            # Process the file in chunks
            for chunk in iter(lambda: f_in.read(1024 * 1024), b''):
                f_out.write(cctx.compress(chunk))

    else:
        raise ValueError(f"Unsupported compression method: {method}")

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

    else:
        raise ValueError(f"Unsupported decompression method: {method}")

    elapsed = time.time() - start
    return elapsed
