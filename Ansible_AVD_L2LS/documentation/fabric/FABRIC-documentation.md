# FABRIC

# Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| FABRIC | leaf | leaf1-DC1 | - | cEOS-LAB | Provisioned |
| FABRIC | leaf | leaf2-DC1 | - | cEOS-LAB | Provisioned |
| FABRIC | leaf | leaf3-DC1 | - | cEOS-LAB | Provisioned |
| FABRIC | leaf | leaf4-DC1 | - | cEOS-LAB | Provisioned |
| FABRIC | spine | spine1-DC1 | - | cEOS-LAB | Provisioned |
| FABRIC | spine | spine2-DC1 | - | cEOS-LAB | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| leaf | leaf1-DC1 | Ethernet1 | mlag_peer | leaf2-DC1 | Ethernet1 |
| leaf | leaf1-DC1 | Ethernet2 | spine | spine1-DC1 | Ethernet2 |
| leaf | leaf1-DC1 | Ethernet3 | spine | spine2-DC1 | Ethernet2 |
| leaf | leaf2-DC1 | Ethernet2 | spine | spine1-DC1 | Ethernet3 |
| leaf | leaf2-DC1 | Ethernet3 | spine | spine2-DC1 | Ethernet3 |
| leaf | leaf3-DC1 | Ethernet1 | mlag_peer | leaf4-DC1 | Ethernet1 |
| leaf | leaf3-DC1 | Ethernet2 | spine | spine1-DC1 | Ethernet4 |
| leaf | leaf3-DC1 | Ethernet3 | spine | spine2-DC1 | Ethernet4 |
| leaf | leaf4-DC1 | Ethernet2 | spine | spine1-DC1 | Ethernet5 |
| leaf | leaf4-DC1 | Ethernet3 | spine | spine2-DC1 | Ethernet5 |
| spine | spine1-DC1 | Ethernet1 | mlag_peer | spine2-DC1 | Ethernet1 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
