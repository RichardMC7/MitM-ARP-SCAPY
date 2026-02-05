README 1 — Ataque Man-in-the-Middle (MitM) mediante ARP Spoofing con Scapy
📌 Objetivo del Script

El objetivo de este laboratorio es demostrar cómo un atacante puede posicionarse entre dos dispositivos dentro de una red local mediante un ataque Man-in-the-Middle (MitM) utilizando ARP Spoofing.

El script desarrollado en Python con Scapy envía respuestas ARP falsificadas a la víctima y al gateway, haciendo que ambos dispositivos asocien la dirección MAC del atacante con direcciones IP legítimas.

Como resultado, todo el tráfico pasa a través del atacante sin que los usuarios lo perciban.

🖥️ Topología de Red

Ejemplo (ajústalo a tu lab real):

Dispositivo	Rol	IP	MAC	Interfaz
Kali Linux	Atacante	10.0.0.10	XX:XX:XX:XX	eth0
Ubuntu	Víctima	10.0.0.20	XX:XX:XX:XX	eth0
Router	Gateway	10.0.0.1	XX:XX:XX:XX	eth0

Segmento de red: 10.0.0.0/24
VLAN: No utilizada (red plana de laboratorio).

👉 Esto es importante porque ARP spoofing solo funciona dentro del mismo dominio de broadcast.

📸 Capturas de Pantalla

Inserta en este orden (MUY importante para que el reporte tenga narrativa técnica):

🔹 Topología en PNETLab

(Insertar imagen aquí)

🔹 Tabla ARP antes del ataque
arp -a


(Insertar imagen)

🔹 Ejecución del Script
sudo python3 ScapyARP2.py


(Insertar imagen)

🔹 Tabla ARP después del ataque

Debe mostrar la MAC del atacante asociada al gateway.

(Insertar imagen)

⚙️ Parámetros Usados

Dentro del script se definieron los siguientes valores:

target_ip = "10.0.0.20"
gateway_ip = "10.0.0.1"
interface = "eth0"

Funciones principales:

✅ Obtención de MAC mediante solicitudes ARP
✅ Envío de respuestas ARP falsas
✅ Activación de IP Forwarding para evitar interrupciones
✅ Restauración de la red al finalizar

🧰 Requisitos para Utilizar la Herramienta
Software:

Kali Linux / cualquier distro con Python

Python 3

Scapy

Permisos root

PNETLab o entorno virtualizado

Instalación de Scapy:
pip install scapy

Activar el reenvío de paquetes:
echo 1 > /proc/sys/net/ipv4/ip_forward

🛡️ Medidas de Mitigación

Este tipo de ataque puede prevenirse implementando controles de seguridad en la red:

🔹 Dynamic ARP Inspection (DAI)

Valida los paquetes ARP contra una tabla DHCP Snooping.

🔹 DHCP Snooping

Evita que dispositivos no autorizados asignen direcciones IP.

🔹 Entradas ARP estáticas

Reduce el riesgo de envenenamiento ARP.

🔹 Segmentación de red (VLANs)

Limita el alcance del ataque.

🔹 Uso de VPN

Cifra el tráfico incluso si es interceptado.

⚠️ Conclusión Técnica

El laboratorio demostró que ARP spoofing sigue siendo un ataque efectivo en redes locales mal configuradas.
La facilidad con la que un atacante puede interceptar tráfico resalta la importancia de aplicar controles de seguridad en la capa 2.
