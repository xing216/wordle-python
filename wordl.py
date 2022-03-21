import json
import random

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

word = "three"
# with open("words.json", "r") as f:
#     words = json.load(f)
#     index = random.randint(0, 10663)
#     word = words[index]

tries = 0
tries_limit = 5
letter_count = {}
for h in word:
    if h not in letter_count:
        letter_count[h] = 1
    else:
        letter_count[h] += 1
while tries < tries_limit:
    guess = input(f"Try {tries+1}: ")
    num_of_correct = 0
    correct = []
    misplaced = []
    incorrect = []
    letter_used_count = {}
    result = []
    for k in guess:
        if k not in letter_used_count:
            letter_used_count[k] = 1
        else:
            letter_used_count[k] += 1
    for i,j in enumerate(guess):
        if j == word[i] and letter_count[j] <= letter_used_count[j]:
            correct.append(j)
            result.append(f"{bcolors.GREEN}{j}{bcolors.ENDC}")
            num_of_correct +=1
        elif j in word and j not in misplaced and j not in correct and letter_count[j] <= letter_used_count[j]:
            misplaced.append(j)
            result.append(f"{bcolors.BLUE}{j}{bcolors.ENDC}")
        elif j not in incorrect:
            incorrect.append(j)
            result.append(f"{bcolors.FAIL}{j}{bcolors.ENDC}")
    if num_of_correct == 5:
        print(f"Yay! You got all 5 letters: {word}")
        break
    else:
        print(f"{''.join(result)}")
    tries +=1
