#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File      : telemetry_modul.py
Tujuan Program : Analisis dan klasifikasi sampel data telemetry CPU.
Nama Pembuat   : Devon Falen Pasae (2409106055)
"""

# Sampel data GPB-decoded yang nilainya disesuaikan tanpa leading zero (menggunakan angka 5)
sampel_telemetry = [
    {"device": "router-cabang-055", "cpuUsage": 55},
    {"device": "switch-access-055", "cpuUsage": 5},
    {"device": "core-switch-055", "cpuUsage": 90},
    {"device": "edge-firewall-055", "cpuUsage": 60},
]


def klasifikasi_telemetry(data_list=None):
    """
    Mengiterasi sampel data telemetry dan mengklasifikasikan cpuUsage:
    - > 80        : "KRITIS"
    - 50 - 80     : "WASPADA"
    - < 50        : "NORMAL"
    """
    if data_list is None:
        data_list = sampel_telemetry

    hasil = []
    for item in data_list:
        cpu = item.get("cpuUsage", 0)
        if cpu > 80:
            kategori = "KRITIS"
        elif 50 <= cpu <= 80:
            kategori = "WASPADA"
        else:
            kategori = "NORMAL"

        hasil.append(
            {
                "device": item["device"],
                "cpuUsage": cpu,
                "klasifikasi": kategori,
            }
        )
    return hasil


if __name__ == "__main__":
    print("=== HASIL ANALISIS TELEMETRY ===")
    for res in klasifikasi_telemetry():
        print(
            f"Device: {res['device']:<20} | CPU: {res['cpuUsage']:>2}% -> Status: [{res['klasifikasi']}]"
        )