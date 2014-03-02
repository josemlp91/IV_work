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


from principal import *
from web import form
import web
import tempfile


             
urls = (
	'/','Principal',
    '/formulario', 'Formulario', 
    '/principal','Principal',
    '/registro','Registro',
    '/editar','Editar',
    '/about','About',
    '/cerrarsesion','CerrarS',
)



app = web.application(urls, globals())

session=web.session.Session(app,web.session.DiskStore(tempfile.mkdtemp()))

def session_hook():
	web.ctx.session=session

# Gestionamos el error 404 (not found)
def notfound():
    return web.notfound("Lo siento, la p&aacute;gina que buscas no existe. Prueba con /formulario")

app.add_processor(web.loadhook(session_hook))

# Asignamos el gestor del not found de la aplicación web a la función anterior
app.notfound = notfound

if __name__ == "__main__":
    app.run()
