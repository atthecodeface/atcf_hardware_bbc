import cdl_desc
from cdl_desc import CdlModule, CModel, CSrc

class Library(cdl_desc.Library):
    name="bbc"
    pass

class BBCChips(cdl_desc.Modules):
    name = "bbc"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    include_dir = "cdl"
    libraries = {"std":True, "apb":True, "video":True}
    export_dirs = [ src_dir, include_dir ]
    modules = []
    modules += [ CdlModule("fdc8271") ]
    modules += [ CdlModule("acia6850") ]
    modules += [ CdlModule("via6522") ]
    modules += [ CdlModule("crtc6845") ]
    modules += [ CdlModule("saa5050") ]
    modules += [ CdlModule("cpu6502") ]
    pass


class BBCModules(cdl_desc.Modules):
    name = "bbc"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    include_dir = "cdl"
    libraries = {"std":True, "apb":True, "video":True}
    export_dirs = [ src_dir, include_dir ]
    modules = []
    modules += [ CdlModule("bbc_keyboard_csr") ]
    modules += [ CdlModule("bbc_vidproc") ]
    modules += [ CdlModule("bbc_display_sram") ]
    modules += [ CdlModule("bbc_floppy_sram") ]
    modules += [ CdlModule("bbc_micro_keyboard") ]
    modules += [ CdlModule("bbc_micro_clocking") ]
    modules += [ CdlModule("bbc_micro") ]
    modules += [ CdlModule("bbc_micro_with_rams") ]
    modules += [ CdlModule("bbc_micro_rams") ]

    modules += [ CdlModule("tb_bbc_with_shm_display", src_dir=tb_src_dir) ]

    pass

class Models(cdl_desc.Modules):
    name = "bbc_models"
    src_dir     = "cmodel"
    include_dir = "cmodel"
    libraries = {"std":True, "apb":True, "video":True}
    modules = []
    modules += [ CModel("bbc_display") ]
    modules += [ CModel("bbc_floppy") ]
    modules += [ CSrc("image_io") ] # used by bbc_display
    modules += [ CSrc("bbc_shm") ]
    modules += [ CSrc("bbc_floppy_disk") ]
    modules += [ CSrc("fb") ]
    modules += [ CSrc("vnc_rfb") ]
    # modules += [ CExec("bbc_display_vnc") ]
    # g++ cmodel/bbc_display_vnc.cpp /Users/gavinprivate/Git/atcf_hardware_bbc_grip/atcf_hardware_bbc/build/bbc/lib_bbc.a -I cmodel -I ~/Git/cdl_tools_grip/tools/include/cdl/

    pass

