from functions.get_files_info import  run_python_file

def main():
    print("<-------------------------------------------------->")
    print(f"Result for current directory:\n{run_python_file("calculator", "main.py")}")
    print("<-------------------------------------------------->")
    print(f"Result for 'pkg' directory:\n{run_python_file("calculator", "main.py", ["3 + 5"])}")
    print("<-------------------------------------------------->")
    print(f"Result for '/bin' directory:\n{run_python_file("calculator", "tests.py")}")
    print("<-------------------------------------------------->")
    print(f"Result for '/bin' directory:\n{run_python_file("calculator", "../main.py")}")
    print("<-------------------------------------------------->")
    print(f"Result for '/bin' directory:\n{run_python_file("calculator", "nonexistent.py")}")
    print("<-------------------------------------------------->")

main()