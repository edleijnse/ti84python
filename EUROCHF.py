from ti_system import *
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

def geteuro():
    try:
        xlist=recall_list("1")
        storedeuro = float(xlist[0])
    except Exception as e:
        storedeuro = .83
        saveeuro(storedeuro)
    return storedeuro

def saveeuro(ieuro):
    xlist=[]
    xlist.append(ieuro)
    store_list("1",xlist)
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