## AMAZON SCRAPPING

Con este pequeño programa, nuestro objetivo es extraer una serie de información de la web de amazon para poder utilizarla mas adelante
en diferentes tipos de análisis. 
El funcionamiento es relativamente sencillo y el código esta debidamente documentado.

Prodecedemos a explicar los pasos a seguir para su utilización:

- 1º Necesitamos el controlador Chromedriver.exe de Selenium que facilito en el repositorio ( en mi caso es para Windows 10 )
     Si el obtenemos un mensaje de error de versiones, bien puede ser porque el sistema operativo es distinto o porque
     necesitamos una version mas reciente. La version que facilito es: ( ChromeDriver 106.0.5249.61 )
     Aqui dejo el link por si necesitan cambiar el controlador -->  https://chromedriver.chromium.org/downloads
  
  - 2º Una vez tenemos instalado el controlador, debemos instalar la libreria --> pip install selenium
       Esto nos dara acceso a todas las funcionalidades para interactuar con Google Chrome.
       Aparte de los propios de las librerias necesitaremos un par de librerias mas que estan pre-instaladas por defecto como pathlib o json.
  
  - 3º Cuando ejecutemos el código, nos pedira un input, que es el objeto que deseamos buscar (iphone 14, bicicleta electrica, etc...)
       Una vez introducido, el código extrae todas las url de las páginas disponibles en amazon con dichos criterios de busqueda, y nos extrae 
       en este caso, el titulo, precio, imagen y link de cada artículo. 
      
     
  - 4º  Esta informacion es agregada a un fichero JSON.
        El fichero se crea la primera vez, y despues va a añadiendo cada búsqueda debajo de la úlitma.
        
  PD --> Si desea cambiar cualquier forma de almacenamiento, o de interacción con la página web, sientase libre de probar.
         Existe mucha documentación y se puede replicar para cualquier tipo de pagina web ( Booking, GoogleFligths, páginas deportivas...)
         
  Espero que lo disfrutes.
  
  Un saludo.
  Juanjo.
     
     



