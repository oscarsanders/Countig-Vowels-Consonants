consonants = ["B","C","D","F","G","H","J","K","L",
               "M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]
vowels = ["A","E","I","O","U"]

word = input("Write the sentence: ").upper()

def check_word(any_word):
  num_vocals = 0
  num_cons = 0
  num_letters = len(word)
  word_lst = list(any_word)
  for char in word_lst:
    if char in consonants:
      num_cons += 1
    elif char in vowels:
      num_vocals += 1
    elif char == ' ':
      num_letters -= 1
  return num_cons, num_vocals, num_letters

nc, nv, nl = check_word(word)
print(f"The word '{word}' have {nl} letters")
print(f"Consonants = {nc}")
print(f"Vowels = {nv}")

