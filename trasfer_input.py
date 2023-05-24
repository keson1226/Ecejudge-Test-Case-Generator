
target_dir = int(input())
case_amoung = int(input())
def create(target_dir,case_num):

    path = f"problem_{target_dir}_test_cases./{case_num}."

    test_case = ""

    with open(path+"in","r",encoding="utf-8") as file: 
        test_case = file.read()
        
    
    with open(path+"in","w",encoding="utf-8") as file:
        file.write(test_case)
    print(f"Input Case {case_num} Finish !")
    



for num in range(1,case_amoung+1):
    create(target_dir,num)
