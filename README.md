
# Taller Contenedor Docker

Este taller tiene como finalidad mostrar el uso de un contenedor docker. En este caso partícular se hizo un programa simple con Python que usa [FastAPI](https://fastapi.tiangolo.com/)

Este ejercicio consiste en consultas sobre un conjunto de idiomas, los cuales tienen un Id y un Nombre. A partir de ahí podemos hacer peticiones GET, POST, PUT y DELETE.


## Tecnologías

**Lenguage de programación:** Python

**Librerías:** FastAPI, Uvicorn


## Funcionamiento

Desde la consola se ejecuta el siguiente comando

```bash
docker pull andresmaldonado200338/taller-web
```

Después ejecutamos el comando
```bash
docker run andresmaldonado200338/taller-web:version1
```
Finalmente, desde nuestro navegador entramos al siguiente enlace
```bash
  http://localhost:8000/
```
Una vez dentro podemos ejecutar las consultas creadas.
## Author

- [@AndresMaldonado200338](https://github.com/AndresMaldonado200338)

