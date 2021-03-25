

x = [-10, -10^(-15), 0, 10^(-15), 10]

def heaviside(x):
  h = []
  for i in x:
    h.append(x(i[0], i[1], i[2], i[3], i[4]))
  return h
  print(heaviside)

def heav():
  heav = []
  for x in range(1,6):
    if x < 0:
      heav.append(0)  
    elif x >= 0:
      heav.append(1)

  print(heav)



#print('heav')

#heaviside defined as h(x)
#h(x) is defeined by appending each term in x to h(x)
#h(x) is then returned to the definition of heaviside
#heaviside is now defined as h(x) and is tested
#for each term 'i' in heaviside (in h(x)) we get 0 or 1
# 0 and 1 is then returned and replaced by each term in h(x) 
# we then print the new list of 0's and 1's as our answer

#def h(x):
  #h = []
 # for i in x:
   # h.append(x(i[0], i[1], i[2], i[3], i[4]))
 # return h