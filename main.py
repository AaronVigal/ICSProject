import sys
from scapy.all import *
ran = random.randint(1024,2000)
ip=IP(src='IP_HERE',proto=6,flags=2)
SYN=TCP(ran=ran,dport=102,flags='S')
SYNACK=sr1(ip/SYN)
ACK=TCP(ran=ran,dport=102,flags='A',seq=1,ack=SYNACK.seq+1)
send(ip/ACK)
header_1= TCP(ran=ran, dport=102, flags='PA', seq=1, ack=SYNACK.seq+1)
rsp_1 = sr1(ip/header_1/protocol)
siemensPLC=TCP(sport=sport,dport=102,flags='A',seq=rsp_1.ack, ack=rsp_1.len+rsp_1.seq-40)
send(ip/siemensPLC)