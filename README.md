# GreenHEP-Compression

A research-grade framework for evaluating compression algorithms in High Energy Physics (HEP) workflows with integrated energy consumption and carbon footprint analysis.

---

## Abstract

Modern High Energy Physics (HEP) experiments generate petabyte-scale datasets.
While compression reduces storage requirements, it introduces computational overhead that consumes energy and produces carbon emissions.

This project provides a reproducible benchmarking framework that evaluates:

* Binary compression algorithms (gzip, lzma, zstd)
* Delta encoding pre-processing
* ROOT internal compression levels
* CPU energy consumption during compression/decompression
* Long-term storage energy costs
* Total carbon footprint impact

The goal is to determine whether compression strategies reduce overall environmental impact when both compute and storage energy are considered.

---

## Motivation

Large-scale experiments such as those conducted at facilities like CERN rely heavily on ROOT-based data formats and multi-year storage infrastructures.

Sustainability in scientific computing is becoming a critical concern.
Compression is typically evaluated only by:

* Compression ratio
* Throughput
* Decompression speed

This framework extends evaluation to include:

* Energy consumption (kWh)
* Storage lifetime energy cost
* CO₂ emissions (kg)

This enables environmentally-aware optimization of data pipelines.

---

## What This Project Does

1. Simulates particle collision events
2. Stores raw binary datasets
3. Applies delta encoding
4. Benchmarks:

   * gzip
   * lzma
   * zstd
5. Generates ROOT files with configurable compression levels
6. Measures:

   * Compression time
   * Decompression time
   * File size
   * Total energy consumption
   * Carbon emissions
7. Exports results to CSV
8. Produces comparative energy visualization plots

---

## Features

* Monte Carlo particle event generation
* Delta encoding implementation
* ROOT TTree generation with configurable compression levels
* Energy consumption modeling
* Carbon emission estimation
* Automatic benchmarking
* CSV export of results
* Energy comparison visualization

---

## Energy Model

Total energy is calculated as:

Total Energy =
CPU Energy (compression + decompression)

* Storage Energy (multi-year retention)

Carbon emissions are computed as:

CO₂ = Energy × Carbon Intensity

Parameters such as CPU power, storage intensity, and retention period are configurable.

---

## Installation

```bash
git clone https://github.com/lynashere/GreenHEP-Compression.git
cd GreenHEP-Compression
pip install -r requirements.txt
```

To install the GreenHEP package, add : 

```bash
pip install .
```
---

## Run Full Experiment

```bash
python main.py
```
---

## Research Applications

* Sustainable computing in High Energy Physics
* Green data center optimization
* Compression-energy tradeoff analysis
* Computational research
* Infrastructure carbon auditing

---

## Future Extensions

* Parallel compression benchmarking
* GPU compression comparison
* Real experimental datasets
* Distributed storage modeling
* Life-cycle analysis of scientific data pipelines

---

## License

MIT License
