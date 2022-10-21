print("Name: {Pitchaya Musimun}")
print("SID: {364211760015}")
print("Group: {MIT221}")
myList = [10,20,30,40,50]
print("********************")
print(myList)
print(myList[1])
print(myList[4])
print("********************")
print(myList[1:4])
print(myList[3:5])
print(myList[:-3])
print("********************")
myList = 10
while myList < 60:
  print(myList)
  myList += 10
print("********************")
myList = [10,20,30,40,50]
for x in myList:
  print(x)
print("********************")
myList.append(100)
myList.append(200)
myList.append(300)
myList
myList.insert(0, 400)
myList
myList.insert(3, 500)
myList
print(myList)
print("********************")
myList.remove(10)
myList.remove(100)
print(myList)
myList.pop()
print(myList)
print("********************")
myList.sort()
print(myList)
print("********************")
myList.sort(reverse=True)
print(myList)
print("********************")
newList = [x for x in myList if x>50]
print(newList)
print("********************")
myFinalList = myList + newList
print(myFinalList)
print("********************")


