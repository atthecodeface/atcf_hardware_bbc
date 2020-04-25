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
