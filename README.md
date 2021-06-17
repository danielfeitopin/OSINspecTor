# Programación Integativa: Práctica Final

## Observaciones
### Docker
* Para utilizar el contenedor de Docker, ejecutar el script de `setup.sh`.

### Aclaraciones sobre las funcionalidades
* La funcionalidad de buscar emails de un dominio dado, tarda unos 30 segundos en obtener los resultados ya que realiza *crawling* y *scrapping* sobre diversas paginas obtenidas por la librería 3rd party *google*.
* Las funcionalidades emails, mx y dns utilizan la capa gratuita de APIs que de realizar demasiadas peticiones sobre ellas en un corto espacio de tiempo se puede correr el riesgo de que baneen la IP del usuario (durante un rato). Obteniendo en consecuencia un error *429 Too Many Requests*.
