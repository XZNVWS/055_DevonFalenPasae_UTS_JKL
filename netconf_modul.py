#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nama File      : netconf_modul.py
Tujuan Program : Membangun struktur pesan XML NETCONF RPC.
Nama Pembuat   : Devon Falen Pasae (2409106055)
"""

from identitas import kode_cabang


def buat_pesan_netconf():
    """
    Membangun string XML rpc edit-config untuk pembuatan VLAN ID = kode_cabang.
    Menandai Messages Layer, Operations Layer, dan Content Layer.
    """
    vlan_id = kode_cabang

    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- === MESSAGES LAYER: Menyediakan mekanisme RPC independen terhadap protokol framing === -->
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <!-- === OPERATIONS LAYER: Menentukan operasi konfigurasi (edit-config) === -->
  <edit-config>
    <target>
      <running/>
    </target>
    <!-- === CONTENT LAYER: Berisi payload data konfigurasi perangkat (VLAN ID) === -->
    <config>
      <vlan xmlns="urn:ieee:std:802.1Q:yang:ietf-vlan">
        <vlan-id>{vlan_id}</vlan-id>
        <name>VLAN_Cabang_{vlan_id}</name>
      </vlan>
    </config>
  </edit-config>
</rpc>"""
    return xml_content.strip()


if __name__ == "__main__":
    print(buat_pesan_netconf())