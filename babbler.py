import random


def gen(odd):
  wsize = random.randint(3, 10)

  if wsize % 2 == 0:
    if odd:
      wsize -= 1
  else:
    if not odd:
      wsize += 1

  return wsize


def genWord(former, latter, wsize):
  str = ''
  isFormer = True
  for _ in range(wsize):
    l = random.choice(former) if isFormer else random.choice(latter)
    str += l
    isFormer = not isFormer
  return str


print("babbler:\n")

a = [chr(ord('a') + i) for i in range(26)]
vowels = "aeio"

consonants = []
for l in a:
  if l not in vowels:
    consonants.append(l)

odd = False
vowelFirst = False
ssize = 10
sentence = []
for i in range(ssize):
  wsize = gen(odd)
  word = genWord(vowels, consonants, wsize) if vowelFirst else genWord(
      consonants, vowels, wsize)
  sentence.append(word)
  odd = not odd
  vowelFirst = not vowelFirst
sentence[0] = sentence[0].capitalize()
sentence = ' '.join(sentence)
sentence += '.'
print(sentence)
