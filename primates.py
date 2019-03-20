#the primate lists are set up as [[traits], [next taxonomic level], [taxanomic name]]
#I used a mix of wikipedia and my anth 102 (intro to physical anthropology) notes for the info
#as of now I'm leaving out extinct sections and specific non homo species
#there are some exceptions to these lists (i.e. aotidae are nocturnal)
#need help with greater ape and homo IDs

cercopithecinae = ["diet of mostly fruits", "low cusps", "cheek pouches", "broad incisor", "similar arm and leg length"], [1], ["cercopithecinae"]
colobinae = ["diet of mostly leaves", "high cusps", "complex stomachs", "hyper saliva bacteria digestion", "narrow incisors"], [1], ["colobinae"]
cercopithecoidea = [["smaller brains", "4 cusps on molars (bilophodant)", "tails (if it doesn't have a tail, it's not a monkey, even if it has a monkey-kind-of-shape)", "long trunks", "shorter arms"], [cercopithecinae, colobinae], ["cercopithecoidea"]]
hylobatidae = ["sing monagomous duets"], [1], ["hylobatidae"] 
ponginae = ["isolation in male and female territories", "rapists"], [1], ["ponginae"]
gorillini = ["origin: Gorillai (Greek for tribe of hairy women)", "intrasexual competition", "harems with alpha males"], [1], ["gorillini"]
pan = ["either sociopathically violent chimpanzees that offer a dark reflection into the origins of man's blood lust in a male dominant society or the superior orgy having bonobos that show us what a utopia looks like under a female dominant society", "fission-fusion social groups"], [1], ["pan"]
homo = [[], [], ["homo"]]
hominini = [["bipedalish (chimps and homo)"], [pan, homo], ["hominini"]]
homininae = [[], [gorillini, hominini], ["homininae"]]
hominidae = [[], [ponginae, homininae], ["hominidae"]]
hominoidea = [["larger brains", "5 cusps on molars (Y-5)", "short trunk", "no tail (if it doesn't have a tail, it's not a monkey, even if it has a monkey-kind-of-shape)", "long arms"], [hylobatidae, hominidae], ["hominoidea"]]
catarrhini = [["2 premolars", "eardrum tube", "old world", "downward facing nostrils", "frontal and sphenoid bone contact"], [cercopithecoidea, hominoidea], ["catarrhini"]]
callitrichidae = ["small bodies", "polyandrous", "usually give birth to twins", "re-evolved claws"], [1], ["callitrichidae"]
cebidae = ["primitive tool use (likely the smartest of the new world monkeys)", "small", "second degree intentionality (can teach others)"], [1], ["cebidae"]
aotidae = ["nocturnal"], [1], ["aotidae"]
pitheciidae = ["singing", "monogamous"], [1], ["pitheciidae"]
atelidae = ["nails on fingers and toes", "tactile pad on tail", "a family only a nerd would spend years studying"], [1], ["atelidae"]
platyrrhini = [["3 premolars", "eardrum ring", "new world", "sideways facing nostrils", "zygomatic and parietal bone contact", "prehensile tails"], [callitrichidae, cebidae, aotidae, pitheciidae, atelidae], ["platyrrhini"]]
simiiformes = [["diurnal", "normalish eyes (doesn't look like it's currently undergoing a colonoscopy)"], [catarrhini, platyrrhini], ["simiiformes"]]
tarsiiformes = ["nocturnal", "arboreal", "giant freaky freaky eyes", "VCL movement", "enlarged tarsus bone (get your mind out of the gutter)", "carnivorous", "2.1.3.3/1.1.3.3 dental formula"], [1], ["tarsiiformes"]
haplorhini = [["fixed ears", "dry noses", "post orbital closure", "no tooth comb or grooming claw", "fused frontal bones and mandibles", "lacrimal on inside of eye", "no tapetum lucidum", "retinal fovea", "single chambered uterus"], [tarsiiformes, simiiformes], ["haplorhini"]]
lemuroidea = ["femal dominent society", "quadrupedal", "VCL movement", "nocturnal"], [1], ["lemuroidea"]
lorisoidea = ["nocturnal", "arboreal", "mostly solitary"], [1], ["lorisoidea"]
strepsirrhini = [["mobile ears", "wet nose", "no post orbital closure", "tooth comb and grooming claw", "unfused frontal bones and mandibles", "lacrimal on outside of eye", "tapetum lucidum", "no retinal fovea", "bicornal uterus"], [lemuroidea, lorisoidea], ["strepsirrhini"]] 
primates = [["starting"], [haplorhini, strepsirrhini], ["primate"]]

def primate_id():
    traits = []
    identity = []
    tax_part = primates #starting position, later add ability to skip to new one
    n = 0
    while ((tax_part[1]) != [1]) and (n <= len(tax_part[1])):
        answer = "u"
        print (len(tax_part))
        while (answer != "1") and (answer != "2"):
            answer = input("is a/are %s present? \n 1. Yes \n 2. No" %(tax_part[1][n][0])) #may need to change grammar
            if answer == "1":
                tax_part = tax_part[1][n]
                if (tax_part[1]) != [1]:
                    traits.append(tax_part[1][n][0])
                    identity.append(tax_part[2])
                    n = 0
                else:
                    traits.append(tax_part[0])
                    identity.append(tax_part[2])
            elif answer == "2":
                n += 1
    print(traits, identity)


def hardy_weinberg(): #input info present and then ask if it wants to find members of a population, add comedic disclaimer about evolutionary forces not being present (yes this is something I have to remind myself to do, congrats if you are reading this, it is currently 10:48pm 3/15/19 and this is where my life is at)
    recessive_allele_frequency = 0
    dominant_allele_frequency = 0
    homozygous_dominant_frequency = 0
    heterozygous_frequency = 0
    homozygous_recessive_frequency = 0
    dominant_phenotype_frequency = 0
    recessive_phenotype_frequency = 0
    which_equation = "u"
    missing = "2"
    while which_equation.isdigit() == False or int(which_equation) not in range(1,7):
        which_equation = input("what info do you have? \n 1. recessive allele frequency \n 2. dominant allele frequency \n 3. homozygous dominant frequency \n 4. homozygous recessive frequency \n 5. dominant phenotype frequency \n 6. recessive phenotype frequency")
    if which_equation == "1":
        while float(missing) > 1 or float(missing) < 0 :
            missing = input("input the frequency in decimal form")
        recessive_allele_frequency = float(missing)
    elif which_equation == "2":
        while float(missing) > 1 or float(missing) < 0 :
            missing = input("input the frequency in decimal form")
        dominant_allele_frequency = float(missing)
    elif which_equation == "3":
        while float(missing) > 1 or float(missing) < 0 :
            missing = input("input the frequency in decimal form")
        dominant_allele_frequency = (float(missing))**(1/2)
    elif (which_equation == "4") or (which_equation == "6"):
        while float(missing) > 1 or float(missing) < 0 :
            missing = input("input the frequency in decimal form")
        recessive_allele_frequency = (float(missing))**(1/2)
    elif which_equation == "5":
        while float(missing) > 1 or float(missing) < 0 :
            missing = input("input the frequency in decimal form")
        recessive_allele_frequency = (1 - float(missing))**(1/2)
    if recessive_allele_frequency != 0:
        dominant_allele_frequency = 1 - recessive_allele_frequency
        homozygous_dominant_frequency = dominant_allele_frequency**(2)
        heterozygous_frequency = 2*(recessive_allele_frequency*dominant_allele_frequency)
        homozygous_recessive_frequency = recessive_allele_frequency**(2)
        dominant_phenotype_frequency = heterozygous_frequency + homozygous_dominant_frequency
        recessive_phenotype_frequency = recessive_allele_frequency**(2)
    elif dominant_allele_frequency != 0:
        recessive_allele_frequency = 1 - dominant_allele_frequency
        homozygous_dominant_frequency = dominant_allele_frequency**(2)
        heterozygous_frequency = 2*(recessive_allele_frequency*dominant_allele_frequency)
        homozygous_recessive_frequency = recessive_allele_frequency**(2)
        dominant_phenotype_frequency = homozygous_dominant_frequency + heterozygous_frequency
        recessive_phenotype_frequency = recessive_allele_frequency**(2)
    print("Disclaimer: All results assume that the factors of evolution are not in play and that the population is infinite. Proceed with caution.")
    print("recessive allele frequency = %s" %(recessive_allele_frequency))
    print("dominant allele frequency = %s" %(dominant_allele_frequency))
    print("homozygous dominant frequency = %s" %(homozygous_dominant_frequency))
    print("heterozygous frequency = %s" %(heterozygous_frequency))
    print("homozygous recessive frequency = %s" %(homozygous_recessive_frequency))
    print("dominant phenotype frequency = %s" %(dominant_phenotype_frequency))
    print("recessive phenotype frequency = %s" %(recessive_phenotype_frequency))
    print("you will likely get near answers due to python storing float (decimal) numbers in binary aproximations")

def standard_deviation():
    data = "u"
    d_points = []
    while (data != "d"):
        data = input("Input your data (do not use decimals or fractions. only use integers), press 'd' when you are done.")
        if data.isdigit() == True:
            d_points.append(int(data))
    sum_of = 0
    for p in d_points:
        sum_of += p
    mean = (sum_of / len(d_points))
    sd = 0
    for q in d_points:
        sd += ((q - mean)**(2))/(len(d_points) - 1)
    sd = sd**(1/2)
    print("standard deviation = %s" %(sd))
    print("mean = %s" %(mean))
    

#UI starts here
finished = False
while finished == False:
    runner = "u"
    while (runner.isdigit() == False) or ((float(runner) < 4) and (float(runner) > -1)):
        runner = input("What would you like to run? \n 1. primate id \n 2. Hardy-Weinberg equation \n 3. standard deviation \n 0. end")
        if runner == "1":
            primate_id()
        elif runner == "2":
            hardy_weinberg()
        elif runner == "3":
            standard_deviation()
        elif runner == "0":
            finished = True
