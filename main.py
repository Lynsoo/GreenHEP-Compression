import os
import pandas as pd
import matplotlib.pyplot as plt

from greenhep.config import RAW_FILE, DELTA_FILE
from greenhep.data_generation import generate_dataset
from greenhep.encoding import delta_encode
from greenhep.compression import compress_file, decompress_file
from greenhep.energy_model import cpu_energy, storage_energy, carbon

def run_experiment(input_file, label):

    raw_size = os.path.getsize(input_file)
    results = []

    for method in ["gzip", "lzma", "zstd"]:
        comp_file, t_comp = compress_file(method, input_file)
        t_decomp = decompress_file(method, comp_file)
        comp_size = os.path.getsize(comp_file)

        e_total = cpu_energy(t_comp + t_decomp) + storage_energy(comp_size)

        results.append([
            label,
            method,
            raw_size,
            comp_size,
            t_comp,
            t_decomp,
            e_total,
            carbon(e_total)
        ])

    return results

if __name__ == "__main__":

    os.makedirs("data", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    generate_dataset(RAW_FILE)
    delta_encode(RAW_FILE, DELTA_FILE)

    results = []
    results += run_experiment(RAW_FILE, "raw")
    results += run_experiment(DELTA_FILE, "delta")

    df = pd.DataFrame(results, columns=[
        "Dataset", "Algorithm", "Raw Size",
        "Compressed Size", "Compression Time",
        "Decompression Time", "Total Energy (kWh)",
        "Total CO2 (kg)"
    ])

    df.to_csv("results/msc_results.csv", index=False)

    plt.figure(figsize=(10, 5))
    for dataset in df["Dataset"].unique():
        subset = df[df["Dataset"] == dataset]
        plt.bar(
            subset["Algorithm"] + "_" + dataset,
            subset["Total Energy (kWh)"]
        )

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("results/energy_comparison.png")
