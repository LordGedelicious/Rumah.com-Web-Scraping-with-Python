import pandas as pd

csv_filename = "cakung_links.csv"
lines_per_file = 101
original_length = 2261
print("Current length of csv file: {}".format(original_length))

filename_count = 0
for i in range(0, original_length, lines_per_file):
    df = pd.read_csv(csv_filename, header=None,
                     skiprows=i, nrows=lines_per_file)
    output_csvfile = "cakung_links_{}.csv".format(filename_count)
    df.to_csv(output_csvfile, index=False, header=False,
              mode="a", chunksize=lines_per_file)
    print("Successfully wrote to {} with length {}".format(output_csvfile, len(df)))
    filename_count += 1
print("Split csv file into {} files".format(filename_count))
