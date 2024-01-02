from pprint import pprint

with open("Data/portfolio.dat", "r") as f:
    headers = next(f).split(",")
    data = []
    
    for line in f:
        row = line.split(",")
        data.append(row)

pprint(data)