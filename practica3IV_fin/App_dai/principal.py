# -*- coding: utf-8 -*-
"""

@author: josemlp
"""

# Practicas de Infraestracturas Virtuales (DAI)
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


import web
import pymongo
import anydbm
import feedparser
import time



from post import *   #Contiene todo el contenido
from web.contrib.template import render_mako
from formulario import *


# def actualiza_tiempo():
#     conn=pymongo.MongoClient()
#     db=conn.mydb
#     cache=db.cache
#     tiempo1=time.time()
#     t=cache.find_one({"rss":"el pais"})
#     tiempo2=t[u'ult_act']

#     if((tiempo2- tiempo1)>600): 
#         cache.update({"rss": "rsss"}, {"$set": {"ult_act": time.time()}})
#         rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')

#     conn.close()  


def actualiza_tiempo():
    db=anydbm.open('./timeStamp.txt','c')

    for i in range (len(twitConGeo)):
        db[str(i)] = str(twit[i]) + '|' + str(twitConGeo[i][0]) + '|' + str(twitConGeo[i][1])

    for i in range (len(twitConGeo)):
        datos = db[str(i)].split('|')
        print(datos)


    db.close() 


render = render_mako(
        directories=['plantillas'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')



categorias=["Categoria-I","Categoria-II"]
categoriasVIP=["Categoria-I","Categoria-II","Categoria-III","Categoria-IV"]

"""
lista_post=[]
lista_post_personal=[]

lista_post_categoriaI=[]
lista_post_categoriaII=[]
lista_post_categoriaIII=[]
lista_post_categoriaIV=[]
"""

class Principal:
	def GET(self):
		reg=False
		login=formuLogin()
		s=web.ctx.session
		i = web.input(categoria = 'Categoria-0')
		vectorLink=[]*3
		#web.websafe(i.categoria)
		try:
			if s.usuario!='':
				log=True
				user=s.usuario
				cat=categoriasVIP
			else:
				log=False
				user=''
				cat=categorias
		except AttributeError:
			s.usuario=''
			log=False
			user=''
			cat=categorias

		if (web.websafe(i.categoria)=='Categoria-0'):
			
			s.link3=s.link2
			s.link2=s.link1
			s.link1=""
			
			losPosts=lista_post

		elif (web.websafe(i.categoria)=='Categoria-I'):
			s.link3=s.link2
			s.link2=s.link1
			s.link1="/principal?categoria=Categoria-I"
			
			losPosts=lista_post_categoriaI
			
		elif (web.websafe(i.categoria)=='Categoria-II'):
			s.link3=s.link2
			s.link2=s.link1
			s.link1="/principal?categoria=Categoria-II"
			
			losPosts=lista_post_categoriaII

		elif (web.websafe(i.categoria)=='About'):
			s.link3=s.link2
			s.link2=s.link1
			s.link1="/principal?categoria=About"	
			
			losPosts=lista_post_personal

		elif (web.websafe(i.categoria)=='Contact'):
			s.link3=s.link2
			s.link2=s.link1
			s.link1="/principal?categoria=Contact"
			
			losPosts=lista_post_contacto
			
		elif ((web.websafe(i.categoria)=='Categoria-III') and (log==True)):
			s.link3=s.link2
			s.link2=s.link1
			s.link1="/principal?categoria=Categoria-III"
			
			losPosts=lista_post_categoriaIII
			
		elif ((web.websafe(i.categoria)=='Categoria-IV')and (log==True)):

			s.link3=s.link2
			s.link2=s.link1
			s.link1="/principal?categoria=Categoria-IV"
			
			losPosts=lista_post_categoriaIV
			
		else:

			s.link3=s.link2
			s.link2=s.link1
			s.link1=""	
			
			losPosts=lista_post
		


		vectorLink.append(s.link3)
		vectorLink.append(s.link2)
		vectorLink.append(s.link1)
		

		if (((web.websafe(i.categoria)=='Categoria-III') or (web.websafe(i.categoria)=='Categoria-IV'))and log==False): return "Registrate para ver el contenido"

		else:
			rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
			return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat,cateA=web.websafe(i.categoria),
        		losPosts=losPosts, autor='Jose Miguel Lopez', reg=reg,log=log,user=user,error=False, vLink=vectorLink,vtS="",rss=rss)


	def POST(self):
		reg=False
		login=formuLogin()
		i = web.input(categoria = 'Categoria-0')
		vectorLink=[]*3

		if not login.validates():
			log=False
			user=''
			rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
			return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=categorias,cateA=web.websafe(i.categoria),
        				losPosts=lista_post, autor='Jose Miguel Lopez', reg=False,log=False,user='',error=True,vLink=vectorLink,vtS="",rss=rss)  ###Error

		else:
			s=web.ctx.session
			conn=pymongo.MongoClient()
			db=conn.mydb
			usuarios=db.usuarios
			us=usuarios.find_one({"user":login['nombre'].value})
			conn.close()
			

			if  (us!=None):                                                      
				
				if (login['password'].value==us[u'pass']):
					s.usuario=login['nombre'].value
					user=s.usuario
					log=True
					cat=categoriasVIP

					if (web.websafe(i.categoria)=='Categoria-0'):
						
						s.link3=s.link2
						s.link2=s.link1
						s.link1=""
						
						losPosts=lista_post

					elif (web.websafe(i.categoria)=='Categoria-I'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-I"
						
						losPosts=lista_post_categoriaI
						
					elif (web.websafe(i.categoria)=='Categoria-II'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-II"
						
						losPosts=lista_post_categoriaII

					elif (web.websafe(i.categoria)=='About'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=About"	
						
						losPosts=lista_post_personal

					elif (web.websafe(i.categoria)=='Contact'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Contact"
						
						losPosts=lista_post_contacto
						
					elif ((web.websafe(i.categoria)=='Categoria-III') and (log==True)):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-III"
						
						losPosts=lista_post_categoriaIII
						
					elif ((web.websafe(i.categoria)=='Categoria-IV')and (log==True)):

						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-IV"
						
						losPosts=lista_post_categoriaIV
						
					else:

						s.link3=s.link2
						s.link2=s.link1
						s.link1=""	
						
						losPosts=lista_post
					
					vectorLink.append(s.link3)
					vectorLink.append(s.link2)
					vectorLink.append(s.link1)
						

					if (((web.websafe(i.categoria)=='Categoria-III') or (web.websafe(i.categoria)=='Categoria-IV'))and log==False): return "Registrate para ver el contenido"

					else:
						rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
						return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat,cateA=web.websafe(i.categoria),
			        		losPosts=losPosts, autor='Jose Miguel Lopez', reg=reg,log=log,user=user, error=False,vLink=vectorLink, vtS="",rss=rss)


				else:
					user=''
					log=False
					cat=categorias
					reg=False

					if (web.websafe(i.categoria)=='Categoria-0'):
						
						s.link3=s.link2
						s.link2=s.link1
						s.link1=""
						
						losPosts=lista_post

					elif (web.websafe(i.categoria)=='Categoria-I'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-I"
						
						losPosts=lista_post_categoriaI
						
					elif (web.websafe(i.categoria)=='Categoria-II'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-II"
						
						losPosts=lista_post_categoriaII

					elif (web.websafe(i.categoria)=='About'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=About"	
						
						losPosts=lista_post_personal

					elif (web.websafe(i.categoria)=='Contact'):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Contact"
						
						losPosts=lista_post_contacto
						
					elif ((web.websafe(i.categoria)=='Categoria-III') and (log==True)):
						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-III"
						
						losPosts=lista_post_categoriaIII
						
					elif ((web.websafe(i.categoria)=='Categoria-IV')and (log==True)):

						s.link3=s.link2
						s.link2=s.link1
						s.link1="/principal?categoria=Categoria-IV"
						
						losPosts=lista_post_categoriaIV
						
					else:

						s.link3=s.link2
						s.link2=s.link1
						s.link1=""	
						
						losPosts=lista_post
					
					vectorLink.append(s.link3)
					vectorLink.append(s.link2)
					vectorLink.append(s.link1)				
						

					if (((web.websafe(i.categoria)=='Categoria-III') or (web.websafe(i.categoria)=='Categoria-IV')) and log==False): return "Registrate para ver el contenido"	

					else:
						rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
						return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat,cateA=web.websafe(i.categoria),
			        		losPosts=losPosts, autor='Jose Miguel Lopez', reg=reg,log=log,user=user, error=True,vLink=vectorLink, vtS="",rss=rss)							
					
			else:
				rss=feedparser.parse('http://ep00.epimg.net/rss/tags/ultimas_noticias.xml')
				cat=categorias
				return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat,cateA=web.websafe(i.categoria),
        					losPosts=lista_post_categoriaI, autor='Jose Miguel Lopez', reg=False,log=False, user='',error=True,vLink=vectorLink, vtS="",rss=rss)  #Error
			
#


class Registro:
	def GET(self):
		reg=True
		login=formuLogin()
		re=regis()
		s=web.ctx.session
		i = web.input(categoria = 'Categoria-0')
		vectorLink=[]*3
		try:
			if s.usuario!='':
				log=True
				user=s.usuario
				cat=categoriasVIP
			else:
				log=False
				user=''
				cat=categorias
		except AttributeError:
			s.usuario=''
			log=False
			user=''
			cat=categorias

		s.link3=s.link2
		s.link2=s.link1
		s.link1="/registro"

		vectorLink.append(s.link3)
		vectorLink.append(s.link2)
		vectorLink.append(s.link1)


		rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
		return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat,cateA=web.websafe(i.categoria),
        	Registro=re, autor='Jose Miguel Lopez', reg=reg,log=log, user=user,error=False,vLink=vectorLink, vtS="",rss=rss)

	def POST(self):
		reg=True
		login=formuLogin()
		re=regis()
		i = web.input(categoria = 'Categoria-0')
		user=''
		cat=categorias
		if not re.validates():
			log=False
			rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
			return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat,cateA=web.websafe(i.categoria),
        	Registro=re, autor='Jose Miguel Lopez', reg=reg,log=log, user=user,error=False, vtS="",rss=rss)

		else:
			#Guardamos datos en base de datos.
			
			conn=pymongo.MongoClient()
			db=conn.mydb
			usuarios=db.usuarios            
			us=None
			try:
				us=usuarios.find_one({"user":login['user'].value})
			except:
				print ("Usename libre")

			if  (us==None):

				usuario={
				"user":re['nombre'].value,
				"pass":re['password'].value,
				"apellidos":re['apellidos'].value,
				"email":re['email'].value,
				"visa":re['visa'].value,
				"dia":re['dia'].value,
				"mes":re['mes'].value,
				"anio":re['anio'].value,
				"direccion":str(re['direccion'].value),
				"formPago":re['formaPago'].value

				}

				usuarios.insert(usuario)    
				conn.close()




				return  """<script type="text/javascript">alert("Registro exitoso"); window.location="/principal";</script>"""
			else:
				#print ("Ya existe")
				conn.close()
				return """<script type="text/javascript">alert("Usuario existente, elija otro nombre"); window.location="/registro";</script>"""
			


class Editar:
	def GET(self):
		reg=True
		edit=True
		login=formuLogin()
		s=web.ctx.session
		re=regis()
		i = web.input(categoria = 'Categoria-0')
		vectorLink=[]*3
		try:
			if s.usuario!='':
				log=True
				user=s.usuario
				cat=categoriasVIP
			else:
				log=False
				user=''
		except AttributeError:
			s.usuario=''
			log=False
			user=''
			cat=categorias

		conn=pymongo.MongoClient()
		db=conn.mydb
		usuarios=db.usuarios            
		us=None
		
		try:
			us=usuarios.find_one({"user":user})
		except:
			print ("No existe!!GET")

		if (us!=None):                                                     
			
			
			re.nombre.value=user
			re.apellidos.value=us[u'apellidos']
			re.email.value=us[u'email']
			re.visa.value=us[u'visa']
			re.dia.value=us[u'dia']
			re.mes.value=us[u'mes']
			re.anio.value=us[u'anio']
			re.direccion.value=us[u'direccion']
			re.formaPago.value=us[u'formPago']
			re.condiciones.type="hidden"
		
		conn.close()

		s.link3=s.link2
		s.link2=s.link1
		s.link1="/editar"

		vectorLink.append(s.link3)
		vectorLink.append(s.link2)
		vectorLink.append(s.link1)		

		rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
		return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat, cateA=web.websafe(i.categoria),
        	Registro=re, autor='Jose Miguel Lopez', reg=reg,log=log, user=user,edit=edit,error=False,vLink=vectorLink,rss=rss)

	def POST(self):
		reg=True
		login=formuLogin()
		s=web.ctx.session
		user=s.usuario
		edit=True
		re=regis()
		vectorLink=[]*3
		
		conn=pymongo.MongoClient()
		db=conn.mydb
		usuarios=db.usuarios            
		us=None


		i = web.input(categoria = 'Categoria-0')
		try:
			us=usuarios.find_one({"user":login['user'].value})
		except:
			print ("No existe!!POST")

		if  (us!=None ):                                                      
			Datos_usuario = d.split('|')
			db.close()

			print (Datos_usuario)
			
			re.nombre.value=user
			re.apellidos.value=us[u'apellidos']
			re.email.value=us[u'email']
			re.visa.value=us[u'visa']
			re.dia.value=us[u'dia']
			re.mes.value=us[u'mes']
			re.anio.value=us[u'anio']
			re.direccion.value=us[u'direccion']
			re.formaPago.value=us[u'formPago']

		conn.close()

		s.link3=s.link2
		s.link2=s.link1
		s.link1="/editar"

		vectorLink.append(s.link3)
		vectorLink.append(s.link2)
		vectorLink.append(s.link1)

		if not re.validates():
			#Repasar
			rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
			return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=categorias, Registro=re, autor='Jose Miguel Lopez',reg=reg,user="pepe",edit=edit,cateA=web.websafe(i.categoria),vLink=vectorLink,rss=rss)        

		else:

			conn=pymongo.MongoClient()
			
			usuarios=db.usuarios
			d=None
			
			try:
				us=usuarios.find_one({"user":login['user'].value})
			except:
				print ("Usename libre")

			if  (us==None or re.nombre.value==user  ):
				
				usuario={

				"user":re['nombre'].value,
				"pass":re['password'].value,
				
				"apellidos":re['apellidos'].value,
				"email":re['email'].value,
				"visa":re['visa'].value,

				"dia":re['dia'].value,
				"mes":re['mes'].value,
				"anio":re['anio'].value,
				
				"direccion":str(re['direccion'].value),
				"formPago":re['formaPago'].value

				}

				    
				usuarios.remove({"user":s.usuario})
				usuarios.insert(usuario)

				s.usuario=str(re.nombre.value)
				conn.close()
				return  """<script type="text/javascript">alert("Datos modificados con exito"); window.location="/principal";</script>"""
			else:
				#print ("Ya existe")
				db.close()
				return """<script type="text/javascript">alert("Usuario existente, elija otro nombre"); window.location="/registro";</script>"""
			
class Datos:
	def GET(self):
		reg=True
		edit=True
		login=formuLogin()
		s=web.ctx.session
		re=regis()
		usu=None
		i = web.input(categoria = 'Categoria-0')
		vectorLink=[]*3
		try:
			if s.usuario!='':
				log=True
				user=s.usuario
				cat=categoriasVIP
			else:
				log=False
				user=''
		except AttributeError:
			s.usuario=''
			log=False
			user=''
			cat=categorias

		conn=pymongo.MongoClient()
		db=conn.mydb
		usuarios=db.usuarios            
		us=None
		
		try:
			us=usuarios.find_one({"user":user})
		except:
			print ("No existe!!GET")

		if (us!=None):                                                     
			
			usu=user
			apell=us[u'apellidos']
			ema=us[u'email']
			vis=us[u'visa']
			d=us[u'dia']
			m=us[u'mes']
			an=us[u'anio']
			di=us[u'direccion']
			pago=us[u'formPago']
			
		
			conn.close()
			lista_post_datos=[]

			s.link3=s.link2
			s.link2=s.link1
			s.link1="/datos"

			vectorLink.append(s.link3)
			vectorLink.append(s.link2)
			vectorLink.append(s.link1)
			post_datos=post("Datos usuario", """http://goo.gl/f1P7sa""", "<div>Nombre: "+ usu +"<br>  Apellidos:"+apell+ "<br> Email: "+ema+"<br> VISA: "+vis+"<br>Fecha Nacimiento:"+ str(d) +"/" +str(m)+"/" +str(an) +"<br>Direccion:"+ di+"</div>","","",
	       					fecha(3,9,2013),"josemlp")

			lista_post_datos.append(post_datos)
		if log==True:
			rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
			return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=categoriasVIP,cateA="",
        		losPosts=lista_post_datos, autor='Jose Miguel Lopez', reg=False,log=log,user=user,error=False,vLink=vectorLink,rss=rss)
		else:
			return "Ningun usuario logueado"

class Cuentas:
	def GET(self):
		reg=True
		edit=True
		login=formuLogin()
		fIngreso=formuIngreso()
		s=web.ctx.session
		re=regis()
		usu=None
		

		conn=pymongo.MongoClient()
		db=conn.mydb
		ingresos=db.ingresos

		vectorSerie=[]

		

		cursor=ingresos.find()
		while cursor.alive:
		 	try:
		 		doc = cursor.next()
				
		 		print (doc[u'nombre'])
		 		nIngreso=[doc[u'nombre'],doc[u'cantidad']]
		 		vectorSerie.append(nIngreso)


			except StopIteration:
			 	time.sleep(1)

		rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
		return render.plantilla(Titulo='https://github.com/josemlp91/IV_work/blob/master/Uso%20de%20m%C3%A1quinas%20virtuales.md', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=categorias,cateA="Cuentas",
         	losPosts='', autor='Jose Miguel Lopez', reg=False,log=False,user="pepe",error=False, vLink="", vtS=vectorSerie, fI=fIngreso,rss=rss)

	def POST(self):

		reg=True
		edit=True
		login=formuLogin()
		fIngreso=formuIngreso()
		s=web.ctx.session
		re=regis()
		usu=None
		
		conn=pymongo.MongoClient()
		db=conn.mydb
		ingresos=db.ingresos
 
		if fIngreso.validates():     #Validarlo de verdad

		
			ingreso={	
					"nombre":fIngreso['nombre'].value,
					"cantidad":fIngreso['ingreso'].value
						
			}
				
			ingresos.insert(ingreso)
		
		#db.drop_collection("ingresos")
		vectorSerie=[]


		cursor=ingresos.find()
		while cursor.alive:
			try:
				doc = cursor.next()
								
				nIngreso=[doc[u'nombre'],doc[u'cantidad']]
				vectorSerie.append(nIngreso)


			except StopIteration:
				print "Vacio"
		rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
		return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=categorias,cateA="Cuentas",
         	losPosts='', autor='Jose Miguel Lopez', reg=False,log=False,user="pepe",error=False, vLink="", vtS=vectorSerie, fI=fIngreso,rss=rss)




class Mapas:
	def GET(self):
		reg=True
		edit=True
		login=formuLogin()
		fIngreso=formuIngreso()
		s=web.ctx.session
		re=regis()
		usu=None
		
		db=anydbm.open('./coordenadasTweets.txt','c')
		listTw=[]
		
		claves=(db.keys())
		for i in  range(len(claves)):
			datos = db[str(i)].split('|')
			listTw.append(datos)
			print(datos)
		
		db.close()

		rss=feedparser.parse('http://feeds.feedburner.com/cyberhades/rss')
		return render.plantilla(Titulo='Infraestracturas Virtuales', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=categorias,cateA="Mapas",
         	losPosts='', autor='Jose Miguel Lopez', reg=False,log=False,user="pepe",error=False, vLink="", lTw=listTw,rss=rss)
		
		


#Clase para cerrar las sesiones
class CerrarS:

    def GET(self):
        s=web.ctx.session
        s.kill()
        web.redirect('/')
