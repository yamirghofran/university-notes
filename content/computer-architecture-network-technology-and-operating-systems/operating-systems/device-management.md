---
title: Device Management
---

!important
Character devices: Data streams from a device sequentially

Block Devices: Data can be randomly accessed

## Device Identification
- Major Number
	- The driver associated with the device. It tells the kernel which device driver is responsible for managing the device.
- Minor Number
	- Distinguishes between different instances of devices managed by the same driver. e.g. if there are multiple disk drives, the minor number helps the system differentiate between them.

## Shell Commands
- mknod !important
	- A command used to create device files. It requires specifying the type of device (character or block), the path where the device file will be created, and the major and minor numbers. e.g. mknod `/dev/example c 10 100` creates a character device with major number 10 and minor number 100.

## The /proc Filesystem
A virtual filesystem in Unix and Linux systems that provides a mechanism for the kernel to expose information to **user space**. It does **not** contain real files in the traditional sense, but rather, it is a **view into the system's internal state**, represented in a hierarchical file-like structure.

`/proc` is an invaluable resource for system monitoring and configuration, as well as for debugging purposes.