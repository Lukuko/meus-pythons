from cgi import print_arguments
import pandas as pd
from openpyxl import workbook
d ={'Nome':['Ana','Joao','Maria'], 'idade':[20, 45, 38], 'Altura':[1.56, 1.78, 1.73]}

dados = pd.DataFrame(data= d)

print(dados)

dados.to_excel('dados.xls', index = False)

