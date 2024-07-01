''' Turing Machine'''
''' 
Autor: José David Velazco Muñoz
'''

''' Numero universal de Turing'''

'''Maquina universal de turing XN+1'''
num_xn_1 =  450813704461563958982113775643437908

'''Maquina universal de turing UN+1'''
num_un_1 =  177642

num =universal_num 
print(bin(num_un_1))
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
    return  [r[1] for r in instr]

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
def letitrun(tape, rules):
    tape = list(tape)
    # Read the symbol in the current position of the tape
    index = 1
    current_symbol = tape[index]
    current_rule = rules[0]
    tape[index] = current_rule[-2]
    while current_rule[-1] != 'STOP':
        index += moveto(current_rule)
        if index >= len(tape):
            tape.append(0)
        if index < 0:
            tape.insert(0, 0)
            index = 0
        current_symbol = tape[index]
       # print('symbol: ',current_symbol)
        # New rule to be applied
        current_rule = nextrule(current_symbol, current_rule, rules)
        #print('xd::: ',current_rule)
        # Replace current symbol depending on the rule
        tape[index] = current_rule[-2]
      #  print(tape)
    return tape
# Helper function to determine the movement of the head
def moveto(rule):
    direction = rule[-1]
    if direction == 'R':
        return 1
    elif direction == 'L':
        return -1
    else:
        return 0
# Helper function to find the next rule to be applied
def nextrule(symbol, lastrule, rules):
    if len(lastrule) < 3:
        raise ValueError("every rule must have at least 3 characters")
    #print(lastrule)
    state = lastrule[:-2] 
    #print('esta',state)# Convertir la lista en una cadena
    nextrule_index = int(str(state[0]) + str(symbol),2) + 1
    #print('nextrule: ',nextrule_index)
    return rules[nextrule_index]

def tape(un,num):
    ceros = '00000'
    separador = '111110'
    tape = ceros + bin(un)[2:] + separador + forma_expandida(num)
    return tape
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
print('Simbolos de subcadenas del numero binario: ',pre_maq)
'''Obtenemos la lista de instrucciones'''
instrucciones = obtener_reglas(pre_maq)
print(instrucciones)
''' Máquina universal de turing U(n,m)'''
termino = convertir_numeros(instrucciones)
print('Terminos: ',termino)
tape = tape(num_xn_1,149)
print('Tape: ',tape)
print('Resultado: ',termino)
next_binary_number = letitrun(tape,instrucciones)
print(next_binary_number)
expandido = forma_expandida(150)
print(expandido)