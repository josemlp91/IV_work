#Post de ejemplo

# -*- coding: 850 -*-

# Practicas de Desarrollo de Aplicaciones para Internet (DAI)
# Copyright (C) 2013 - Jose Miguel Lopez (josemlp@correo.ugr.es)
#    
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class fecha:
	dia=0
	mes=0
	agno=0
	def __init__(self,d,m,a):
		self.dia=d
		self.mes=m
		self.agno=a


class post:
	titulo=""
	imagen=""
	texto1=""
	textoResaltado=""
	texto2=""
	fecha=fecha(0,0,0)
	autor=""

	def __init__(self,titu,imag,tex1,texR,tex2,fecha,aut):
		self.titulo=titu
		self.imagen=imag
		self.texto1=tex1
		self.textoResaltado=texR
		self.texto2=tex2
		self.fecha=fecha
		self.autor=aut


lista_post=[]
lista_post_personal=[]

lista_post_categoriaI=[]
lista_post_categoriaII=[]
lista_post_categoriaIII=[]
lista_post_categoriaIV=[]
lista_post_contacto=[]


post1=post("WebPy", 

     "http://webpy.org/static/webpy.gif",  #Imagen

     """Web.py es su apuesta para revitalizar la web, para volverla simple, como parte del
		movimiento Web2.0. Si Ruby on Rails simplifico las monstruosidades de J2EE y
		compania, Web.py convierte el desarrollo web en una cosa de ninos. En menos de
		10 segundos se puede tener funcionando una pagina web dinamica.
		Y es que mucha gente de la llamada Web2.0 quiere volver a los tiempos en los
		que usar la web era divertido, asi que Aaron ha hecho de Web.py una herramienta muy potente y sencilla.""",

      """Jose Maria Ruiz actualmente esta realizando el Proyecto Fin de Carrera de Ingenieria Tecnica
		en Informatica de Sistemas.
		Lleva 8 anos usando y desarrollando software libre y, desde hace dos, se esta especializando en FreeBSD.""",
		"""
		Con Web.py podemos comenzar a crear webs de manera muy sencilla y rapida. 
		Es un herramienta muy buena para crear prototipos o explorar nuevos conceptos. 
		Y eso que, cuando se escribe este articulo, solo esta disponible la version 0.13.
		El sitio web www.reddit.com emplea Web.py y su uso se esta extendiendo a la vez que mas personas se unen a su desarrollo.
		Desde luego, es un proyecto interesante y debemos estar atentos a su futuro desarrollo.
		""",
       
      fecha(3,9,2013),
       
      "josemlp" 

      )

post1_categoriaI=post("Fallece la anciana que corrio el Maraton de NY.", 

     """http://www.lapagina.com.sv/userfiles/Nov_2013/NVOS_WlUxNzMxMy5qcGc=.jpg""",  #Imagen

     """Joy Johnson, quien a sus 86 agnos corrio el pasado domingo su vigesimo quinto maraton de Nueva York fallecio un dia despues de la prueba segun ha informado la television estadounidense NBC.
        Johnson, podia presumir a su edad de ser desde 2011 la  mujer mas anciana en correr esta prueba. Esta veterana corredora era conocida, querida y admirada en todo el pais por su espiritu atletico y por las ganas que siempre le puso. De hecho, 
        durante el maraton, sufrio una caida en el kilometro 32 del recorrido y se golpeo la cabeza, pero no se detuvo, con la venda que le pusieron los servicios de emergencia siguio corriendo hasta cruzar la meta en algo menos de 8 horas.""",

      """""","DEP",
       
      fecha(3,9,2013),
       
      "josemlp" 

      )


post1_categoriaII=post("No hay dos caras iguales.", 

     """http://www.nosabesnada.com/uploads/2013/11/Gemelos-300x230.jpg""",  #Imagen

     """A todos nos cuesta distinguir quien es quien cuando vemos una pareja de gemelos, incluso para algunos padres los primeros dias no es facil. 
    Sin embargo, a pesar de lo que pensemos no existen dos caras iguales aunque compartan el mismo ADN. 
    Una investigacion publicada recientemente en la revista Science resuelve este  misterio.
    Segun los investigadores algunas regiones de ADN que no codifican proteinas pero que disminuyen o incrementan la expresion de los genes, 
    son los responsables de algunos rasgos, como la forma de la cara.

    Para comprobar la importancia de estos potenciadores los cientificos escogieron regiones no codificantes del genoma de los ratones. 
    Despues analizaron la expresion de dichos potenciadores gracias a un modelo tridimensional craneofacial de los ratones. 
    Y por ultimo, eliminaron de manera selectiva dichos potenciadores y analizaron de nuevo el efecto que habia tenido sobre
    la expresion genetica y la morfologia craneofacial durante el desarrollo.""",

      """""","",
       
      fecha(3,9,2013),
       
      "josemlp" 

      )


post1_categoriaIII=post("Las bebidas alcoholicas que mas engordan.", 

     """http://goo.gl/F8Li46""",  #Imagen

     """Cuando una persona se pone a dieta lo primero que se tiene que retirar de su menu son los alimentos y bebidas ricos en grasas y azucares.
     Y dentro de esta restriccion se encuentran las bebidas alcoholicas. 
    -ANIS: Segun un informe realizado por el investigador Jose Mataix Verdu, de la Universidad de Granada, las bebidas alcoholicas que mas calorias contienen son los anises.
    Por cada 100 mililitros esta bebida aporta 297 kcal.
	-WHISKY: Esta bebida ocupa el segundo lugar en el ranking de las bebidas con mas aporte calorico.
	100 ml contienen la cantidad de 240 Kcal. No es de sorprender cuando se obtiene por la destilacion de la malta fermentada de cereales (trigo, cebada, centeno maiz).
	-AGUARDIENTE: Completa el podio con una aportacion de 231 Kcal por cada 100 ml. La destilacion de esta bebida proviene de multitud de plantas sacarosas.
	-RON: Continua en el ranking este destilado de la cana de azucar. Que como no podia ser de otra manera, aporta 101 kcal por cada 100 ml.

	Entre los vinos, los mas caloricos son los dulces (Moscatel, Malaga, Oporto), con 149 kcal por cada 100 mililitros,
	seguidos de los blancos (79 kcal) y los tintos (74 kcal).

	Cierra la lista el Sidra con 40 kcal y la cerveza con 45 kcal.""",

      """""","",
       
      fecha(3,9,2013),
       
      "josemlp" 

      )

post1_categoriaIV=post("Como quitar la ultima hora en linea en Whatsapp sin dejar pasar 24 hrs.", 

     """http://bulevar21.bligoo.com/media/users/28/1415496/images/public/478330/roto-whatsapp.png?v=1383065517512""",  #Imagen

     """Cada vez es mas habitual que la gente oculte su ultima hora de conexion en Whatsapp. 
     Esto se hace en el menu de ajustes de la aplicacion: ajustes de chat>avanzado>ultima hora en linea

	Esto parece genial, pero tiene su inconveniente. Debes esperar 24 horas antes de poner volver a ver y mostrar la ultima conexion.

 	Te proponemos un truco:  Una vez hayas desactivado la ultima hora en linea, cambia la hora de tu dispositivo: 
 	ajustes>general>fecha y hora>ajuste automatico desactivar>poner un dia mas.
 	Una vez hayas hecho esto, podras quitar la ultima hora en linea y a continuacion volver a poner el ajuste de hora en automatico.
 	""",

    """""","",
       
    fecha(3,9,2013),
       
    "josemlp" 

    )



post_personal=post("Presentacion", 

     """https://pbs.twimg.com/profile_images/378800000688632035/80bfdbf377c097a87fa369328acc6fd8_bigger.jpeg""",  #Imagen

     """Comienzo a elaborar este espacio con cosas interesantes del mundo de la informatica y de las nuevas tecnologias.
        Para empezar comenzare presentandome para que nos vayamos conociendo, mi nombre es Jose Miguel, 
        Naci el 3 de Septiembre de 1991 en un bonito pueblo del poniente granadino, llamado Montefrio.
        Alli vivi felizmente  hasta que decidi comenzar a estudiar Ingenieria de Informatica en Granada,
        pues tenia especial curiosidad en conocer a esos duendecillos que habitaban mi anticuado ordenador.
        Tras muchas asignaturas, muchas horas de clase y muchas horas humillando a mi portatil por lanzarme algun capricho error,
        me encuentro en el primer cuatrimestre del ultimo curso.""",

      """La mejor forma de predecir el futuro es implementarlo <br>  <cite>David Heinemeier Hansson - creador de Ruby on Rails </cite>""","",
       
      fecha(3,9,2013),
       
      "josemlp" 

      )

post_contacto=post("Contacto", 

     """http://our.blog.com/files/2012/02/fi-commentssocial-640x290.png""",  #Imagen

     """ <a id="mapa" href="http://goo.gl/maps/b0dYi"><img align=center src="http://png-3.findicons.com/files/icons/2305/mobile_icon_set/128/04_maps.png" WIDTH=70 HEIGHT=70 alt"mapa"/></a> <br>""",

      """Hay dos cosas que son infinitas: el universo y la estupidez humana; de la primera no estoy muy seguro. 
              <br>  <cite>(Einstein, Albert)</cite>""","""

        <a style="style="margin: 0 auto; width: 350px;"" id="foxyform_embed_link_124850" href="http://es.foxyform.com/">foxyform</a>
        <script type="text/javascript">
        (function(d, t){
           var g = d.createElement(t),
               s = d.getElementsByTagName(t)[0];
           g.src = "http://es.foxyform.com/js.php?id=124850&sec_hash=3b7418c831d&width=350px";
           s.parentNode.insertBefore(g, s);
        }(document, "script"));
        </script>
         <br>
         
        """
,
       
      fecha(3,9,2013),
       
      """""" 

      )


#Anadimos los post a las correspondientes listas.

lista_post.append(post1)

lista_post_personal.append(post_personal)

lista_post_categoriaI.append(post1_categoriaI)
lista_post_categoriaII.append(post1_categoriaII)
lista_post_categoriaIII.append(post1_categoriaIII)
lista_post_categoriaIV.append(post1_categoriaIV)

lista_post_contacto.append(post_contacto)