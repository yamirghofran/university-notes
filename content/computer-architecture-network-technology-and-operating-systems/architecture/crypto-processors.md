---
title: Crypto Processors
---

- [Trusted Platform Module](/computer-architecture-network-technology-and-operating-systems/architecture/trusted-platform-module)
## Secured Firmware
To secure a firmware using a crypto processor:
1. Use a trusted processor and tamper-resistant storage to store the firmware image encrypted with a private key.
2. Store the [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader) unencrypted in the tamper-resistant storage e.g. ROM.
3. Hard-code the public key needed to load and verify the firmware into the [bootloader](/computer-architecture-network-technology-and-operating-systems/architecture/bootloader).
4. Load, decrypt, and verify the firmware image by the bootloader.

Any other image not signed by the original manufacturer won’t be loaded by the bootloader. Public key cannot be changed on ROM.
