

def readFile():
    path = "../data/a280.txt"
    counter = 0
    length = -1
    coordsList = []

    textFile = open(path, "r")
    lines = textFile.readlines()

    for line in lines:
        counter=counter+1

        if counter<7: #info lines
            if counter==4: #length line
                splits=line.split()
                length=splits[1]
                print(length)
            continue
        
        # print("length "+length)
        # print("coords" + str(len(coordsList)))
        if len(coordsList) == int(length):
            break

        splitString = line.split()
        dataPt = (splitString[1], splitString[2])
        # print(dataPt)
        coordsList.append(dataPt)
    return coordsList

# def create_data_model():
#     """Stores the data for the problem."""
#     data = {}
#     # Locations in block units

#     data['locations'] = readFile()  # yapf: disable
#     data['num_vehicles'] = 1
#     data['depot'] = 0
#     return data

# print(create_data_model())

arrayCoords = readFile()
print(arrayCoords[5])