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

from web import form

# Creamos el formulario. Su ámbito es global
# Validacion de campos

vemail=form.regexp(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b',"Introduzca una direccion de correo valida")
vvisa=form.regexp(r'([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})',"El formato del Nº de visa debe ser valido")
vpass=form.regexp(r'.{7,20}$',"La contrasenia debe tener mas de 7 caracteres")

meses31=['1','3','4','7','8','10','12']
meses30=['5','6','9','11']

regis=form.Form( 
        form.Textbox("nombre",form.notnull,description = "Nombre:",value=""),
        form.Textbox("apellidos",form.notnull, description = "Apellidos:",value=""),
        form.Textbox("email",form.notnull,vemail, description = "Email:",value=""),
        form.Textbox("visa",form.notnull,vvisa ,description = "Numero de Visa:",value=""),
        form.Dropdown("dia",range(1,32),value=""),
        form.Dropdown("mes",range(1,13),value=""),
        form.Dropdown("anio",range(1940,2014),value=""),
        form.Textarea("direccion",form.notnull,description = "Direccion:",value=""),
        form.Password("password",vpass,description = "Password:",value=""),
        form.Password("password2",description = "Repita el Password:",value=""),
        form.Radio("formaPago",["Transferencia","PayPal","VISA"],description = "Forma de Pago:",value=""),
        form.Checkbox("condiciones",description="Acepto las condiciones",value="on"),
        form.Button("Registrar"),
        validators = [
            form.Validator("No coinciden las contraseñas", lambda i: i.password == i.password2)
            ,form.Validator("Hay que aceptar las condiciones", lambda j: j.condiciones == "on")
            , form.Validator("Fecha incorrecta",lambda k: (k.mes in meses31) or ((k.mes in meses30) and int(k.dia)<31) or ((int(k.mes) == 2) and int(k.dia)<29) or ((int(k.mes) == 2) and int(k.dia)<30 and int(k.anio)%4==0))
            ])


formuLogin = form.Form( 
    form.Textbox("nombre",description = "Nombre:",id="login-text"),
    form.Password("password",description = "Pass:",id="login-pass"),
    form.Button('OK',id="login-submit"),
)


formuIngreso = form.Form( 
    form.Textbox("nombre", form.notnull, description = "Nombre:",id="ingreso-name",value=""),
    form.Textbox("ingreso", form.notnull, form.regexp('\d+', 'Must be a digit'), description = "Cantidad Ingreso:",id="ingreso-cantidad",value=""),
    form.Button('OK',id="ingreso-submit"),
)




