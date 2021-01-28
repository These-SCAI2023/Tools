import time

def lire_fichier (chemin):
    f = open(chemin , encoding = 'utf−8')
    chaine = f.read ()
    f.close ()
    #print(chaine)
    return chaine
        


def cer(ref, hyp ,debug=False):
    a = 0
    b=0
    liste_caract_r=[]
    r = ref.split()
    #print(r)
    for a in r :
        for b in a :
            liste_caract_r.append(b)
    # print(liste_caract)
    r= liste_caract_r
    print(r)
   
    x = 0
    z=0
    liste_caract_h=[]
    h = hyp.split()
    for x in h :
        for z in x :
            liste_caract_h.append(z)
    # print(liste_caract)
    h= liste_caract_h
    print(h)
    
    
    #costs will holds the costs, like in the Levenshtein distance algorithm
    costs = [[0 for inner in range(len(h)+1)] for outer in range(len(r)+1)]
    # backtrace will hold the operations we've done.
    # so we could later backtrace, like the WER algorithm requires us to.
    backtrace = [[0 for inner in range(len(h)+1)] for outer in range(len(r)+1)]

    OP_OK = 0
    OP_SUB = 1
    OP_INS = 2
    OP_DEL = 3

    DEL_PENALTY=1 # Tact
    INS_PENALTY=1 # Tact
    SUB_PENALTY=1 # Tact
    # First column represents the case where we achieve zero
    # hypothesis words by deleting all reference words.
    for i in range(1, len(r)+1):
        costs[i][0] = DEL_PENALTY*i
        backtrace[i][0] = OP_DEL

    # First row represents the case where we achieve the hypothesis
    # by inserting all hypothesis words into a zero-length reference.
    for j in range(1, len(h) + 1):
        costs[0][j] = INS_PENALTY * j
        backtrace[0][j] = OP_INS

    # computation
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                costs[i][j] = costs[i-1][j-1]
                backtrace[i][j] = OP_OK
            else:
                substitutionCost = costs[i-1][j-1] + SUB_PENALTY # penalty is always 1
                insertionCost    = costs[i][j-1] + INS_PENALTY   # penalty is always 1
                deletionCost     = costs[i-1][j] + DEL_PENALTY   # penalty is always 1

                costs[i][j] = min(substitutionCost, insertionCost, deletionCost)
                if costs[i][j] == substitutionCost:
                    backtrace[i][j] = OP_SUB
                elif costs[i][j] == insertionCost:
                    backtrace[i][j] = OP_INS
                else:
                    backtrace[i][j] = OP_DEL

    # back trace though the best route:
    i = len(r)
    j = len(h)
    numSub = 0
    numDel = 0
    numIns = 0
    numCor = 0
    if debug:
        print("OP\tREF\tHYP")
        lines = []
    while i > 0 or j > 0:
        if backtrace[i][j] == OP_OK:
            numCor += 1
            i-=1
            j-=1
            if debug:
                lines.append("OK\t" + r[i]+"\t"+h[j])
        elif backtrace[i][j] == OP_SUB:
            numSub +=1
            i-=1
            j-=1
            if debug:
                lines.append("SUB\t" + r[i]+"\t"+h[j])
        elif backtrace[i][j] == OP_INS:
            numIns += 1
            j-=1
            if debug:
                lines.append("INS\t" + "****" + "\t" + h[j])
        elif backtrace[i][j] == OP_DEL:
            numDel += 1
            i-=1
            if debug:
                lines.append("DEL\t" + r[i]+"\t"+"****")
    if debug:
        lines = reversed(lines)
        for line in lines:
            print(line)
        print("Ncor " + str(numCor))
        print("Nsub " + str(numSub))
        print("Ndel " + str(numDel))
        print("Nins " + str(numIns))
    return (numSub + numDel + numIns) / (float) (len(r))
    wer_result = round( (numSub + numDel + numIns) / (float) (len(r)), 3)
    return {'WER':wer_result, 'Cor':numCor, 'Sub':numSub, 'Ins':numIns, 'Del':numDel}

start_time=time.time()
res_txt_propre = lire_fichier("./data/aimard_resultat_en_propre1L_without_virg.txt")
hypothese_ocr = lire_fichier("./data_ocr/aimard_resultat_en_ocr_sans_ajout1L_witoutvirg.txt")
# res_txt_propre = lire_fichiers("./output_propre/*")
# hypothese_ocr = lire_fichiers("./output_ocr/*")
resultat_cer=cer(res_txt_propre, hypothese_ocr)
#resultat_wer=wer("/home/antonomaz/Documents/SORBONNE/Doctorat/EXPE_PROGRA_2020_2021/EXPE_COMPARE_TXTBRUIT/test_extraction_propre/output/output_resultat_propre_alignement.txt","/home/antonomaz/Documents/SORBONNE/Doctorat/EXPE_PROGRA_2020_2021/EXPE_COMPARE_TXTBRUIT/test_extraction_propre/output/output_resultat_ocr_alignement.txt")
print(resultat_cer)
interval = time.time() - start_time 
    
print(interval)

 
