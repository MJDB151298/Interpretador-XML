import xml_parser as parser

def get_dtd_name(dtd_line):
    first_space_index = dtd_line.find(" ")
    second_space_index = dtd_line.find(" ", first_space_index+1)
    return dtd_line[first_space_index+1:second_space_index]

def get_dtd_attribute(dtd_line):
    first_space_index = dtd_line.find(" ")
    second_space_index = dtd_line.find(" ", first_space_index+1)
    third_space_index = dtd_line.find(" ", second_space_index+1)
    return dtd_line[second_space_index+1:third_space_index]


def get_dtd_sons(dtd_line):
    first_paragraph_index = dtd_line.find("(")
    second_paragraph_index = dtd_line.find(")", first_paragraph_index+1)
    return_list = dtd_line[first_paragraph_index+1:second_paragraph_index].split(",")
    for i in range(0, len(return_list)):
        return_list[i] = return_list[i].strip()
    return return_list

def has_symbol(dtd_son):
    if dtd_son[len(dtd_son)-1] == "?" or dtd_son[len(dtd_son)-1] == "+" or dtd_son[len(dtd_son)-1] == "*":
        return True
    return False

def validate_xml_attributes(attribute_list, xml_file):
    xml_data = parser.get_tags_info(xml_file)
    for data in xml_data:
        for attribute in attribute_list:
            if data["name"] == attribute[0]:
                if data["key"] != attribute[1]:
                    return "Attribute " + data["key"] + " must be declared for element type " + data["name"]
    return True

#Function: validate_xml_grammar.
#Attribute: element_list, list, lista de todos los ELEMENTS declarados.
#Attribute: xml_file, list, archivo xml transformado en lista.
#Return: True si todos los tags estan nombrado correctamente, mensaje de error si no.
def validate_xml_grammar(element_list, xml_file):
    tags_name = parser.get_all_tags_name(xml_file)
    for name in tags_name:
        if name not in element_list:
            return "Element type " + name + " must be declared."
    return True

#Function: validate_dtd_sons.
#Attribute: element, string, nombre del atributo del archivo dtd.
#Attribute: dtd_sons, list, lista de los hijos que debe tener un atributo de un dtd.
#Attribute: element_sons, list, lista de las etiquetas y sus hijos.
#Return: True si cumple con las condiciones, mensaje de error si no.
def validate_dtd_sons(element, dtd_sons, element_sons):
    error_message = "The content of element type " + element + " must match " + "(" + str(dtd_sons) + ")"
    for dtd_son in dtd_sons:
        if has_symbol(dtd_son):      
            dtd_son_name = dtd_son[:len(dtd_son)-1]
        else:
            dtd_son_name = dtd_son
        for x in element_sons:
            count = 0
            for i in range(0, len(x[1])):
                if parser.find_tag_name(x[1][i]) == dtd_son_name:
                    count += 1
            if dtd_son[len(dtd_son)-1] == "+" and count < 1:
                return error_message
            elif dtd_son[len(dtd_son)-1] == "?" and count > 1:
                return error_message
            elif not has_symbol(dtd_son) and count == 0:
                return error_message
    return True

def validate_dtd(xml_file, dtd_file):
    element_list = []
    attribute_list = []
    father_sons = parser.find_sons(xml_file)
    for dtd_line in dtd_file:
        tag_type = dtd_line[dtd_line.find("!")+1:dtd_line.find(" ")]
        element = get_dtd_name(dtd_line)
        if tag_type == "ELEMENT":     
            if dtd_line.find("#PCDATA") == -1:
                dtd_sons = get_dtd_sons(dtd_line)
                element_sons = parser.find_sons_by_tag_name(father_sons, element, 0)
                validation_result = validate_dtd_sons(element, dtd_sons, element_sons)
                if validation_result is not True:
                    print(validation_result)
                    return False
        elif tag_type == "ATTLIST":
            attribute = get_dtd_attribute(dtd_line)
            attribute_list.append([element, attribute])
        element_list.append(element)
    attribute_validation = validate_xml_attributes(attribute_list, xml_file)
    if attribute_validation is not True:
        print(attribute_validation)
        return False
    grammar_validation = validate_xml_grammar(element_list, xml_file)
    if grammar_validation is not True:
        print(grammar_validation)
        return False
    return True

def start_validation(xml_file, dtd_file):
    xf = list(xml_file).copy()
    df = list(dtd_file).copy()
    if validate_dtd(xf, df):
        print("Good xml!")
    return True




