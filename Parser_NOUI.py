import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt


class Datas1():

    def rowInfo(self, data, query_row): #find row data

        row_index = data.set_index('Country')
        row = row_index.loc[query_row]
        print (row)

    def Query_Point_in_row(self, data, query_row, point):
        indx = 0
        row_index = data.set_index('Country')
        row = row_index.loc[query_row]
        for elements in row:

            elementsKey = (round(elements,3))
            if (point) == (elementsKey):
                print (str(point) + " Found at : " + str(row.iloc[indx:indx+1]))
            indx = indx + 1

    def Threshold_Query(self, data, col, threshLow, threshHigh):

        threshLow = float(threshLow)
        threshHigh = float(threshHigh)

        data[col] = pd.to_numeric(data[col], errors = 'coerce')
        thresh_accepted = data[(data[col] > threshLow) & (data[col] < threshHigh)]
        print(thresh_accepted)

    def plot(self, data, column1, column2):

        plt.scatter(data[column1], data[column2])
        plt.show()


    def columnInfo(self,cData, query_column): #find column data

        print (cData[query_column])

    def Query_Point_in_Column(self, data, point, column):
        print (data[(data[column] > (point - 0.002)) & (data[column] < (point + 0.002))])

    def printAll(self, data):
        for row in data:
            print(', '.join(row))
    def Query_PointAll(self,data, point):
        col_indx = 0
        cell_indx = 0
        for columns in data:
            if col_indx > 0:
                truth_set = data[(data[columns] > (point - 0.005)) & (data[columns] < (point + 0.005))]
                if len(truth_set):

                    print ("Key Found In : \n" + str(truth_set.iloc[:,:2]))



            col_indx+=1


    pd.set_option('display.height', 1000)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    pd.set_option('max_colwidth', 25)
    pd.set_option('display.precision', 3)
    data = pd.read_csv('2017.csv')


    #rowInfo(object, data, "Canada")
    #Query_Point_in_row(object, data, "Canada", 1.481)
    #columnInfo(object, data, "Family")
    Query_Point_in_Column(object, data, 1.510, "Family")
    Query_PointAll(object, data, 20)
    Threshold_Query(object,data,"Family", 1.5, 1.6)