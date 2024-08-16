from panos.panorama import Panorama
from panos import base
from dotenv import load_dotenv
import os

load_dotenv(override=True)
# Conectar ao Panorama
pan_ip = os.getenv("pan_ip")
pan_user = os.getenv("pan_user")
pan_pass = os.getenv("pan_pass")
pan_key = os.getenv("pan_key")

panorama = Panorama(pan_ip, pan_user, pan_pass, api_key=pan_key)

# Definir o tipo de log que você quer puxar (por exemplo, tráfego)
log_type = 'traffic'

source_ip = 'IP_AQUI'
destination_ip = 'IP_AQUI'

# Criar a consulta de filtro
query = f'(addr.src eq {source_ip})'

# Puxar logs com o filtro aplicado
logs = panorama.op(f"<show><log><{log_type}><equal><query>{query}</query></equal></{log_type}></log></show>", xml=True)

# Exibir logs
print(logs)