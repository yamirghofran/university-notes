---
title: Filesystem
---

The role of a files system in managing files and directories on storage devices.
1. Directory Structure
2. Metadata
3. File Allocation
4. Managing Free Space
5. File Operations
6. Journaling and Consistency

Examples of file systems: NTFS, FAT32, ext4, etc.

## Filesystem Examples
- FAT32 (File Allocation Table 32)
	- Maximum file and volume sizes
- exFAT (Extended File Allocation Table)
- NTFS (New Technology File System)
	- Windows
	- Robust and includes recovery features
- EXT4 (Fourth Extended Filesystem)
	- Unix
	- Optimized for SSD
- APFS (Apple File System)
	- Apple
	- Optimizaed for SSD

![](../attachments/cleanshot-2025-02-21-at-1125082x.png)
## Types of File Systems
- Disk-based
- Network
	- NFS (Network File System), SMB/CIFS (Server Message Block/Common Internet File System), or AFP (Apple Filing Protocol)
- Virtual Filesystems
	- not a file system itself but an abstraction layer in an [operating system](/computer-architecture-network-technology-and-operating-systems/operating-systems/operating-system) that provides a standard interface for different file systems.
![](../attachments/cleanshot-2025-02-21-at-1125342x.png)

**Partitions**
e.g. Hard drive is divided into 2 virtual partitions. Computer thinks that they are 2 separate drives. You can corrupt one without impacting the other. 

Disadvantage is that you lose some space.

**Dynamic re-partitioning**: Dynamically resize partitions.

## Structure
Blocks
- Superblock
- **Inode**: very small piece of information that says what the file has. separate from content. Doesn't point to bytes. Points to data blocks.
	- File metadata
- Directory structure
- Data blocks
Faster to use blocks because random access was slow.
![](../attachments/cleanshot-2025-02-21-at-1125592x.png)
### Inodes![](../attachments/cleanshot-2025-02-21-at-1126392x.png)

## How to track free space
- Bitmaps (or Bit Arrays)
	- ext2/3/4 in Linux
- Free SpaceLists
	- (Older file systems)
- Free space Trees
	- NTFS and some versions of UFS
- Grouping
	- ext4
- Superblock with Free Block Count