
#n precisar fechar o arquivo, ele fecha automáticamente
with open('abc.txt', 'a+') as file:
    file.write('Outra Linha\n')
    file.seek(0)
    print(file.read())
    
    
