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
