# 🌎 GlobalTaste — Recetario Internacional

Este proyecto es una página web llamada **GlobalTaste**, donde se pueden ver recetas típicas de distintos países del mundo.  
Está pensada para mostrar platos internacionales de forma visual y ordenada, con imágenes, descripciones e información básica de cada receta.



## Descripción del proyecto

La pagina home cntiene una barra de menu, con Inicio y Favoritos, seguido de un header con el titulo principal, continuando con una selección de banderas de países del mundo,
de los cuales los que tienen funcionalidad son Perú e Italia. Continuando con el home tambien tenemos una selección de las recetas mas populares de la página , cada una con su
boton de "ver receta", descripción básica, y una etiqueta en cada una encasilladolas en "Clásica", "Sin GLuten" o "Vegetariana". La unica receta de populares con funcionalidad 
es el ceviche Peruano ya que es la misma que la de la página de Perú. 
Ya entrando en peru.html nos encontramos con un dato sobre su gastronomía, una portada y 12 recetas, con las mismas funcionalidades que las de populares, teniendo en cuenta que 
el unico "Ver mas" funcioinal es el de la primera receta , el ceviche peruano, entrando en recetaPeru.html, con una portada tambien , los ingredientes y los pasos para realizarla además de unos tips. Exactamente igual que esto también hemos implementado italia.html y recetaItalia.html (la pasta alla Carbonara), conectados todos estos a styles.css (a diferencia de home y favoritos que tienen los suyos propios) . Tambien tenemos favoritos.html y favorites.js cuya funcionalidad es guardar las recetas a las que se le de en el boton del corazon , cuyo interior se rellenará para confirmar el guardado, todas las recetas lo tienen.


## Tecnologías utilizadas

- **HTML5** → estructura de las páginas.  
- **CSS3** → diseño, colores, fuentes y maquetación.  
- **JavaScript** → para añadir la función de favoritos.  



## Estructura de carpetas

actividad1.3/
│
├── css/
│ ├── favorites.css
│ ├── home.css
│ └── styles.css
│
├── js/
│ └── favorites.js
│
├── img/
│ └── logo.png ( e imágenes de las banderas)
│
├── imgCom/
│ └── ... (imágenes de la seccion Populares)
│
├── imgGui/
│ └── ... ( imágenes de recetas de Perú)
│
├── imgItalia/
│ └── ... (imágenes de recetas de Italia)
│
├── favoritos.html
├── home.html
├── italia.html
├── peru.html
├── recetaItalia.html
├── recetaPeru.html
└── README.md



## ⚙️ Cómo se usa

1. Abre el archivo **`home.html`** en el navegador.  
2. Elige un país y explora sus recetas.  
3. Puedes ver los ingredientes y pasos en cada receta.  
4. Si lo deseas, puedes marcar recetas como favoritas (función añadida con JavaScript).  




## Funcionalidad adicional

Aunque no formaba parte del objetivo principal, se añadió una función extra en JavaScript para permitir que el usuario guardara recetas como favoritas.  
Esta parte guarda los datos en el propio navegador mediante `localStorage`, y los corazones se actualizan entre las páginas. Por ejemplo la Causa Limeña estando tanto en home.html como en peru.html teniendo el mismo nombre si guardas o borras una de favoritos cuenta como si las 2 fuesen la misma, ya que se guardan las recetas en el js por su nombre.
El archivo encargado de esto es **`js/favorites.js`**.



## Autoras

Proyecto realizado por Alexandra Lorena Candrea y Guisell Ortiz.
