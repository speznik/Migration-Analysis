import csv

# Function to read data from CSV file
def read_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

# Example usage to access rows and columns
if __name__ == "__main__":
    filename = 'country_location_mapping_900.csv'  # Change this to the name of your CSV file
    output = "output1.csv"
    
    csv_data = read_csv(filename)
    
    d = {}
    # Accessing rows
    print("Rows:")
    i = 0
    temp = []
    for row in csv_data:
        t = row[:2]
        if(i == 0):
            pass
        else:
            d[t[1]] = t[0]
        i += 1
    print(d)
    # # Accessing columns
    # print("\nColumns:")
    # for col in zip(*csv_data):
    #     print(col)