from scapy.all import sniff, Raw

def catch_packet(packet):
    if packet.haslayer(Raw):
        print(packet.summary())
        
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        if 'username' in payload:
            print(payload[payload.find('username='):])

print("Starting packet sniffer...")
sniff(prn=catch_packet, filter="tcp port 8080", store=0)

# Run with: "sudo $(which python) sniffer.py"
