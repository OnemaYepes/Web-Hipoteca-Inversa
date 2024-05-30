from flask import Blueprint, render_template, request

blueprint = Blueprint( "vista_usuarios", __name__, "templates" )

import sys
sys.path.append("src")
from model.Usuario import Usuario
import controller.Controlador_Usuarios as ControladorUsuarios

@blueprint.route("/")
def Home():
   return render_template("home.html")

@blueprint.route( "/form" )
def Form():
   return render_template("form.html")

@blueprint.route("/submit")
def createUser():
   nuevo_usuario = Usuario(cedula=request.args["cedula"], edad=request.args["edad"], estado_civil=request.args["estado_civil"], edad_conyugue=request.args["edad_conyugue"], 
                           sexo_conyugue=request.args["sexo_conyugue"], valor_inmueble=request.args["valor_inmueble"], tasa_interes=request.args["tasa_interes"])
   ControladorUsuarios.Controlador_Usuarios.Insertar_Usuario(nuevo_usuario)
   return render_template("user.html", user = nuevo_usuario)