import scapy

pnio = load_contrib('pnio')

print(raw(ProfinetIO()/b'AAA'))
print(raw(PROFIsafe.build_PROFIsafe_class(PROFIsafeControl, 4)(data = b'AAA', control=0x20, crc=0x424242)))
print(hexdump(PNIORealTime_IOxS()))

p=PNIORealTimeCyclicPDU(cycleCounter=1024, data=[
    PNIORealTime_IOxS(),
    PNIORealTimeCyclicPDU.build_fixed_len_raw_type(4)(data = b'AAA') / PNIORealTime_IOxS(),
    PROFIsafe.build_PROFIsafe_class(PROFIsafeControl, 4)(data = b'AAA', control=0x20, crc=0x424242)/PNIORealTime_IOxS(),
])

print(p.show())

e = Ether(src='00:01:02:03:04:05', dst='06:07:08:09:0a:0b') / ProfinetIO(frameID="RT_CLASS_1") / p
print(e.show2())

conf.contribs["PNIO_RTC"].update({('00:01:02:03:04:05', '06:07:08:09:0a:0b', 0x8000): [
    PNIORealTime_IOxS,
    PNIORealTimeCyclicPDU.build_fixed_len_raw_type(4),
    PNIORealTime_IOxS,
    PROFIsafe.build_PROFIsafe_class(PROFIsafeControl, 4),
    PNIORealTime_IOxS,
]})

print(e.show2())