import sys, random

if len(sys.argv) == 1:
  print("Give some information to generate name!")
  exit()
  
name = [ x[0:4].capitalize()  for x in sys.argv[1:] ]
if random.uniform(0,2) > 1:
  name.append("Tex")
else:
  name.append("Pol")

random.shuffle(name)
print( "Your \"innovative buisness\" name: {}".format("".join(name)) )
