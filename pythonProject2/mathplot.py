import matplotlib.pyplot as py
from matplotlib import style
import numpy as np

py.subplot(2, 2, 1)
data = [34, 10, 15, 33, 8]
py.title("LANGUAGE MARKET SHARE")
py.pie(data, shadow=True, autopct="%d%%", explode=[0.1, 0, 0, 0, 0], labels=["Python", "C", "java", "C++", "others"],colors=["pink", "purple", "maroon", "cyan", "grey"])

py.subplot(2, 2, 2)
# # py.style.use("ggplot")
overs = np.arange(1, 11)
iruns = [8, 15, 7, 2, 12, 16, 0, 13, 19, 10]
# # sruns = [2, 6, 20, 30, 16, 21, 1, 7, 10, 17]
# py.title("LANGUAGE MARKET SHARE")
py.xlabel("Overs")
py.ylabel("Runs")
py.xticks(overs)
py.yticks(np.arange(1, 31))
# py.pie(data, shadow=True, autopct="%d%%", explode=[0.1, 0, 0, 0, 0], labels=["Python", "C", "java", "C++", "others"],colors=["pink", "purple", "maroon", "cyan", "grey"])
py.bar(overs-0.2, iruns, color="blue", label="IND", width=0.4)
# # py.bar(overs+0.2, sruns, color="green", label="SA", width=0.4)
# # py.legend()
# # #py.plot(overs, sruns, color="green", marker="o", label="SA")
py.subplot(2,2,3)
year=np.arange(2010,2024)
lsales=np.random.randint(100,3000,14)
msales=np.random.randint(100,3000,14)
ssales=np.random.randint(100,3000,14)
py.style.use('bmh')
py.title("Laptop Sales")
py.xlabel("Years")
py.ylabel("Units Sales Per Year")
py.xticks(year)
py.plot(year,lsales,color="maroon",label="Laptop")
py.plot(year,msales,color="green",label="Mobile")
py.plot(year,ssales,color="cyan",label="Mobile")


py.subplot(2, 2, 4)
no = np.arange(1, 101)
math = np.random.randint(1, 30, 100)
py.scatter(no, math, marker="*")

py.show()
