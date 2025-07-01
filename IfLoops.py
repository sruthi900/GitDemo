
Greeting1="Good morning"

if Greeting1 =="Goodday morning":
    print("condition matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition code is completed")

###########

obj=[2,3,5,7,9]
for i in obj:
    print(i*2)

####################
#i to j-1
summation=0
for j in range(1,6):
    summation=summation+j
    print(j)
print(summation)


###############skipping with index
for k in range(1,10,5):
    print(k)

#### starts from 0 to 9
for m in range(10):
    print(m)

##############
it=4
while it>1:
    if it!=3:
        print(it)
    it=it-1
print("while loop executed successfully")

################# break will skip all teh belwo stesp of execution

it=4
while it>1:
    if it==3:
        break
    print(it)
    it=it-1
print("while lopp")
################# continue keyword skips the iterations and goes to next one
it=10
while it>1:
    if it==9:
        it=it-1
        continue
    if it==3:
        break
    print(it)
    it=it-1

###########
Greeting="Hello"
if Greeting== "Hello":
   print("Hello there!")
   print("How can i assist today")
else:
   print("Greetings!")

print("program has completed")







