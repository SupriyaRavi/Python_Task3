#Question 1 :

import time

def create_timestamp_file():
    current_timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = current_timestamp + ".txt"
    with open(file_name, "w") as file:
        file.write(current_timestamp)
    
    print("File", file_name, "created with timestamp as content.")

create_timestamp_file()
