import json
import os
import pandas


def main():
    columns = ['DATE', 'LATITUDE', 'LONGITUDE', 'PRCP']

    parsed_data = {}
    i = 0

    for file in os.listdir(os.getcwd()):
        if file.endswith(".csv"):
            try:
                data = pandas.read_csv(file, usecols = columns)
                # Since every file has info about the sampe place, we
                # only need to read it once
                print("Filename is ", file)
                longitude = data.get_value(0, 'LONGITUDE')
                latitude = data.get_value(0, 'LATITUDE')
                time_period = data['DATE'].iget(-1)
                prcp = data['PRCP'].iget(-1)
                parsed_data[str((latitude, longitude, time_period))] = prcp
                print(parsed_data)

                with open('data.txt', 'w') as outfile:
                    json.dump(parsed_data, outfile)
            
            # There would be a ValueError because data set is polluted with links to them
            # We would need some robust glob pattern matching for this t work
            except ValueError:
               continue

if __name__== "__main__":
    main()
    # profile.run('main')
    # import profile
