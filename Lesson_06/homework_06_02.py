while True:
    word = input("Enter a word that contains the letter 'h' or 'H': ")
    if 'h' in word or 'H' in word:
        break
    else:
        print("This word does not contain the letter 'h' or 'H'. Try again.")
