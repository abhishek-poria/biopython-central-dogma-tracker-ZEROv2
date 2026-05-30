#
from Bio.Seq import Seq
from rich import print
import pyttsx3

#___Amino acid based on R group____
aminoDict = {"Hydrogen" : "Glycine", 
             "Methyl" : "Alanine",
             "Hydroxy methyl" : "Serine"}

#___secondary metabolites__
pigmentsList = ["Carotenoids", "Anthocyanins"]
alkaloidsList = ["Morphine" , "Codine"]
terpenoidsList = ["Monoterpenes", "Diterpenes"]
toxinList = ["Abrin", "Ricin"]
drugsList = ["Vinblastin", "Curcumin"]
polymericSubstanceList = ["Rubber", "Gum", "Cellulose"]

def secondary_metabolites() :
    while True :
        print("1.Pigments")
        print("2.Alkaloids")
        print("3.Terpenoids")
        print("4.Toxins")
        print("5.Drugs")
        print("6.Polymeric substances")
        try :
            ask = int(input("which one do you want to know?"))
            if ask == 1 :
                print(f"examples of pigments are : {pigmentsList}")
                break
            elif ask == 2:    
                print(f"examples of alkaloids are : {alkaloidsList}")
                break
            elif ask == 3:    
                print(f"examples of terpenoids are : {terpenoidsList}")
                break
            elif ask == 4:    
                print(f"examples of toxins are : {toxinList}")
                break
            elif ask == 5:
                print(f"examples of drugs are : {drugsList}")
                break
            elif ask == 6:
                print(f"examples of polymeric substances are : {polymericSubstanceList}")
                break
        except ValueError :
            print("Enter an valid integer")
            
            
def acid_on_carbon():
    while True :
        print("Amino acid depends on the nature of R group present in it")
        print("Press 1 to know what if R group is Hydrogen")
        print("Press 2 to know what if R group is Methyl")
        print("Press 3 to know what if R group is Hydroxy Methyl")
        try :
            ask = int(input("whom you are curious about??"))
            if ask == 1 :
                print(aminoDict["Hydrogen"])
                print("It is an amino acid having two hydrogen group in its side chain. And considered as neutral amino acid.")
                print("Fun Fact -> It is the lightest among all")
                break
            elif ask == 2:
                print(aminoDict["Methyl"])
                print("It is an amino acid having methyl group in its side chain.")
                break
            elif ask == 3:
                print(aminoDict["Hydroxy methyl"])
                print("It is an amino acid having hydroxymethyl in its side chain.")
                break
        except ValueError :
            print("Enter an valid integer")

def central_dogma() :
    with open("centraldogma.txt", "a" , encoding= "utf-8") as f :
        my_dna_seq = " "
        while True :
            print("1.DNA sequence length calculator")
            print("2.DNA to mRNA conversion : Transcription")
            print("3.DNA to protein : Translation")
            try :
                ask = int(input("what you want me to do?"))
                if ask in [1, 2, 3] :
                    my_dna_seq = Seq(input("Please Enter your sequence here :")).upper().strip()
                    if ask == 1:
                        print(f"length of your given DNA sequence is : {len(my_dna_seq)} nucleotide")
                        break
                    elif ask == 2:
                        mRNA = my_dna_seq.transcribe()
                        print(f"mRNA for given DNA sequence is :{mRNA}")
                        break
                    elif ask == 3:
                        Protein = my_dna_seq.translate()
                        print(f"Protein from DNA : {Protein}")
                        break
            except ValueError :
                print("Enter valid integer.")
        f.write(str(my_dna_seq) + "\n")




#INTRO....

pyttsx3.speak("Hii. I'm ZERO. Your Personal AI Assistant.")
print("1.CENTRAL DOGMA")
print("2.SECONDARY METABOLITES")
print("3.AMINO ACID DICTIONARY")
pyttsx3.speak("Where are we heading today??")
while True :
    try :
        ask = int(input("Enter :"))
        if ask == 1:
            print("YES! lets explore central dogma together")
            print("INITIALIZING.......")
            print("DONE!")
            central_dogma()
            break
        elif ask == 2:
            print("SURE! Secondary Metabolites are way more interseting")
            print("INITIALIZING.......")
            print("DONE!")
            secondary_metabolites()
            break
        elif ask == 3:
            print("Ah! CLASSIC...")
            print("INITIALIZING.......")
            print("DONE!")
            acid_on_carbon()
            break
        else :
            print("ERROR 404 : NOT FOUND")
            print("Enter 1, 2, or 3")
    except ValueError :
        print("ERROR 404 : NOT FOUND")
        print("Enter valid integer")

