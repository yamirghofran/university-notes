---
title: Trusted Platform Module
---

A hardware-based security feature that provides a secure storage of cryptographic keys and other sensitive data.

It is a small chip that is installed on the motherboard of a computer and can be used to secure a variety of applications, including disk encryption, secure boot, and digital rights management.

Trusted Platform Module (TPM) provides:
- A hardware random number generator.
	- facilities for the secure generation of cryptographic keys for limited uses.
- Remote attestation
	- creates a nearly unforgeable hash key summary of the hardware and software configuration.
- Binding
	- data is encrypted using the TPM bind key, a unique RSA key descended from a storage key.
- Sealed storage
	- specifies the TPM state for the data to be decrypted (unsealed)
- Other Trusted Computing functions for the data to be decrypted (unsealed)

![](../attachments/cleanshot-2025-02-08-at-1859132x.png)