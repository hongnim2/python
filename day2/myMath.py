#function
#return total sum coming list parameter
def mysum(data):
    tot=0
    for x in data:
        tot+=x
    return tot


#return max value coming list parameter
def mymax(data):
    result=data[0]
    for x in range(1,len(data)):
        if result <= data[x]:
            result=data[x]
    return result


#return min value coming list parameter
def mymin(data):
    result=data[0]
    for x in range(1,len(data)):
        if result >= data[x]:
            result=data[x]
    return result


#return average value coming list parameter
def myavg(data):
    tot=mysum(data)
    avg=tot/len(data)
    return avg

def printname():
    print(__name__)

if __name__="__main__":
    data=[1,2,3,4,5]
    print(mysum(data))
    print(mymax(data))
    print(mymin(data))
    print(myavg(data))
