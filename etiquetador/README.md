# Herramienta de etiquetado

# Requisitos
* nodejs

# Pasos para levantar el proyecto
**Instalar las dependencias de node**

`npm install`

**Crear archivo de configuracion**

Crear el archivo **.env** copiando el archivo **.env.example**.

Luego ingresar el puerto y los accesos a la base de datos.

**Acceso a los archivos de grabacion y muestras**

En la carpeta **public/**, asegurarse que los links `data` y `audios` esten apuntando a las carpetas donde estan los archivos 
de grabacion y las muestras.

**Despliegue**

Para desplegar utilizar lo siguiente:
`npm start`

En modo desarrollo
`npm run dev`
