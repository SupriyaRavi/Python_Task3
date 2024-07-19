#Question 1 :

import time

def my_timestamp_file():
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    my_file = current_time + ".txt"
    with open(my_file, "w") as file:
        file.write(current_time)
    
    print(my_file)

my_timestamp_file()
