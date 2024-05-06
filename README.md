# Implementación de un Stack de Visualización con Elasticsearch y Kibana
Autor: Imanol Anda Garcia
## Descripción del Proyecto
Este proyecto demuestra cómo configurar un entorno utilizando Elasticsearch y Kibana para recopilar, almacenar y visualizar datos dinámicamente. El objetivo es crear una plataforma robusta que permita visualizar datos en tiempo real y proporcionar insights a través de dashboards interactivos.

## Explicación de los Pasos Seguidos
- Configuración de Docker Compose: Utilicé Docker Compose para desplegar Elasticsearch y Kibana, asegurando que ambos servicios se comuniquen eficientemente en una red definida.
- Generación de Datos: Desarrollé un script en Python que simula datos de operaciones de máquinas en una fábrica y los inserta continuamente en Elasticsearch.
- Visualización con Kibana: Configuré varios tipos de visualizaciones en Kibana para representar los datos, incluyendo gráficos de líneas y tablas, que ayudan a monitorizar el estado de las máquinas.
## Instrucciones de Uso
- Configurar el Entorno
Ejecutar docker-compose up para iniciar los servicios de Elasticsearch y Kibana.
Asegurarse de que los puertos 5601 para Kibana y 9200 para Elasticsearch están disponibles y correctamente mapeados.
- Generar y Insertar Datos
Ejecutar el script datos.py para comenzar la generación y la inserción de datos simulados en Elasticsearch.
- Visualizar Datos en Kibana
Acceder a Kibana a través de http://localhost:5601.
Configurar índices y crear dashboards para visualizar los datos insertados.
## Problemas Encontrados
- Visualización de los Últimos Estados en Kibana: Tuve dificultades con Kibana Lens para mostrar el último estado de las máquinas, ya que requería configuraciones de agregación complejas.
- Configuración de Docker Compose: Inicialmente enfrenté problemas de permisos y de red, que resolví ajustando la configuración de Docker y los parámetros de seguridad.
## Mejoras Posibles
- Automatización de Inserciones de Datos: Implementar un cron job o un scheduler para insertar datos automáticamente en intervalos regulares, simulando un flujo de datos en vivo.
- Habilitar Seguridad en Elasticsearch: Configurar X-Pack para mejorar la seguridad del entorno de Elasticsearch, protegiendo los datos y el acceso a Kibana.
## Alternativas de Visualización
- Grafana: Considerar usar Grafana para visualizaciones alternativas, especialmente para monitoreo en tiempo real, dado su robusto sistema de alertas.
- Redash: Tableau es una herramienta de visualización de datos líder en la industria, conocida por su capacidad de integrar diversas fuentes de datos y proporcionar visualizaciones complejas y comprensibles.
## Conclusión
Este proyecto me ha permitido desarrollar una comprensión profunda de cómo configurar y utilizar un stack de visualización con Elasticsearch y Kibana, proporcionando una plataforma valiosa para análisis de datos en tiempo real. La flexibilidad de este stack permite adaptarlo a diversas necesidades de visualización y análisis.
