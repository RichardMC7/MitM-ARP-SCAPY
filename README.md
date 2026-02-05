README — Ataque Man-in-the-Middle (MitM) mediante ARP Spoofing con Scapy
Objetivo del Script

El objetivo de este laboratorio es demostrar cómo un atacante puede interceptar el tráfico de red entre dos dispositivos dentro de una red local mediante un ataque Man-in-the-Middle (MitM) utilizando ARP Spoofing.

El script desarrollado en Python con Scapy envía respuestas ARP falsificadas tanto a la víctima como al gateway, provocando que ambos asocien la dirección MAC del atacante con direcciones IP legítimas. Como resultado, el tráfico pasa a través del equipo atacante sin ser detectado por los usuarios.

Topología de Red

Ejemplo (ajústalo según tu laboratorio real):

Dispositivo	Rol	Dirección IP	Interfaz
Kali Linux	Atacante	10.0.0.10	eth0
Ubuntu/Linux	Víctima	10.0.0.20	eth0
Router	Gateway	10.0.0.1	eth0

Segmento de red: 10.0.0.0/24
VLAN: No utilizada (red plana de laboratorio).

Nota técnica: El ARP spoofing solo funciona dentro del mismo dominio de broadcast.

Capturas de Pantalla

Inserta las imágenes en el siguiente orden para mantener coherencia técnica en la documentación:

Topología en PNETLab

(Insertar imagen)

Tabla ARP antes del ataque

Comando:

arp -a


(Insertar imagen)

Ejecución del script
sudo python3 ScapyARP2.py


(Insertar imagen)

Tabla ARP después del ataque

Debe evidenciar que la MAC del atacante aparece asociada al gateway o a la víctima.

(Insertar imagen)

Parámetros Usados

Ejemplo de variables definidas en el script:

target_ip = "10.0.0.20"
gateway_ip = "10.0.0.1"
interface = "eth0"

Funcionalidades principales del script

Obtención de direcciones MAC mediante solicitudes ARP.

Envío continuo de respuestas ARP falsificadas.

Activación de IP Forwarding para evitar la interrupción de la comunicación.

Restauración de la configuración ARP original al finalizar el ataque.

Requisitos para Utilizar la Herramienta
Software requerido

Kali Linux o cualquier distribución Linux

Python 3

Biblioteca Scapy

Permisos de superusuario

Entorno virtualizado (PNETLab, VMware o VirtualBox)

Instalación de Scapy
pip install scapy

Activación del reenvío de paquetes
echo 1 > /proc/sys/net/ipv4/ip_forward

Medidas de Mitigación

Para reducir el riesgo de ataques ARP spoofing se recomienda implementar los siguientes controles:

Dynamic ARP Inspection (DAI): valida los paquetes ARP comparándolos con la tabla generada por DHCP Snooping.

DHCP Snooping: previene la asignación de direcciones IP por dispositivos no autorizados.

Entradas ARP estáticas: limitan la posibilidad de envenenamiento ARP.

Segmentación mediante VLANs: reduce el alcance del dominio de broadcast.

Uso de VPN: protege la confidencialidad del tráfico incluso si es interceptado.

Conclusión Técnica

El laboratorio evidencia que el ARP spoofing continúa siendo un método efectivo de interceptación en redes locales que carecen de controles de seguridad en la capa 2. La facilidad con la que un atacante puede posicionarse entre dos dispositivos resalta la necesidad de implementar mecanismos de protección adecuados.

Este laboratorio fue realizado en un entorno controlado con fines educativos y siguiendo principios éticos de ciberseguridad.
