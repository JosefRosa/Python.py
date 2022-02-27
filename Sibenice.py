import random

def draw_man(progress):
	
	if progress == 0:
		print("Pocet pismen:")
		return
	for i in range(0, progress): 
		if i == 0:
			print(" O")
		elif i == 1 and progress == 2:
			print(" |")
		elif i == 2 and progress == 3:
			print("/|") 
		elif i == 3 and progress >= 4:
			print("/|\\")
		elif i == 4 and progress == 5:
			print("/")
			print("Jejda.")
		elif i == 5 and progress == 6:
			print("/ \\")
	return


category = random.choice(["Barvy", "Jazyky", "Zvirata"])
print("Kategorie: " + category)
if category == "Barvy":
	word = random.choice(["fialova", "cervena", "oranzova", "zelena", "modra", "ruzova", "zluta", "cerna", "bila"])
elif category == "Jazyky":
	word = random.choice(["Cestina", "Slovenstina", "Rustina", "Nemcina", "Spanelstina", "Madarstina", "Portugalstina", "Svedstina"])
else: # kategorie == "Zvírata"
	word = random.choice(["tygr", "lev", "pes", "kocka", "klokan", "veverka","zralok","opice","koroptev"]) #zde si muzete navolit slova dle vasich predstav


word_progress = ["-"] * len(word)


guessed = []


incorrect = 0

while incorrect < 6 and "-" in word_progress:
	
	print()
	draw_man(incorrect)
	print(" ".join(word_progress))
	print("Hadej slovo: ")
	print(" ".join(guessed))
	print()
	
	
	guess = "0"
	if not guess.isalpha():
		guess = input("Napis pismeno nebo slovo: ").lower()
	
	if guess == word.lower():
		
		break
	elif len(guess) > 1: 
		print("Omlouvám se, ale tohle slovo to není.")
		incorrect += 1
	elif guess in guessed:
		print("Tohle uz jste.")
	elif guess not in word.lower():
		print(guess + " není ve slove!")
		incorrect += 1
		guessed.append(guess)
	else: 
		print(guess + " je ve slove!")
		guessed.append(guess)
		for i in range(len(word)):
			if word_progress[i] == "-" and word[i].lower() == guess:
				word_progress[i] = word[i] 

print()
if incorrect == 6:
	print("Prohrál si!")
	print("Slovo bylo: " + word)
else: 
	if "-" in word_progress:
		print("Uhádl si  slovo! Vyhrál si!")
		for i in range(len(word)):
			word_progress[i] = word[i]
	else: 
		print("Nasel si slovo! Vyhral si!")

draw_man(incorrect)
print(" ".join(word))
print("Pouzita pismena: ")
print(" ".join(guessed))
print()
print("Děkuji ze sis zahral!")