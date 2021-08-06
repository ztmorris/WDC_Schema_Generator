import os
import pandas as pd

from os import path

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    schemaDef = ["id", "dataType: tableau.dataTypeEnum."]
    fileTypes = ["csv"]
    schemaSetDirectory = "/Users/zacmorris/Documents/BIMO/DataSamples/CurrentDataSets"
    allCols = []
    dataCol = {}


    dataSets = os.listdir(schemaSetDirectory)

    # for d in dataSets:
    #     with open(schemaSetDirectory + "/" + d, "r") as newSchema:
    #         line = newSchema.readline()
    #         print(d + ":" + line)

    # with open(populatedFileName, 'w') as newFile:
    count = 1

    for ds in dataSets:
        file, ext = os.path.splitext(ds)

        if ext.replace(".", "") in fileTypes:
            # with open(schemaSetDirectory + "/" + ds, "r") as newSchema:
            # header = pd.read_csv(schemaSetDirectory + "/" + ds, nrows=1)
            try:
                # print(pd.read_csv(schemaSetDirectory + "/" + ds, nrows=0))
                header = pd.read_csv(schemaSetDirectory + "/" + ds, nrows=0)

                for h in header:
                    print('"' + schemaDef[0] + '"' + ":" + '"' + h + '"')

                # print(header)
            except Exception as e:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)
                print(message)
        print(ds)
        print("Counter: " + str(count))
        count += 1


# line = newSchema.readline()
#                 print(line)
#             print(ds)