from data_utils import download_data, read_data


def main():
    path_to_file = download_data()
    data_frame = read_data(path_to_file)
    print(data_frame.head())
    print(data_frame['Class'].value_counts())

    return 0

if __name__ == "__main__":
    main()