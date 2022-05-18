import pandas as pd
from openpyxl import workbook

m = str(input(""))
n = str(input(""))
d ={'Matrícula':[m],'Nome':[n]}

dados = pd.DataFrame(data= d)

print(dados)

dados.to_excel('dados_alunos.xls', index = False)
