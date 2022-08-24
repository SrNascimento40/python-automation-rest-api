f = open('inputFile.txt', 'r')
#lê o arquivo inputFile (arquivo, interação com o arquivo {r=read})
print(f.read())
#printa o que foi lido em f
f.close()
#para a leitura para evitar consequencias inesperadas
f = open('inputFile.txt', 'r')
count = 0
for line in f:
    print(str(count) + " - " + line)
    count = count + 1
#conta as linhas
f.close()

f = open('inputFile.txt', 'r')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

f.close()

#printa apenas os aprovados

f = open('inputFile.txt','r')
#lê o arquivo
output1 = "PassFile.txt"
output2 = "FailFile.txt"
#define as variáveis
passFile = open(output1,'w')
failFile = open(output2, 'w')
#Cria as variáveis e escreve nelas
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)
passFile.close()
failFile.close()
#lê quem passou e quem reprovou e cria um arquivo com cada um

