import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt


class Datas1():

    def rowInfo(self, data, query_row): #find row data
        print ("hi")

        row_index = data.set_index('Country')
        row = row_index.loc[query_row]
        return row

    def Query_Point_in_row(self, row, point):
        indx = 0

        for elements in row:

            elementsKey = str((round(elements, 3)))

            if point == (elementsKey):
                print (indx)
                print(row.iloc[7:7])
                return str((point) + " Found at : " + str(row.iloc[indx:indx+1]))
            indx = indx + 1

    def Threshold_Query(self, data, col, threshLow, threshHigh):

        threshLow = float(threshLow)
        threshHigh = float(threshHigh)
        #print ((data[(data[col] > threshHigh)]))
        data[col] = pd.to_numeric(data[col], errors = 'coerce')
        thresh_accepted = data[(data[col] > threshLow) & (data[col] < threshHigh)]
        return thresh_accepted

    def plot(self, data, column1, column2):

        plt.scatter(data[column1], data[column2])
        plt.show()

    def columnInfo(self,cData, query_column): #find column data

        return(cData[query_column])

    def Query_Point_in_Column(self, data, point, column):
        return (data[(data[column] > (point - 0.002)) & (data[column] < (point + 0.002))])


    def Query_PointAll(self, data, point):
        col_indx = 0
        cell_indx = 0
        for columns in data:
            if col_indx > 0:
                truth_set = data[(data[columns] > (point - 0.005)) & (data[columns] < (point + 0.005))]
                if len(truth_set):
                    return("Key Found In : \n" + str(truth_set.iloc[:, :2]))

            col_indx += 1
    """
    columnData = pd.read_csv('2017.csv')

    query_column = input('Enter column to find\n Enter all if none in particular')

    columnInfo(object, columnData, query_column)"""