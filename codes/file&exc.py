#the program creates a new file and allows the user to enter data
# then it copies the data of this file into another file

def func1(f1):
    f = open(f1,"w")
    line = input()
    while line != '':
        f.write(line)
        line = input()

def func2(f1,f2):

        file1 = open(f1,"r")
        file2 = open(f2,"w")
        line = file1.readline()
        while line != '':
            file2.write(line,'\n')
            line = file1.readline()
        
    

def main():
    filename1 = input("Enter the source file :")
    func1(filename1)
    filename2 = input("Enter the destination file :")
    func2(filename1,filename2)
        
main()
