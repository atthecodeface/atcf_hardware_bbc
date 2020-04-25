#include <verilated.h>
//#include "Vbbc_micro_with_rams.h"
double sc_time_stamp () {
    return 0;
}
// #include <errno.h>
// #include <stdlib.h>
// #include <stdio.h>
int main(int argc, char** argv, char** env) {
    (void) argc;
    (void) argv;
    (void) env;
    long long clks;

    VTOP* m = new VTOP;
    m->reset_n = 0;
    m->CLK1 = 0;
#ifdef CLK2
    m->CLK2 = 0;
#endif
    clks = 0;
    while (!Verilated::gotFinish() && (clks<100*1000*1000)) {
        int toggled=0;
        if (clks%(1000*1000)==0) {
            // fprintf(stderr,"Clocking 1000*1000 from %lld\n",clks);
        }
        clks++;
        if ((clks%CLK1_P)==0) {
            m->CLK1 = !m->CLK1;
            toggled = 1;
        }
#ifdef CLK2
        if ((clks%CLK2_P)==0) {
            m->CLK2 = !m->CLK2;
            toggled = 1;
        }
#endif        
        if ((!m->CLK1) && (clks>10)) {
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
