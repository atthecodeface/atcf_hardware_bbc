import cdl_desc
from cdl_desc import CdlModule, CdlSimVerilatedModule, CModel, CSrc

class Library(cdl_desc.Library):
    name="bbc"
    pass

class BBCChips(cdl_desc.Modules):
    name = "bbc"
    c_src_dir    = "cmodel"
    src_dir      = "cdl"
    tb_src_dir   = "tb_cdl"
    libraries = {"std":True, "apb":True, "video":True}
    cdl_include_dirs = ["cdl"]
    export_dirs = cdl_include_dirs + [ src_dir ]
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
    cdl_include_dirs = ["cdl"]
    libraries = {"std":True, "apb":True, "video":True}
    export_dirs = cdl_include_dirs + [ src_dir ]
    modules = []
    modules += [ CdlModule("bbc_keyboard_ps2") ]
    modules += [ CdlModule("bbc_keyboard_csr") ]
    modules += [ CdlModule("bbc_vidproc") ]
    modules += [ CdlModule("bbc_display_sram") ]
    modules += [ CdlModule("bbc_floppy_sram") ]
    modules += [ CdlModule("bbc_micro_keyboard") ]
    modules += [ CdlModule("bbc_micro_clocking") ]
    modules += [ CdlModule("bbc_micro") ]
    modules += [ CdlModule("bbc_micro_rams") ]
    modules += [ CdlModule("bbc_micro_with_rams") ]

    modules += [ CdlSimVerilatedModule("cwv__bbc_micro_with_rams",
                                       cdl_filename="bbc_micro_with_rams",
                                       verilog_filename="bbc_micro_with_rams",
                                       extra_verilog=["../std/srw_srams.v", "../std/mrw_srams.v"]) ]
    pass


    modules += [ CdlModule("tb_bbc_with_shm_display", src_dir=tb_src_dir) ]
    modules += [ CdlModule("tb_cwv_bbc_with_shm_display",
                           src_dir=tb_src_dir,
                           cdl_filename="tb_bbc_with_shm_display",
                           cdl_module_name="tb_bbc_with_shm_display",
                           instance_types={"bbc_micro_with_rams":"cwv__bbc_micro_with_rams"}
    ) ]

    pass

class DE1Modules(cdl_desc.Modules):
    name = "de1"
    libraries = {"std":True, "apb":True, "video":True, "utils":True, "io":True, "de1":True}
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    cdl_include_dirs = ["cdl"]
    export_dirs      = cdl_include_dirs + [ src_dir ]
    modules = []
    modules += [ CdlModule("bbc_micro_de1_cl") ]
    modules += [ CdlModule("bbc_micro_de1_cl_io") ]
    modules += [ CdlModule("bbc_micro_de1_cl_bbc") ]

    pass

class SharedSrc(cdl_desc.Modules):
    """
    Code shared by the CPP C models and the executables
    """
    name = "bbc_shared"
    src_dir      = "csrc"
    cpp_include_dirs = ["csrc"]
    modules = []
    modules += [ CSrc("bbc_shm") ]
    pass

class Models(cdl_desc.Modules):
    name = "bbc_models"
    src_dir      = "cmodel"
    cpp_include_dirs = ["cmodel"]
    libraries = {"std":True, "apb":True, "video":True}
    modules = []
    modules += [ CModel("bbc_display", cpp_include_dirs=["cmodel", "csrc"]) ]
    modules += [ CModel("bbc_floppy",  cpp_include_dirs=["cmodel", "csrc"]) ]
    modules += [ CSrc("image_io") ] # used by bbc_display
    modules += [ CSrc("bbc_floppy_disk") ]
    pass

class Executable(cdl_desc.Executable):
    name = "display_vnc"
    src_dir     = "csrc"
    cpp_include_dirs = ["cmodel", "csrc"]
    srcs = []
    srcs += [ CSrc("bbc_display_vnc") ]
    srcs += [ CSrc("fb") ]
    srcs += [ CSrc("vnc_rfb") ]
    pass

