from .config import (
    CPU_POWER_WATTS,
    STORAGE_KWH_PER_GB_YEAR,
    YEARS_STORED,
    CARBON_INTENSITY
)

def cpu_energy(time_sec):
    return (CPU_POWER_WATTS * time_sec) / (1000 * 3600)


def storage_energy(size_bytes):
    size_gb = size_bytes / (1024**3)
    return size_gb * STORAGE_KWH_PER_GB_YEAR * YEARS_STORED


def carbon(energy_kwh):
    return energy_kwh * CARBON_INTENSITY
