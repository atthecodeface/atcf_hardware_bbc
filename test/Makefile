smoke: smoke_mifs
	${SIM} smoke.csm

bbc:
	${SIM} tb_bbc_with_shm_display.csm

smoke_mifs: smoke_rom.py
	PYTHONPATH=.:${PYTHONPATH} apb_processor_rom.py --src smoke_rom --mif smoke_rom.mif
