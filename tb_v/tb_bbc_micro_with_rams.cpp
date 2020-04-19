// make CDL_EXTRA_FLAGS='--v_clks_must_have_enables  --v_use_always_at_star' clean_verilog verilog
// verilator --cc -f a --top-module bbc_micro_with_rams -Wno-fatal
// export VERILATOR_ROOT=~/Git/cdl_tools_grip/tools/share/verilator/
// (cd obj_dir && make VERILATOR_ROOT=~/Git/cdl_tools_grip/tools/share/verilator/ -f Vbbc_micro_with_rams.mk )
// (cd obj_dir && g++ ../../atcf_hardware_bbc/tb_v/tb_bbc_micro_with_rams.cpp ~/Git/cdl_tools_grip/tools/share/verilator/include/verilated.cpp Vbbc_micro_with_rams__ALL.a -I /home/gavin/Git/cdl_tools_grip/tools/share/verilator/include -I.)

// apb/apb_logging.v
// apb/apb_master_mux.v
// apb/apb_processor.v
// apb/apb_target_gpio.v
// apb/apb_target_timer.v
// apb/csr_master_apb.v
// apb/csr_target_apb.v
// apb/csr_target_csr.v
// apb/csr_target_timeout.v
// ../atcf_fpga/rtl/clock_gate_module.v
// ../atcf_fpga/rtl/mrw_srams.v
// ../atcf_fpga/rtl/srw_srams.v
// ../atcf_fpga/rtl/xilinx/srams.v
// bbc/acia6850.v
// bbc/bbc_display_sram.v
// bbc/bbc_floppy_sram.v
// bbc/bbc_keyboard_csr.v
// bbc/bbc_micro_clocking.v
// bbc/bbc_micro_keyboard.v
// bbc/bbc_micro_rams.v
// bbc/bbc_micro.v
// bbc/bbc_micro_with_rams.v
// bbc/bbc_vidproc.v
// bbc/cpu6502.v
// bbc/crtc6845.v
// bbc/fdc8271.v
// bbc/saa5050.v
// bbc/via6522.v
// std/tech_sync_bit.v
// std/tech_sync_flop.v
// video/framebuffer_teletext.v
// video/framebuffer_timing.v
// video/framebuffer.v
// video/teletext.v

#include <verilated.h>
#include "Vbbc_micro_with_rams.h"
double sc_time_stamp () {
    return 0;
}
int main(int argc, char** argv, char** env) {
    (void) argc;
    (void) argv;
    (void) env;
    long long clks;

    Vbbc_micro_with_rams* m = new Vbbc_micro_with_rams;
    m->reset_n = 0;
    m->clk = 0;
    m->video_clk = 0;
    clks = 0;
    while (!Verilated::gotFinish() && (clks<100*1000*1000)) {
        int toggled=0;
        clks++;
        if ((clks%4)==0) {
            m->clk = !m->clk;
            toggled = 1;
        }
        if ((clks%4)==0) {
            m->video_clk = !m->video_clk;
            toggled = 1;
        }
        if ((!m->clk) && (clks>10)) {
            m->reset_n = 1;
            toggled = 1;
        }
        if (toggled) {
            m->eval();
        }
    }
    m->final();
    delete m;
    return 0;
}
