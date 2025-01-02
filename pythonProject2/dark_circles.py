# import pandas
# import matplotlib.pyplot as pt
#
# data = pandas.read_excel("hospital_data_set.xls")
# # die = input("Enter disease name")
# # print(data.id[data.diseases == die].count())
# m = data[data.gender == 'M'].groupby('diseases')["id"].count()
# f = data[data.gender == 'F'].groupby('diseases')["id"].count()
# pt.subplot(1,2,1)
# m.plot(kind="bar")
# pt.subplot(1,2,2)
# f.plot(kind="bar", color="pink")
# pt.show()

names = ['Amir', 'Bear', 'Charlton', 'Daman']
print (names[-1][-1])




