print("Name: {Pitchaya Musimun}")
print("SID: {364211760015}")
print("Group: {MIT221}")
print("********************")
def getPTD():
  sumPID = [int(x) for x in input(f'Enter PID : ').split()]
  return sumPID

def getFortune(*var):
  resultlist = []
  for x in var:
    if x % 2 == 0:
      resultlist.append('Your Fortune Is Good')
    else:
      resultlist.append('Your Fortune Is Very Good')
  return resultlist

PID = getPTD()
print(f'เลขบัตรประชาชน: {sum(PID)}')
print(f'ทำนายดวงชะตา: {getFortune(sum(PID))}')
print("********************")

