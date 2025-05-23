def remove_elements(list_to_remove_elements):
    lista= []

    for i in range(len(list_to_remove_elements)):

        if i != 0 and i != 4 and i!= 5:
            lista.append(list_to_remove_elements[i])

    return lista



def add_elements(list_to_add_elements):
    
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")

    return list_to_add_elements


def is_empty(list_to_check):

    if len(list_to_check) == 0:
        return "Lista vacía" 


def check_lists(list_to_compare1, list_to_compare2):
    
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2: 
        if list_to_compare1[2] != list_to_compare2[2]:
            return False


        elif list_to_compare1[2] == list_to_compare2[2]:
            return True


def list_of_lists(list_of_lists_to_modify):
    
    lista = []

    if len(list_of_lists_to_modify) >= 3:

        lista.append(list_of_lists_to_modify[0][:2])
        lista.append(list_of_lists_to_modify[1][1:4])
        lista.append(list_of_lists_to_modify[2][-2:])

    return lista

