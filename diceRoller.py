import random
import re
def diceRoller(i):
    mysum = 0
    vals = []
    xands = i.split("d")
    x, s = int(xands[0]), int(xands[1])
    for i in range(x):
        n = random.randint(1, s)
        vals.append(n)
        mysum += n
    return ["Total: {}\nRolls: {}".format(str(mysum), str(vals)), mysum]
    
def extensionDiceRoller(s):
    finalstr = ""
    gt = 0
    if re.search("^(([1-9]|1[0-9]|20)d(4|6|8|10|12|20|100))(\s*[(+|,)]*\s*([1-9]|1[0-9]|20)d(4|6|8|10|12|20|100))*$",s):
        sub = [i.strip() for i in s.replace("+", " ").replace(",", " ").split()]
        for i in range(len(sub)):
            lol = diceRoller(sub[i])
            if lol != None:
                finalstr += "Group {}: {}\n".format(str(i+1), sub[i])
                gt += lol[1]
                if i != len(sub)-1:
                    finalstr += "{}\n".format(lol[0])
                else:
                    finalstr += lol[0]
            else:
                print("Incorrect Format")
                return
        if finalstr != "":
            return "\nGrand Total: {}\n{}".format(gt,finalstr)
    else:
        print("\nIncorrect Format")
end = 1
while end:
    inp = input("Enter a string in the format \"XdS\", whereby X is the number of dices and S is the number of sides for each given dice: ")
    val = extensionDiceRoller(inp)
    if val != None:
        print(val)
        end = 0
    else:
        print("\n\nRe-", end="")
