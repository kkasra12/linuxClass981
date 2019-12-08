from random import randint
numbers =[None,'First','Second','Third','Fourth','Fifth','Sixth','Seventh',
           'Eighth','Ninth','Tenth','Eleventh','Twelfth','Thirteenth',
           'Fourteenth','Fifteenth','Sixteenth','Seventeenth','Eighteenth',
           'Nineteenth','Twentieth','Twenty first','Twenty second',
           'Twenty third','Twenty - fourth','Twenty - fifth']
for i in range(1,11):
    f=open(f'{i}{numbers[i]}BigFile','w')
    f.write("\n".join([f'{j}\t{numbers[i]} big file' for j in range(randint(1000,5000))]))
    f.close()
