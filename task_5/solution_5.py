front_vow = "eiöü"
back_vow = "aıou"
vows = "aıoueiöü"
harmony = 0
no_harmony = 0
for smth in 'a'*10:
    user_input = input()
    form = ""
    lemma = ""
    pos_t1 = 0
    pos_t2 = 0
    pos_t3 = 0
    count = 0
    last_vow_type = ""
    vows_type = ""
    if user_input == "":
        pass
    else:
        if user_input[0] == '#':
            pass
        else:
            for i in user_input:
                if i == '\t':
                    if pos_t1 == 0:
                        pos_t1 = count
                    else:
                        if pos_t2 == 0:
                            pos_t2 = count
                        else:
                            if pos_t3 == 0: 
                                pos_t3 = count
                count = count + 1
            symbol_pos = 0
            for j in user_input:
                if symbol_pos > pos_t1 and symbol_pos < pos_t2:
                    form = form + j
                if symbol_pos > pos_t2 and symbol_pos < pos_t3:
                    lemma = lemma + j
                symbol_pos = symbol_pos + 1
            symbol_pos = 0
            lemma_len = 0 
            for a in lemma:
                lemma_len = lemma_len + 1
                if a in vows:
                    if a in front_vow:
                        last_vow_type = "front"
                    else:
                        last_vow_type = "back"
            form_beginning = ""
            for i in form:
                if symbol_pos < lemma_len:
                    form_beginning = form_beginning + i
                symbol_pos = symbol_pos + 1
            front_counter = 0
            back_counter = 0
            number_of_vows = 0
            for a in form:
                if a in vows:
                    number_of_vows += 1
                    if a in front_vow:
                        front_counter = front_counter + 1 
                    else:
                        back_counter = back_counter + 1
            if front_counter == number_of_vows:
                vows_type = "front"
            if back_counter == number_of_vows:
                vows_type = "back"
            if lemma != form and lemma == form_beginning:
                if vows_type == last_vow_type:
                    harmony = harmony + 1
                else:
                    no_harmony = no_harmony + 1
print("harmony:", harmony, "no harmony:", no_harmony)
