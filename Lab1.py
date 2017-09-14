def main():
  arr1 = [1,2,3,4,5,6,7,8]
  arr2 = [2,3,4,5,6,7, 18]
  Vstrane = "Çà ÑCÑĞ!"
  print("min =", find_min(arr1))
  print ("average =", average(arr1))

  print("min =", find_min(arr2))
  print ("average =", average(arr2))
  
  print("replaced = ", perevorot(Vstrane))
  
  ivan = {
  "name": "ivan",
  "age": 34,
  "children": [{
    "name": "vasja",
    "age": 19,
  },{
    "name": "petja",
    "age": 12,
  }]
        } 

  darja = {
  "name": "darja",
  "age": 41,
  "children": [{
    "name": "kirill",
    "age": 21,
  },{
    "name": "pavel",
    "age": 15,
  }]
        } 

  emps = [ivan, darja]
  
  find(emps)

#Minimum
def find_min(value):
  min = value[0]
  for v in value:
    if v <= min:
      min = v
  return min

#Average
def average(av):
  sum = 0;
  for v in av:
    sum += v
    average_value = sum/len(av)
  return average_value


#Stroki
def perevorot(stroka):
  replace = ""
  length = len(stroka)  
  while length != 0:
    length -= 1
    replace = replace + stroka[length]
  return replace
  
#Ñëîâàğü


def find(emp):
  for f in emp:
    for g in f["children"]:
      if g["age"] >= 18:
        print (f["name"])
        break
  return 0

  

main()