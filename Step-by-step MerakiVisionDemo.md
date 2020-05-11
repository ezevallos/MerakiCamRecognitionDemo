# Table of contents
1. [Introducción - Cisco DevNet](#intro)
2. [Lab 4: Reconocimiento de imágenes mediante un comando de voz.](#para4)

<div id='intro'/>

# Cisco DevNet
_Cisco Developer’s Network_ o _Cisco DevNet_ es nuestra comunidad de práctica para desarrolladores y profesionales de TI que buscan escribir aplicaciones y desarrollar integraciones con productos, plataformas y APIs de Cisco. A continuación, navegaremos por los componentes principales que conforman la plataforma de Cisco DevNet, a la que podemos acceder mediante la dirección: [https://developer.cisco.com/](https://developer.cisco.com/).
![DevNet](https://i.ibb.co/dDrKd7d/DN-IN-1.png)

## Start Now
Aquí ([https://developer.cisco.com/startnow/](https://developer.cisco.com/startnow/)) encontraremos una lista curada de contenidos para empezar nuestro viaje, es el lugar ideal para aquellos que desean tomar el primer paso en programación, o llevar sus habilidades al siguiente nivel. Es el lugar para tener una experiencia de aprendizaje guiada y aplicada, en las plataformas y tecnologías de Cisco.
![DevNetStartNow](https://i.ibb.co/BCqvtR7/DN-IN-2.png)

## Learning Tracks
Aquí ([https://developer.cisco.com/learning/tracks](https://developer.cisco.com/learning/tracks)) encontraremos una ruta guiada de aprendizaje en tecnologías de Cisco selectas. Están basadas en los DevNet Learning Labs, un track está conformado por módulos, que a su vez están conformados por los learning labs. Algunos módulos se enfocan en conocimientos generales de programación, redes y otros temas.

 - [https://developer.cisco.com/learning/modules](https://developer.cisco.com/learning/modules)
 - [https://developer.cisco.com/learning/labs](https://developer.cisco.com/learning/labs)
![DevNetLearningTracks](https://i.ibb.co/kg9shVs/DN-IN-3.png)

## Video-Course
Aquí ([https://developer.cisco.com/video/net-prog-basics/](https://developer.cisco.com/video/net-prog-basics/)) encontraremos un inicio al viaje hacia la programabilidad de la red con este video curso dirigido por expertos. Tenemos 6 módulos, cada uno con lecciones que incluyen API y ejemplos de código que puede usar en su propio entorno de desarrollo para seguir junto con los videos.
![DevNetVideoCourse](https://i.ibb.co/HDDrpmG/DN-IN-4.png)

## Sandbox
Aquí ([https://developer.cisco.com/site/sandbox/](https://developer.cisco.com/site/sandbox/)) encontraremos un entorno donde ingenieros, desarrolladores, administradores de red, arquitectos o cualquier otra persona que desee desarrollar / probar las API, controladoras, equipo de red, herramientas de colaboración de Cisco y más, pueden hacerlo de forma gratuita. Ejecute su código contra la infraestructura en vivo 24x7, el acceso es gratuito, a una variedad de laboratorios; elija entre entornos virtualizados, simuladores y hardware real.
![DevNetSandBox](https://i.ibb.co/fnJctHw/DN-IN-5.png)

## Code-Exchange
Aquí ([https://developer.cisco.com/codeexchange/](https://developer.cisco.com/codeexchange/)) encontraremos un conjunto de repositorios de código en línea, públicos en GitHub, que han sido seleccionados y están relacionados con todas las áreas de tecnología de Cisco. En Code Exchange, contamos con cientos de repositorios de código, puede encontrar código creado y mantenido por equipos de ingenieros de Cisco, colaboradores de la comunidad, socios del ecosistema, comunidades de tecnología y de código abierto y desarrolladores individuales. Los miembros de la comunidad DevNet de Cisco pueden usar este código para impulsar su desarrollo de aplicaciones e integraciones usando las API de Cisco.

<div id='para4'/>

# Lab: Reconocimiento de imágenes mediante un comando de voz. Utilice las *APIs* de *Cisco Meraki*, *Imagga* y *Google Actions* para analizar la captura de una cámara de Meraki, mediante un comando de voz en un dispositivo *Android* con *Google Assistant* 

## Introducción
En este laboratorio obtenemos un *snapshot* de una cámara *Cisco Meraki*, haciendo uso del *Dashboard API*. Luego, envíamos la imagen a un software de reconocimiento de imágenes llamado *Imagga*, cuyo *API* es de uso abierto. Finalmente, utilizamos la *API* de *Google Actions* para que nos lea las características de la imagen en voz alta, y nos muestre la imagen; mediante un comando de voz de *Google Assistant*.


## Objetivos

Al completar este laboratorio, estará familiarizado con el uso básico de las *APIs* de *Cisco Meraki*, *Imagga* y *Google Actions*, y además:

 - Obtener la captura de una cámara Meraki, mediante el *Dashboard API*.
 - Utilizar el URL de la imagen, para obtener el archivo donde esta se encuentra.
 - Enviar esta imagen al software de reconocimiento, llamado *Imagga*, mediante su *API*
 - Modularizar el código para llamarlo desde nuestro *web server*.
 - Crear un *web server Flask* que sirva las características e imagen obtenidas en el script previo
 - Publicar nuestro proyecto a *Heroku* para acceder a él desde una dirección web.
 - Configurar *Google Actions* para llamar a nuestro *web server* mediante un comando de voz en *Google Assistant*, usando *DialogFlow*.

## Pre-requisitos

 - Manejo de ***Python*** y sus librerías, en particular ***Flask*** para desplegar *web servers*
 - Cuenta de ***DevNet*** para utilizar el ***Sandbox Meraki Always-On***.
 - Cuenta de ***GitHub*** y un conocimiento básico de contol de versiones, según lo descrito en [Introducción a Git](https://developer.cisco.com/learning/tracks/devnet-beginner-es/fundamentals-es/intro-to-git-es/step/1).
 - [***Git Bash***](https://git-scm.com/downloads) instalado en nuestro entorno de desarrollo. 
 - Cuenta de ***Imagga*** para contar con un *api_key* y *api_secret* y enviar imágenes a reconocer.
 - Cuenta de ***Heroku*** para acceder a nuestro código de ***Python*** desde una URL pública
 - Cuenta de ***Google*** para acceder a ***DialogFlow***

## Acerca de Cisco Meraki

***[Cisco Meraki](https://meraki.cisco.com/)*** es la solución de red gestionada en nube de **Cisco**. Ofrece un portafolio de productos de infraestructura de red que incluye Access points, Enterprise switches, routers, dispositivos de seguridad de red e incluso cámaras. Su versátil modelo de gestión basado en nube permite administrar la topología desde cualquier lugar del mundo, y provisionar equipos con tan solo una conexión a internet, y una fuente de poder.

## Utilizar el ***SandBox Meraki Always-On***

***[DevNet](https://developer.cisco.com/)*** nos provee muchos SandBoxes. Estos son entornos virtuales que emulan equipos físicos o redes donde podemos aprender a realizar configuraciones como la que intentamos efectuar. En este caso en particular, haremos uso del ***SandBox Meraki Always On*** que nos permite acceder a una cámara de ***Cisco Meraki*** en caso no contemos con una para realizar el laboratorio. Esta cámara en particular, se encuentra apuntando a una TV que se encuentra prendida 24/7. Nos dirigimos a la página principal de ***DevNet*** y navegamos a _Discover_ --> _**Code**_ --> _Sandbox Remote Labs_ donde encontraremos más información acerca de los _Sandboxes_. Encontramos información sobre cómo utilizarlos, si se trata de un _Sandbox_ que siempre se encuentra activo, o si es necesario reservarlo por cierta cantidad de tiempo, caso en el que además debemos esperar unos minutos para que _DevNet_ prepare los recursos que utilizaremos. Es importante mencionar que todos los recursos que encontraremos en ***DevNet*** son totalmente libres para los miembros de nuestra comunidad. Para acceder, debemos crearnos una cuenta, o utilizar nuestro ***Cisco ID*** en caso ya contemos con uno. Los alumnos de ***Cisco Networking Academy*** tienen una pre-cuenta de _DevNet_ utilizando sus credenciales NetAcad.

![DevNet Sandbox](https://i.ibb.co/Lrf0X6y/DN-SB.png)
Aquí encontraremos la respuesta a muchas preguntas acerca de estos entornos virtuales, donde desarrolladores, ingenieros, administradores de red, arquitectos, y todos podemos desarrollar y probar las APIs, controladoras, equipos de red y suites de colaboración de Cisco.  Podremos correr nuestro código en infraestructura que se encuentra activa 24/7, en una variedad de laboratorios de acceso libre, y escoger entre entornos virtualizados, simuladores, e infraestructura física. Nos dirigimos al catálogo completo haciendo click en “_View all Sandboxes_”.
![All DevNet Sandboxes](https://i.ibb.co/hH8DkjN/DN-SB-2.png)
![Buscador Sandboxes](https://i.ibb.co/jvBXdxS/DN-SB-3.png)
El catálogo cuenta con 70 _Sandboxes_ distintos. Para filtrar, podemos hacerlo por tipo, por categoría, por status, o simplemente hacer click en la búsqueda, y tipeamos la palabra “**_Meraki_**” para encontrar el que vamos a usar.
![Sandbox Meraki Always-On](https://i.ibb.co/MfcwkGM/DN-SB-4.png)
Encontraremos tres _Sandboxes_ de **_Meraki_**, el que utilizaremos se llama “**_Meraki Always On_**” y se trata de una red de prueba **_Meraki_** a la que podemos acceder en cualquier momento para realizar pruebas. En este _Sandbox_ podemos encontrar los detalles importantes para que el script funcione correctamente. En primer lugar, las credenciales de acceso al Dashboard API, Username: [devnetmeraki@cisco.com](mailto:devnetmeraki@cisco.com), Password: ilovemeraki, y por otro lado, el *API Key* que utilizaremos es 6bec40cf957de430a6f1f2baa056b99a4fac9ea0.

## El script `GetSnap.py`
Nuestro código en ***Python*** va a obtener una captura de la cámara Meraki modelo MV12W, cuyo número serial es el Q2GV-7HEL-HC6C, y se ubica en la red con Id L_566327653141856854 llamada *DNEAlertsNet*. Esta red no la encontraremos dentro de la interfaz del Dashboard API, pero sí estará listada si hacemos las llamadas de **Postman** *Get Organization Id* y *Get Networks Id*, utilizando el *API Key* previamente mencionado. La organización lleva el nombre *DeLab* y su Id es el 681155. Esta cámara ha sido posicionada delante de una TV que se encuentra prendida 24/7, de forma que siempre tiene algo qué mostrar, y su contenido es dinámico.

En primer lugar, debemos especificar las librerías que estaremos utilizando. Estas son *pprint*, *requests* y *json*, las importamos a continuación:
```python
from pprint import pprint
import requests
import json
```
Para obtener una captura de lo registrado en la cámara, debemos hacer uso del *API* de la siguiente forma:
```python
    def setHeaders_meraki():
	    header = {
		    "X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
		    "Accept":"application/json",
		    "Content-Type":"application/json"
		    }
		    return header
	def getSnap(theHeader):
		uri = "https://api.meraki.com/api/v0/networks/L_566327653141856854/cameras/Q2GV-7HEL-HC6C/snapshot?X-Cisco-Meraki-API-Key=6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
		resp = requests.post(uri, headers = theHeader,data={})
		return resp.json()
		
	header = setHeaders_meraki()
	snapshot = getSnap(header)
```
En el código anterior, definimos primero los headers que enviaremos en nuestra llamada al *API* de *Meraki Dashboard*,  a través de la función *setHeaders_meraki*, especificamos el *API Key*, y los parámetros que debe aceptar y devolver nuestra llamada(JSON). Estos parámetros los alimentamos a nuestra función *getSnap*, la cual se encarga de hacer el llamado mediante el método *POST* y devuelve un *JSON* en forma de diccionario que podremos indexar para extraer la URL, `url = snapshot["url"]`.
Para obtener la imagen de la URL, debemos realizar un pequeño artificio:
```python
def get_image(url):
	code = 404
	while code != 200:
		response = requests.get(url)
		code = response.status_code
	return response.content
```
Luego podemos obtener la imagen y asignarla en una variable `image = get_image(url)`. Nuestro código hasta este punto:
```python
from pprint import pprint
import requests
import json

def setHeaders_Meraki():
	header = {
		    "X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
		    "Accept":"application/json",
		    "Content-Type":"application/json"
		    }
		    return header
		    
def getSnap(theHeader):
		uri = "https://api.meraki.com/api/v0/networks/L_566327653141856854/cameras/Q2GV-7HEL-HC6C/snapshot?X-Cisco-Meraki-API-Key=6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
		resp = requests.post(uri, headers = theHeader,data={})
		return resp.json()

def get_image(url):
	code = 404
	while code != 200:
		response = requests.get(url)
		code = response.status_code
	return response.content

header = setHeaders_meraki()
snapshot = getSnap(header)
url = snapshot["url"]
print(40*"-")
print(url)
print(40*"-")
image = get_image(url)
```
### Recapitulemos
Hasta este punto, nuestro código consta de tres funciones. La primera, `setHeaders_Meraki` se encarga de crear un diccionario y asignarlo a la variable header. Este será el *JSON* con el que realizaremos nuestra llamada al *Dashboard API* de *Meraki*. Luego la segunda función, `getSnap`, se encarga de la realización de esta llamada, utilizando el método *POST* del módulo `requests` y de esta forma recibe otro *JSON* como respuesta. Este *JSON* lo almacenamos en forma de diccionario en la variable `snapshot`, y lo indexamos para obtener la URL de la imagen, mediante `url = snapshot["url"]`. Finalmente, la tercera función se encarga de buscar la imagen en la URL mediante el método *GET* y guarda el contenido en la variable `image`.

Habiendo obtenido la imagen, procedemos a enviarla a un software de reconocimiento de imágenes llamado *Imagga*. Esto lo haremos a través de su *API*, para lo cual es necesario crearnos una cuenta. Ingresamos a la dirección [http://imagga.com/](http://imagga.com/)
![SignUp Imagga](https://i.ibb.co/xGz65vT/IG-SU-1.png)
Procedemos a llenar el formulario con los datos apropiados, para este caso de uso sólo es necesario una cuenta gratuita.
![SignUp Imagga Form](https://i.ibb.co/F408zdG/IG-SU-2.png)
Con esto ya podemos acceder al [Dashboard de Imagga](https://imagga.com/profile/dashboard) y aquí encontraremos el *API Key* y *API Secret* necesarios para realizar el reconocimiento de la imagen.
![Imagga API Keys](https://i.ibb.co/gPwMJcx/IG-SU-3.png)
Habiendo obtenido estos parámetros, podemos proceder a realizar el reconocimiento de la imagen. Para esto definiremos las variables `imagga_url`, `api_key` y `api_secret`, y una función llamada `analyze` que se encarga de realizar la llamada mediante el método *POST* y asignarlo a una variable llamada `response`:
```python
imagga_url = 'https://api.imagga.com/v2/tags'
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

def analyze(url, image, key, secret):
	response = requests.post(
		url,
		auth=(key, secret),
		files={'image':image})
	return response

response = analyze(imagga_url, image, api_key, api_secret)
```
Luego podemos indexar las etiquetas de reconocimiento y asignarlo a una variable de la siguiente manera:
`tags = [item['tag']['en'] for item in response.json()['result']['tags']]`
De esta manera, obtenemos una lista ordenada con las etiquetas, que procedemos a transformar en un *string*. Para esto es necesario crear una última función que convierta una lista a un string y acorte la lista luego de cierta cantidad de caracteres sin dejar palabras cortadas o comas flotantes, y lo asignamos a la variable `speech`:
```python
def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 = str1 + ele + ","
    # cut string without leaving floating characters or slashed words
    str1 = str1[:415]
    while(str1[-1]!=','):
        str1 = str1[:-1]
    str1 = str1[:-1]
    # return string   
    return str1
	
speech = listToString(tags)
```
### Recapitulemos
Hasta este punto, nuestro código obtiene una imagen de la siguiente manera: la función `setHeaders_Meraki`, se encarga de crear un diccionario(*JSON*) y asignarlo a la variable header. Con este *JSON* realizamos una llamada al *Dashboard API* de *Meraki*. Luego la segunda función, `getSnap`, se encarga de realizar esta llamada, utilizando el método *POST* del módulo `requests` y de esta forma recibe otro *JSON* como respuesta. Este *JSON* lo almacenamos en forma de diccionario en la variable `snapshot`, y lo indexamos para obtener la URL de la imagen, mediante `url = snapshot["url"]`. La tercera función, `get_image` se encarga de buscar la imagen en la URL mediante el método *GET* y guarda el contenido en la variable `image`. 
Habiendo conseguido esta imagen, realizamos el análisis apalancando la *API* de *Imagga*. Para esto hemos obtenido un *API_Key* y un *API_Secret* en la web de [*Imagga*](https://imagga.com/), y creamos una función llamada `analyze`, que toma estos parámetros, además de utilizar un endpoint especificado por *Imagga*. Nos devuelve un nuevo *JSON* con la clasificación que realizado de nuestra imagen. Finalmente, la función `listToString` se encarga de convertir la lista de etiquetas que hemos obtenido, en un *String* que podrá enunciar el Asistente de nuestro dispositivo Android. Nuestro código hasta esta etapa es el siguiente:
```python
from pprint import pprint
import requests
import json

#Vars
imagga_url = 'https://api.imagga.com/v2/tags'
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

#Helper functions
def setHeaders_meraki():
	header = {
		"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
		"Accept": "application/json",
		"Content-Type":"application/json"
	}
	return header

def getSnap(theHeader):
	uri = "https://api.meraki.com/api/v0/networks/L_566327653141856854/cameras/Q2GV-7HEL-HC6C/snapshot?X-Cisco-Meraki-API-Key=6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    resp = requests.post(uri, headers = theHeader,data={})
    return resp.json()

def get_image(url):
    code = 404
    while code != 200:
        response = requests.get(url)
        code = response.status_code
    return response.content

def analyze(url, image, key, secret):
    response = requests.post(
        url,
        auth=(key, secret),
        files={'image': image})
    return response

def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 = str1 + ele + ","
    str1 = str1[:415]
    while(str1[-1]!=','):
        str1 = str1[:-1]
    str1 = str1[:-1]
    # return string   
    return str1
    
# Main function
def main():
    header = setHeaders_meraki()
    snapshot = getSnap(header)
    url = snapshot["url"]
    print(40*"-")
    print(url)
    print(40*"-")
    image = get_image(url)
    response = analyze(imagga_url, image, api_key, api_secret)
    pprint(response.json(), indent=2, width=200)
    print(40*"-")
    tags = [item['tag']['en'] for item in response.json()['result']['tags']]
    speech = listToString(tags)
    return (speech, url)

if __name__ == '__main__':
	main()
```
Hasta este punto en nuestro desarrollo, hemos creado un código en *Python* que se encarga de obtener una captura en una cámara Meraki, obtener la imagen que se encuentra en esta URL, y enviarla a un software de reconocimiento de imágenes llamado *Imagga*. Esto lo realiza nuestra función principal llamada `Main`.¡Fantástico! Si han llegado hasta este punto, lo han hecho muy bien. Sin embargo, ahora deseamos poder apalancar esta funcionalidad desde nuestro Asistente de Android, llamado *Google Assistant*. Para lograr esto, será necesario correr un servidor *Flask* haciendo uso de una librería en particular llamada *Flask Assistant* la cual permite la comunicación con asistentes de voz como es *Google Assistant* o *Alexa Skills* por nombrar algunos ejemplos. Este servidor web debemos almacenarlo en un lugar de acceso público en internet, de manera que el *API* de *Google Actions* pueda acceder a él, y para esto utilizaremos *Heroku*. Para crear este servidor, importaremos el script `GetSnap.py`,  por lo que vamos a renombrar la función principal y eliminar las últimas dos líneas del código. Se vería de la siguiente forma (notar que el resto del código se ha omitido y colocado tres puntos "..." para enfocarnos en la parte clave que estamos modificando):
```python
...
	return str1

# return speech function
def return_speech():
    header = setHeaders_meraki()
    snapshot = getSnap(header)
    url = snapshot["url"]
    print(40*"-")
    print(url)
    print(40*"-")
    image = get_image(url)
    response = analyze(imagga_url, image, api_key, api_secret)
    pprint(response.json(), indent=2, width=200)
    print(40*"-")
    tags = [item['tag']['en'] for item in response.json()['result']['tags']]
    speech = listToString(tags)
    return (speech, url)
```
De esta forma, podemos importar el archivo `GetSnap.py` como un módulo en nuestro servidor web *Flask*, y utilizar todas sus funcionalidades. Este nos devuelve una tupla con las etiquetas de categorización en formato *String* y el URL de la imagen.

---
**Nota:**
Es importante que el archivo o fichero `GetSnap.py` se encuentre en el mismo directorio que nuestro servidor web.
---


## El script app.py
Nuestro código debe importar la funcionalidad del script `GetSnap.py` y servirlo desde un *web server* a través de rutas especificadas. Primero es necesario importar las librerías necesarias, y el script previamente mencionado:
```python
from flask import Flask
from flask_assistant import Assistant, tell
from flask_cors import CORS
import GetSnap
``` 
La librería *Flask* nos permite la creación del servidor web en forma local. Por otro lado, la librería *Flask Assistant* habilita el uso de asistentes como *Google Assistant* o *Alexa Skills*, en particular utilizaremos el módulo *tell* que nos devolverá la respuesta en forma enunciada. Adicionalmente, importamos *Flask CORS* que habilita el intercambio de recursos de distintos orígenes. Finalmente, importamos el script `GetSnap.py` que creamos previamente que contiene la lógica para obtener la imagen de la captura y realizar el reconocimiento.
Ahora es necesario crear el aplicativo que se encontrará en el *web server*, mediante la línea de código `app = Flask(__name__)`. Lo configuramos para *Google Actions* con `app.config['ASSIST_ACTIONS_ON_GOOGLE'] = True` y `app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']`.  Inicializamos la extensión de *Flask-Cors* con los argumentos por defecto que permite el *CORS* para todos los dominios, en todas las rutas, `cors = CORS(app)`. Inicializamos un objeto de tipo *Assistant* utilizando el *Flask app*, y la ruta a la URL de nuestro *webhook*, `assist = Assistant(app, route='/google')`.
A continuación creamos nuestras rutas: 
- La primera será para propósitos de debugging cuando hacemos una llamada de tipo *GET* al servidor, nos devuelve un mensaje de prueba como "Eureka".
```python
@app.route("/", methods=['GET'])
def main():
	return "Eureka"
```
- La segunda es la principal, utilizaremos el decorador *action* para mapear nuestro *intent* o propósito llamado "*tv-watch*", a la función apropiada. El decorador acepta el nombre de nuestro propósito como parámetro, y hace la función de visor de nuestra acción, cuando recibimos el pedido de *Dialogflow*. La función de acción devolverá un *tell* como respuesta enunciada,  
```python
@assist.action('tv-watch')
def google_tv_watch():
	speech,url = GetSnap.return_speech()
	return tell("I see " + speech[:415]).card(
		text="See...",
		title="Image:",
		img_url=url
	)
```
Hacemos uso de una tarjeta para presentar la información, mostrando las etiquetas como texto, un título y la imagen analizada.
Esta será nuestra función principal, y será un *web server* que se engargue de servir los recursos llamados mediante los *requests* realizados desde el *Google Assistant* a través de *Dialogflow*. Es por esto que incluímos una última línea de código 
```python
if __name__ == '__main__':
	app.run(threaded=True, port=5000)
```
Es decir, nuestro aplicativo estará habilitado para utilizar hilos, y se encontrará disponible en el puerto 5000.
### Recapitulemos
Hasta este punto, nuestro código obtiene la imagen de una cámara *Meraki Vision* utilizando el *Dashboard API* y realiza un análisis mediante el API de *Imagga*, un software de reconocimiento de imágenes. Obtiene el url de la imagen, y las etiquetas del análisis y lo asigna a una tupla que será enunciada y mostrada utilizando un servidor web de *Flask* que utiliza la librería *Flask Assistant*. Sin embargo, para que podamos realizar llamadas a nuestro servidor web, será necesario que este se encuentre en una dirección pública. Mientras nos encontremos en estado de prueba, podemos hacer uso de algún servicio de *tunneling* como *Ngrok*, para exponer nuestro aplicativo a la web. En este caso en particular, utilizaremos *Heroku* que ofrece la opción de guardar nuestro aplicativo en la nube, con una dirección pública a la cual nuestro *webhook* de *Dialogflow* puede acceder para hacer las llamadas correspondientes.
Nuestro script **app.py** hasta este punto es el siguiente:
```python
from flask import Flask
from flask_assistant import Assistant, tell
from flask_cors import CORS
import GetSnap

app = Flask(__name__)

app.config['ASSIST_ACTIONS_ON_GOOGLE'] = True
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']

cors = CORS(app)
assist = Assistant(app, route='/google')


@app.route("/", methods=['GET'])
def main():
    return "Eureka"

@assist.action('tv-watch')
def google_tv_watch():
    speech,url = GetSnap.return_speech()
    return tell("I see " + speech[:415]).card(
        text="See...",
        title="Image:",
        img_url=url
    )

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
```
## Debemos subir nuestro proyecto a Heroku
Nuestro *web server* actualmente corre desde nuestro *Local Host*. Esto para probar que nuestro código funciona, está muy bien. Sin embargo, para que podamos activarlo mediante el *Google Assistant*, será necesario que se encuentre expuesto desde una dirección pública. Aquí será muy útil el uso de *Heroku*, una plataforma basada en nube que soporta diversos lenguajes de programación y se utiliza mediante *Git*.
En primer lugar, nos dirijmos a [Heroku](https://www.heroku.com/), y nos registramos si no contamos con una cuenta.
![Heroku Landing](https://i.ibb.co/5szqf5S/HK-SU-1.png)
Ingresamos nuestra información... Luego damos click en crear cuenta.
![Heroku SignUp](https://i.ibb.co/K0KVy3t/HK-SU-2.png)
Posteriormente, es necesario validar nuestra cuenta desde nuestro correo.
![ConfirmHerkouAccount](https://i.ibb.co/vZrHp5C/HK-SU-3.png)
Y finalmente, crear una contraseña.
![CreatePasswordHerokuAccount](https://i.ibb.co/SrXyFrb/HK-SU-4.png)
*Heroku* funciona a través de la línea de comandos *Heroku CLI*, es por esto que es importante haber instalado el ***Git Bash*** pues es ahí donde correremos los comandos.
Debemos ingresar a [*Heroku Set up*](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) y elegir la descarga apropiada para nuestra plataforma (Windows, macOS, o Ubuntu). Habiendo instalado el *Heroku CLI*, ingresamos el comando `heroku login` y aparece un prompt en el que ingresamos cualquier tecla (excepto "q" que saldrá) para ser redireccionados al navegador ([Heroku Login](https://cli-auth.heroku.com/auth/browser/)) en el que debemos autenticarnos con las credenciales previamente generadas. Es necesario este paso para que funcionen correctamente los comandos `heroku`y `git`.
Habiendo instalado y configurado apropiadamente el *Heroku CLI*, debemos crear nuestro repositorio de *GitHub* y vincularlo con nuestro directorio local. 
En primer lugar creamos nuestro repositorio desde [GitHub](https://github.com/).
![GitHubRepoCreate](https://i.ibb.co/MCNbBjp/GH-R-1.png)
Le damos un nombre al repositorio, y lo creamos.
![GitHubRepoCreation](https://i.ibb.co/6tQbTzP/GH-R-2.png)
Luego accedemos a nuestro directorio local desde el *Git Bash*, y ejecutamos los comandos para subir nuestro proyecto.

 1. Inicializar el directorio local como un repositorio de Git
```git
$ git init
```
 2. Agregar los archivos de nuestro nuevo repositorio local. Esto lo añadimos al área de ensayo, para el primer *commit*.
```git
$ git add .
```
 3. Realizamos el commit de los archivos que hemos añadido al área de ensayo en nuestro repositorio local.
```git
$ git commit -m "Primer commit"
```
 4. En la sección superior de la página de GitHub que acabamos de crear aparecerá la URL del repositorio remoto.
 ![GitHubRepoLink](https://ibb.co/D45pkBZ)
 5. En la línea de comando, agregamos el URL para el repositorio remoto, desde nuestro repositorio local.
```git
$ git remote add origin <URL repositorio remoto>
# Este comando configura el nuevo URL remoto
$ git remote -v
# Este comando verifica el nuevo URL remoto
```
 6. Finalmente, publicamos nuestro proyecto al repositorio de GitHub.
```git
$ git push origin master
```
Ahora finalmente pasamos a desplegar nuestro aplicativo en Heroku, debemos ejecutar los siguientes comandos:
```git
$ heroku create
# Este comando crea el app
$ git push heroku master
# Este comando despliega nuestro proyecto al app que hemos creado
$ heroku ps:scale web=1
# Este comando asegura que al menos una instancia del aplicativo esté corriendo
$ heroku open
# Si todo ha salido bien hasta este punto, deberíamos ver una página que dice "Eureka"
$ heroku logs --tail
# Este comando nos permitirá ver los logs y hacer debugging y troubleshooting luego de desplegar la app.
```

## Conectar con Dialogflow

Una vez que hemos subido nuestro código a Heroku, ya tenemos una dirección pública a la cual podemos 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc4ODM5OTE1NCwtMTEwODYyNzUyOSwxMD
Q1MTM0ODc5LC0xNDc4MjE2OTEsLTk0NTQ5MzgzMSw3MDQ0MTgz
MjYsMTY3MzMyMzcxMywtMjkxMzc0NDI0LC0xMjYyMzE1MzIzLD
g3NzI2MTIzLC01MDQxMDk2NjksLTY4MzUzMTAyMSwxMTg5NTE5
OTE0LDE4NTgwNzEwMTEsNzE4MjAwMDY4LDE3ODEwNjAzMTMsMT
E1MzUyNDkwOSwtMTM3NTg3MDI3MywtMTcwOTM5MzkyOCw4MTE2
MzcxNzddfQ==
-->