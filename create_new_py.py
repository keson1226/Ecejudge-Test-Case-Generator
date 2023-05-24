out = """
target_dir = int(input())
case_amoung = int(input())
def create(target_dir,case_num):

    path = f"problem_{{target_dir}}_test_cases./{{case_num}}."

    test_case = ""

    with open(path+"in","r",encoding="utf-8") as file: 
        test_case = file.read().split("\\n")
        
    
    with open(path+"out","w",encoding="utf-8") as file:
        def write(text,needto = 1,another=""):
            file.write(str(text))
            file.write(str(another))
            if needto :file.write(\"\\n\")
    
    
{}
    print(f\"Output Data {{case_num}} Finish !\")

for num in range(1,case_amoung+1):
    create(target_dir,num)
"""
code = ""

with open("solve.py","r",encoding="utf-8") as file:
    lines = file.read().split("\n")
    for line in lines:
        line = line.replace("print","write")
        
        line = line.replace("input()","test_case.pop(0)")
        if ",end=" in line : 
            code += "        "+line.replace(",end=",",needto = 0 ,another=")+"\n"
        else :
            code+="        "+line+"\n"

out = out.format(code)

with open("output_generate.py","w",encoding="utf-8") as file:
    file.write(out)