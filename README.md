# atcf_hardware_bbc

This repository contains all the CDL source code for a BBC
microcomputer design, including the required chips (such as the 6502
and SAA5050, and Vidproc).

It also includes C models to permit a CDL simulation to tie in to a
shared memory framebuffer and keyboard, which can be viewed and
controlled by a VNC RFB server. This can in turn be accesses using a
VNC client of your choice (on port localhost:1080).

## Status

The design runs the standard ROMs (including the OS, ADFS, etc) and
interfaces to a (currently read-only) floppy disk emulation (emulating
the drive itself, using SRAM for the disk image).

It is possible (although slow in simulation) to run, for example,
Elite.

The design builds in an Altera FPGA; although not all the files have
been ported to the grip environment repositories as yet.

# VNC simulation

You can connect to this on port 6980

Function key F12 maps to the BBC break key.

