global sumNum
sumNum = 1

def conbin(num , origin , end) :
    global sumNum
    if sumNum != 1 : print("")
    return f"第{sumNum}次搬運:圓盤{num} 從 木釘{origin} 搬到 木釘{end}"


def hona( num , origin , end ,other) :
    global sumNum
    if num==1 :
        print(conbin(num,origin,end),end="")
        sumNum += 1
    else :
        hona(num-1,origin,other,end)
        print(conbin(num,origin,end),end="")
        sumNum += 1
        hona(num-1,other,end,origin)
    


x = int(input())
hona(x,'1','3','2')