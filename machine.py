def UM(tape, rules):
    tape = list(tape)
    rules = list(rules)
    index = 0
    current_symbol = tape[index]
    current_rule = rules
    print(tape[index])
    tape[index] = str(current_rule[-2])
    
    while current_rule[-1] != 'STOP':
        index += moveto(current_rule)
        
        if index >= len(tape):
            tape.append('0')
        
        if index < 0:
            tape.insert(0, '0')
            index = 0
        
        current_symbol = tape[index]
        print('current_symbol: ',current_symbol)
        print('current_rule: ',current_rule)
        current_rule = nextrule1(current_symbol, current_rule, rules)
        print('Aqui: ',current_rule)
        tape[index] = str(current_rule[-2])
    
    return tape


'''''aqui '''

def nextrule(symbol, lastrule, rules):
    if len(lastrule) < 3:
        raise ValueError("every rule must have at least 3 characters")
    
    state = lastrule[:-2]
    print('estado: ',state)
    binary_number = ''.join(str(symbol) for symbol in state)
    nextrule_index = int(binary_number + str(symbol), 2) 
    print('este: ',nextrule_index)
    return rules[nextrule_index]

def nextrule1(symbol, rule, rules):
    for i in range(len(rules)):
        if rules[i][0] == symbol and rules[i][1] == rule[-1]:
            return rules[i]

def moveto(rule):
    if rule[-1] == 'R':
        return 1
    elif rule[-1] == 'L':
        return -1
    else:
        return 0
universal_num = 7244855335339317577198395039615711237952360672556559631108144796606505059404241090310483613632359365644443458382226883278767626556144692814117715017842551707554085657689753346356942478488597046934725739988582283827795294683460521061169835945938791885546326440925525505820555989451890716537414896033096753020431553625034984529832320651583047664142130708819329717234151056980262734686429921838172157333482823073453713421475059740345184372359593090640024321077342178851492760797597634415123079586396354492269159479654614711345700145048167337562172573464522731054482980784965126988788964569760906634204477989021914437932830019493570963921703904833270882596201301773727202718625919914428275437422351355675134084222299889374410534305471044368695876405178128019437530813870639942772823156425289237514565443899052780793241144826142357286193118332610656122755531810207511085337633806031082361675045635852164214869542347187426437544428790062485827091240422076538754264454133451748566291574299909502623009733738137724162172747723610206786854002893566085696822620141982486216989026091309402985706001743006700868967590344734174127874255812015493663938996905817738591654055356704092821332221631410978710814599786695997045096818419062994436560151454904880922084480034822492077304030431884298993931352668823496621019471619107014619685231928474820344958977095535611070275817487333272966789987984732840981907648512726310017401667873634776058572450369644348979920344899974556624029374876688397514044516657077500605138839916688140725455446652220507242623923792115253181625125363050931728631422004064571305275802307665183351995689139748137504926429605010013651980186945639498

def UM(tape, rules):
    tape = list(tape)
    rules = list(rules)
    index = 0
    current_symbol = tape[index]
    current_rule = rules

    tape[index] = str(current_rule[-2])
    
    while current_rule[-1] != 'STOP':
        index += moveto(current_rule)
        
        if index >= len(tape):
            tape.append('0')
        
        if index < 0:
            tape.insert(0, '0')
            index = 0
        
        current_symbol = tape[index]
        print('current_symbol: ',current_symbol)
        print('current_rule: ',current_rule)
        current_rule = nextrule(current_symbol, current_rule, rules)
        print('Aqui: ',current_rule)
        tape[index] = str(current_rule[-2])
    return tape