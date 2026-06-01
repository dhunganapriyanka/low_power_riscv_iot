# Low Power RISC-V IoT Simulation (gem5)

A gem5 simulation project demonstrating DVFS (Dynamic Voltage and Frequency Scaling) on a RISC-V processor running a simple IoT sensor averaging workload.

## Workload

`sensor_average.c` reads 8 temperature sensor values and computes their average. It is compiled as a static RISC-V binary.

## DVFS Configurations

| Config File | Frequency | Mode |
|---|---|---|
| `low_power_riscv_iot.py` | 1 GHz | Baseline |
| `low_power_riscv_iot_500MHz.py` | 500 MHz | Low-power |
| `low_power_riscv_iot_1500MHz.py` | 1500 MHz | Performance |

## Results Summary

| Metric | 500 MHz | 1 GHz | 1500 MHz |
|---|---|---|---|
| simSeconds | 0.000004 s | 0.000003 s | 0.000002 s |
| simTicks | 4,348,000 | 2,753,000 | 2,239,786 |
| numCycles | 2,174 | 2,753 | 3,358 |
| simInsts | 743 | 743 | 743 |
| L1D hits | 320 | 320 | 320 |
| L1D misses | 9 | 9 | 9 |

## Project Structure

```
low_power_riscv_iot/
├── config/
│   ├── low_power_riscv_iot.py
│   ├── low_power_riscv_iot_500MHz.py
│   └── low_power_riscv_iot_1500MHz.py
├── sensor_average.c
├── sensor_average
├── stats_1GHz.txt
├── stats_500MHz.txt
├── stats_1500MHz.txt
└── README.md
```

## How to Run

From the gem5 root directory:

```bash
# Baseline (1 GHz)
build/RISCV/gem5.opt configs/low_power_riscv_iot.py

# Low-power (500 MHz)
build/RISCV/gem5.opt configs/low_power_riscv_iot_500MHz.py

# Performance (1500 MHz)
build/RISCV/gem5.opt configs/low_power_riscv_iot_1500MHz.py
```

## System Configuration

- **CPU**: RISC-V Timing CPU, 1 core
- **Cache**: 16 KiB L1 instruction + 16 KiB L1 data (private)
- **Memory**: 512 MiB DDR3-1600
- **gem5 version**: 25.1.0.1
