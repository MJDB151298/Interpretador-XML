import dtd_validator
import xml_parser as parser

if dtd_validator.start_validation(open("recetas.xml"), open("validator.dtd")):
    data = parser.get_tags_info(list(open("recetas.xml")))
    sons = parser.find_sons(list(open("recetas.xml")))

    grasa_caloria_info = []

    for x in sons:
        if parser.find_tag_name(x[0]) == "ingrediente":
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
    print(grasa_caloria_info)