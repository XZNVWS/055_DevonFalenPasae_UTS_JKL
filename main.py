#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File      : main.py
Tujuan Program : Integrasi akhir seluruh modul dan menampilkan laporan terpusat.
Nama Pembuat   : Devon Falen Pasae (2409106055)
"""

from identitas import buat_id_perangkat, kode_cabang, nama, nim
from netconf_modul import buat_pesan_netconf
from snmp_modul import cek_snmp
from ssh_modul import cek_ssh
from telemetry_modul import klasifikasi_telemetry


class LaporanCabang:

    def __init__(self):
        self.nim = nim
        self.nama = nama
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self):
        print("=" * 70)
        print("   LAPORAN AKHIR AUTOMATION & MONITORING CABANG VIRTUAL")
        print("=" * 70)
        print(f" Nama Pembuat : {self.nama}")
        print(f" NIM          : {self.nim}")
        print(f" Kode Cabang  : {self.kode_cabang}")
        print(f" Sample ID    : {buat_id_perangkat('RTR', '01')}")
        print("=" * 70)

        # 1. SSH Section
        print("\n[A. DIAGNOSTIK AKSES SSH]")
        ssh_res = cek_ssh()
        print(f"  Status    : {ssh_res['status']}")
        print(f"  Username  : {ssh_res['username']}")
        if ssh_res["status"] == "SUKSES":
            for cmd, out in ssh_res["data"].items():
                print(f"  $ {cmd} => {out}")
        else:
            print(f"  Info/Error: {ssh_res.get('error')}")

        # 2. SNMP Section
        print("\n[B. PEMANTAUAN IDENTITAS SNMP]")
        snmp_res = cek_snmp()
        print(f"  Target sysName (OID 1.3.6.1.2.1.1.5.0): {snmp_res}")

        # 3. NETCONF Section
        print("\n[C. STRUKTUR PESAN CONFIGURATION NETCONF (XML)]")
        print(buat_pesan_netconf())

        # 4. Telemetry Section
        print("\n[D. HASIL KLASIFIKASI DATA TELEMETRY CPU]")
        telemetry_res = klasifikasi_telemetry()
        for t in telemetry_res:
            print(
                f"  - Perangkat: {t['device']:<20} | CPU: {t['cpuUsage']:>2}% | Status: [{t['klasifikasi']}]"
            )

        print("\n" + "=" * 70)
        print("                      LAPORAN SELESAI")
        print("=" * 70)


if __name__ == "__main__":
    laporan = LaporanCabang()
    laporan.tampilkan_laporan()