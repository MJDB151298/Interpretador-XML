def find_tag_name(line):
    search = line.strip()
    opening_tag_index = search.find("<")
    closing_tag_index = search.find(">")
    closing_line_index = search.find("/")
    if closing_line_index < closing_tag_index and closing_line_index != -1:
        return search[closing_line_index+1 : closing_tag_index] 
    else:
        first_space_index = search.find(" ")
        return {True: search[opening_tag_index+1:closing_tag_index], False: search[opening_tag_index+1:first_space_index]} [closing_tag_index <= first_space_index or first_space_index == -1]

def get_all_tags_name(xml_file):
    result = []
    for xml_line in xml_file:
        if is_not_empty(xml_line):
            result.append(find_tag_name(xml_line))
    return result

def find_tag_key(line):
    search = line.strip()
    equal_index = search.find("=")
    if equal_index != -1:
        first_space_index = search.find(" ")
        second_space_index = search.find(" ", first_space_index+1)
        return search[first_space_index+1 : second_space_index]
    return ""

def find_tag_value(line):
    search = line.strip()
    equal_index = search.find("=")
    if equal_index != -1:
        opening_index = search.find("'")
        closing_index = search.find("'", opening_index+1)
        return search[opening_index+1 : closing_index]
    return ""

def find_tag_content(line):
    search = line.strip()
    closing_tag_index = search.find(">")
    opening_closing_tag_index = search.find("<", closing_tag_index+1)
    return search[closing_tag_index+1:opening_closing_tag_index]

def get_tags_info(xml_file):
    result = []
    for xml_line in xml_file:
        name = find_tag_name(xml_line)
        if is_not_empty(xml_line) and not is_only_closing_tag(xml_line, name):
            result.append({
                "name": find_tag_name(xml_line),
                "key": find_tag_key(xml_line),
                "value": find_tag_value(xml_line),
                "content": find_tag_content(xml_line)
            })
    return result

def get_tabs(line):
    opening_tag_index = line.find("<")
    return len(line[:opening_tag_index])

def is_not_empty(line):
    return (True, False) [len(line.strip()) == 0]

def is_only_closing_tag(line, name):
    return (False, True) [line.strip() == "</"+name+">"]

def find_sons(xml_file):
    father_sons = []
    for i in range(0, len(xml_file)):
        line_tabs = get_tabs(xml_file[i])
        if i+1 != len(xml_file) and get_tabs(xml_file[i+1]) > line_tabs and is_not_empty(xml_file[i]):
            father = xml_file[i].strip()
            sons = []
            for j in range(i+1, len(xml_file)):
                son_tabs = get_tabs(xml_file[j])
                son_name = find_tag_name(xml_file[j])
                if line_tabs == son_tabs:
                    break 
                if son_tabs == line_tabs+4 and not is_only_closing_tag(xml_file[j], son_name):
                    sons.append(xml_file[j].strip())
            father_sons.append([father, sons])
        elif not is_only_closing_tag(xml_file[i], find_tag_name(xml_file[i])) and is_not_empty(xml_file[i]):
            father_sons.append([xml_file[i].strip(), []])
    return father_sons

def find_sons_by_tag_name(father_sons, tag_name, count):
    hits = 0
    result = []
    for x in father_sons:
        if find_tag_name(x[0]) == tag_name:
            if count != 0:
                hits += 1
                result.append(x)
                if hits == count:
                    break
            else:
                result.append(x)
    return result
    
#print(find_sons_by_tag_name(result, "ingredientes", 2))