#input example
sentence = input('Masukkan Kalimat: ')
tokens = sentence.lower().split()
tokens.append('EOS')

#symbol definition
non_terminal = ['S', 'NN', 'VB']
terminal = ['bror', 'soster', 'far', 'mor', 'sko', 'jakke', 'toj', 'brug', 'selge', 'kobe', 'vask']

#parse table definition
parse_table = {}

parse_table[('S', 'bror')] = ['NN', 'VB', 'NN']
parse_table[('S', 'soster')] = ['NN', 'VB', 'NN']
parse_table[('S', 'far')] = ['NN', 'VB', 'NN']
parse_table[('S', 'mor')] = ['NN', 'VB', 'NN']
parse_table[('S', 'sko')] = ['NN', 'VB', 'NN']
parse_table[('S', 'jakke')] = ['NN', 'VB', 'NN']
parse_table[('S', 'toj')] = ['NN', 'VB', 'NN']
parse_table[('S', 'brug')] = ['error']
parse_table[('S', 'selge')] = ['error']
parse_table[('S', 'kobe')] = ['error']
parse_table[('S', 'vask')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'bror')] = ['bror']
parse_table[('NN', 'soster')] = ['soster']
parse_table[('NN', 'far')] = ['far']
parse_table[('NN', 'mor')] = ['mor']
parse_table[('NN', 'sko')] = ['sko']
parse_table[('NN', 'jakke')] = ['jakke']
parse_table[('NN', 'toj')] = ['toj']
parse_table[('NN', 'brug')] = ['error']
parse_table[('NN', 'selge')] = ['error']
parse_table[('NN', 'kobe')] = ['error']
parse_table[('NN', 'vask')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'bror')] = ['error']
parse_table[('VB', 'soster')] = ['error']
parse_table[('VB', 'far')] = ['error']
parse_table[('VB', 'mor')] = ['error']
parse_table[('VB', 'sko')] = ['error']
parse_table[('VB', 'jakke')] = ['error']
parse_table[('VB', 'toj')] = ['error']
parse_table[('VB', 'brug')] = ['brug']
parse_table[('VB', 'selge')] = ['selge']
parse_table[('VB', 'kobe')] = ['kobe']
parse_table[('VB', 'vask')] = ['vask']
parse_table[('VB', 'EOS')] = ['error']

#stack initilization
stack = []
stack.append('#')
stack.append('S')

#input reading initilization
idx_token = 0
symbol = tokens[idx_token]

#parsing process
while (len(stack) > 0):
  top = stack[len(stack)-1]
  print('top = ', top)
  print('symbol =', symbol)
  if top in terminal:
    print('top adalah simbol terminal')
    if top == symbol:
      stack.pop()
      idx_token = idx_token + 1
      symbol = tokens[idx_token]
      if symbol == 'EOS':
        print('isi stack: ', stack)
        stack.pop()
    else:
      print('error')
      break;
  elif top in non_terminal:
    print('top adalah simbol non terminal')
    if parse_table[(top, symbol)][0] != 'error':
      stack.pop()
      symbol_to_be_pushed = parse_table[(top, symbol)]
      for i in range(len(symbol_to_be_pushed)-1,-1,-1):
        stack.append(symbol_to_be_pushed[i])
    else:
      print('error')
      break;
  else:
    print('error')
    break;
  print('isi stack: ', stack, '\n')

#conclusion
if symbol == 'EOS' and len(stack)==0:
  print('input string: ', sentence, ' diterima, sesuai Grammar')
else:
  print('Error, input string: ', sentence, ' tidak diterima, tidak sesuai Grammar')