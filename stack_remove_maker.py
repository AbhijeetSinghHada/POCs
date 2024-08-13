import os

def main():
    filedata =  open("test.txt", "r")
    data = filedata.read()
    stack_names = ""
    for line in data.split("\n"):
        if "ahada" in line:
            stack_names+=line.strip()+","
    
    print(stack_names)
            
            

if __name__=="__main__":
    main()