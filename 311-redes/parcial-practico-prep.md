### Prep parcial práctico

Ejercicio: configurar una red básica en Packet Tracer con los siguientes requisitos:

1. **Red de partida:**
   - El examen puede comenzar con una red base dada por el profesor. Tendrás que subdividir la red utilizando el subneteo, teniendo en cuenta la cantidad de máquinas por VLAN que se necesiten.

2. **VLANs y subredes:**
   - Configurar 4 VLANs (por ejemplo, `Admin`, `Server`, `Ventas`, `Desarrollo`). Cada VLAN tendrá un rango de direcciones IP específico obtenido a partir del subneteo inicial.

3. **Configuración de DHCP:**
   - Un servidor DHCP deberá proveer direcciones IP a dispositivos en diferentes VLANs. Puede requerir configuraciones especiales para que cada VLAN reciba el rango de direcciones correcto.

4. **Configuración de DNS:**
   - Configurar un servidor DNS en la red para que resuelva nombres de dominio de dispositivos de la red.

5. **Pruebas de conectividad:**
   - Realizar pruebas de conectividad utilizando `ping`, `tracert` y otros comandos para verificar que las VLANs pueden comunicarse correctamente según lo especificado.
   - Podrían incluirse escenarios donde ciertas VLANs no deben tener acceso a otras, implementando restricciones en las configuraciones de los switches.

6. **Modificación de puertos y telnet:**
   - Cambiar la velocidad de ciertos puertos y verificar su estado.
   - Configurar el switch para acceso remoto mediante Telnet y hacer configuraciones utilizando esta conexión.