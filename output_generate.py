
target_dir = int(input())
case_amoung = int(input())
def create(target_dir,case_num):

    path = f"problem_{target_dir}_test_cases./{case_num}."

    test_case = ""

    with open(path+"in","r",encoding="utf-8") as file: 
        test_case = file.read().split("\n")
        
    
    with open(path+"out","w",encoding="utf-8") as file:
        def write(text,needto = 1,another=""):
            file.write(str(text))
            file.write(str(another))
            if needto :file.write("\n")
    
    
        global sumNum
        sumNum = 1
        
        def conbin(num , origin , end) :
            global sumNum
            if sumNum != 1 : write("")
            return f"第{sumNum}次搬運:圓盤{num} 從 木釘{origin} 搬到 木釘{end}"
        
        
        def hona( num , origin , end ,other) :
            global sumNum
            if num==1 :
                write(conbin(num,origin,end),needto = 0 ,another="")
                sumNum += 1
            else :
                hona(num-1,origin,other,end)
                write(conbin(num,origin,end),needto = 0 ,another="")
                sumNum += 1
                hona(num-1,other,end,origin)
            
        
        
        x = int(test_case.pop(0))
        hona(x,'1','3','2')

    print(f"Output Data {case_num} Finish !")

for num in range(1,case_amoung+1):
    create(target_dir,num)
