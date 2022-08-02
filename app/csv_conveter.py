#!/usr/bin/python

import csv, iso3166
from datetime import datetime

#add errors handling and write the test cases
#dockerise this stuff
class Error(Exception):
    """My Base class for other exceptions related to this program"""
    pass

class WrongArgumentNumber(Error):
    """Raised when number of columns is wrong"""
    pass




    """
            Function name: csv_converter
            arguments: filename(str)
            description: takes a filename,opens the file, sorts(and formats) the rows, then outputs the result into a string
            returns: return_string, a string
    """

def csv_converter(filename: str):
    #open the the file
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')#for reading the csv
            big_arr = []#we are going to use this array to store each transformed row

            #for each line in the input file
            for line in csv_reader:
                try:
                    arr = []#list to store the cells(data) of each line
                    #No transformation needed for id, sow e just add it to our array
                    id = line[0]
                    arr.append(id)

                    #Change the format of the date and add it to arr
                    date = datetime.strptime(line[1],'%Y/%m/%d')
                    new_date = datetime.strftime(date,'%Y.%m.%d')
                    arr.append(new_date)

                    #Remove the hyphen in-between the strings of the game name and Capitalize the first letter of each word, add it to arr
                    game_name = line[2].split("-")
                    game_name = " ".join(game_name).capitalize()
                    arr.append(game_name)

                    #convert the country code to name using the iso3166 module and add it to arr
                    try:
                        country_name = iso3166.countries.get(line[3]).name
                        arr.append(country_name)
                    except:
                        print("Invalid Date")
                        return 1
                    #add the number of copies sold to arr
                    copy_sold = int(line[4])#we are going to use this for calculation#
                    arr.append(str(copy_sold))

                    #add the copy price to arr
                    copy_price = line[5].split()
                    arr.append(line[5])
                    copy_price = float(copy_price[0])
                    #Calculate the total revenue. Total revenue = Copies sold * Total Price
                    total_revenue = round(float(copy_sold) * float(copy_price))
                    arr.append(str(total_revenue) + " " + "USD")

                    #if the number of cell in a row, raise an error and catch it
                    try:
                        if len(arr) != 7:
                            raise WrongArgumentNumber
                    except WrongArgumentNumber:
                        print("Wrong number of Argument")
                        return 1
                    #print(arr)
                    big_arr.append(arr)
                except:
                    print("Invalid Inputs")
                    return 1
            #Sort the big_arr according to date
            big_arr.sort(key=lambda output: datetime.strptime(output[1], "%Y.%m.%d"))
            return_string = "ID,Release Date,Name,Country,Copies Sold,Copy Price,Total Revenue\n"

            # turn the big_arr to a csv string using join
            for output in big_arr:
                return_string += ",".join(output)
                return_string += "\n"
            return return_string # return the string
    except:
        print('File cannot open')
        return 1

t = csv_converter("example.txt")



