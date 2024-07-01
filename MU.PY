''' Turing Machine'''
''' 
Autor: José David Velazco Muñoz
'''

''' Numero universal de Turing'''
universal_num = 724485533533931757719839503961571123795236067255655963110814479660650505940424109031048361363235936564444345838222688327876762655614469281411771501784255170755408565768975334635694247848859704693472573998858228382779529468346052106116983594593879188554632644092552550582055598945189071653741489603309675302043155362503498452983232065158304766414213070881939717234151056980262734686429921838172157333482823073453713421475059740345184372359593090640024321077342178851492760797597634415123079586396354492269159479654614711345700145048167337562172573464522731054482980784965126988788964569760906634204477989021914437932830019493570963921703904833270882596201301773727202718625919914428275437422351355675134084222299889374410534305471044368695876405178128019437530813870639942772823156425289237514565443899052780793241144826142357286193118332610656122755531810207511085337633806031082361675045635852164214869542347187426437544428790062485827091240422076538754264454133451748566291574299909502623009733738137724162172747723610206786854002893566085696822620141982486216989026091309402985706001743006700868967590344734174127874255812015493663938996905817738591654055356704092821332221631410978710814599786695997045096818419062994436560151454904880922084480034822492077304030431884298993931352668823496621019471619107014619685231928474820344958977095535611070275817487333272966789987984732840981907648512726310017401667873634776058572450369644348979920344899974556624029374876688397514044516657077500605138839916688140725455446652220507242623923792115253181625125363050931728631422004064571305275802307665183351995689139748137504926429605010013651980186945639498 

'''Maquina universal de turing XN+1'''
num_xn_1 =  450813704461563958982113775643437908

'''Maquina universal de turing UN+1'''
num_un_1 =  177642

num = num_xn_1
''' Convertimos el número a binario'''
bin_num = bin(num)
len_num = len(bin_num) 
#print('Numero binario: ',bin_num)

'''Agregamos la subcadena '110' al principio y al final de la cadena binaria
   del número ingresado'''

num_binario = [1,1,0]
# Agregamos la cadena binaria
for i in range(2, len_num):
    num_binario.append(int(bin_num[i]))
# Agregamos al final 
num_binario.append(1)
num_binario.append(1)
num_binario.append(0)


#print(num_binario)

''' Establecemos las regls en un diccionario'''

reglas = {
      0: [0],
      1: [1, 0],
    "R": [1, 1, 0],
    "L": [1, 1, 1, 0],
 "STOP": [1, 1, 1, 1, 0]}

''' Convertimos las subcadenas de la cadena binaria en las respectivas reglas'''
''' 
Reconoce una secuencia binaria y busca coincidencias con las reglas.
Cada regla busca coincidencias entre un patrón y una proporción de la 
secuencia binaria, se agrega el resultado correspondiente en una lista.
'''

def convert_bin_maq(bin_maq, rules):
    pre_maq = []
    len_bin_maq = len(bin_maq)
    i = 0
    while i < len_bin_maq:
        binary_rule = []
        # Obtaining the regla until zero from bin_maq
        while bin_maq[i] == 1:
            binary_rule.append(bin_maq[i])
            i += 1
      
        # Append a zero since a zero wasn't appended before
        binary_rule.append(0)
        i += 1
        
        # Search for the regla
        for result, binary_pattern in rules.items():
            if binary_rule == binary_pattern:
                pre_maq.append(result)
                break
    
    return pre_maq

''' 
    La función tiene como objetivo tomar una lista con reglas. El proceso
    implica separar cada regla en movimiento, sobrescrituras y estados 
    siguientes, luego generar una nueva estructura de instrucciones. Al
    final se devuelve una lista con las instrucciones en listas dentro 
    de una lista.
'''

def obtener_reglas(pre_maq_rules):
    len_pmr = len(pre_maq_rules)
    spr = []
    i = 0

    # Separar cada regla de las demás
    while i < len_pmr:
        r = []

        # Hasta llegar a un movimiento: 'R', 'L' o 'STOP'
        while pre_maq_rules[i] == 1 or pre_maq_rules[i] == 0:
            r.append(pre_maq_rules[i])
            i += 1

        # Agregar el movimiento
        r.append(pre_maq_rules[i])
        i += 1

        # Agregar la nueva regla a la lista de reglas
        spr.append(r)

    rspr = []

    # Separar movimiento, sobrescritura y ns
    for r in spr:
        lr = len(r)

        # Si la regla tiene solo el movimiento 'R', 'L' o 'STOP'
        if lr == 1:
            rspr.append([0, 0, r[0]])
        else:
            # De lo contrario, obtener el movimiento, sobrescritura y ns
            m = r[lr - 1]
            o = r[lr - 2]
            ns = []

            # Recuperar el siguiente estado hasta la sobrescritura
            for j in range(lr - 2):
                ns.append(r[j])

            # Si ns es una lista vacía
            if not ns:
                ns = 0
            else:
                # De lo contrario, convertirlo a entero
                ns = int("".join(map(str, ns)))

            rspr.append([ns, o, m])

    lrspr = len(rspr)
    instr = []
    j = 0

    for i in range(lrspr):
        sp = rspr[i]
        es_bin = bin(j)[2:]
        es = int(es_bin)

        if i % 2 == 0:
            instr.append([[es, 0], sp])
        else:
            instr.append([[es, 1], sp])
            j += 1
    return  [r[1] for r in instr], instr

def forma_expandida(numero):
    # Convertir el número a su representación binaria sin el prefijo '0b'
    binario_str = bin(numero)[2:]
    # Inicializar la cadena expandida
    expandido_str = ""
    # Recorrer cada dígito del número binario
    for digito in binario_str:
        # Si el dígito es '0', agregar un '0' a la cadena expandida
        if digito == '0':
            expandido_str += '0'
            continue
        # Si el dígito es '1', agregar '10' a la cadena expandida
        expandido_str += "10"
    return expandido_str
def MUT(cinta_de_entrada,reglas):
    estado_actual = 0  # Estado actual
    caja_actual = -1  # Caja actual en la cinta
    movimiento_actual = 'R'  # Movimiento actual

    while movimiento_actual != 'STOP':
        if movimiento_actual == 'R':
            caja_actual += 1  # Si es DERECHA, moverse a la siguiente caja
        elif movimiento_actual == 'L':
            caja_actual -= 1  # Si es IZQUIERDA, moverse a la caja anterior

        simbolo_actual = cinta_de_entrada[caja_actual]  # Leer el contenido de la caja actual en la entrada

        # Buscar en las reglas correspondientes
        regla_encontrada = -1
        for regla in reglas:
            estado = regla[0][0]  # Estado
            simbolo = regla[0][1]  # Símbolo leído

            if estado_actual == estado and simbolo_actual == simbolo:
                regla_encontrada = regla[1]  # Devolver resultado

        siguiente_estado = regla_encontrada[0]  # Siguiente estado
        simbolo_sobrescribir = regla_encontrada[1]  # Símbolo a sobrescribir
        movimiento_actual = regla_encontrada[2]  # Siguiente movimiento

        # Actualizar el estado actual y sobrescribir el símbolo
        estado_actual = siguiente_estado
        cinta_de_entrada[caja_actual] = simbolo_sobrescribir

    return cinta_de_entrada

def tape(un,num):
    ceros = '0'
    separador = '111110'
    tape = ceros + bin(un)[2:] + separador + forma_expandida(num)
    tapes = []
    for catacter in tape:
        tapes.append(int(catacter))
    return tapes
def convertir_numeros(lista_original):
    lista_nueva = []
    for elemento in lista_original:
        nuevo_elemento = []
        for item in elemento:
            if isinstance(item, int):
                nuevo_elemento.extend([int(digito) for digito in str(item)])
            else:
                nuevo_elemento.append(item)
        lista_nueva.append(nuevo_elemento)
    return lista_nueva

''' Conversion de las subcadenas a simbolos de regla'''
pre_maq = convert_bin_maq(num_binario,reglas)
#print('Simbolos de subcadenas del numero binario: ',pre_maq)
'''Obtenemos la lista de instrucciones'''
instrucciones,instr = obtener_reglas(pre_maq)
#print(instrucciones)
#print('Estas son: ',instr)
''' Máquina universal de turing U(n,m)'''
#termino = convertir_numeros(instrucciones)
#print('Terminos: ',termino)
#tape = tape(num_xn_1,149)
print('Tape int: ',[0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0])
#print('Resultado: ',termino)
next_binary_number = MUT([0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],instr)
print('Tape out: ',next_binary_number)
#expandido = forma_expandida(150)
#print(expandido)