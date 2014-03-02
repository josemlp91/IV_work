# -*- coding: utf-8 -*-
"""

@author: josemlp
"""


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
from web.contrib.template import render_mako
from formulario import *
import anydbm
from post import *   #Contiene todo el contenido


render = render_mako(
        directories=['plantillas'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


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
			losPosts=lista_post

		elif (web.websafe(i.categoria)=='Categoria-I'):
			losPosts=lista_post_categoriaI
			
		elif (web.websafe(i.categoria)=='Categoria-II'):
			losPosts=lista_post_categoriaII
			
		elif ((web.websafe(i.categoria)=='Categoria-III') and (log==True)):
			losPosts=lista_post_categoriaIII
			
		elif ((web.websafe(i.categoria)=='Categoria-IV')and (log==True)):
			losPosts=lista_post_categoriaIV
			
		else:
			losPosts=lista_post
			

		if (((web.websafe(i.categoria)=='Categoria-III') or (web.websafe(i.categoria)=='Categoria-IV'))and log==False): return "Registrate para ver el contenido"

		else:
			return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
        		losPosts=losPosts, autor='Jose Miguel Lopez', reg=reg,log=log,user=user,error=False)


	def POST(self):
		reg=False
		login=formuLogin()
		i = web.input(categoria = 'Categoria-0')

		if not login.validates():
			log=False
			user=''
			return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=categorias,cateA=web.websafe(i.categoria),
        				losPosts=lista_post, autor='Jose Miguel Lopez', reg=False,log=False,user='',error=True)  ###Error

		else:
			s=web.ctx.session

			db=anydbm.open('./registro.txt','c')
			d=None
			try:
				d=db[str(login.nombre.value)]
			except:
				print ("No existe!!")

			if  (d!=None):                                                      
				Datos_usuario = d.split('|')
				print (Datos_usuario)
				db.close()

				if (login['password'].value==Datos_usuario[0]):
					s.usuario=login['nombre'].value
					user=s.usuario
					log=True
					cat=categoriasVIP

					if (web.websafe(i.categoria)=='Categoria-0'):
						losPosts=lista_post

					elif (web.websafe(i.categoria)=='Categoria-I'):
						losPosts=lista_post_categoriaI
						
					elif (web.websafe(i.categoria)=='Categoria-II'):
						losPosts=lista_post_categoriaII
						
					elif ((web.websafe(i.categoria)=='Categoria-III') and (log==True)):
						losPosts=lista_post_categoriaIII
						
					elif ((web.websafe(i.categoria)=='Categoria-IV')and (log==True)):
						losPosts=lista_post_categoriaIV
						
					else:
						losPosts=lista_post
						

					if (((web.websafe(i.categoria)=='Categoria-III') or (web.websafe(i.categoria)=='Categoria-IV'))and log==False): return "Registrate para ver el contenido"

					else:
						return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
			        		losPosts=losPosts, autor='Jose Miguel Lopez', reg=reg,log=log,user=user, error=False)


				else:
					user=''
					log=False
					cat=categorias
					reg=False

					if (web.websafe(i.categoria)=='Categoria-0'):
						losPosts=lista_post

					elif (web.websafe(i.categoria)=='Categoria-I'):
						losPosts=lista_post_categoriaI
						
					elif (web.websafe(i.categoria)=='Categoria-II'):
						losPosts=lista_post_categoriaII
						
					elif (web.websafe(i.categoria)=='Categoria-III'):
						losPosts=lista_post_categoriaIII
						
					elif (web.websafe(i.categoria)=='Categoria-IV'):
						losPosts=lista_post_categoriaIV
						
					else:
						losPosts=lista_post
						

					if (((web.websafe(i.categoria)=='Categoria-III') or (web.websafe(i.categoria)=='Categoria-IV')) and log==False): return "Registrate para ver el contenido"	

					else:
						return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
			        		losPosts=losPosts, autor='Jose Miguel Lopez', reg=reg,log=log,user=user, error=True)							
					
			else:
				cat=categorias
				return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
        					losPosts=lista_post_categoriaI, autor='Jose Miguel Lopez', reg=False,log=False, user='',error=True)  #Error
			
#

class About:
	def GET(self):
		reg=False
		login=formuLogin()
		s=web.ctx.session
		log=False

		i = web.input(categoria = 'Categoria-0')
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
		
		return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
        	losPosts=lista_post_personal, autor='Jose Miguel Lopez', reg=reg,log=log, user=user,error=False)

	def POST(self):
		reg=False
		log=False
		login=formuLogin()
		i = web.input(categoria = 'Categoria-0')
		if not login.validates():
			log=False
			user=''


		else:
			s=web.ctx.session
			if login['nombre'].value=='josemlp' and login['password'].value=='0000': #Arreglar
				s.usuario=login['nombre'].value
				user=s.usuario
				log=True
				cat=categoriasVIP
				#return "Bienvenido"
			else:
				user=''
				log=False
				cat=categorias


		return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
        	losPosts=lista_post_personal, autor='Jose Miguel Lopez',reg=reg,log=log, user=user,error=False)


class Registro:
	def GET(self):
		reg=True
		login=formuLogin()
		re=regis()
		s=web.ctx.session
		i = web.input(categoria = 'Categoria-0')
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
		
		return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
        	Registro=re, autor='Jose Miguel Lopez', reg=reg,log=log, user=user,error=False)

	def POST(self):
		reg=True
		login=formuLogin()
		re=regis()
		i = web.input(categoria = 'Categoria-0')
		user=''
		if not re.validates():
			log=False
			return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat,cateA=web.websafe(i.categoria),
        	Registro=re, autor='Jose Miguel Lopez', reg=reg,log=log, user=user,error=False)

		else:
			#Guardamos datos en base de datos.
			db=anydbm.open('./registro.txt','c')
			d=None
			try:
				d=db[str(re.nombre.value)]
			except:
				print ("Usename libre")

			if  (d==None ):                                                      
				db[str(re.nombre.value)] = str(re.password.value) + '|' + str(re.apellidos.value) + '|' + str(re.email.value)  + '|' + str(re.visa.value)  + '|' + str(re.dia.value) + '|' + str(re.mes.value) + '|' +str(re.anio.value)+ '|' + str(re.direccion.value)+ '|' +str(re.formaPago.value)

				datos = db[str(re.nombre.value)].split('|')
				print (datos)
				db.close()
				return  """<script type="text/javascript">alert("Registro exitoso"); window.location="/principal";</script>"""
			else:
				#print ("Ya existe")
				db.close()
				return """<script type="text/javascript">alert("Usuario existente, elija otro nombre"); window.location="/registro";</script>"""
			


class Editar:
	def GET(self):
		reg=True
		edit=True
		login=formuLogin()
		s=web.ctx.session
		re=regis()
		i = web.input(categoria = 'Categoria-0')
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

		db=anydbm.open('./registro.txt','c')
		d=None
		try:
			print (user)
			d=db[str(user)]
		except:
			print ("No existe!!GET")

		if (d!=None):                                                     
			Datos_usuario = d.split('|')
			db.close()

			print (Datos_usuario)
			re.nombre.value=user
			re.apellidos.value=Datos_usuario[1]
			re.email.value=Datos_usuario[2]
			re.visa.value=Datos_usuario[3]
			re.dia.value=Datos_usuario[4]
			re.mes.value=Datos_usuario[5]
			re.anio.value=Datos_usuario[6]
			re.direccion.value=Datos_usuario[7]
			re.formaPago.value=Datos_usuario[8]
			re.condiciones.type="hidden"

		return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=cat, cateA=web.websafe(i.categoria),
        	Registro=re, autor='Jose Miguel Lopez', reg=reg,log=log, user=user,edit=edit,error=False)

	def POST(self):
		reg=True
		login=formuLogin()
		s=web.ctx.session
		user=s.usuario
		edit=True
		re=regis()
		db=anydbm.open('./registro.txt','c')
		d=None
		i = web.input(categoria = 'Categoria-0')
		try:
			print (user)
			d=db[str(user)]
		except:
			print ("No existe!!POST")

		if  (d!=None ):                                                      
			Datos_usuario = d.split('|')
			db.close()

			print (Datos_usuario)
			
			re.nombre.value=user
			re.apellidos.value=Datos_usuario[1]
			re.email.value=Datos_usuario[2]
			re.visa.value=Datos_usuario[3]
			re.dia.value=Datos_usuario[4]
			re.mes.value=Datos_usuario[5]
			re.anio.value=Datos_usuario[6]
			re.direccion.value=Datos_usuario[7]
			re.formaPago.value=Datos_usuario[8]
			re.condiciones.type="hidden"

		if not re.validates():
			#Repasar
			return render.plantilla(Titulo='Infraestructuras Virtuales', Subtitulo='Servidor Enjaulado',login=login,cate=categorias, Registro=re, autor='Jose Miguel Lopez',reg=reg,user="pepe",edit=edit,cateA=web.websafe(i.categoria))        

		else:
			#Guardamos datos en base de datos.
			db=anydbm.open('./registro.txt','c')
			d=None
			try:
				d=db[str(re.nombre.value)]
			except:
				print ("Usename libre")

			if  (d==None or re.nombre.value==user  ):
				
				db[str(re.nombre.value)] = str(re.password.value) + '|' + str(re.apellidos.value) + '|' + str(re.email.value)  + '|' + str(re.visa.value)  + '|' + str(re.dia.value) + '|' + str(re.mes.value) + '|' +str(re.anio.value)+ '|' + str(re.direccion.value)+ '|' +str(re.formaPago.value)

				s.usuario=str(re.nombre.value)
				db.close()
				return  """<script type="text/javascript">alert("Datos modificados con exito"); window.location="/principal";</script>"""
			else:
				#print ("Ya existe")
				db.close()
				return """<script type="text/javascript">alert("Usuario existente, elija otro nombre"); window.location="/registro";</script>"""
			


#Clase para cerrar las sesiones
class CerrarS:

    def GET(self):
        s=web.ctx.session
        s.kill()
        web.redirect('/')
