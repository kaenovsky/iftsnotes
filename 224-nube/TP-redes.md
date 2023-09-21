## TP Nube

1. Qué es un firewall y qué función cumpple en una red?

Un firewall es un sistema que permite o deniega el paso de paquetes de datos a través de una red, basándose en un conjunto de reglas. Se puede implementar en hardware o software. Su función es la de proteger a la red de accesos no autorizados, filtrando el tráfico de datos que entra y sale de la red.

Teniendo en cuenta que la seguridad informática es uno de los principales vectores de ataque a las empresas, es fundamental contar con un firewall que proteja la red de accesos no autorizados. Como vemos en el Capítulo 1 del libro Cisco CCNA Routing and Switching 200-120 Official Cert Guide, los firewalls pueden ser de hardware o de software. Los firewalls de hardware son dispositivos que se conectan entre la red interna y la red externa, y que filtran el tráfico de datos que entra y sale de la red. Los firewalls de software son programas que se instalan en un servidor y que filtran el tráfico de datos que entra y sale de la red. En ambos casos, el firewall se basa en un conjunto de reglas para permitir o denegar el paso de paquetes de datos a través de la red.

2. Qué se entiede por DMZ o Zona Desmilitarizada

Una DMZ (Demilitarized Zone) es una subred que se encuentra entre la red interna y la red externa, y que se utiliza para alojar los servidores que deben ser accesibles desde Internet. La DMZ se encuentra protegida por un firewall, que permite el acceso a los servidores de la DMZ desde Internet, pero no permite el acceso a la red interna desde la DMZ. De esta forma, si un atacante logra vulnerar la seguridad de un servidor de la DMZ, no podrá acceder a la red interna.

3. Explique brevemente las capas 4, 6 y 7 del modelo OSI

La capa 4 del modelo OSI es la capa de transporte. Su función es la de establecer una conexión entre dos hosts, y asegurar que los datos lleguen correctamente de un host a otro. Los protocolos de la capa de transporte son TCP y UDP.
La capa 6 del modelo OSI es la capa de presentación. Su función es la de convertir los datos en un formato que pueda ser entendido por la aplicación que los va a utilizar. Los protocolos de la capa de presentación son SSL y TLS.
Por último, la capa 7 del modelo OSI es la capa de aplicación. Su función es la de proporcionar servicios de red a las aplicaciones. Los protocolos de la capa de aplicación son HTTP, FTP, SMTP, POP3, IMAP, SSH, Telnet, DNS, DHCP, etc.

Los puertos 22, 80 y 443 corresponden a los protocolos SSH, HTTP y HTTPS, respectivamente. El protocolo SSH se utiliza para acceder de forma remota a un servidor, y es el protocolo que se utiliza para acceder a un servidor Linux desde una terminal. El protocolo HTTP se utiliza para acceder a sitios web, y el protocolo HTTPS se utiliza para acceder a sitios web de forma encriptada, utilizando SSL o TLS.

El puerto 3389 corresponde al protocolo RDP (Remote Desktop Protocol), que se utiliza para acceder de forma remota a un servidor Windows.

4. Qué es una IP pública?
Una IP pública es una dirección IP que identifica a un dispositivo en Internet. Las direcciones IP públicas son únicas, y no pueden repetirse en Internet. Se asignan a los dispositivos que se conectan a Internet y funcionan como referencia para conectarnos a distintos dispositivos. Por ejemplo, cuando accedemos a un sitio web, lo hacemos a través de su dirección IP pública.

Las IP estáticas se diferencian de las dinámicas en que las primeras no cambian, mientras que las segundas sí. Las IP estáticas se utilizan para servidores, ya que es necesario que la dirección IP del servidor sea siempre la misma. Las IP dinámicas se utilizan para dispositivos que se conectan a Internet de forma temporal, como por ejemplo los dispositivos móviles o las redes hogareñas.

Azure tiene servicio de IP estática y dinámica:

![](./224-assets/tp1-assets/azure-ip.png)

5. Qué tipos de discos rígidos ofrece Azure para VPS?

Azure ofrece discos duros SSD y discos duros HDD. Los discos duros SSD son más rápidos que los discos duros HDD, pero también son más caros. Por lo tanto, los discos duros SSD se utilizan para aplicaciones que requieren un alto rendimiento, como por ejemplo bases de datos, y los discos duros HDD se utilizan para aplicaciones que no requieren un alto rendimiento, como por ejemplo almacenamiento de archivos.

![](./224-assets/tp1-assets/azure-discos.png)

TBD: Diagrama de red