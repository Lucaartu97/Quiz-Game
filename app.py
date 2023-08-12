def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Risposta corretta !")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Mi spiace, risposta sbagliata, riprova")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Indovina l'animale")
guess1 = input("Quale animale vive al polo nord ? ")
check_guess(guess1, "Orso Polare")
guess2 = input("Qual è l'animale più veloce ? ")
check_guess(guess2, "Ghepardo")
guess3 = input("Qual è l'animale più grande ? ")
check_guess(guess3, "Balena Blu")
print("Il tuo punteggio è: "+ str(score))