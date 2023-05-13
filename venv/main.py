from utils import *

def main():


    COUNT_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data = get_data()
    print(len(data))
    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    print(len(data))
    data = get_last_values(data, COUNT_VALUES)
    print(len(data))
    data = get_formated_data(data)
    print(len(data))

    for row in data:
        print(row, end='\n')

if __name__ == "__main__":
    main()