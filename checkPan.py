from panos.firewall import Firewall
from panos.errors import *
from dotenv import load_dotenv
import xml.etree.ElementTree as ET
import os, xmltodict

class panLogCollect:
    def __init__(self) -> None:
        load_dotenv(override=True)
        self.pan_ip = os.getenv("pan_ip")
        self.pan_user = os.getenv("pan_user")
        self.pan_pass = os.getenv("pan_pass")
        self.pan_key = os.getenv("pan_key")

    def getWanIfnet(self, ip_fws):
        if type(ip_fws) != list:
            ip_fws = []
            ip_fws.append(ip_fws)
        for ip_fw in ip_fws:
            try:
                firewall = Firewall(ip_fw, self.pan_user, self.pan_pass)
                logs = firewall.op('show interface "all"')
                logs2str = ET.tostring(logs, encoding='utf8').decode('utf8')
                logs2json = xmltodict.parse(logs2str)
                if logs2json['response']['@status'] == 'success':
                    for ifnet in logs2json['response']['result']['ifnet']['entry']:
                        if ifnet['zone'] == "WAN":
                            print(f"{ip_fw} - {ifnet['ip']}")
                else:
                    print(f"Erro ao obter resposta de {ip_fw}")
            except PanURLError:
                print(f"Não foi possível conectar ao {ip_fw}")