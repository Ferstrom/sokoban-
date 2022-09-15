def aplanador (llst): 
    lista_plana = []
    for elem in llst:
        if isinstance (elem, list):
            lista_plana.extend(aplanador(elem))
        else:
            list.append(elem)
    return lista_plana
