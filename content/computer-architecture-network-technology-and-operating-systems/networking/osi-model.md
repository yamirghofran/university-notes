---
title: OSI Model
---

Common basis for the coordination of standards development for the purpose of system interconnection.

## Layer 1 - Physical
- Computer data exists in the form of bits (ones and zeros)
- Something has to transport those bits between hosts.
- Cables (ethernet twisted pair, coaxial, fiber), Wifi, Repeaters, Hubs (multiport repeaters)
## Layer 2 - Data Link (Hop to Hop)
- Interacts with physical layer (put bits on the wire and retrieve bits from the wire)
	- NIC - Network Interface Card
	- Wifi access cards
	- Switches
- Addressing Scheme - MAC addresses
	- 48 bits, represented as 12 hex digits
	- Every NIC has a unique MAC address
## Layer 3 - Network (End to End)
- Addressing Scheme - IP Addresses 
	- 32 bits, represented as 4 octets, each 0-255
	- Routers, Hosts, anything with IP
## Layer 4 - Transport (Service to Service)
- Distinguish data streams
- Addressing Scheme - Ports
	- 0-65535 - TCP (favors reliability)
	- 0-65535 - UDP (favors efficiency)
- Servers listen for requests to pre-defined ports
- Clients select random port for each connection
	- Response traffic will arrive on this port

## Layer 5,6,7 - Session, Presentation, Application
- Application protocols


![](../attachments/cleanshot-2025-05-11-at-1458442x.png)
![](../attachments/cleanshot-2025-04-05-at-1211372x.png)

## Examples
![](../attachments/cleanshot-2025-04-05-at-1211512x.png)![](../attachments/cleanshot-2025-04-05-at-1212002x.png)
![](../attachments/cleanshot-2025-04-05-at-1212192x.png)
## OSI Model and Internet
![](../attachments/cleanshot-2025-04-05-at-1212412x.png)

## SSL Opinion 1
![](../attachments/cleanshot-2025-04-05-at-1213212x.png)

## SSL Opinion 2
![](../attachments/cleanshot-2025-04-05-at-1213332x.png)

## Physical: Ethernet
![](../attachments/cleanshot-2025-04-05-at-1214032x.png)