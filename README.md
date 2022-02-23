# Rogue Phisher

Este proyecto consiste en un portal cautivo utilizado para recopilar credenciales a través de
un falso punto de acceso WiFi. Concretamente, credenciales de Google, simulando ser la autenticación
delegada de los puntos de acceso encontrados en los aeropuertos gestionados por AENA.

### Requisitos

Se ha comprobado su funcionamiento en distribuciones Linux (concretamente Debian 11),
por lo que los requisitos necesarios para sistemas con gestores de paquetes de tipo DEB
son los siguientes:

- python3-virtualenv
- python3-pip

La versión de Python con la que se han hecho las pruebas es la 3.9, por lo que cualquiera
igual o superior a ésta no debería dar problemas.

### Uso

Es necesario crear un entorno virtual en el que se instalen los paquetes especificados en
*requirements.txt*.
