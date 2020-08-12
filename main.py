import dtd_validator
import xml_parser as parser
#from pyswip import Prolog


if dtd_validator.start_validation(open("recetas.xml"), open("validator.dtd")):
    data = parser.get_tags_info(list(open("recetas.xml")))
    sons = parser.find_sons(list(open("recetas.xml")))
    ingrediente_sons = parser.find_sons_by_tag_name(sons, "ingrediente", 0)
    grasa_caloria_info = []

    for x in ingrediente_sons:
        nombre = ""
        calorias = ""
        grasas = ""
        for son in x[1]:
            if parser.find_tag_name(son) == "nombre":
                nombre = parser.find_tag_content(son)
            elif parser.find_tag_name(son) == "calorias":
                calorias = parser.find_tag_content(son)
            elif parser.find_tag_name(son) == "grasas":
                 grasas = parser.find_tag_content(son)
        grasa_caloria_info.append([nombre, calorias, grasas])

    #print(grasa_caloria_info)

def get_platos_ingredientes(xml_file, dtd_file):
    if dtd_validator.start_validation(xml_file, dtd_file):
        in_receta = False
        nombre_receta = ""
        platos_ingredientes = []
        for x in data:
            if x['name'] == 'receta':
                in_receta = True
                nombre_receta = x['value']
            if x['name'] == 'receta' and in_receta:
                nombre_receta = x['value']
            if x['name'] == 'nombre' and in_receta == True:
                platos_ingredientes.append("plato_ingrediente(" + nombre_receta.lower() + "," + x['content'].lower() + ")") #lista con nombre receta e ingredientes
        return platos_ingredientes
    return "This xml stinks!"

def get_platos_procedimientos(xml_file, dtd_file):
    if dtd_validator.start_validation(xml_file, dtd_file):
        in_receta = False
        nombre_receta = ""
        platos_procedimientos = []
        for x in data:
            if x['name'] == 'receta':
                in_receta = True
                nombre_receta = x['value']
            if x['name'] == 'receta' and in_receta:
                nombre_receta = x['value']
            if x['name'] == 'procedimiento' and in_receta == True:
                platos_procedimientos.append("plato_procedimiento(" + nombre_receta.lower().replace(" ", "_") + "," + x['content'].lower().replace(" ", "_") + ")") #lista con nombre receta e ingredientes
        return platos_procedimientos
    return "This xml stinks!"

def plato_ingrediente(prolog):
    for y in get_platos_ingredientes(open("recetas.xml"), open("validator.dtd")):
        prolog.asserta(y)

def plato_procedimiento(prolog):
    for y in get_platos_procedimientos(open("recetas.xml"), open("validator.dtd")):
        prolog.asserta(y)