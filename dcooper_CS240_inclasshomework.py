def main():
    """ (file open for reading) -> Nonetype
    Is the main function of the program
    """
    data_list = internet_data()
    print(data_list)
    countries = internet_countries(data_list)
    print(countries)
    years = internet_years(data_list)
    print(years)
    earliest_year = earliest_year_reported(data_list)
    print(earliest_year)
    latest_year = latest_year_reported(data_list)
    print(latest_year)
    no_data = countries_no_data(data_list)
    print(no_data)


def internet_data():
    """ (file open for reading) -> str
    Receives the data from the internet site and appends the data to a list of\
    lists.
    """

    import urllib.request
    url = 'http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/WHS3_45&profile=crosstable&filter=COUNTRY:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR'
    data_list = []
    with urllib.request.urlopen(url) as webpage:
        for line in webpage.readlines():
            line = line.decode('utf-8')
            line = line.strip()
            line = line.split(',')
            newline = []
            for item in line:
                newline.append(item[1:-1])
            data_list.append(newline)
    return(data_list)


def internet_countries(data_list):
    """ (file open for reading) -> int
    Counts how many countries are in the dataset.
    """

    num_of_countries = len(data_list) - 2
    return (num_of_countries)
    # return len(data_list) - 2


def internet_years(data_list):
    """ (file open for reading) -> Nonetype
    Counts how many years are in the dataset.
    """
    country = data_list[1]
    return len(country[1:])
    # return len(data_list[0]) - 1


def earliest_year_reported(data_list):
    """ (file open for reading) -> int
    Returns the earliest year reported.
    """
    country = data_list[1]
    return min(country[1:])
    # return sorted(data_list[1][1:])[0]


def latest_year_reported(data_list):
    """ (file open for reading) -> int
    Returns the latest year reported.
    """
    country = data_list[1]
    return max(country[1:])
    # return sorted(data_list[1][1:])[-1]


def countries_no_data(data_list):
    """ (file open for reading) -> Nonetype
    Returns how many countries have no data for all years.
    """
    no_data_list = data_list
    item = 'No data'
    for no_data_list in data_list:
        if item in no_data_list:
            return len(no_data_list)
    # number_of_countries_with_no_data = 0
    # for line in data_list:
        # if(line.count('No data') == len(data_list[0]) -1):
            # number_of_countries_with_no_data += 1
    # return number_of_countries_with_no_data


def countries_data(data_list):
    """ (file open for reading) -> Nonetype
    Returns how many countries have data for all years.
    """
    # number_of_countries_with_all_data = 0
    # for line in data_list:
        # if(line.count('No data') == 0):
            # number_of_countries_with_all_data += 1
    # return number_of_countries_with_all_data


def highest_number(data_list):
    """ (file open for reading) -> Nonetype
    Returns which counry had the highest number of reported cases for each\
    reporting year.
    """
    # output = []
    # for column in range(1, len(data[0])):
        # year = []
        # for row in range(1, len(data)):
            # if data[row][column] == 'No data':
                # year.append(0)
            # else:
                # year.append(int(data[row][column]))
        # years = data[1][column]
        # deaths = max(year)
        # country = data[year.index(deaths) + 1][0]
        # output.append("{} {} ({})".format(years, country, deaths))
    # return output


if __name__ == '__main__':
    main()
