CDL_ROOT=/Users/gavinprivate/Git/cdl_tools_grip/tools
include ${CDL_ROOT}/lib/cdl/cdl_templates.mk
SRC_ROOT   = $(abspath ${CURDIR})
OTHER_SRCS = ${SRC_ROOT}/../*
BUILD_ROOT = ${SRC_ROOT}/build

all: sim

-include ${BUILD_ROOT}/Makefile

$(eval $(call cdl_makefile_template,${SRC_ROOT},${BUILD_ROOT},${OTHER_SRCS}))

clean:
	rm -rf ${BUILD_ROOT}
	mkdir -p ${BUILD_ROOT}

smoke: sim
	(cd test && PATH=${SRC_ROOT}/python:${PATH} ${MAKE} SIM=${SIM} smoke)

bbc: sim
	(cd test && PATH=${SRC_ROOT}/python:${PATH} ${MAKE} SIM=${SIM} bbc)

$(info ${BIN_OBJS__bbc__display_vnc})
$(info ${BIN_LIBS__bbc__display_vnc})
