#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File      : snmp_modul.py
Tujuan Program : Mengambil data sysName via SNMPv2c.
Nama Pembuat   : Devon Falen Pasae (2409106055)
"""

from identitas import kode_cabang
from pysnmp.hlapi import (
    CommunityData,
    ContextData,
    ObjectIdentity,
    ObjectType,
    SnmpEngine,
    UdpTransportTarget,
    getCmd,
)


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
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community_string, mpModel=1),
            UdpTransportTarget((target_ip, 161), timeout=2, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity(oid_sysname)),
        )

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            return f"SNMP Error Indication: {errorIndication}"
        elif errorStatus:
            return f"SNMP Error Status: {errorStatus.prettyPrint()} at {errorIndex}"
        else:
            for varBind in varBinds:
                return str(varBind[1])

    except Exception as e:
        return f"Koneksi SNMP Gagal: {str(e)}"


if __name__ == "__main__":
    print("Hasil SNMP sysName:", cek_snmp())