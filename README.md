# Proyecto TFG

## Instalación de docker

Para llevar a cabo este proyecto, es imprescindible contar con Docker instalado. Toda la información necesaria para realizar la instalación se encuentra detallada en la documentación de [Docker](https://docs.docker.com/engine/install/).

## Instalación de Odoo con docker

### Paso 1: Clonar el repositorio

Primero, clona el repositorio del proyecto TFG desde GitHub:
``` bash
git clone https://github.com/albertolj/TFG-Odoo 
```

### Paso 2: Iniciar Odoo con Docker

Dirígite al directorio raiz del proyecto y ejecuta el archivo yaml:

``` bash
docker-compose up
```

### Paso 3: Acceder a Odoo
Una vez que Odoo se haya iniciado correctamente, puedes acceder a la aplicación en tu navegador con el siguiente enlace:
[Enlace a tu localhost con puerto 8300](http://localhost:8300/).

### Paso 4: Configuración de la Base de Datos

Al configurar la base de datos, ten en cuenta que la "Master Password" es "odoo" y el "Database Name" debe empezar por una cadena "15.". Esta configuración es debido al archivo odoo.conf.

### Paso 5: Iniciar sesión en Odoo

Después de configurar la base de datos, inicia sesión en la aplicación utilizando las credenciales que definiste en el paso anterior.

## Configuración de Odoo

Una vez que hayas accedido a la aplicación, los siguientes pasos indican cómo configurar los módulos personalizado que he añadido.

### Paso 1: Instalar el módulo "Ventas"

Dirígete al apartado de "Aplicaciones" y selecciona "Ventas" para instalarla. Si aparece para instalar el módulo "Tarifas Wizard" puedes ir directamente al Paso 4.

### Paso 2: Activar el modo desarollador

En el apartado de "Ajustes/Opciones generales/Herramientas de desarrollador", activamos el modo desarrollador. Esto permite realizar configuraciones avanzadas.

### Paso 3: Actualizar aplicaciones

En "Aplicaciones" selecciona "Actualizar lista de aplicaciones" para agregar los módulos personalizados que se encuentran en la carpeta local "extra-addons".

### Paso 4: Instalar el módulo "Tarifas Wizard"

A continuación, instala el módulo "Tarifas Wizard". Dicho módulo también va a instalar todos los módulos necesarios para que funcione correctamente. Los módulos que se van a instalar se encuentran especificados en el archivo "\__manifest\__.py".

### Paso 5: Instalar el módulo "Inventario"

El único módulo que no está vinculado a los módulos desarrollados es el módulo de inventario. Por lo tanto, en la sección de "Aplicaciones", procedemos a buscar y luego instalar dicho módulo.

### Paso 6: Instalar la opción de Ventas "Tarifas"

Por último, dirígite en "Ajustes" a "Ventas", en el apartado de "Precio" se encuentra la opción de "Tarifas". Activa la opción, y señala el parámetro de "Reglas de precio avanzadas" y guarde los cambios.
