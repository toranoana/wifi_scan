# coding:utf-8
import json
import datetime
from aws_iot import awsIot
from scapy.all import *


def packet_callback(packet):
    if packet.type == 0 and packet.subtype == 4:
        print(str(packet.addr2 or '' )  + str(packet.info or '' ))
        now = datetime.now()
        data = {"datetime": now.strftime('%Y-%m-%d  %H:%M:%S'),\
                "addr": str(packet.addr2 or "" ),\
                "info": (packet.info or b' ').decode(),\
                "dBm_AntSignal": packet.dBm_AntSignal or "" }

        jsonData = json.dumps(data)
        try:
                awsIot(jsonData)
        except:
                print("exception発生")
        

sniff(iface="wlan0", prn=packet_callback, store=0 )