import string

#input example
sentence = 'bror brug selge'
print("Kata yang dimasukan :",sentence)
input_string = sentence.lower()+'#'

#initialization
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35']

transition_table = {}

for state in state_list:
  for alphabet in alphabet_list:
    transition_table[(state, alphabet)] = 'error'
  transition_table[(state, '#')] = 'error'
  transition_table[(state, ' ')] = 'error'

#spacing string
transition_table['q0', ' '] = 'q0'
transition_table['q14', ' '] = 'q20'
transition_table['q6', ' '] = 'q20'
transition_table['q11', ' '] = 'q20'
transition_table['q19', ' '] = 'q20'
transition_table['q20', ' '] = 'q20'
transition_table['q24', ' '] = 'q20'
transition_table['q28', ' '] = 'q20'

#transition table for following token
transition_table['q0', 't'] = 'q12'
transition_table['q12', 'o'] = 'q13'
transition_table['q13', 'j'] = 'q14'
transition_table['q0', 's'] = 'q1'
transition_table['q1', 'k'] = 'q10'
transition_table['q10', 'o'] = 'q11'
transition_table['q1', 'o'] = 'q2'
transition_table['q2', 's'] = 'q3'
transition_table['q3', 't'] = 'q4'
transition_table['q4', 'e'] = 'q5'
transition_table['q5', 'r'] = 'q6'
transition_table['q0', 'b'] = 'q7'
transition_table['q7', 'r'] = 'q8'
transition_table['q8', 'o'] = 'q5'
transition_table['q0', 'm'] = 'q21'
transition_table['q21', 'o'] = 'q5'
transition_table['q0', 'f'] = 'q9'
transition_table['q9', 'a'] = 'q5'
transition_table['q0', 'j'] = 'q15'
transition_table['q15', 'a'] = 'q16'
transition_table['q16', 'k'] = 'q17'
transition_table['q17', 'k'] = 'q18'
transition_table['q18', 'e'] = 'q19'
transition_table['q8', 'u'] = 'q23'
transition_table['q23', 'g'] = 'q24'
transition_table['q0', 'v'] = 'q25'
transition_table['q25', 'a'] = 'q26'
transition_table['q26', 's'] = 'q27'
transition_table['q27', 'k'] = 'q28'
transition_table['q1', 'e'] = 'q30'
transition_table['q30', 'l'] = 'q31'
transition_table['q31', 'g'] = 'q32'
transition_table['q32', 'e'] = 'q33'
transition_table['q0', 'k'] = 'q34'
transition_table['q34', 'o'] = 'q35'
transition_table['q35', 'b'] = 'q18'

#transition table for new token
transition_table['q20', 'f'] = 'q9'
transition_table['q20', 's'] = 'q1'
transition_table['q20', 'b'] = 'q7'
transition_table['q20', 'm'] = 'q21'
transition_table['q20', 't'] = 'q12'
transition_table['q20', 'v'] = 'q25'
transition_table['q20', 'k'] = 'q34'
transition_table['q20', 'j'] = 'q15'

#transition table Last
transition_table['q11', '#'] = 'accept'
transition_table['q6', '#'] = 'accept'
transition_table['q24', '#'] = 'accept'
transition_table['q20', '#'] = 'accept'
transition_table['q28', '#'] = 'accept'
transition_table['q14', '#'] = 'accept'
transition_table['q19', '#'] = 'accept'
transition_table['q33', '#'] = 'accept'

#lexical analysis
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept':
  current_char = input_string[idx_char]
  current_token += current_char
  state = transition_table[(state, current_char)]
  if state=='q11' or state=='q6' or state=='q24' or state=='q28' or state=='q14' or state=='q19' or state=='q33':
    print('current token: ', current_token, ', valid')
    current_token = ''
  if state =="error":
    print("error")
    break
  idx_char = idx_char + 1

#conclusion
if state == "accept":
  print('semua token diinput: ', sentence, ', valid')