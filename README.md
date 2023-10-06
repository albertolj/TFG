# Proyecto TFG

## Instalación de docker

## Instalación de Odoo con docker

### Paso 1: Clonar el repositorio

Primero, clona el repositorio del proyecto TFG desde GitHub:
``` bash
git clone https://github.com/albertolj/TFG 
```

### Paso 2: Iniciar Odoo con Docker

Dirígite al directorio raiz del proyecto y ejecuta el archivo yaml:

``` bash
docker-compose up
```


### Paso 3: Acceder a Odoo
Una vez que Odoo se haya iniciado correctamente, puedes acceder a la aplicación en tu navegador con el siguiente enlace:
[Enlace a tu localhost](http://localhost:8300/)

### Paso 4: Configuración de la Base de Datos

Al configurar la base de datos, ten en cuenta que la "Master Password" es "odoo" y el "Database Name" debe empezar por una cadena "15.". Esta configuración es debido al archivo odoo.conf.

### Paso 5: Iniciar sesión en Odoo

Después de configurar la base de datos, inicia sesión en la aplicación utilizando las credenciales que definiste en el paso anterior.

## Configuración de Odoo

Una vez que hayas accedido a la aplicación, los siguientes pasos indican cómo configurar los módulos personalizado que he añadido

### Paso 1: Instalar la Aplicación Ventas

Dirígete al apartado de "Aplicaciones" y selecciona "Ventas" para instalarla.

### Paso 2: Activar el modo desarollador

En el apartado de "Ajustes/Opciones generales/Herramientas de desarrollador", activamos el modo desarrollador. Esto permite realizar configuraciones avanzadas.

### Paso 3: Actualizar aplicaciones

En "Aplicaciones" selecciona "Actualizar lista de aplicaciones" para agregar los módulos personalizados que se encuentran en la carpeta local "extra-addons".

### Paso 4: Instalar el módulos "Tarifas Wizard"

Por último, instala el módulo "Tarifas Wizard". Dicho módulo también va a instalar todos los módulos necesarios para que funcione correctamente. Los módulos que se van a instalar se encuentran especificados en el archivo "__manifest__.py"
