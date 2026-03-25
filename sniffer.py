from scapy.all import sniff, Raw

def catch_packet(packet):
    if packet.haslayer(Raw):
        print(packet[Raw].load.decode('utf-8', errors='ignore'))

print("Starting packet sniffer...")
sniff(prn=catch_packet, filter="tcp port 8080", store=0)