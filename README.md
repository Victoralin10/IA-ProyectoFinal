# IA-ProyectoFinal
Proyecto Final del Curso ST-414 Inteligencia Artificial

# Grupo
Integrantes:
- CABALLA CASTRO, ARNOLD POOL
- CUEVA LLANOS, VICTOR ALIN
- LEONARDO APOLINARIO, LESLIE
- GALINDO AGUILAR, ERICK

# Requisitos para correr el proyecto
* Ubuntu
* python3
* ffmpeg
* libavcodec-extra
* mysql-server
* nodejs

# Cargar entorno de desarrollo
**Instalar python3**

Verificar si python3 esta instalado, sino instalar con:
`sudo apt-get install python3`

**Instalar ffmpeg y libavcode-extra**

`sudo apt-get install ffmpeg libavcodec-extra`

**Instalar mysql**

`sudo apt-get install mysql-server`

**Instalar nodejs**
```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

**Obtener codigo fuente**

Descargar este repositorio como zip o clonar.
`git clone https://github.com/Victoralin10/IA-ProyectoFinal.git`

**Instalar dependencias de python**

`pip3 install -r requirements.txt --user`

# Ejecutar proyecto
## Grabar transmision
Para realizar las grabaciones se utiliza el script **record-stream.py**. La lista de estacione de radio online se carga desde un 
archivo json que se puede especificar mediante la opcion `-f`. Mediante la opcion `-df` se indica la carpeta donde se van a guardar
los archivos. Mediante la opcion -i se indica la duracion en segundos de cada archivo.

Ejemplo para guardar la grabacion en la carpeta data, con archivos de 10 minutos de duracion cada uno.
`./record-stream.py -i 600 -f stations.json -df data/`

## Extraer muestras de audio
Para separar los archivos de grabacion en pequeños archivos que pueda etiquetar, usar el sclipt *split-audio.py*.
Mediante la opcion `-d` se indica la duracion en segundos de cada muestra de audio.

Ejemplo para separar los archivos de la carpeta **data** y guardarlos en la carpeta **samples**, con intervalos de 2 segundos.
`./split-audio.py -d 2 data/ samples/`

## Levantar herramienta de etiquetado
Para levantar la herramienta de etiquetado se necesita primero crear la base de datos en mysql.

Luego utilizar el script **mysql-load-samples.py**.

Para desplegar la herramienta de etiquetado ver la 
[documentacion](https://github.com/Victoralin10/IA-ProyectoFinal/tree/master/etiquetador)

## Obetener dataset en archivo csv
Esto se hace en 2 paso.

**Exportar los tags a archivo csv**
Para esto utilizar el script **mysql-export-tags.py**, con ello se obtendra un archivo csv con dos columnas, el identificador
de cada muestra de audio y su etiqueta correspondiente.

**Extraccion de caracteristicas de las muestras de audio**
Para esto utilizar el script **./generate-dataste.py**

# Adicional
* Puede obtener ayuda de como utilizar cualquier script con la opcion --help. Ejemplo: `./record-stream.py --help`
