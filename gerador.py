import csv
import random

filme = csv.reader(open('filmes2.csv', newline=''), delimiter=';')
filmes=[]
pessoasql=open("pessoas.sql","w+")
pessoacql=open("pessoas.cql","w+")
filmesql=open("filmes.sql","w+")
filmecql=open("filmes.cql","w+")

pessoa = csv.reader(open('pessoas2.csv', newline=''), delimiter=';')
pessoas =[]

for row in pessoa:
    pessoas.append(row)
    pessoacql.write('CREATE (p'+row[0]+':Pessoa {id:'+row[0]+', nome:"'+row[1]+'", nascEm:'+row[2]+'})\n')
    pessoasql.write("INSERT INTO Pessoa VALUES("+row[0]+",'"+row[1]+"',"+row[2]+");\n")

npessoas=len(pessoas)
print(npessoas)

relacao=[]
cont=0
row=[]

for row in filme:
    
    filmes.append(row)
    filmecql.write('CREATE (f'+row[0]+':Filme {id:'+row[0]+', titulo:"'+row[1]+'",genero:"'+row[2]+'", lancamento:'+row[3]+',duracao:'+row[4]+'})\n')
    filmesql.write('INSERT INTO Filme VALUES('+row[0]+',"'+row[1]+'","'+row[2]+'",'+row[3]+','+row[4]+');\n')
    diretor=random.randrange(1,npessoas,10)
    produtor=random.randrange(2,npessoas,10)
    escritor=random.randrange(3,npessoas,10)
    atores=random.randint(1,5)
    crew=[cont,diretor,produtor,escritor]
    for i in range(atores):
        crew.append(random.randint(1,npessoas))
    cont+=1
    relacao.append(crew)
    
print(len(filmes))






#for row in filmes:
    
print(len(relacao))
mssql=open("relacoes.sql","w+")
cypher=open("relacoes.cql","w+")
j=0
for row in relacao:
    mssql.write("INSERT INTO dirigiu VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[1])+"),(SELECT $node_id FROM Filme WHERE id = "+str(row[0])+"));\n")
    mssql.write("INSERT INTO produziu VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[2])+"),(SELECT $node_id FROM Filme WHERE id = "+str(row[0])+"));\n")
    mssql.write("INSERT INTO escreveu VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[3])+"),(SELECT $node_id FROM Filme WHERE id = "+str(row[0])+"));\n")
    for i in range((len(row)-4)):
        mssql.write("INSERT INTO atuouEm VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[i+4])+"),(SELECT $node_id FROM Filme WHERE id = "+str(row[0])+"));\n")
mssql.close()

for row in relacao:
    cypher.write("CREATE \n")
    cypher.write("    (p"+str(row[1])+")-[:DIRIGIU]->(f"+str(row[0])+"),\n")
    cypher.write("    (p"+str(row[2])+")-[:PRODUZIU]->(f"+str(row[0])+"),\n")
    cypher.write("    (p"+str(row[3])+")-[:ESCREVEU]->(f"+str(row[0])+"),\n")
    #cypher.write("INSERT INTO dirige VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[1])+"),(SELECT $node_id FROM filmes WHERE id = "+str(row[0])+"));\n")
    #cypher.write("INSERT INTO produz VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[2])+"),(SELECT $node_id FROM filmes WHERE id = "+str(row[0])+"));\n")
    #cypher.write("INSERT INTO escreve VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[3])+"),(SELECT $node_id FROM filmes WHERE id = "+str(row[0])+"));\n")
    for i in range((len(row)-4)):
        if i==(len(row)-5):
            cypher.write("    (p"+str(row[i+4])+")-[:ATUOU_EM]->(f"+str(row[0])+")\n")
            break
        cypher.write("    (p"+str(row[i+4])+")-[:ATUOU_EM]->(f"+str(row[0])+"),\n")
        #cypher.write("INSERT INTO atuaEm VALUES ((SELECT $node_id FROM Pessoa WHERE id ="+str(row[i+4])+"),(SELECT $node_id FROM filmes WHERE id = "+str(row[0])+"));\n")
cypher.close()
pessoasql.close()
pessoacql.close()
filmesql.close()
filmecql.close()

    #print('CREATE (f'+row[0]+':Filme {id:'+row[0]+', titulo:"'+row[1]+'",genero:"'+row[2]+'", lancamento:'+row[3]+',duracao:'+row[4]+'})')
    #print('CREATE (p'+row[0]+':Pessoa {id:'+row[0]+', nome:"'+row[1]+'", nascEm:'+row[2]+'})')
    #print("INSERT INTO Pessoa VALUES("+row[0]+",'"+row[1]+"',"+row[2]+");")
    #print('INSERT INTO Pessoa VALUES('+row[0]+',"'+row[1]+'",'+row[2]+');')
    #print('INSERT INTO Filme VALUES('+row[0]+',"'+row[1]+'",'+row[2]+');')
    #print('INSERT INTO Filme VALUES('+row[0]+',"'+row[1]+'","'+row[2]+'",'+row[3]+','+row[4]+');')

