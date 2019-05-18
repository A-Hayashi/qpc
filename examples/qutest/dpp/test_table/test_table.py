# test-script for QUTest unit testing harness
# see https://www.state-machine.com/qtools/qutest.html

# preamble...
def on_reset():
    expect_pause()
    continue_test()
    glb_filter(GRP_ON)
    loc_filter(OBJ_SM_AO, "AO_Table")
    current_obj(OBJ_SM_AO, "AO_Table")

def on_setup():
    print("on_setup")

def on_teardown():
    print("on_teardown")

# tests...
test("post HUNGRY")
post("HUNGRY_SIG", pack("<B", 2))
expect("@timestamp QF-New   Sig=HUNGRY_SIG,*")
expect("@timestamp MP-Get   Obj=EvtPool1,*")
expect("@timestamp AO-Post  Sdr=QS_RX,Obj=AO_Table,Evt<Sig=HUNGRY_SIG,*")
expect("@timestamp QUTEST_ON_POST HUNGRY_SIG,Obj=AO_Table 2")
expect("@timestamp AO-GetL  Obj=AO_Table,Evt<Sig=HUNGRY_SIG,*")
expect("@timestamp Disp===> Obj=AO_Table,Sig=HUNGRY_SIG,State=Table_serving")
expect("@timestamp BSP_CALL BSP_displayPhilStat 2 hungry  ")
expect("@timestamp QF-New   Sig=EAT_SIG,*")
expect("@timestamp MP-Get   Obj=EvtPool1,*")
expect("@timestamp QF-Pub   Sdr=AO_Table,Evt<Sig=EAT_SIG,*")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gc    Evt<Sig=EAT_SIG,Pool=1,Ref=1>")
expect("@timestamp MP-Put   Obj=EvtPool1,*")
expect("@timestamp BSP_CALL BSP_displayPhilStat 2 eating  ")
expect("@timestamp =>Intern Obj=AO_Table,Sig=HUNGRY_SIG,State=Table_serving")
expect("@timestamp QF-gc    Evt<Sig=HUNGRY_SIG,*")
expect("@timestamp MP-Put   Obj=EvtPool1,*")
expect("@timestamp Trg-Done QS_RX_EVENT")

test("post HUNGRY(2)", NORESET)
post("HUNGRY_SIG", pack("<B", 1))
expect("@timestamp QF-New   Sig=HUNGRY_SIG,*")
expect("@timestamp MP-Get   Obj=EvtPool1,*")
expect("@timestamp AO-Post  Sdr=QS_RX,Obj=AO_Table,Evt<Sig=HUNGRY_SIG,*")
expect("@timestamp QUTEST_ON_POST HUNGRY_SIG,Obj=AO_Table 1")
expect("@timestamp AO-GetL  Obj=AO_Table,Evt<Sig=HUNGRY_SIG,*")
expect("@timestamp Disp===> Obj=AO_Table,Sig=HUNGRY_SIG,State=Table_serving")
expect("@timestamp BSP_CALL BSP_displayPhilStat 1 hungry  ")
expect("@timestamp =>Intern Obj=AO_Table,Sig=HUNGRY_SIG,State=Table_serving")
expect("@timestamp QF-gc    Evt<Sig=HUNGRY_SIG,*")
expect("@timestamp MP-Put   Obj=EvtPool1,*")
expect("@timestamp Trg-Done QS_RX_EVENT")

test("post DONE", NORESET)
publish("DONE_SIG", pack("<B", 2))
expect("@timestamp QF-New   Sig=DONE_SIG,*")
expect("@timestamp MP-Get   Obj=EvtPool1,*")
expect("@timestamp QF-Pub   Sdr=QS_RX,Evt<Sig=DONE_SIG,*")
expect("@timestamp AO-Post  Sdr=QS_RX,Obj=AO_Table,Evt<Sig=DONE_SIG,*")
expect("@timestamp QUTEST_ON_POST DONE_SIG,Obj=AO_Table 2")
expect("@timestamp QF-gcA   Evt<Sig=DONE_SIG,Pool=1,Ref=2>")
expect("@timestamp Trg-Done QS_RX_EVENT")
expect("@timestamp AO-GetL  Obj=AO_Table,Evt<Sig=DONE_SIG,*")
expect("@timestamp Disp===> Obj=AO_Table,Sig=DONE_SIG,State=Table_serving")
expect("@timestamp BSP_CALL BSP_displayPhilStat 2 thinking")
expect("@timestamp QF-New   Sig=EAT_SIG,*")
expect("@timestamp MP-Get   Obj=EvtPool1,*")
expect("@timestamp QF-Pub   Sdr=AO_Table,Evt<Sig=EAT_SIG,Pool=1,Ref=0>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gcA   Evt<Sig=EAT_SIG,Pool=1,Ref=2>")
expect("@timestamp QF-gc    Evt<Sig=EAT_SIG,Pool=1,Ref=1>")
expect("@timestamp MP-Put   Obj=EvtPool1,*")
expect("@timestamp BSP_CALL BSP_displayPhilStat 1 eating  ")
expect("@timestamp =>Intern Obj=AO_Table,Sig=DONE_SIG,State=Table_serving")
expect("@timestamp QF-gc    Evt<Sig=DONE_SIG,*")
expect("@timestamp MP-Put   Obj=EvtPool1,*")
expect("@timestamp Trg-Done QS_RX_EVENT")
