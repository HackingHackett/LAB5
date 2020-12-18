"""
The prograsm is trying to translate a sentence captured as uder input.
We first read in the text file textese.txt
then from the text file, we create a list of strings from each lines in the text file.
Then we create a dictinary the list.
once the text file has been read into memory we close the file

we then define a fucntion for trasnlating ehich envolves spliting the user input (sentence into an arroy of strings ("enjoy the excellent band tonight") ["enjoy, "the","excellent","band","tonight"]

once we have the arry of string repsenting the user's input sentence we
looop through each words, find the key matching the word and returns back the vaule tired to that word in our dictionary 
After each word is trasnlated we then
Print out the trasnlated sentance to the user.
"""

""" 
main():
 Set sentence = input()
 set dictionary = create_dictionary()
 traslate(sentence, dictionary)

traslate(sentence, dictionary)
 words = for each of the word in the sentence 
 for each words, translate the word
 print translated sentence to user 

 create_dictionary():
 read in textese.txt
 create list = each line from file
 close the file
 create a dict off of the list
 return the dict

main()
"""


def main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
        infile = open(txt_file, "r")
        words = [word.rstrip() for word in infile]
        infile.close()

        #print("words", words)
        translation = dict ([word.split(",")for word in words]) #"tonight":"2nite",
           #  [k,v] = word.split(",") #["tonight":"2nite"]

            # tanslation [k] = v 
        # print (translation)
        return dict ([word.split(",")for word in words])

def translate(sentence, dictionary):
 #print("From translate", sentence)
 words = sentence.split() # ["enjoy","the", "excellent", "band", "tonight"]
 for word in words:
      print(dictionary.get(word,word), " ", end="")
main ()
