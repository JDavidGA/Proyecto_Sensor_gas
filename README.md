SENSOR DE SONIDO

MATERIALES: 
•	SENSOR DE SONIDO: Este nos ayuda a captar los sonidos (es una de las cosas primordiales)


![image](https://user-images.githubusercontent.com/87454368/139084797-65bbf293-e133-4b4e-b591-22f30311beb4.png)


•	PROTOBOARD: Es la placa de prueba en la que se puede insertar las cosas que vamos a usar. Como los cables, sensor, la placa ESP32 y el cable USB 

![image](https://user-images.githubusercontent.com/87454368/139084966-d053e1d7-bb13-46e0-a9e6-af9166c1cc0a.png)


•	ESP32: Esta tiene consumo de energía, con tecnología Wi-Fi y Bluetooth y también un procesador integrado con interfaces para conectarse con varios periféricos.

![image](https://user-images.githubusercontent.com/87454368/139086563-0cfe5655-fd08-4bbb-b5be-e6c67b04c723.png)
 
•	CABLES ELECTRICOS: Estos estan construidos por uno o mas hilos los cuales pueden ser de cobre o aluminio, tiene un aislamiento que recubre el conductor,0020mediante el mismo se evita que la corriente se escape del cable y tiene una cubierta que se encarga de proteger al cable de la intemperie y elementos externos.
 
 ![image](https://user-images.githubusercontent.com/87454368/139086478-d87a4517-001f-4cb8-a75b-38f325c1b82f.png)

•	CABLE USB: Es el conector que permite vincular diferentes elementos a través del Universal Serial.
 
![image](https://user-images.githubusercontent.com/87454368/139086265-707f25ea-6d10-46ba-9f93-9b1aa692a6de.png)

Y ya con todos estos materiales por ultimo tendremos este circuito armado de esta manera: 

![image](https://user-images.githubusercontent.com/87454368/139085711-dac9899e-5758-4e36-b001-d9788ccd3984.png)

![image](https://user-images.githubusercontent.com/87454368/139085757-2d3e68f1-92c0-42df-a571-593f77f6033a.png)

Acá en esta imagen podemos ver que usamos solamente 3 cables, usamos uno de color azul que es el de la energía, uno marrón que es el de la 
tierra y uno verde que está conectado al PIN32

CODIGO

![image](https://user-images.githubusercontent.com/87454368/139086874-6613b8d3-de82-4238-be4e-330147477bca.png)

![image](https://user-images.githubusercontent.com/87454368/139086918-02f6b1d7-ffe7-470d-bcbc-09a7918bca9b.png)

![image](https://user-images.githubusercontent.com/87454368/139086940-0a7b2c71-b79a-4ffb-a263-112433afa316.png)

En las imágenes podemos notar que el código que usamos para esto no es tan extenso, usamos un código un poco básico y también hay uso de IFTTT.
Podemos ver que de la línea del 1 al 4, entre estas se importa las librerías con las funciones.
De la 7 a la 16 lo que hace entre estas es tener la lectura para detectar los datos del sensor y así cumpla su función.
Entre la línea 18 a la 36 entra el uso del IFTTT, acá nos conectamos con la red WIFI como lo podemos notar para así poder conectar los datos con IFTTT.
Y por último de la línea 38 a la 39 se finaliza el código con while (True):
Time.sleep (4)

