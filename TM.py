#Number of the Turing Machine
num_maq = 177642
num_maq= 450813704461563958982113775643437908
#num_maq=724485533533931757719839503961571123795236067255655963110814479660650505940424109031048361363235936564444345838222688327876762655614469281411771501784255170755408565768975334635694247848859704693472573998858228382779529468346052106116983594593879188554632644092552550582055598945189071653741489603309675302043155362503498452983232065158304766414213070881939717234151056980262734686429921838172157333482823073453713421475059740345184372359593090640024321077342178851492760797597634415123079586396354492269159479654614711345700145048167337562172573464522731054482980784965126988788964569760906634204477989021914437932830019493570963921703904833270882596201301773727202718625919914428275437422351355675134084222299889374410534305471044368695876405178128019437530813870639942772823156425289237514565443899052780793241144826142357286193118332610656122755531810207511085337633806031082361675045635852164214869542347187426437544428790062485827091240422076538754264454133451748566291574299909502623009733738137724162172747723610206786854002893566085696822620141982486216989026091309402985706001743006700868967590344734174127874255812015493663938996905817738591654055356704092821332221631410978710814599786695997045096818419062994436560151454904880922084480034822492077304030431884298993931352668823496621019471619107014619685231928474820344958977095535611070275817487333272966789987984732840981907648512726310017401667873634776058572450369644348979920344899974556624029374876688397514044516657077500605138839916688140725455446652220507242623923792115253181625125363050931728631422004064571305275802307665183351995689139748137504926429605010013651980186945639498 


#Some examples of Turing Machines
# XN + 1: 450813704461563958982113775643437908
# XN * 2: 10389728107
# UN + 1:  177642
# UN * 2: 1492923420919872026917547669

bin_nm = bin(num_maq) # Machine Binary number
len_bnm = len(bin_nm) # Length binary number

# Drop first two boxes of bin_nm '0b...'
bin_maq = [] # New machine binary number

# Initializing machine in extended binary (with RIGHT instruction: 110)
bin_maq.append(1)
bin_maq.append(1)
bin_maq.append(0)

#Then add the rest of the binary number
for i in range(2, len_bnm):
    bin_maq.append(int(bin_nm[i]))

#Finally, add the finalization of the machine (with RIGHT instruction: 110)
bin_maq.append(1)
bin_maq.append(1)
bin_maq.append(0)
# Rules of extended binary
rules = []
rules.append([0, [0]])
rules.append([1, [1, 0]])
rules.append(['R', [1, 1, 0]])
rules.append(['L', [1, 1, 1, 0]])
rules.append(['STOP', [1, 1, 1, 1, 0]])
# Convert bin_maq from extended binary in second part rules
pre_maq = []
len_bem = len(bin_maq)
i = 0
while i < len_bem:
    biin = []
    
    # Getting the rule until zero from bin_maq
    while bin_maq[i] == 1:
        biin.append(bin_maq[i])
        i += 1
    
    # Append a zero 'cause a zero wasn't appended before
    biin.append(0)
    i += 1
    
    # Search rule
    for r in rules:
        res = r[0]
        bnn = r[1]
        
        if biin == bnn:
            pre_maq.append(res)
            break;
# Convert pre_maq in a set of rules
len_pmaq = len(pre_maq)
second_part_rules = []
i = 0

# Separate each rule from others
while i < len_pmaq:
    sp_rule = []
    
    # Until a move: 'R', 'L' or 'STOP'
    while pre_maq[i] == 1 or pre_maq[i] == 0:
        sp_rule.append(pre_maq[i])
        i += 1
    
    # Add the move
    sp_rule.append(pre_maq[i])
    i += 1
    
    #Adding the new rule to the list of rules
    second_part_rules.append(sp_rule)

real_spr = []

# Separate move, overwrite and next_state
for r in second_part_rules:
    len_r = len(r)
    
    # If the rule have only the move 'R', 'L' or 'STOP'
    if len_r == 1:
        real_spr.append([0, 0, r[0]])
    else:
        # Else, get the move, overwrite and next_state
        move = r[len_r - 1]
        overwrite = r[len_r - 2]
        
        next_state = []
        # Recover next state until the overwrite
        for j in range(len_r - 2):
            next_state.append(r[j])
        
        # If next_state is a empty list
        if next_state == []:
            next_state = 0
        else:
            # Else, convert it into an int
            s = [str(ns) for ns in next_state]
            astr = "".join(s)
            next_state = int(astr)
        
        real_spr.append([next_state, overwrite, move])
        len_rspr = len(real_spr)
the_rules = []

j = 0
for i in range(len_rspr):
    second_part = real_spr[i]
    
    # current_state_bin
    current_state_bin = bin(j)
    lb = len(current_state_bin)
    listb = []
    
    # From str bin to int bin
    for w in range(2, lb):
        listb.append(current_state_bin[w])
    
    astr = "".join(listb)
    current_state = int(astr)
    
    if i % 2 == 0:
        the_rules.append([[current_state, 0], second_part])
    else:
        the_rules.append([[current_state, 1], second_part])
        j += 1

print(the_rules)
inpt = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Input tape

inpt2 = inpt[:]

state = 0 # Current state
cas = -1 # Current box in the tape
mov = 'R' # Current movement
while mov != "STOP": # While the rules does not indicate to STOP
    if mov == 'R':
        cas += 1 # If RIGHT, move to the the next box
    elif mov == 'L':
        cas -= 1 # If LEFT, move to the previous box

    read = inpt[cas] # Read the current box in the input
    
    # Look into the corresponding state
    get_res = -1
    for r in the_rules:
        s = r[0][0] ## state
        re = r[0][1] ## read
        
        if state == s and read == re: 
            get_res = r[1] # Return result
    
    next_state = get_res[0] # Next state
    subw = get_res[1] # Symbol to overwrite
    mov = get_res[2] # Next movement
    
    # Printing during performance
    print("Current box:", cas, "Input:", inpt)
    print("Current state:", state, "Read:", read, "->", "Next state:", next_state, "Overwrite:", subw, "Mov read box:", mov)
    
    # Next
    state = next_state # Reasigning new state
    inpt[cas] = subw # Performing overwritting
    print("Output state:", inpt, "\n")

print("Input:", inpt2)
print("Output:", inpt)