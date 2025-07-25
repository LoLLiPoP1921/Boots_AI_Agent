from functions.get_files_info import  write_file

def main():
    print("<-------------------------------------------------->")
    print(f"Result for current directory:\n{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}")
    print("<-------------------------------------------------->")
    print(f"Result for 'pkg' directory:\n{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}")
    print("<-------------------------------------------------->")
    print(f"Result for '/bin' directory:\n{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}")
    print("<-------------------------------------------------->")


main()