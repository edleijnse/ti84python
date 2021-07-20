try:
  from ti_system import *
except Exception as e:
    print ("no module ti_system")
def euro2chf(initeuro):
  print("")
  try:
     neweuro = float(input("new euro value? (" + '{:.2f}'.format(initeuro) + "): "))
  except Exception as e:
     neweuro=initeuro

  euro= neweuro

  print("euro: " + '{:.2f}'.format(euro))
  print("")
  eurocount=float(input("count "))
  print("euro count: ", eurocount)
  chf=euro*eurocount
  print ("CHF: " + '{:.2f}'.format(chf))
  return neweuro

def getEuroFromFile():
    try:
       file1 = open("eurostore.txt","r")
       storedeuro = file1.read()
       file1.close()
    except Exception as e:
       storedeuro = .95
    return storedeuro
def geteuro():
    try:
        xlist=recall_list("1")
        storedeuro = float(xlist[0])
    except NameError as e:
        storedeuro=getEuroFromFile()
    except Exception as e:
        storedeuro = .83
    saveeuro(storedeuro)
    return storedeuro
def saveEuroToFile(iEuro):
    file1 = open("eurostore.txt","w")
    file1.write(str(iEuro))
    file1.close()
def saveeuro(ieuro):
    xlist=[]
    xlist.append(ieuro)
    try:
       store_list("1",xlist)
    except NameError as e:
       saveEuroToFile(ieuro)
    return

initeuro=geteuro()
while True:
  try:
    stopnow = input("continue currency calc (n)? ")
    if stopnow == "n":
       break
    initeuro = euro2chf(initeuro)
    saveeuro(initeuro)
  except Exception as e:
    print(e)