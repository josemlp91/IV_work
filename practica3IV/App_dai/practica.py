# -*- coding: utf-8 -*-
"""
@author: josemlp
"""
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


from principal import *
from web import form
from pymongo import *
from tweet import *
from keys import *

import web
import tempfile
import sys
import anydbm
import codecs
import tweepy
import re
import time




             
urls = (
	'/','Principal',
    '/formulario', 'Formulario', 
    '/principal','Principal',
    '/registro','Registro',
    '/editar','Editar',
    '/about','About',
    '/datos','Datos',
    '/Cuentas', 'Cuentas',
    '/Mapas', 'Mapas',
    '/cerrarsesion','CerrarS'
)



app = web.application(urls, globals())

session=web.session.Session(app,web.session.DiskStore(tempfile.mkdtemp()),initializer={'usuario':'','link1':'','link2':'','link3':''})

def session_hook():
	web.ctx.session=session

# Gestionamos el error 404 (not found)
def notfound():
    return web.notfound("""<img class="center" src="/static/images/error.png" alt="Error 404"  />""")

app.add_processor(web.loadhook(session_hook))

# Asignamos el gestor del not found de la aplicación web a la función anterior
app.notfound = notfound

if __name__ == "__main__":
    print "Conectando al Servidor de Base de Datos Local..."
    
    #Maneja Twitter

    #Autentifica y crea conexion 
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)


    result = api.user_timeline("josemlp91_TIC")
    twitConGeo=[]
    twit=[]
                                                                            #####Ojo esto esta mal, seria necesario hacerlo como una hebra "daemon" que se ejecute cada x tiempo.
    for status in result:
        gt=status.geo
        if (gt!=None):
            print (status.author.name)
            twit.append(status.text)
            twitConGeo.append((gt[u'coordinates']))

    db=anydbm.open('./coordenadasTweets.txt','c')

    for i in range (len(twitConGeo)):
        db[str(i)] = str(twit[i]) + '|' + str(twitConGeo[i][0]) + '|' + str(twitConGeo[i][1])

    for i in range (len(twitConGeo)):
        datos = db[str(i)].split('|')
        print(datos)


    db.close()

    conexion = Connection()

    
    app.run()

