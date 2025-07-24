---
title: Assembly
---

# Overview
## Arithmetic Logic Instructions
- `ADD`
- `ANDLW`
- `INC`
- `DEC`
## Data Transference Instructions
- `MOV`
- `LD`
## Jump Instructions
- `JP`
## Input Output Instructions
- `IN`
- `OUT`
## CPU Control Instructions
- `HALT`
- `NOP`
# Addressing Modes

## Implied
The data that is used in the instruction is defined by the instruction itself.
```assembly
SCF (used to set Carry flag to 1)
```
## Immediate
The data is present after the instruction as a constant.
```assembly
LD HL, 08010H (move the data 08010H into HL register)
```
## Register
The data is on the register specified by the instruction.
```assembly
LD A,C (move the contents of C register to A register)
```
## Direct or Absolute
The operand's offset is given in the instruction as an 8-bit or 16-bit displacement element.
```assembly
ADD A, (0301) (add the contents of offset address 0301) to A
```
## Register Indirect
The address containing the data is stored on the register following the instruction.
```assembly
LD AX, (BX) (move the contents of memory location s addressed by the register BX to the register AX)
```
## Indexed
The operand's offset is the sum of the content of an index register SI or DI and an 8-bit or 16-bit displacement.
```assembly
LD A, (IX + 05) (load the contents of IX + 0x05 register into A)
```

## Example
```assembly
ORG 0000h
JP 0100h
ORG 0100h
;register + inmediate
LD HL, 80F0h ;indirect + immediate
LD (HL), 3Fh ; Initialize HL register at 80F0h, this 16-bit number
; will be used as memory address.
; Write the value 3Fh into the memory location
; 80F0h, pointed by the register HL.
;register
INC HL ;indirect + inmediate
LD (HL), 12h ; Increment the HL content (it becomes 80F1h).
; Write the value 12h into the next memory location,
; that is pointed by HL = 80F1h.
;register
INC HL ; Increment the HL content (it becomes 80F2h).
;... ; (cont.)
;register + direct
LD A, (80F0h)
ADD A, 255
;iplicit
CCF
HALT
```
