# Network Automation & Monitoring Cabang Virtual

Proyek ini merupakan sistem otomatisasi dan pemantauan jaringan modular berbasis Python. Sistem ini dirancang untuk menangani tugas-tugas manajemen jaringan seperti akses remote via SSH, monitoring SNMP, pembuatan payload NETCONF, serta pengolahan telemetry performa CPU perangkat.

---

## Struktur Folder & File Proyek

```text
055_DevonFalenPasae_UTS_JKL/
│
├── identitas.py       # Modul identitas cabang dan parameter sistem
├── ssh_modul.py       # Modul fungsi akses remote via SSH (Paramiko)
├── snmp_modul.py      # Modul monitoring perangkat via SNMP (PySNMP)
├── netconf_modul.py   # Modul pembuat pesan/payload NETCONF XML
├── telemetry_modul.py # Modul analisis data telemetry dan klasifikasi CPU Usage
├── main.py            # Script utama untuk integrasi seluruh modul
│
├── .gitignore         # Daftar file/folder yang diabaikan oleh Git
└── README.md          # Dokumentasi proyek
```

## Cara Menjalankan Program

1. Prasyarat (Prerequisites)
Pastikan Python versi 3.x dan lingkungan virtual (virtual environment) sudah aktif serta pustaka yang dibutuhkan telah terinstal:

```python
# Aktifkan Virtual Environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Instalasi pustaka yang dibutuhkan (jika belum)
pip install paramiko pysnmp
```
