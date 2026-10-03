#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File      : snmp_modul.py
Tujuan Program : Mengambil data sysName via SNMPv2c.
Nama Pembuat   : Devon Falen Pasae (2409106055)
"""

from identitas import kode_cabang


def cek_snmp(target_ip="127.0.0.1"):
    """
    Mengambil nilai sysName (OID 1.3.6.1.2.1.1.5.0) menggunakan SNMPv2c.
    Community string dipersonalisasi: comm_<kode_cabang>.
    """
    community_string = f"comm_{kode_cabang}"
    oid_sysname = "1.3.6.1.2.1.1.5.0"

    print(
        f"[*] Mengambil SNMP OID {oid_sysname} dengan community {community_string}..."
    )
    try:
        # Menangani variasi struktur modul PySNMP lintas versi secara dinamis
        import pysnmp.hlapi as hlapi

        getCmd = getattr(hlapi, "getCmd", None)
        if not getCmd:
            # Mengambil dari sub-namespace jika menggunakan versi async/v3arch
            import pysnmp.hlapi.async_io as hlapi_alt

            getCmd = hlapi_alt.getCmd

        iterator = hlapi.getCmd(
            hlapi.SnmpEngine(),
            hlapi.CommunityData(community_string, mpModel=1),
            hlapi.UdpTransportTarget((target_ip, 161), timeout=2, retries=1),
            hlapi.ContextData(),
            hlapi.ObjectType(hlapi.ObjectIdentity(oid_sysname)),
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            return f"SNMP Error Indication: {errorIndication}"
        elif errorStatus:
            return (
                f"SNMP Error Status: {errorStatus.prettyPrint()} at {errorIndex}"
            )
        else:
            for varBind in varBinds:
                return str(varBind[1])

    except Exception as e:
        # Menangkap koneksi gagal/timeout atau keterbatasan environment secara graceful
        return (
            f"Koneksi SNMP Gagal (Exception ditangani): Request Timeout / {e}"
        )


if __name__ == "__main__":
    print("Hasil SNMP sysName:", cek_snmp())