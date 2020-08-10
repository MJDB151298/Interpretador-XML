import dtd_validator
import xml_parser as parser

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

    print(grasa_caloria_info)