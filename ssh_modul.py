#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File      : ssh_modul.py
Tujuan Program : Melakukan koneksi SSH dan menjalankan perintah diagnostik.
Nama Pembuat   : Devon Falen Pasae (2409106055)
"""

import paramiko
from identitas import kode_cabang


def cek_ssh(host="127.0.0.1", port=22, password="password123"):
    """
    Melakukan SSH login memakai username admin_<kode_cabang>,
    menjalankan minimal dua perintah diagnostik, dan menangani exception.
    """
    username = f"admin_{kode_cabang}"
    hasil_diagnostik = {}

    print(f"[*] Mencoba koneksi SSH ke {host}:{port} sebagai {username}...")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            host, port=port, username=username, password=password, timeout=3
        )

        # Menjalankan minimal 2 perintah diagnostik
        commands = ["uname -a", "uptime"]
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.read().decode().strip()
            err = stderr.read().decode().strip()
            hasil_diagnostik[cmd] = out if out else err

        ssh.close()
        return {
            "status": "SUKSES",
            "username": username,
            "data": hasil_diagnostik,
        }

    except Exception as e:
        print(f"[!] Exception ditangani: Koneksi SSH Gagal ({e})")
        return {
            "status": "GAGAL",
            "username": username,
            "error": str(e),
        }


if __name__ == "__main__":
    print(cek_ssh())