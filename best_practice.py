# Best practices according to Real python to control code execution

from time import sleep

print("this is my file to demonstrate best practices")

def process_data(data):
    print("beginning data processing...")
    modified_data = data + " that has been processed"
    sleep(3)
    print("data processing finished")
    return modified_data

def read_data_from_web():
    print("reading data from web")
    data = "data from the web"
    return data

def write_to_database(data):
    print("writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_to_database(modified_data)

if __name__ == "__main__":
    main()