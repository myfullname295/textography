#Python for Humanists
#12.16.2015

    
def textography():
    
    text = """Imagine someone (a kind of Monsieur Teste in reverse)
who within himself all barriers, all classes, all
exclusions, not by syncretism but by simple discard of that
old specter: logical contradiction; who mixes every language,
even those said to be incompatible; who silently
accepts every charge of illogicality, of incongruity; who
remains passive in the face of Socratic irony (leading the
interlocutor to the supreme disgrace: self-contradiction)
and legal terrorism (how much penal evidence is based on
a psychology of consistency!). Such a man would be the
mockery of our society: court, school, asylum, polite
conversation would cast him out: who endures contradiction
without shame? Now this anti-hero exists: he is the
reader of the text at the moment he takes his pleasure.
Thus the Biblical myth is reversed, the confusion of
tounges is no longer a punishment, the subject gains access
bliss by the cohabitation of languages working side by racecar
side: the text of pleasure is a sanctioned ethos those Babel.
(Pleasure/Bliss: terminologically, there is always a vacilation-
I stumble, I err. In any case, there will always be a
margm of indeclSlon; the distinction will not be the source
of absolute classifications, the paradigm will falter the
meaning will be precarious, revocable, reversible: the
discourse incomplete.) Roland Barthes, "The Pleasure of the Text" """
       
    #I deleted all the punctuation, because at bottom, my interest is the syntax.
    text = text.replace("(","").replace(")","").replace("?","").replace("!","").replace(".","").replace(",","").replace(";","").replace(":","").replace("/"," ").replace("\""," ").replace("\n", " ").replace("-", " ")
    text = text.upper()
    text = text.split(' ')
    
    tiebreaker = input("Please enter a \"1\" or a \"2\":") #This may come in handy later, if there is a tie between the distance between palindromes or in palindrome saturation of anagrams.

    anagram_sorted_text = []
    list_for_palindromes = []
    
    
    anagrams = {}
    #using a for loop to look for palindromes. 
    for word in text:
        if word == word[::-1] and len(word) > 1:
            list_for_palindromes.append(word)#If length of palindrome is greater than 1, it is a palindrome.
            print()
            print("Palindrome/s printed below:")
            print (list_for_palindromes)
            #print(word)            
            print("Anagrams printed below:")

    for word in text: #Using a for loop to create a alphabetized version of the text
        listed_word = list(word)
        listed_word.sort()
        anagram_sorted_text.append(str(listed_word))
        str_listed_word = ''.join(listed_word) 
        #print (str_listed_word)
        
        if str_listed_word in anagrams: #Appending to the dictionary was hard, so I got some help. I haven't quite gotten the positions yet.
          #print(str_listed_word)
            if anagrams[str_listed_word].count(word) == 0:  #If word is an anagram and not yet in dictionary, append to anagram.
                #print (str_listed_word)
                #print(anagrams[str_listed_word])
                anagrams[str_listed_word].append(word)
                #print(anagrams[str_listed_word].count(word))
        else: #else append word to list of not anagrams.
            new_list = []
            # print(new_list)
            new_list.append(word)
            anagrams[str_listed_word] = new_list
            #print(new_list)
            
        ##print(sorted_text)
        ##print(len(text))
        
    #for k in anagrams.keys(): 
        #print(k,anagrams[k])
    #print(anagrams)    
        
    #print()
    
        
    for word in anagrams.keys():
        word_list = anagrams[word] 
        if len(word_list) > 1:  #If word is not equal to itself, word is an anagram.
            print(word_list) 
        
    
#I got some help on this code, but it didn't quite work. Saving it in case I can use it later.
   # for i in range(len(anagram_sorted_text)):
    #    for j in range(i+1,len(anagram_sorted_text)):
     #       if anagram_sorted_text[i] == anagram_sorted_text[j]:
      #          ##print (j)
       #         print(anagram_sorted_text[i]) #Here is where I will need to begin using the dictionary           
#find text[i] == text[j]
        
textography()    
