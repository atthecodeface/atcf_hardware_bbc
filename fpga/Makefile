
SRC_ROOT    = ${GRIP_ROOT_PATH}/atcf_hardware_bbc
BUILD_ROOT  = $(abspath ${CURDIR})/build
VERILOG_DIR = $(abspath ${CURDIR})/verilog
SRAMS_DIR   = $(abspath ${CURDIR})/srams
CDL_EXTRA_FLAGS = '--v_clks_must_have_enables  --v_use_always_at_star'
MAKE_OPTIONS = SRC_ROOT=${SRC_ROOT} BUILD_ROOT=${BUILD_ROOT} CDL_EXTRA_FLAGS=${CDL_EXTRA_FLAGS}

FPGA_ROOT      = ${GRIP_ROOT_PATH}/atcf_fpga
ALTERA_RTL_DIR = ${CDL_ROOT}/lib/cdl/verilog/altera
RTL_DIR        = ${FPGA_ROOT}/rtl/altera
PROJECTS_DIR   = 
FPGA_OPTS      = ROOT=${FPGA_ROOT} SRC_ROOT=${BUILD_ROOT} SRAM_CONTENTS=${SRAMS_DIR} VERILOG_DIR=${VERILOG_DIR} ALTERA_RTL_DIR=${ALTERA_RTL_DIR} RTL_DIR=${RTL_DIR} BUILD_ROOT=${BUILD_ROOT} PROJECTS_DIR=${PROJECTS_DIR}  USE_MTL_AS_VGA=  PROJECT=de1_cl/bbc

MEM_CONVERT = PYTHONPATH=${CDL_ROOT}/python:${PYTHONPATH} python3 ${CDL_ROOT}/python/cdl/tools/cdl_mem_convert.py
MEM_CONVERT = PYTHONPATH=${CDL_ROOT}/lib/cdl/python:${PYTHONPATH} python3 ${CDL_ROOT}/libexec/cdl/cdl_mem_convert.py
#f convert_memory_mif_to_qmif
# @param $1 source MIF filename
# @param $2 output MIF filename
# @param $3 number of words in memory
# @param $4 bits per word in memory
# @param $5 dont output zeros
define convert_memory_mif_to_qmif

.PHONY: qmif
qmif : $2

$2 : $1
	${Q}${MEM_CONVERT} --load_mif $1 --qmif $$@ --num_words=$3 --bit_width=$4
endef

make_verilog:
	mkdir -p ${VERILOG_DIR}
	mkdir -p ${BUILD_ROOT}
	${MAKE} ${MAKE_OPTIONS} -f ${SRC_ROOT}/Makefile clean
	${MAKE} ${MAKE_OPTIONS} -f ${SRC_ROOT}/Makefile makefiles
	${MAKE} ${MAKE_OPTIONS} -f ${SRC_ROOT}/Makefile clean_verilog verilog
	cp ${BUILD_ROOT}/*/*.v ${VERILOG_DIR}

altera_clean:
	make -f ${FPGA_ROOT}/Makefile ${FPGA_OPTS} clean

altera_build: qmif
	make -f ${FPGA_ROOT}/Makefile ${FPGA_OPTS} synth timing fit 

altera_jtag:
	make -f ${FPGA_ROOT}/Makefile ${FPGA_OPTS} find_cables

altera_program:
	make -f ${FPGA_ROOT}/Makefile ${FPGA_OPTS} jtag_program

altera_shell:
	make -f ${FPGA_ROOT}/Makefile ${FPGA_OPTS} quartus_shell

clean_qmif:
	mkdir -p ${SRAMS_DIR}

$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/elite.mif,${SRAMS_DIR}/elite.qmif,32768,32))
$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/os12.rom.mif,${SRAMS_DIR}/os12.qmif,16384,8))
$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/adfs.rom.mif,${SRAMS_DIR}/adfs.qmif,16384,8))
$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/dfs.rom.mif,${SRAMS_DIR}/dfs.qmif,16384,8))
$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/basic2.rom.mif,${SRAMS_DIR}/basic2.qmif,16384,8))

$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/ps2_bbc_kbd.mif,${SRAMS_DIR}/ps2_bbc_kbd.qmif,256,7))
$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/teletext.mif,${SRAMS_DIR}/teletext.qmif,128,64))
$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/apb_rom.mif,${SRAMS_DIR}/apb_rom.qmif,256,40))
$(eval $(call sram.qmif_from_mif,${SRC_ROOT}/test/roms/apb_vga_rom.mif,${SRAMS_DIR}/apb_vga_rom.qmif,256,40))

mount_xilinx:
	sudo modprobe nbd max_part=8
	sudo qemu-nbd --connect=/dev/nbd0 /vm/images/Vivado19.0.qcow
	sudo qemu-nbd --connect=/dev/nbd1 /vm/images/Altera18_1.qcow2
	sudo mount /dev/nbd0p1 /xilinx
	sudo mount /dev/nbd1p1 /altera

mount_altera:
	sudo modprobe nbd max_part=8
	sudo qemu-nbd --connect=/dev/nbd1 /vm/images/Altera18_1.qcow2
	sudo mount /dev/nbd1p1 /altera
