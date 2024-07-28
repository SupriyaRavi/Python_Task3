#Question 2: 

def my_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
    
file_name = 'Readme.txt'  
my_file(file_name)
