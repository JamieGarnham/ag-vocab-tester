# vocab tester
import random

dict_1V = {'ἄγω': [['lead', 'drive', 'bring']], 'ἄρχω': [['begin'], ['rule']], 'λύω': [['free', 'loosen', 'release'], ['destroy', 'break'], ['ransom']]}

"""def vocab_tester_1V(run=True):"""

vocab_dict = dict_1V
greek_list = list(vocab_dict.keys())
ready = input("Press any key to start. ")
max_count = 'xxx'
while type(max_count) != int or max_count < 1 or max_count > 1000:
    try:
        max_count = int(input("How many words? "))
        if max_count < 1:
            print('Please enter a number between 1 and 1000')
    except ValueError:
        print('Please enter a valid positive integer.')

if ready:    
    for count in range(max_count):       
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
    
        score = 0
        rerun = False     
        while score in range(distinct_engs):
            target = 'Middle/alternate meaning: '
            if rerun:
                target = 'Try another: '
                rerun = False
            elif score == 0:
                target = 'English meaning: '
                    
            input_eng = input(target)
            if input_eng == 'exit':
                print("Exiting...")
            
            correct = False
            for eng_set in cur_engs:
                if input_eng in eng_set:
                    filled_sets.append(eng_set)
                    cur_engs.remove(eng_set)
                    correct = True
                    score += 1
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