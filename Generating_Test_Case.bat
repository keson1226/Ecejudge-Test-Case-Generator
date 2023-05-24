@echo off

echo "Start"
echo ========================================

SET /p target_dir="Which folder need to edit ? (Input the number) :"
SET /p case_num="Test Case Amoung ? (Input the number) :"

echo %target_dir% > temp.txt
echo %case_num% >> temp.txt

powershell.exe "cat temp.txt | python.exe trasfer_input.py"

python.exe create_new_py.py

powershell.exe "cat temp.txt | python.exe output_generate.py"

del temp.txt

echo ========================================
echo "Done"