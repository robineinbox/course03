from utils import get_data, get_filtered_data, get_last_values, formatted_data


def main():
    COUNT_VALUES = 5
    FILTERED_EMPTY_FROM = True


    data = get_data()

    data = get_filtered_data(data, FILTERED_EMPTY_FROM)

    data = get_last_values(data, COUNT_VALUES)

    data = formatted_data(data)



if __name__ == "__main__":
    main()