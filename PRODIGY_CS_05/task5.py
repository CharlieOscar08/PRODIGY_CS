from scapy.all import *

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        # Extract source and destination IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        # Extract the protocol
        protocol = packet[IP].proto
        # Check if the packet has a Raw layer before accessing it
        if packet.haslayer(Raw):
            # Extract payload data
            payload = packet[Raw].load
        else:
            payload = "No payload"
        # Print packet details
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}, Payload: {payload}")

# Start sniffing packets
sniff(prn=packet_callback, filter="ip", store=0)
