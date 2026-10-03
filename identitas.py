#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 
nim = "2409106055" 
nama = "Devon Falen Pasae" 
kode_cabang = "055" 
 
def buat_id_perangkat(jenis, nomor): 
    return f"{jenis}-{kode_cabang}-{nomor}" 
 
if __name__ == "__main__": 
    print(f"Identitas: {nama} ({nim}) | Kode Cabang: {kode_cabang}") 
