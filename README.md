LINK DEL VIDEO DE LOS ATAQUES:
https://youtu.be/v5858w0WOPo

README — Ataque Man-in-the-Middle (MitM) mediante ARP Spoofing con Scapy
Objetivo del Script

El propósito de este laboratorio es demostrar cómo un atacante puede interceptar la comunicación entre una víctima y su gateway mediante un ataque Man-in-the-Middle utilizando ARP Spoofing.

El script desarrollado con Scapy envía respuestas ARP falsas que manipulan las tablas ARP de los dispositivos objetivo, redirigiendo el tráfico hacia el atacante sin interrumpir la comunicación.

Esto permite observar la exposición de datos cuando no existen mecanismos de protección en la red local.

Topología de Red
Dispositivo	Rol	Dirección IP	Interfaz
Kali Linux	Atacante	192.168.10.10	eth0
Linux / Windows	Víctima	192.168.10.20	eth0
Router	Gateway	192.168.10.1	eth0

Red: 192.168.10.0/24
VLAN: No requerida para el laboratorio.
Condición clave: Todos los equipos deben estar en el mismo dominio de broadcast.

Capturas de Pantalla
Topología en PNETLab


Tabla ARP antes del ataque
arp -a



Ejecución del script
sudo python3 arp_mitm.py



Tabla ARP después del ataque

Debe observarse la MAC del atacante asociada al gateway o a la víctima.


Evidencia de tráfico interceptado (Wireshark o tcpdump)

Filtros sugeridos:

arp
dns
icmp



Parámetros Usados

Ejemplo:

target_ip = "192.168.10.20"
gateway_ip = "192.168.10.1"
interface = "eth0"

Funciones implementadas

Descubrimiento de direcciones MAC mediante ARP.

Envío continuo de respuestas ARP falsificadas.

Activación de IP Forwarding para mantener la conectividad.

Restauración de la red tras finalizar el ataque.

Requisitos para Utilizar la Herramienta

Kali Linux o distribución similar

Python 3

Biblioteca Scapy

Permisos root

Entorno virtualizado

Instalación
pip install scapy

Habilitar IP Forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

Medidas de Mitigación

Dynamic ARP Inspection (DAI): valida paquetes ARP contra una base confiable.

DHCP Snooping: evita asignaciones IP fraudulentas.

Entradas ARP estáticas: reducen el riesgo de manipulación.

Segmentación mediante VLANs: limita ataques dentro del broadcast.

Uso de cifrado (HTTPS, VPN): protege la confidencialidad del tráfico.

Sistemas IDS/IPS: permiten detectar anomalías.

Conclusión Técnica

El ARP spoofing continúa siendo una técnica efectiva para interceptar tráfico en redes locales sin controles de seguridad adecuados. Este laboratorio evidencia la importancia de implementar mecanismos de protección en la capa 2 y utilizar protocolos cifrados para resguardar la información.

La práctica se realizó en un entorno controlado con fines académicos.
