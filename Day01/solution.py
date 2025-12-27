def solve_part1(data):
  data = data.split()
  code=50
  counter =0 

  for i in data:
      num = int(i[1:])
    
      if i[0] == "R":
          code += num
      else:
          code -= num
      
      while code>99:
          code-=100
      while code<0:
          code+=100
      if code == 0:
          counter+=1
  print(counter)
        
