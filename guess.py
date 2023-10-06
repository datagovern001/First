import randomx
x=random.randint(10,20)
i=1
while i<3:
  num = int(input())
  if x==num:
    print("you won")
    i+=1
  else:
    print("Lose")
    i+=4
