import json
import os

def convert_to_glue_format(args):
    
    if not os.path.isdir(args.tmp_data_dir):
        os.mkdir(args.tmp_data_dir)
    
    fp_ont = open(os.path.join(args.data_dir, "ontology_sumbt.json"), "r")
    ontology = json.load(fp_ont)
 #   ontology = ontology["informable"]
  #  ontology
    for slot in ontology.keys():
        if "informable" in slot:
            ontology[slot].append("dontcare")
    fp_ont.close()

    print(args.tmp_data_dir)

    ### Read woz logs and write to tsv files
    if os.path.exists(os.path.join(args.tmp_data_dir, "train.tsv")):
        print('data has been processed!')
        return 0


    source_files = [os.path.join(args.data_dir,"train.json"), os.path.join(args.data_dir,"dev.json"), os.path.join(args.data_dir,"test.json")]
    target_files = [os.path.join(args.tmp_data_dir,"train.tsv"), os.path.join(args.tmp_data_dir,"dev.tsv"),os.path.join(args.tmp_data_dir, "test.tsv")]
    
    target_slots = ['informable-essen', 'informable-gegend', 'informable-preisklasse', 'request-adresse', 'request-essen', 'request-gegend', 'request-name', 'request-postleitzahl', 'request-preisklasse', 'request-telefon']


    

    
    for idx, src in enumerate(source_files):
        
        trg = target_files[idx]
    
        fp_src = open(src, "r")
        fp_trg = open(trg, "w")
    
        data = json.load(fp_src)
#        fp_trg.write('# Dialogue ID\tTurn Index\tUser Utterance\tSystem Response\t')
#        fp_trg.write('\n')


        for dialogue in data:
            dialogue_idx = dialogue["dialogue_idx"]
            for turn in dialogue["dialogue"]:
                turn_idx = turn["turn_idx"]
                user_utterance = turn["transcript"]
                system_response = turn["system_transcript"]
                belief_state = turn["belief_state"]
    
                # initialize turn label and belief state to "none"
                belief_st = {}
                for ts in target_slots:
                    belief_st[ts] = "none"
                
    
                # extract slot values in belief state
                for bs in belief_state:
                    for slots in bs["slots"]:
                        if "informable-" + slots[0] in belief_st:
                            #if slots[1] == "center": slots[1] = "centre"
                            #if slots[1] == "east side": slots[1] = "east"
                            #if slots[1] == "corsican": slots[1] = "corsica"
                            #if slots[1] == " expensive": slots[1] = "expensive"
                            if slots[1] == "dontcare": slots[1] = "do not care"
    
                            assert(belief_st["informable-"+slots[0]] == "none" or belief_st["informable-"+slots[0]] == slots[1])
                            #assert(slots[1] in ontology["informable-"+slots[0]])
                            belief_st["informable-" + slots[0]] = slots[1]
                        if slots[0] == "slot":
                            belief_st["request-"+str(slots[1])] = "yes"
    
                fp_trg.write(str(dialogue_idx))                 # 0: dialogue index
                fp_trg.write("\t" + str(turn_idx))              # 1: turn index
                fp_trg.write("\t" + str(user_utterance.replace("\t", " ")))        # 2: user utterance
                fp_trg.write("\t" + str(system_response.replace("\t", " ")))       # 3: system response
    
                for slot in sorted(belief_st.keys()):
                    fp_trg.write("\t" + str(belief_st[slot]))   # 4-14: belief state
    
                fp_trg.write("\n")
                fp_trg.flush()
    
        fp_src.close()
        fp_trg.close()
