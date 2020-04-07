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
 - Cuenta de ***Imagga*** para contar con un *api_key* y *api_secret* y enviar imágenes a reconocer.
 - Cuenta de ***Heroku*** para acceder a nuestro código de ***Python*** desde una URL pública
 - Cuenta de ***Google*** para acceder a ***DialogFlow***

## Acerca de Cisco Meraki

***Cisco Meraki*** es la solución de red gestionada en nube de **Cisco**. Ofrece un portafolio de productos de infraestructura de red que incluye Access points, Enterprise switches, routers, dispositivos de seguridad de red e incluso cámaras. Su versátil modelo de gestión basado en nube permite administrar la topología desde cualquier lugar del mundo, y provisionar equipos con tan solo una conexión a internet, y una fuente de poder.

## Utilizar el ***SandBox Meraki Always-On***

***DevNet*** nos provee muchos SandBoxes. Estos son entornos virtuales que emulan equipos físicos o redes donde podemos aprender a realizar configuraciones como la que intentamos efectuar. En este caso en particular, haremos uso del ***SandBox Meraki Always On*** que nos permite acceder a una cámara de ***Cisco Meraki*** en caso no contemos con una para realizar el laboratorio. Esta cámara en particular, se encuentra apuntando a una TV que se encuentra prendida 24/7. Nos dirigimos a la página principal de ***DevNet*** y navegamos a _Discover_ --> _**Code**_ --> _Sandbox Remote Labs_ donde encontraremos más información acerca de los _Sandboxes_. Encontramos información sobre cómo utilizarlos, si se trata de un _Sandbox_ que siempre se encuentra activo, o si es necesario reservarlo por cierta cantidad de tiempo, caso en el que además debemos esperar unos minutos para que _DevNet_ prepare los recursos que utilizaremos. Es importante mencionar que todos los recursos que encontraremos en ***DevNet*** son totalmente libres para los miembros de nuestra comunidad. Para acceder, debemos crearnos una cuenta, o utilizar nuestro ***Cisco ID*** en caso ya contemos con uno. Los alumnos de ***Cisco Networking Academy*** tienen una pre-cuenta de _DevNet_ utilizando sus credenciales NetAcad.

![DevNet Sandbox](https://i.ibb.co/T2FpjXt/DN-SB.png)
Aquí encontraremos la respuesta a muchas preguntas acerca de estos entornos virtuales, donde desarrolladores, ingenieros, administradores de red, arquitectos, y todos podemos desarrollar y probar las APIs, controladoras, equipos de red y suites de colaboración de Cisco.  Podremos correr nuestro código en infraestructura que se encuentra activa 24/7, en una variedad de laboratorios de acceso libre, y escoger entre entornos virtualizados, simuladores, e infraestructura física. Nos dirigimos al catálogo completo haciendo click en “_View all Sandboxes_”.
![All DevNet Sandboxes](https://i.ibb.co/xHCnR3f/DN-SB-2.png)
![Buscador Sandboxes](https://i.ibb.co/sbhg02K/DN-SB-3.png)
El catálogo cuenta con 70 _Sandboxes_ distintos. Para filtrar, podemos hacerlo por tipo, por categoría, por status, o simplemente hacer click en la búsqueda, y tipeamos la palabra “**_Meraki_**” para encontrar el que vamos a usar.
![Sandbox Meraki Always-On](https://i.ibb.co/cK9pxQG/DN-SB-4.png)
Encontraremos tres _Sandboxes_ de **_Meraki_**, el que utilizaremos se llama “**_Meraki Always On_**” y se trata de una red de prueba **_Meraki_** a la que podemos acceder en cualquier momento para realizar pruebas. En este _Sandbox_ podemos encontrar los detalles importantes para que el script funcione correctamente. En primer lugar, las credenciales de acceso al Dashboard API, Username: [devnetmeraki@cisco.com](mailto:devnetmeraki@cisco.com), Password: ilovemeraki, y por otro lado, el *API Key* que utilizaremos es 6bec40cf957de430a6f1f2baa056b99a4fac9ea0.

## El archivo GetSnap en ***Python***

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


## Rename a file

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

## Delete a file

You can delete the current file by clicking the **Remove** button in the file explorer. The file will be moved into the **Trash** folder and automatically deleted after 7 days of inactivity.

## Export a file

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# Synchronization

Synchronization is one of the biggest features of StackEdit. It enables you to synchronize any file in your workspace with other files stored in your **Google Drive**, your **Dropbox** and your **GitHub** accounts. This allows you to keep writing on other devices, collaborate with people you share the file with, integrate easily into your workflow... The synchronization mechanism takes place every minute in the background, downloading, merging, and uploading file modifications.

There are two types of synchronization and they can complement each other:

- The workspace synchronization will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.
	> To start syncing your workspace, just sign in with Google in the menu.

- The file synchronization will keep one file of the workspace synced with one or multiple files in **Google Drive**, **Dropbox** or **GitHub**.
	> Before starting to sync files, you must link an account in the **Synchronize** sub-menu.

## Open a file

You can open a file from **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Open from**. Once opened in the workspace, any modification in the file will be automatically synced.

## Save a file

You can save any file of the workspace to **Google Drive**, **Dropbox** or **GitHub** by opening the **Synchronize** sub-menu and clicking **Save on**. Even if a file in the workspace is already synced, you can save it to another location. StackEdit can sync one file with multiple locations and accounts.

## Synchronize a file

Once your file is linked to a synchronized location, StackEdit will periodically synchronize it by downloading/uploading any modification. A merge will be performed if necessary and conflicts will be resolved.

If you just have modified your file and you want to force syncing, click the **Synchronize now** button in the navigation bar.

> **Note:** The **Synchronize now** button is disabled if you have no file to synchronize.

## Manage file synchronization

Since one file can be synced with multiple locations, you can list and manage synchronized locations by clicking **File synchronization** in the **Synchronize** sub-menu. This allows you to list and remove synchronized locations that are linked to your file.


# Publication

Publishing in StackEdit makes it simple for you to publish online your files. Once you're happy with a file, you can publish it to different hosting platforms like **Blogger**, **Dropbox**, **Gist**, **GitHub**, **Google Drive**, **WordPress** and **Zendesk**. With [Handlebars templates](http://handlebarsjs.com/), you have full control over what you export.

> Before starting to publish, you must link an account in the **Publish** sub-menu.

## Publish a File

You can publish your file by opening the **Publish** sub-menu and by clicking **Publish to**. For some locations, you can choose between the following formats:

- Markdown: publish the Markdown text on a website that can interpret it (**GitHub** for instance),
- HTML: publish the file converted to HTML via a Handlebars template (on a blog for example).

## Update a publication

After publishing, StackEdit keeps your file linked to that publication which makes it easy for you to re-publish it. Once you have modified your file and you want to update your publication, click on the **Publish now** button in the navigation bar.

> **Note:** The **Publish now** button is disabled if your file has not been published yet.

## Manage file publication

Since one file can be published to multiple locations, you can list and manage publish locations by clicking **File publication** in the **Publish** sub-menu. This allows you to list and remove publication locations that are linked to your file.


# Markdown extensions

StackEdit extends the standard Markdown syntax by adding extra **Markdown extensions**, providing you with some nice features.

> **ProTip:** You can disable any **Markdown extension** in the **File properties** dialog.


## SmartyPants

SmartyPants converts ASCII punctuation characters into "smart" typographic punctuation HTML entities. For example:

|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDkxNTAyMzM0LC0xNzg5OTY0MzAwLDI4Nz
QzNTQ2NSwtMzIwNjEyNDk0LDE5ODMwNTIyNDksNjgyNzc0ODEx
LC0zMDA4Njg3NzIsMTg2NjIxMzIwNSwtMTkwNDU4NTc2NiwtND
A2OTcyMDMxLC05OTU0MjYwMjMsMjI5MzkyNzUsMTQ4OTYyMzc5
OCwzNjUzNDAxOTgsMTk1ODg4MzM0N119
-->