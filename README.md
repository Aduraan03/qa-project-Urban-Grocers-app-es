# Proyecto Urban Grocers 
## Autor
Alejandro Duran, Sprint 7, grupo 17
# Proyecto de Creación de Kits para Usuarios en Urban Grocers

## Descripción del Proyecto

Este proyecto es un conjunto de pruebas automatizadas para validar la funcionalidad de creación de kits personalizados para usuarios en la aplicación **Urban Grocers**. Las pruebas verifican diversos escenarios para el campo `name` del kit, asegurando que cumpla con las reglas y restricciones establecidas, como límites de caracteres, el uso de caracteres especiales, y otros requisitos.
Este proyecto implementa un conjunto de pruebas automáticas para validar la funcionalidad de creación de kits en una API REST. Las pruebas están construidas utilizando pytest y simulan distintos escenarios positivos y negativos para asegurar que la API maneje correctamente diferentes tipos de datos en el campo name.

## Objetivo

Este proyecto tiene como objetivo verificar que la API de creación de kits cumpla con los requerimientos de negocio en cuanto a validación de datos. A través de pruebas automatizadas, se evalúa el correcto funcionamiento de la API bajo diferentes entradas de datos.

## Tecnologías y Técnicas Utilizadas

- **Python**: Lenguaje de programación utilizado para implementar las pruebas.
- **pytest**: Framework de pruebas utilizado para ejecutar y gestionar los casos de prueba.
- **requests**: Librería para hacer solicitudes HTTP, empleada para enviar peticiones a la API de Urban Grocers.
- **apiDoc**: Herramienta de documentación para la API, utilizada para estructurar y presentar la documentación de los endpoints.
- **Control de Versiones (Git)**: Control de versiones con archivos `.gitignore` y `README.md` para gestionar cambios en el código y facilitar la colaboración.
- **Pruebas Automatizadas**: Implementación de pruebas para validar los requisitos de la API y asegurar la correcta funcionalidad en diferentes escenarios de entrada.
## Estructura del Proyecto
El proyecto está organizado en las siguientes carpetas y archivos:
- **create_kit_test.py**:  Contiene las pruebas de creación de kits, tanto positivas como negativas.
- **sender_stand_request.py**:  Define las funciones para realizar solicitudes HTTP a la API.
- **data.py**: Archivo centralizado para almacenar datos de prueba y configuraciones reutilizables.
- **configuration.py**: Configuración de URL y rutas para el servicio de API (no requiere modificaciones).

## configuracion e instalacion
Requisitos Previos
Asegúrate de tener instalado Python 3 y pip. Luego, instala las dependencias necesarias:

bash
Copiar código
pip install -r requirements.txt
Configuración del Entorno
Asegúrate de que el archivo configuration.py contenga la URL correcta para el servicio, y que las rutas estén configuradas según tu API:

python
Copiar código
URL_SERVICE = "https://tu_url_del_servicio"
CREATE_USER_PATH = "/api/v1/users"
KITS_PATH = "/api/v1/kits"
Uso
Clona el repositorio en tu máquina local.
Instala las dependencias siguiendo los pasos anteriores.
Modifica configuration.py si es necesario.
Ejecución de Pruebas
Para ejecutar las pruebas, usa el siguiente comando en la terminal dentro de la carpeta principal del proyecto:

bash
Copiar código
pytest folder/del/proyecto
Esto ejecutará todas las pruebas y mostrará un resumen en la terminal con los resultados. Asegúrate de estar en el entorno adecuado y que los servicios de la API estén disponibles.

## Notas
Este proyecto implementa buenas prácticas de desarrollo en Python:

Centralización de Datos: Todos los datos de prueba están centralizados en data.py para evitar valores hardcodeados.
Reutilización de Headers: Los headers se definen en data.py y se agregan de forma dinámica según las necesidades de cada solicitud.
Cobertura de Escenarios de Prueba: Las pruebas consideran diferentes tipos de valores para el campo name, incluyendo caracteres especiales, espacios, números, valores vacíos, y otros escenarios específicos.
