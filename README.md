# JSON to SRT

###### Github said miniature-potato, I loved it and here we are. // Github dijo "miniature-potato", lo amé y aquí estamos.

<div align="center"><img src="https://github.com/NovaFugaz/miniature-potato/assets/124105557/02aca929-7142-4415-bee3-e6eea20c0ebb"</img></div>


##### A little script that reads spotify's synced lyrics' JSON data and converts it to an SRT file. // Un pequeño script que lee las letras sincronizadas de un JSON de spotify y lo convierte a un archivo SRT.

### What does this little thing do? // ¿Qué hace esta pequeña cosa?

This little thing converts the lyrics synced data that I can't manage to learn how to scrape from Spotify and then creates a SRT file. However, it still can, pretty much, access the data and get it so it can perform its little task. There are two ways you can get this data as it's not available via API.

Esta cosita convierte la información de las letras sincronizadas que no pude aprender a conseguir a la mala de spotify y crea un archivo SRT. Sin embargo, igual accesa a la información para hacer su tarea, aunque ahora es un 15% más engorroso. Hay dos formas de conseguirlo, porque no está disponible via spotify's official API.

I will learn how to do this through the other way, just pasting spotify's song link, because I know I can do it, [but it is not this day](https://y.yarn.co/a4afb7c0-9e46-4264-a9c6-b21bb885a02c.mp4). 

Voy a aprender cómo hacer esto de la otra forma, con solo pegar el enlace a la canción de spotify, porque sé que puedo hacerlo, [pero hoy no es ese día](https://y.yarn.co/a4afb7c0-9e46-4264-a9c6-b21bb885a02c.mp4). 

### Why? // ¿Por qué?

Because why not? That's why.
To be honest, I really wanted to simplify my translation work.

Porque por qué no. Por eso.
Para ser honesta, quería simplificar mi proceso de traducción.

### Usage // Funcionamiento

- You need to go to open.spotify.com. If you had lyrics opened, close it and reload.
- Ve a open.spotify.com. Si tenías letras ya abiertas, ciérrala y recarga la página.

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/72e92ce3-2f05-4f42-aabc-d07279899798)


 
- Press F12 to open devepoler tools and press "Network" tab. 
- Pulsa F12 para abrir las herramientas del desarrollador y anda a la pestaña "Red/Network"

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/94b759b5-f70b-4c61-9491-329420873091)



- Filter the responses writing "color". This is very important or you're going to have A LOT of responses and you will not find the one needed.
- Filtra las respuestas de la pestaña red escribiendo "color". Es importante, porque sino la cantidad que va a salir va a ser enorme y no vas a pillar la que necesitas. 

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/a392b879-7c47-48a2-83d6-d3b234b00ec5)



- Press the mic button to open the lyrics, now you'll have a few specific responses. The way it works is loading the song you're actually listening and preload the next one. In my case with this specific playlist, it's Placebo's The Bitter End (red) and Open Hand's Time to Talk (blue). You can "preview" the response to be sure you chose the right one you need by clicking "response" tab.
- Pulsa el botón de micrófono para abrir las letras y aparecerán unas respuestas específicas. Funciona así: carga la letra de la canción que estás escuchando ahora y la que sigue en la lista (en mi caso, en rojo: The Bitter End de Placebo y Time to Talk de Open Hand en azul). Puedes previsualizar la respuesta para asegurarte que escoges la que necesitas clicando la pestaña "respuesta".

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/d76f3c3b-893f-47cd-9327-817d0236e8a9)


- Now, copy JSON data. We have two ways. Either you open the response into a new tab and copy it or you rightclick the response data and select copy -> copy response. 
- Ahora copia los datos del JSON. Tenemos dos formas. O abres la respuesta en una pestaña nueva y copias la información seleccionando copy -> copy response. 


![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/b5643ba8-0cad-43db-aad5-0f12f87b50c3)

Si elegiste abrir pestaña, tienes que copiar todo esto.
![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/47eda585-dc2d-4811-beec-2f8b98f6c3d5)

- Now open CMD/Console and run this script (use python before the filepath if you're using Windows like I'm sadly doing), and press enter. You'll be prompted to paste your JSON data.
- Ahora abre una CMD o consola y corre este script (usa python antes del archivo si usas Windows como tristemente hago yo). Pulsa Enter y se te pedirá que ingreses el dato del JSON.

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/699f3ab0-cecc-4653-bbb7-b67594ca426f)


- Now you'll be asked to name the SRT file with the info you just gave. After that, the script will prompt a successfully done and it will close.
- Luego, se te pedirá que des nombre al archivo SRT que contendrá los datos que acabas de dar. Luego el script dirá que se ha creado exitosamente y se cerrará.

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/7b1deb5c-c81d-4112-999a-988214015ad9)

- The file will be in the folder you've run the script or the root directory. As mine was C:\Users\Nacchi there it is.
- El archivo estará en la carpeta desde la que corriste el archivo o en el directorio raíz. Como mi script partía de C:\Users\Nacchi ahí está.

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/b4c426dc-7aff-41ba-9eee-0ef771797dd1)

##### Opening the file will reveal its contents:

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/623822e0-eaf4-440d-886c-18a1d0665e45)


### Mini Translation of the prompts overadapted for english-speaking users (to avoid skill issues):

- Ingrese el contenido JSON // Paste your JSON here
- Ingrese el nombre del archivo SRT para guardar (sin la extensión .srt) // Insert SRT filename to save (without extension).
- El archivo SRT ha sido generado exitosamente. // SRT file generated successfully.

### Badges for badges sake

![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/084e643e-24b7-4b84-9847-9f7b61e4f8a1) ![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/81e3c897-6d0d-49eb-9fd1-a0472a24a88a) ![image](https://github.com/NovaFugaz/miniature-potato/assets/124105557/5b76bcaf-1aa3-479a-acdc-6b3a6c3475bc)

### Agradecimientos

A Yuki, Gabi, Fran Pika y Lily.
