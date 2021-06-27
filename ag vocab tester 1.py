# vocab tester
import random

dict_1V = {'ἄγω': [['lead', 'drive', 'bring']], 'ἄρχω': [['begin'], ['rule']], 'λύω': [['free', 'loosen', 'release'], ['destroy', 'break'], ['ransom']]}

"""def vocab_tester_1V(run=True):"""

vocab_dict = dict_1V
greek_list = list(vocab_dict.keys())

ready = input("Press any key to start." )

if ready:    
    while True:       
        n = random.randint(0, len(greek_list) - 1)
        cur_greek = greek_list[n]
        cur_engs = vocab_dict[cur_greek]
        filled_sets = []
        distinct_engs = len(cur_engs)
        
        correct_str_list = []
        for eng_set in cur_engs:
            correct_str = ", ".join(eng_set)
            correct_str_list.append(correct_str)
        correct_strs = "; ".join(correct_str_list)
        print("   ~")
        print(f"'{cur_greek}':")
    
        i = 0
        rerun = False     
        while i in range(distinct_engs):

            if rerun:
                input_eng = input('Try another: ')
                rerun = False
            elif i == 0:
                input_eng = input('English meaning: ')
            else:
                input_eng = input('Middle/alternate meaning: ')
            
            correct = False
            for eng_set in cur_engs:
                if input_eng in eng_set:
                    filled_sets.append(eng_set)
                    cur_engs.remove(eng_set)
                    correct = True
                    i += 1
                    print('Correct!')
                    break
                
            if not correct:
                for filled_set in filled_sets:
                    if input_eng in filled_set:
                        rerun = True
                        print('Yes, but think outside the square.')
                        break
                if not rerun:
                    print('Incorrect!')
                    print(f"Correct answers are: {correct_strs}")
                    break                    