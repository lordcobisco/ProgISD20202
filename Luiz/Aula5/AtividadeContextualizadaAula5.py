
RioDeJaneiro = ('Rio de Janeiro', 'Niteroi','Petrópoli', 'São Gonçalo', 'Duque de Caixias', 'Nova Iguaçu', 'Nova Friburgo', 'Angra dos Reis', 'Volta Redonda', 'Macaé')
for municípios in RioDeJaneiro:
    print(f'Casos de COVID-19 na Cidades do Rio de Janeiro: {municípios}')
print('até a data de 18/08/2020')

#AviSos
print("********Coronavírus no Brasil ********")
casos=int(input("Você que ver os Casos de Coronavírus no Brasil por Estados? 1 para SIM e 2 para NÃO: "))
estados=27 #R2: i
if (casos==1):
    print("Vamos dar Início")
    casos=True   
else:
     print("\n ********Inicie a Pesquisa Novamente********")
#R2: ii 
     print("\n Escolher outro Estado Brasileiro")
     estado=int(input("Estamos verificando: Digite de 1 a 27 referente aos estados brasileiro que você deseja pesquisa "))
     capital= estado-casos
     if (capital<27):
         print("Vamos Iniciar!!!")
print('-=' *50)
#Vendo os Casos de CoVD-19 no Brasil
########ESCOLHENDO O ESTADO
print("\n Iremos perguntar qual Estado do Brasil você quer Saber")
Acre=int(input("Você quer saber sobre os casos do Acre? 1 para sim e 2 para não: "))#1
if (Acre==1):
        print("Acre - AC   - Casos: 24.462 | Obitos: 608| Mortalidade: 68,9") 
        print('Região de Saúde 1: Baixo Acre (Purus')
        print('Região de Saúde 2: Alto Acre')
        print('Região de Saúde 3: Juruá')
        print('Região de Saúde 4: Tarauacá-Envira') 
        print('Região de Saúde 5: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 6: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 7: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 8: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print("Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO")
else: 
    Alagoas=int(input("E os casos de Alagoas, 1 para sim e 2 para não: "))#2
print('-=' *50)
Alagoas=int(input("Você quer saber sobre os casos de Alagoas, 1 para sim e 2 para não: "))#2
if (Alagoas==1):
    print('Alagoas - AL   - Casos: 78.174 | Obitos: 1.861 | Mortalidade: 55,8')
    print('Região de Saúde 1: Maceió')
    print('Região de Saúde 2: Arapiraca')
    print('Região de Saúde 3: Rio Largo')
    print('Região de Saúde 4: Palmas dos Índios')
    print('Região de Saúde 5: União dos Palmares')
    print('Região de Saúde 6: Penedo')
    print('Região de Saúde 7: Viçosa')
    print('Região dee Saúde 8: Palestina')
    print('Região de Saúde 9: Maragogi')
    print('Região de Saúde 10: Mata Grande')
else:
     Amapa=int(input("E os casos do Amapá, 1 para sim e 2 para não: "))#2
print('-=' *50)     
Amapa=int(input("Você quer saber sobre os casos do Amapá, 1 para sim e 2 para não: "))#3
if (Amapa==1):
        
        print("Amapá- AP   - Casos: 42.625 | Obitos: 657 | Mortalidade: 77,7")
        print('Região de Saúde 1: Norte')
        print('Região de Saúde 2: Central')
        print('Região de Saúde 3: Sudoeste')
        print('Região de Saúde 4: Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 5: Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 6: Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 7: Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 8: Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 9: Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 10: Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else:
    Amazonas=int(input("Você quer saber sobre os casos do Amazonas, Colega 1 para sim e 2 para não: "))#4  
print('-=' *50)     
Amazonas=int(input("Você quer saber sobre os casos do Amazonas, 1 para sim e 2 para não: "))#4
if (Amazonas==1):
         
         print('Amazonas- AM   - Casos:  118.844| Obitos:3.674  | Mortalidade:87,6') 
         print('Região de Saúde 1: Alto Solimões')
         print('Região de Saúde 2: Baixo Amazonas')
         print('Região de Saúde 3: Manau, Entorno do Rio Negro')
         print('Região de Saúde 4: Médio Amazonas')
         print('Região de Saúde 5: Regional Jurua')
         print('Região de Saúde 6: Regional Purus')
         print('Região de Saúde 7: Rio Madeira')
         print('Região de Saúde 8: Rio Negro e Solimões')
         print('Região de Saúde 9: Triangulo') 
         print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else:
     Bahia=int(input("E os casos do Bahia, Beh?, 1 para sim e 2 para não: "))#5
print('-=' *50)          
Bahia=int(input("Você quer saber sobre os casos da Bahia, 1 para sim e 2 para não: "))#5
if (Bahia==1):
         
         print("Bahia - BA   - Casos: 250.977 | Obitos: 5.243 | Mortalidade: 35,3")    
         print('Bahia - BA   - Casos: 250.977 | Obitos: 5.243 | Mortalidade: 35,3')
         print('Região de Saúde 1: Alagoinhas')
         print('Região de Saúde 2: Barreiras')
         print('Região de Saúde 3: Brumado')
         print('Região de Saúde 4: Camacari')
         print('Região de Saúde 5: Cruz das Almas')
         print('Região de Saúde 6: Feira de Santana')
         print('Região de Saúde 7: Guanambi')
         print('Região de Saúde 8: Ibotirama')
         print('Região de Saúde 9: Ilheus')
         print('Região de Saúde 10: Salvador')

else: 
    Ceara=int(input(" E os casos da Caerá, Mah?, 1 para sim e 2 para não: "))#6
print('-=' *50)    
Ceara=int(input("Você quer saber sobre os casos do Ceará, 1 para sim e 2 para não: "))#6
if (Ceara==1):
         
         print('Ceará - CE   - Casos: 212.484  | Obitos: 8.376 | Mortalidade: 91,7')
         print('Região de Saúde 1: Fortaleza')
         print('Região de Saúde 2: Cuacaia')
         print('Região de Saúde 3: Maracanaú')
         print('Região de Saúde 4: Baturité')
         print('Região de Saúde 5: Canidé')
         print('Região de Saúde 6:: Itapipoca')
         print('Região de Saúde 7: Acarati')
         print('Região de Saúde 8: Quixadá')
         print('Região de Saúde 9: Russas')
         print('Região de Saúde 10: Limoeiro do Norte')
else: 
    Espirito=int(input(" E os casos da Espirito Santo?, 1 para sim e 2 para não: "))#7
print('-=' *50)    
Espirito=int(input("Você quer saber sobre os casos do Espirito Santo, 1 para sim e 2 para não: "))#7
if (Espirito==1):
         
         print('Espírito Santo - ES   - Casos: 109.493 | Obitos: 3.117 | Mortalidade: 77,6')
         print('Região de Saúde 1: Norte') 
         print('Região de Saúde 2: Central')
         print('Região de Saúde 3: Metropolitana')
         print('Região de Saúde 4: Sul')
         print('Região de Saúde 5: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 6: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 7: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 8: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else: 
    Goias=int(input(" E os casos da Goias?, 1 para sim e 2 para não: "))#8
print('-=' *50)        
Goias=int(input("Você quer saber sobre os casos do Goiás, 1 para sim e 2 para não: "))#8
if (Goias==1):
                
         print('Goiás - GO - Casos: 128.965 | Obitos: 3.003 | Mortalidade 42,8')
         print('Região de Saúde 1: Central')
         print('Região de Saúde 2: Centro Sul')
         print('Região de Saúde 3: Entorno Norte')
         print('Região de Saúde 4: Entorno Sul')
         print('Região de Saúde 5: Estrada de Ferro')
         print('Região de Saúde 6: Nordeste I')
         print('Região de Saúde 7 Nordeste II')
         print('Região de Saúde 8: Norte') 
         print('Região de Saúde 9: Sul')
         print('Região de Saúde 10: Oeste ')
     
else:
    Maranhao=int(input(" E os casos Maranhão?, 1 para sim e 2 para não: "))#9
print('-=' *50)     
Maranhao=int(input("Você quer saber sobre os casos do Maranhão, 1 para sim e 2 para não: "))#9
if (Maranhao==1):
         
         print('Maranhão - MA   - Casos: 150.144 | Obitos: 3.412  | Mortalidade: 48,2')
         print('Região de Saúde 1: Acailandia')
         print('Região de Saúde 2: Bacabal')
         print('Região de Saúde 3: São Luis')
         print('Região de Saúde 4: Imperatriz')
         print('Região de Saúde 5: Codo')
         print('Região de Saúde 6: Caxias')
         print('Região de Saúde 7: Balsas')
         print('Região de Saúde 8: Barra do Corda')
         print('Região de Saúde 9: Chapadinha')
         print('Região de Saúde 10: Pedreira')
else:
    MatoGrosso=int(input("Você quer saber sobre os casos do Mato Grosso, sem moagem então: 1 para sim e 2 para não: "))#10
print('-=' *50)

MatoGrosso=int(input("Você quer saber sobre os casos do Mato Grosso, 1 para sim e 2 para não: "))#10
if (MatoGrosso==1):
         
         print('Mato Grosso - MT - Casos: 89.140 | Obitos: 2.677 | Mortalidade: 76,8')
         print('Região de Saúde 1: Norte Matogrossence')
         print('Região de Saúde 2: Sul Matogrossence')
         print('Região de Saúde 3: Oeste Matogrossence')
         print('Região de Saúde 4: Alto Patajos')
         print('Região de Saúde 5: Araguaia Xingu')
         print('Região de Saúde 6: Garça Araguaia')
         print('Região de Saúde 7: Baixada Cuiabana')
         print('Região de Saúde 8: Medio Araguaia')
         print('Região de Saúde 9: Norte Araguaia Karaja')
         print('Região de Saúde 10: Teles Pires')
else: 
    MatoGrosso=int(input(" E os casos do Mato Grosso?, 1 para sim e 2 para não: "))#10
print('-=' *50)
MatoSul=int(input("Você quer saber sobre os casos do Mato Grosso do Sul, 1 para sim e 2 para não: "))#11
if (MatoSul==1):
         
         print('Mato Grosso do Sul - MS   - Casos: 47.152 | Obitos:  823| Mortalidade: 29,6')
         print('Região de Saúde 1: Campo Grande')
         print('Região de Saúde 2: Corumba')
         print('Região de Saúde 3: Dourados')
         print('Região de Saúde 4: Três Lagoas')
         print('Região de Saúde 5: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 6: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 7: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 8: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
         print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else: 
    MatoSul=int(input(" E os casos do Mato Grosso do Sul?, 1 para sim e 2 para não: "))#11
print('-=' *50)
Minas=int(input("Você quer saber sobre os casos de Minas Gerais, 1 para sim e 2 para não: "))#12
if (Minas==1):
        
        print('Minas Gerais - MG   - Casos:  209.465| Obitos: 5.167 | Mortalidade: 24,4')
        print('Região de Saúde 1')
        print('Região de Saúde 2')
        print('Região de Saúde 3')
        print('Região de Saúde 4')
        print('Região de Saúde 5')
        print('Região de Saúde 6')
        print('Região de Saúde 7')
        print('Região de Saúde 8')
        print('Região de Saúde 9')
        print('Região de Saúde 10')
else: 
    Minas=int(input(" E os casos da Minas Gerais, Uai?, 1 para sim e 2 para não: "))#12
print('-=' *50)
Para=int(input("Você quer saber sobre os casos do Pará, 1 para sim e 2 para não: "))#13
if (Para==1):
               
         print('Pará - PA   - Casos: 196.874 | Obitos: 6.106  | Mortalidade: 71,0')
         print('Região de Saúde 1: Viçosa')
         print('Região de Saúde 2: Araxa')
         print('Região de Saúde 3: Aracuai')
         print('Região de Saúde 4: Aguas Formosas')
         print('Região de Saúde 5: Barbacena')
         print('Região de Saúde 6: Bocaiuva')
         print('Região de Saúde 7: Betim')
         print('Região de Saúde 8: Campo Belo')
         print('Região de Saúde 9: Carangola')
         print('Região de Saúde 10: Caratinga')
else: 
    Para=int(input(" E os casos do Pará, CalipsooooH?, 1 para sim e 2 para não: "))#13
print('-=' *50)
Paraiba=int(input("Você quer saber sobre os casos da Paraíba, 1 para sim e 2 para não: "))#14
if (Paraiba==1):
               
        print('Paraíba - PB   - Casos: 104.803 | Obitos: 2.404  | Mortalidade: 59,8')
        print('Região de Saúde 1: Mata Atlantica')
        print('Região de Saúde 2')
        print('Região de Saúde 3')
        print('Região de Saúde 4')
        print('Região de Saúde 5')
        print('Região de Saúde 6')
        print('Região de Saúde 7')
        print('Região de Saúde 8')
        print('Região de Saúde 9')
        print('Região de Saúde 10')
else: 
    Goias=int(input(" E os casos da Paraíba, Olha faca?, 1 para sim e 2 para não: "))#14

print('-=' *50)
Parana=int(input("Você quer saber sobre os casos do Paraná, 1 para SIM e 2 para NÃO: "))#15
if (Parana==1):
        
        print("Paraná - PR   - Casos:  126.964| Obitos: 3.194 | Mortalidade: 27,9")
        print('Região de Saúde 1: Paranagua')
        print('Região de Saúde 2: Metropolitana')
        print('Região de Saúde 3: Ponta Grossa')
        print('Região de Saúde 4: Irati')
        print('Região de Saúde 5: Guarapuava')
        print('Região de Saúde 6: União da Vitoria')
        print('Região de Saúde 7: Pato Branco')
        print('Região de Saúde 8: Francisco Beltrão')
        print('Região de Saúde 9: Foz do Iguaçu')
        print('Região de Saúde 10: Cascavel')
else: 
    Parana=int(input(" E os casos do Paraná, NéH?, 1 para sim e 2 para não: "))#15
print('-=' *50)
Pernambuco=int(input("Você quer saber sobre os casos do Pernambuco, 1 para sim e 2 para não: "))#16
if (Pernambuco==1):
        
        print("Pernambuco - PE   - Casos:123.146  | Obitos:7.512  | Mortalidade: 78,6")
        print('Região de Saúde 1: Afogados')
        print('Região de Saúde 2: Arco Verde')
        print('Região de Saúde 3: Recife')
        print('Região de Saúde 4: Caruaru')
        print('Região de Saúde 5: Palmares')
        print('Região de Saúde 6: Limoeiro')
        print('Região de Saúde 7: Goiana')
        print('Região de Saúde 8: Ouricuri')
        print('Região de Saúde 9: Garanhuns ')
        print('Região de Saúde 10: Petrolina')
else: 
    Pernambuco=int(input(" E os casos do Pernambuco, Tabacudo?, 1 para sim e 2 para não: "))#16
print('-=' *50)
Piaui=int(input("Você quer saber sobre os casos do Piauí, 1 para sim e 2 para não: "))#17
if (Piaui==1):
        
        print("Piauí - PI   - Casos: 76.033 | Obitos: 1.785 | Mortalidade: 54,5")
        print('Região de Saúde 1: Carnaubais')
        print('Região de Saúde 2: Cocais')
        print('Região de Saúde 3: Entre Rios')
        print('Região de Saúde 4: Planicie Litoranea')
        print('Região de Saúde 5: Serra da Capivara ')
        print('Região de Saúde 6: Tabuleiro do Alto Parnaiba')
        print('Região de Saúde 7: Vale do Canidé')
        print('Região de Saúde 8: Vale do Sambito')
        print('Região de Saúde 9: Vale Rio Guaribas')
        print('Região de Saúde 10: Vale do Rio Piaui e Itaueiras')
else: 
    Piaui=int(input(" E os casos do Piauí?, 1 para sim e 2 para não: "))#17
print('-=' *50)

Rio=int(input("Você quer saber sobre os casos do Rio de Janeiro, 1 para sim e 2 para não: "))#18
if (Rio==1):
         
         print('Rio de Janeiro - RJ   - Casos: 219.198 | Obitos: 15.859 | Mortalidade: 91,9')
         print('Região de Saúde 1: Metropolitana I')
         print('Região de Saúde 2: Metropolitana II')
         print('Região de Saúde 3: Centro Sul')
         print('Região de Saúde 4: Norte')
         print('Região de Saúde 5: Nordest:e')
         print('Região de Saúde 6: Baia Ilha Grande')
         print('Região de Saúde 7: Medio Paraiba')
         print('Região de Saúde 8: Serrana')
         print('Região de Saúde 9: Baixada Litoranea')
         print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else: 
    Rio=int(input(" E os casos do Rio de Janeiro, Muleke?, 1 para sim e 2 para não: "))#18
print('-=' *50)
Potiguar=int(input("Você quer saber sobre os casos do Rio Grande do Norte, 1 para sim e 2 para não: "))#19
if (Potiguar==1):
        
        print('Rio Grande do Norte - RN  - Casos: 61.219 | Obitos:2.234  | Mortalidade: 63,7')
        print('Região de Saúde 1: São José de Mipibu')
        print('Região de Saúde 2: Mossoró')
        print('Região de Saúde 3: João Camara')
        print('Região de Saúde 4: Caicó')
        print('Região de Saúde 5: Santa Cruz')
        print('Região de Saúde 6: Pau dos Ferros')
        print('Região de Saúde 7: Metropolitana')
        print('Região de Saúde 8: Açú')
        print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else: 
    Potiguar=int(input(" E os casos do Rio Grande do Norte, Boyzinho?, 1 para sim e 2 para não: "))#19
print('-=' *50)
Riosul=int(input("Você quer saber sobre os casos do Rio Grande do Sul, 1 para sim e 2 para não: "))#20
if (Riosul==1):
       
       print('Rio Grande do Sul - RS   - Casos: 120.739 | Obitos: 3.322| Mortalidade: 29,2')
       print('Região de Saúde 1')
       print('Região de Saúde 2')
       print('Região de Saúde 3')
       print('Região de Saúde 4')
       print('Região de Saúde 5')
       print('Região de Saúde 6: Vale do Paranhana e Costa Serra')
       print('Região de Saúde 7')
       print('Região de Saúde 8')
       print('Região de Saúde 9')
       print('Região de Saúde 10')
else: 
    Riosul=int(input(" E os casos do Rio Grande do Sul, Bah Tchê?, 1 para sim e 2 para não: "))#20
print('-=' *50)
Ro=int(input("Você quer saber sobre os casos de Rondônia, 1 para sim e 2 para não: "))#21
if (Ro==1):
        
        print('Rondônia - RO   - Casos: 54.205 | Obitos: 1.114 | Mortalidade: 62,7')
        print('Região de Saúde 1: Café')
        print('Região de Saúde 2: Central')
        print('Região de Saúde 3: Cone Sul')
        print('Região de Saúde 4: Madeira-Mamoré')
        print('Região de Saúde 5: Vale do Guaporé')
        print('Região de Saúde 6: Vale do Jamari')
        print('Região de Saúde 7: Zona da Mata')
        print('Região de Saúde 8: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else: 
    Ro=int(input(" E os casos do Rondônia?, 1 para sim e 2 para não: "))#21
print('-=' *50)
RR=int(input("Você quer saber sobre os casos de Roraima, 1 para sim e 2 para não: "))#22
if (RR==1):
        
        print('Roraima - RR   - Casos: 42.997 | Obitos: 587 | Mortalidade: 96,9')
        print('Região de Saúde 1: Centro Norte ')
        print('Região de Saúde 2: Sul')
        print('Região de Saúde 3: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 4: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 5: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 6: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 7: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 8: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
else: 
    RR=int(input(" E os casos de Roraima?, 1 para sim e 2 para não: "))#22
print('-=' *50)

Catarina=int(input("Você quer saber sobre os casos de Santa Catarina, 1 para sim e 2 para não: "))#23
if (Catarina==1):
        
        print('Santa Catarina - SC   - Casos:141.692  | Obitos: 2.193  | Mortalidade: 30,6')
        print('Região de Saúde 1: Xanxeré')
        print('Região de Saúde 2: Grande Florianopolis')
        print('Região de Saúde 3: Carbonifera')
        print('Região de Saúde 4: Extremo Oeste')
        print('Região de Saúde 5: Extremo Sul Catarinense')
        print('Região de Saúde 6: Foz do Rio Itajaí')
        print('Região de Saúde 7: Laguna')
        print('Região de Saúde 8: Meio Oeste')
        print('Região de Saúde 9: Nordeste')
        print('Região de Saúde 10: Planalto Norte')
else: 
    Catarina=int(input(" E os casos de Santa Catarina?, 1 para sim e 2 para não: "))#23
print('-=' *50)

Sampa=int(input("Você quer saber sobre os casos de São Paulo, 1 para sim e 2 para não: "))#24
if (Sampa==1):
        
        print('São Paulo - SP    - Casos: 796.209  | Obitos: 29.694 | Mortalidade: 64,7')
        print('Região de Saúde 1: São Paulo')
        print('Região de Saúde 2: Bauru')
        print('Região de Saúde 3: Bragança')
        print('Região de Saúde 4: Catanduva')
        print('Região de Saúde 5: Alto Tiete')
        print('Região de Saúde 6: Alto Capivari')
        print('Região de Saúde 7: Arara')
        print('Região de Saúde 8: Assis')
        print('Região de Saúde 9: Grande ABC')
        print('Região de Saúde 10: Itapetininga')

else: 
    Catarina=int(input(" E os casos de São `Paulos?, 1 para sim e 2 para não: "))#24
print('-=' *50)

Sergipe=int(input("Você quer saber sobre os casos do Sergipe, 1 para sim e 2 para não: "))#25
if (Sergipe==1):
        
        print('Sergipe - SE   - Casos: 72.039  | Obitos: 1.837  | Mortalidade: 79,9')
        print('Região de Saúde 1: Aracaju')
        print('Região de Saúde 2: Estância')
        print('Região de Saúde 3: Itabaiana')
        print('Região de Saúde 4: Largato')
        print('Região de Saúde 5: Nossa Senhora da Gloria')
        print('Região de Saúde 6: Nossa Senhora do Socorro')
        print('Região de Saúde 7: Própria')
        print('Região de Saúde 8: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')


else: 
    Sergipe=int(input(" E os casos de Sergipe?, 1 para sim e 2 para não: "))#25
print('-=' *50)
Tocantins=int(input("Você quer saber sobre os casos do Tocantis, 1 para sim e 2 para não: "))#26
if (Tocantins==1):
        
        print('Tocantins - TO   - Casos: 48.580 | Obitos: 649 | Mortalidade: 41,3')
        print('Região de Saúde 1: Amor Perfeito')
        print('Região de Saúde 2: Bico do Papagaio')
        print('Região de Saúde 3: Cantão')
        print('Região de Saúde 4: Capim Dourado')
        print('Região de Saúde 5: Cerrado Tocantis Araguaia')
        print('Região de Saúde 6: Ilha do Bananal')
        print('Região de Saúde 7: Medio Norte Araguaia')
        print('Região de Saúde 8: Sudeste')
        print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')

else:
    Brasilia=int(input("Você quer saber sobre os casos do Distrito Federal, 1 para sim e 2 para não: "))#27
print('-=' *50)
 

Brasilia=int(input("Você quer saber sobre os casos do Distrito Federal, 1 para sim e 2 para não: "))#27
if (Brasilia==1):
        
        print('Distrito Federal - DF  - Casos: 158.180 | Obitos: 2.440 | Mortalidade: 80,9')
        print('Região de Saúde 1: Distrito Federal')
        print('Região de Saúde 2: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 3: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 4: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 5: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 6: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 7: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 8: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 9: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')
        print('Região de Saúde 10: NÃO EXISTE ESTA REGIÃO DE SAÚDE NESTE ESTADO')

else:
    print("E esses foram os Casos reegistrados até o dia 29 de Agosto de 2020!!!")

letraB = ['Rio de Janeiro',  'RJ','Casos: 219.198',  'Obitos: 15.859',  'Mortalidade: 91,9']
print(letraB[0])
print('-=' *50)
print(letraB[1])
print('-=' *50)
print(letraB[2])
print('-=' *50)
print(letraB[3])
print('-=' *50)
print(letraB[4])
print('-=' *50)


#listaMenu = ['Data da Atualização',	'Casos de Obtos', 'RJ',	'Data de Casos Acumulados',	'Casos Acumulados RJ','RF,'	'Municipio',	'N° de Entrada',	'Hopital',	'CPF',	'Sexo',	'Data de Nasc.',	'Idade',	'Nº Protocolo',	'N° Região de Saúde',	'Nacionalidade',		'Estado',	'Naturalidade',	'N° Cadastros',	'Sintomas',	'Grupo de Risco',	'Data da Entrada',	'Entrada na Enfremaria',	'Saida da Enfermaria', 	'Entrada na UTI',	'Saida da UTI',]																																																																																																																																

lista = [8/4/2020,	    15,	28/3/2020,	13,	'RJ',   'RIO DE JANEIRO',   330455,     'CASA DE PORTUGAL',                             3113205,    'M',    23/11/1963,	56,	3056,   9,  'BRASIL',   1,  'RJ',   'RIO DE JANEIRO',   330455,	1,    'S',  31/3/2020,31/3/2020,8/4/2020,	8/4/2020,	9/4/2020,      ]
lista2 = [25/3/2020,	13,	21/3/2020,	12,	'RJ',	'SAO GONCALO',	    330490,     'HOSPITAL SAO GONCALO LTDA', 	                2696851,    'F',    26/9/2016,	3,	3003,	1,	'BRASIL',	1,	'RJ',	'SAO GONCALO',	    330490,	1,	  'S',	25/3/2020,	25/3/2020,	7/5/2020,	1/7/2020,	20/4/2020,]
lista3 = [30/1/2020,	5,	23/1/2020,	4,	'RJ',	'NITEROI',	        330330,	    'HOSPITAL ICARAI',	                            6734014,	'F',	6/10/1957,	62,	3062,	1,	'BRASIL',	1,	'RJ',	'NITEROI',	        330330,	2,	  'S',	24/1/2020,	24/1/2020,	1/2/2020,	7/8/2020,	4/2/2020, ]
lista4 = [8/4/2020,	    15,	7/4/2020,	15,	'RJ',	'DUQUE DE CAXIAS',	330170,	    'UPA INFANTIL WALTER GARCIA',	                7427549,	'M',	26/6/2019,	1,	2010,	9,	'BRASIL',	1,	'RJ',	'DUQUE DE CAXIAS',	330170,	2,	  'N',	8/4/2020,	9/4/2020,	17/4/2020,	4/5/2020,	13/4/2020, ]   
lista5 = [20/4/2020,	17,	15/4/2020,	16,	'RJ',	'RIO DE JANEIRO',	330455,	    'SMS UPA 24H ROCINHA AP 21',                 	6507409,	'M',	17/4/1967,	52,	3052,	4,	'BRASIL',	1,	'RJ',	'RIO DE JANEIRO',	330455,	2,	  'N',	20/4/2020,	20/4/2020,	7/5/2020,	1/7/2020,	20/4/2020, ]
lista6 = [17/4/2020,	16,	15/4/2020,	16,	'RJ',	'RIO DE JANEIRO',	330455,	    'CASA DE SAUDE SAO JOSE',	                    2271443,	'M',	9/8/1940,	79,	3079,	9,	'BRASIL',	1,	'RJ',	'RIO DE JANEIRO',	330455,	1,	  'N',	17/4/2020,	15/4/2020,	1/2020,	    4/5/2020,	9/4/2020,	]    
lista7 = [28/4/2020,	18,	21/4/2020,	17,	'RJ',	'RIO DE JANEIRO',	330455,	    'SMS RIO HOSPITAL MUNICIPAL SALGADO FILHO',  	2296306,	'M',	27/5/1963,	56,	3056,	4,	'BRASIL',	1,	'RJ',	'RIO DE JANEIRO',	330455,	2,	  'S',	24/4/2020,	30/4/2020,	7/5/2020,	4/5/2020,	9/4/2020,	]  
lista8 = [19/3/2020,	12,	17/3/2020,	12,	'RJ',	'RIO DE JANEIRO',	330455,	    'SEMIU SERVICOS DE ESP MED E INT DE URGENCIA',	3531228,	'F',    3/6/1924,	95,	3095,	1,	'BRASIL',	1,	'RJ',	'RIO DE JANEIRO',	330455,	1,	  'S',	18/3/2020,	18/3/2020,	4/5/2020,	1/7/2020,	9/4/2020,	]
lista9 = [27/3/2020,	13,	22/3/2020,	13,	'RJ',	'RIO DE JANEIRO',	330455,	    'HOSPITAL RIOS DOR',                         	6176666,	'M',	6/3/1951,	68,	3068,	1,	'BRASIL',	1,	'RJ',	'RIO DE JANEIRO',	330455,	1,	  'S',	23/3/2020,	24/3/2020,	1/2/2020,	1/4/2020,	29/3/2020,	]
lista10 = [27/3/2021,	19,	13/4/2020,	16,	'RJ',	'RIO DE JANEIRO',	330455, 	'UERJ HOSPITAL UNIV PEDRO ERNESTO',	            2269783	,   'M',    11/10/1951,	68,	3068,	2,	'BRASIL',	1,	'RJ',	'DUQUE DE CAXIAS',	330170,	1,	  'S',	21/4/2020,	21/4/2020,	27/4/2020,	12/5/2020,	24/5/2020,	]


print('CASOS DE ÓBITOS')



Acre = ["AC","Casos: 24.462", "Obitos: 608", "Mortalidade: 68,9"]
Alagoas = ['AL', "Casos: 78.174", "Obitos: 1.861","Mortalidade: 55,8"]
Amapa = ["AP" ,"Casos: 42.625", "Obitos: 657","Mortalidade: 77,7"]
Amazonas = ["AM","Casos:  118.844", "Obitos:3.674" ,"Mortalidade:87,6"]
Bahia = ["BA", "Casos: 250.97", "Obitos: 5.243", "Mortalidade: 35,3"]
Ceara = ["CE", "Casos: 212.484" ,"Obitos: 8.376", "Mortalidade: 91,7"]
Espirito = ["Espirito Santo-ES", "Casos: 109.493", "Obitos: 3.117", "Mortalidade: 77,6"]
Goias = ["GO", "Casos: 128.965", "Obitos: 3.003", "Mortalidade 42,8"]
Maranhao = ["MA","Casos: 150.144", "Obitos: 3.412", "Mortalidade: 48,2"]
MatoGrosso = ['MT', 'Casos: 89.140', ''"Obitos: 2.677", "Mortalidade: 76,8"]
MatoGrossoSul = ['MS', 'Casos: 47.152', 'Obitos:  823', 'Mortalidade: 29,6']
MinasGerais = ['MG', 'Casos:  209.465', 'Obitos: 5.167', 'Mortalidade: 24,4']
para = ['PA',  'Casos: 196.874', 'Obitos: 6.106',  'Mortalidade: 71,0']
Parana = ['PR', 'Casos: 126.964','Obitos: 3.194', 'Mortalidade: 27,9']
Pernambuco = ['PE', 'Casos:123.146' , 'Obitos:7.512', 'Mortalidade: 78,6']
Piaui = ['PI', 'Casos: 76.033', 'Obitos: 1.785','Mortalidade: 54,5']
RioJaneiro = ['RJ', 'Casos: 219.198' , 'Obitos: 15.859', 'Mortalidade: 91,9']
RioNorte = ['RN', 'Casos: 61.219', 'Obitos:2.234', 'Mortalidade: 63,7']
RioSul = ['RS', 'Casos: 120.739', 'Obitos: 3.322' ,'Mortalidade: 29,2']
Rondonia = ['RO', 'Casos: 54.205', 'Obitos: 1.114', 'Mortalidade: 62,7']
Roraima = ['RR', 'Casos: 42.997 ', 'Obitos: 587', 'Mortalidade: 96,9']
SantaCatarina = ['SC',  'Casos:141.692',  'Obitos: 2.193', 'Mortalidade: 30,6']
SãoPaulo = ['SP','Casos: 796.209', 'Obitos: 29.694', 'Mortalidade: 64,7']
Sergipe = [ 'SE'  ,'Casos: 72.039' , 'Obitos: 1.837', 'Mortalidade: 79,9']
Tocantins = [ 'TO',  'Casos: 48.580', 'Obitos: 649', 'Mortalidade: 41,3']
DistritoFederal = ['DF', 'Casos: 158.180', 'Obitos: 2.440', 'Mortalidade: 80,9']

print(Acre [1])
print(Alagoas  [1])
print(Amapa  [1])
print(Amazonas  [1])
print(Bahia [1])
print(Ceara [1])
print(Espirito [1])
print(Goias  [1])
print(Maranhao [1])
print(MatoGrosso  [1])
print(MatoGrossoSul  [1])
print(MinasGerais  [1])
print(para [1])
print(Parana [1])
print(Pernambuco  [1])
print(Piaui  [1])
print(RioJaneiro [1])
print(RioNorte[1])
print(RioSul [1])
print(Rondonia [1])
print(Roraima[1])
print(SantaCatarina[1])
print(SãoPaulo[1])
print(Sergipe[1])
print(Tocantins[1])
print(DistritoFederal[1])

print('Dados COVID-19 Acre')

NorteAC1 = ('Acrelândia',		'12',	'BAIXO ACRE E PURUS',	 '27/03/2020',	'15256')
NorteAC2 = ('Assis Brasil',		'12',	'ALTO ACRE',		 '27/03/2020',	'7417')
NorteAC3 = ('Brasiléia',		'12',	'ALTO ACRE',		 '27/03/2020',	'26278')
NorteAC4 = ('Bujari',		'12',	'BAIXO ACRE E PURUS',	 '27/03/2020',	'10266')
NorteAC5 = ('Capixaba',		'12',	'BAIXO ACRE E PURUS',	 '27/03/2020',	'11733')
NorteAC6 = ('Cruzeiro do Sul',	'12',	'JURUA E TARAUACA/ENVIRA', '27/03/2020',	'88376')
NorteAC7 = ('Epitaciolândia',	'12',	'ALTO ACRE',		' 27/03/2020',	'18411')
NorteAC8 = ('Feijó',		'12',	'JURUA E TARAUACA/ENVIRA', '27/03/2020',	'34780')
NorteAC9 = ('Jordão',		'12',	'BAIXO ACRE E PURUS',	'27/03/2020',	'8317')
NorteAC10 = ('Mâncio Lima	',	'12',	'JURUA E TARAUACA/ENVIRA', '27/03/2020',	'18977')
NorteAC11 = ('Manoel Urbano',	'12',	'BAIXO ACRE E PURUS',	 '27/03/2020',	'9459')
NorteAC12 = ('Marechal Thaumaturgo',	'12',	'JURUA E TARAUACA/ENVIRA', '27/03/2020',	'18867')
NorteAC13 = ('Plácido de Castro',	'12',	'BAIXO ACRE E PURUS',	'27/03/2020',	'19761')
NorteAC14 = ('Porto Acre',		'12',	'BAIXO ACRE E PURUS',	'27/03/2020',	'18504')
NorteAC15 = ('Porto Walter',	'12',	'JURUA E TARAUACA/ENVIRA', '27/03/2020',	'11982')
NorteAC16 = ('Rio Branco',		'12',	'BAIXO ACRE E PURUS',	'27/03/2020',	'407319')
NorteAC17 = ('Rodrigues Alves',	'12',	'JURUA E TARAUACA/ENVIRA', '27/03/2020',	'18930')
NorteAC18 = ('Santa Rosa do Purus',	'12',	'BAIXO ACRE E PURUS',	'27/03/2020',	'6540')
NorteAC19 = ('Sena Madureira',	'12',	'BAIXO ACRE E PURUS',	'27/03/2020',	'45848')
NorteAC20 = ('Senador Guiomard',	'12',	'BAIXO ACRE E PURUS',	'27/03/2020',	'23024')
NorteAC21 = ('Tarauacá',		'12',	'JURUA E TARAUACA/ENVIRA', '27/03/2020',	'42567')
NorteAC22 = ('Xapuri',		'12',	'ALTO ACRE',		'27/03/2020',	'19323')


print('DADOS COVID-19 PARAIBA')
print('Seguindo as orientações da atividade. Os casos de Óbitos da Paraíba')
Paraiba = ('PB',	'João Pessoa',	'25',	'250750',	'25001',	'1ª REGIAO MATA ATLANTICA',	'5/8/2020',	'32',	'809015',	'22384',	'277',	'668')
print(Paraiba[11])

lista2 = [['Sudeste', 'SP', 'Adamantina', 35, 350010, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 35068.0, 250, 25, 7, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Adolfo', 35, 350020, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 3562.0, 84, 9, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Aguaí', 35, 350030, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 36305.0, 240, 17, 5, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Agudos', 35, 350070, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 37214.0, 464, 36, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Alambari', 35, 350075, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 6025.0, 56, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Alfredo Marcondes', 35, 350080, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 4166.0, 42, 10, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Altair', 35, 350090, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 4160.0, 33, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Altinópolis', 35, 350100, 35133, 'VALE DAS CACHOEIRAS', '2020-08-27 00:00:00', 35, 16184.0, 183, 16, 7, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Alto Alegre', 35, 350110, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 4099.0, 51, 5, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Alumínio', 35, 350115, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 18628.0, 139, 10, 6, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Alvinlândia', 35, 350150, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 3222.0, 23, 8, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Americana', 35, 350160, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 239597.0, 3692, 171, 111, 10, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Amparo', 35, 350190, 35074, 'CIRCUITO DAS AGUAS', '2020-08-27 00:00:00', 35, 72195.0, 687, 41, 20, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Américo Brasiliense', 35, 350170, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 40504.0, 409, 21, 4, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Américo de Campos', 35, 350180, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 5969.0, 246, 18, 6, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Analândia', 35, 350200, 35104, 'RIO CLARO', '2020-08-27 00:00:00', 35, 4995.0, 35, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Andradina', 35, 350210, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 57157.0, 396, 41, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Angatuba', 35, 350220, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 25228.0, 250, 21, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Anhembi', 35, 350230, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 6724.0, 15, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Anhumas', 35, 350240, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 4115.0, 26, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Aparecida', 35, 350250, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 36157.0, 240, 19, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Aparecida dOeste', 35, 350260, 35153, 'JALES', '2020-08-27 00:00:00', 35, 4196.0, 42, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Apiaí', 35, 350270, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 24374.0, 113, 10, 5, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Aramina', 35, 350300, 35083, 'ALTA MOGIANA', '2020-08-27 00:00:00', 35, 5620.0, 72, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Arandu', 35, 350310, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 6357.0, 28, 4, 2, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Arapeí', 35, 350315, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 2469.0, 4, 1, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Araraquara', 35, 350320, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 236072.0, 3191, 181, 28, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Araras', 35, 350330, 35101, 'ARARAS', '2020-08-27 00:00:00', 35, 134236.0, 2348, 212, 53, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Araçariguama', 35, 350275, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 22364.0, 282, 15, 7, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Araçatuba', 35, 350280, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 197016.0, 5321, 419, 117, 10, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Araçoiaba da Serra', 35, 350290, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 34146.0, 531, 35, 10, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Arco-Íris', 35, 350335, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 1791.0, 7, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Arealva', 35, 350340, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 8560.0, 90, 19, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Areias', 35, 350350, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 3886.0, 41, 18, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Areiópolis', 35, 350360, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 11129.0, 75, 9, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ariranha', 35, 350370, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 9668.0, 102, 22, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Artur Nogueira', 35, 350380, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 54408.0, 620, 38, 13, 3, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Arujá', 35, 350390, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 89824.0, 1550, 63, 69, 4, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Aspásia', 35, 350395, 35153, 'JALES', '2020-08-27 00:00:00', 35, 1822.0, 31, 11, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Assis', 35, 350400, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 104386.0, 947, 66, 21, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Atibaia', 35, 350410, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 142761.0, 1266, 52, 46, 7, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Auriflama', 35, 350420, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 15189.0, 298, 26, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Avanhandava', 35, 350440, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 13649.0, 98, 24, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Avaré', 35, 350450, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 90655.0, 414, 33, 14, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Avaí', 35, 350430, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 5403.0, 54, 11, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bady Bassitt', 35, 350460, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 17502.0, 642, 39, 15, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Balbinos', 35, 350470, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 5735.0, 80, 10, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Bananal', 35, 350490, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 10945.0, 126, 14, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Barbosa', 35, 350510, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 7402.0, 96, 10, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bariri', 35, 350520, 35064, 'JAU', '2020-08-27 00:00:00', 35, 35264.0, 484, 30, 10, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Barra Bonita', 35, 350530, 35064, 'JAU', '2020-08-27 00:00:00', 35, 36126.0, 506, 36, 11, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Barra do Chapéu', 35, 350535, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 5724.0, 42, 10, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Barra do Turvo', 35, 350540, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 7659.0, 94, 14, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Barretos', 35, 350550, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 122098.0, 3121, 163, 91, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Barrinha', 35, 350560, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 32812.0, 506, 47, 19, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Barueri', 35, 350570, 35014, 'ROTA DOS BANDEIRANTES', '2020-08-27 00:00:00', 35, 274182.0, 5272, 316, 318, 14, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Barão de Antonina', 35, 350500, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 3469.0, 11, 3, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Bastos', 35, 350580, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 20953.0, 52, 9, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Batatais', 35, 350590, 35133, 'VALE DAS CACHOEIRAS', '2020-08-27 00:00:00', 35, 62508.0, 383, 31, 17, 8, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bauru', 35, 350600, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 376818.0, 6548, 285, 134, 8, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bebedouro', 35, 350610, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 77496.0, 504, 44, 21, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bento de Abreu', 35, 350620, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 2980.0, 30, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bernardino de Campos', 35, 350630, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 11148.0, 89, 15, 3, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bertioga', 35, 350635, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 63249.0, 1631, 117, 37, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bilac', 35, 350640, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 8034.0, 76, 8, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Birigui', 35, 350650, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 123638.0, 1654, 105, 59, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Biritiba Mirim', 35, 350660, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 32598.0, 284, 19, 18, 2, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Boa Esperança do Sul', 35, 350670, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 14923.0, 124, 11, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bocaina', 35, 350680, 35064, 'JAU', '2020-08-27 00:00:00', 35, 12329.0, 101, 20, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bofete', 35, 350690, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 11730.0, 110, 16, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Boituva', 35, 350700, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 60997.0, 683, 32, 15, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bom Jesus dos Perdões', 35, 350710, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 25448.0, 205, 14, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bom Sucesso de Itararé', 35, 350715, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 3954.0, 2, 1, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Boracéia', 35, 350730, 35064, 'JAU', '2020-08-27 00:00:00', 35, 4823.0, 63, 7, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Borborema', 35, 350740, 35032, 'CENTRO OESTE DO DRS III', '2020-08-27 00:00:00', 35, 16046.0, 128, 17, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Borebi', 35, 350745, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 2653.0, 28, 5, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Borá', 35, 350720, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 837.0, 3, 1, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Botucatu', 35, 350750, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 146497.0, 1777, 75, 31, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bragança Paulista', 35, 350760, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 168668.0, 2143, 133, 47, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Braúna', 35, 350770, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 5686.0, 71, 6, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Brejo Alegre', 35, 350775, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 2865.0, 31, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Brodowski', 35, 350780, 35133, 'VALE DAS CACHOEIRAS', '2020-08-27 00:00:00', 35, 24939.0, 388, 13, 14, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Brotas', 35, 350790, 35064, 'JAU', '2020-08-27 00:00:00', 35, 24403.0, 100, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Buri', 35, 350800, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 19878.0, 232, 17, 4, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Buritama', 35, 350810, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 17144.0, 218, 16, 9, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Buritizal', 35, 350820, 35083, 'ALTA MOGIANA', '2020-08-27 00:00:00', 35, 4481.0, 50, 18, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Bálsamo', 35, 350480, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 9068.0, 286, 14, 10, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cabreúva', 35, 350840, 35073, 'JUNDIAI', '2020-08-27 00:00:00', 35, 49707.0, 996, 71, 37, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cabrália Paulista', 35, 350830, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 4264.0, 70, 11, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Cachoeira Paulista', 35, 350860, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 33327.0, 253, 33, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Caconde', 35, 350870, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 18985.0, 78, 7, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Cafelândia', 35, 350880, 35065, 'LINS', '2020-08-27 00:00:00', 35, 17767.0, 221, 32, 2, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Caiabu', 35, 350890, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 4191.0, 35, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Caieiras', 35, 350900, 35012, 'FRANCO DA ROCHA', '2020-08-27 00:00:00', 35, 101470.0, 1728, 67, 85, 7, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Caiuá', 35, 350910, 35114, 'EXTREMO OESTE PAULISTA', '2020-08-27 00:00:00', 35, 5874.0, 51, 7, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Cajamar', 35, 350920, 35012, 'FRANCO DA ROCHA', '2020-08-27 00:00:00', 35, 76801.0, 1318, 43, 67, 5, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Cajati', 35, 350925, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 28549.0, 1448, 133, 21, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cajobi', 35, 350930, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 10542.0, 136, 14, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cajuru', 35, 350940, 35133, 'VALE DAS CACHOEIRAS', '2020-08-27 00:00:00', 35, 26167.0, 373, 29, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Campina do Monte Alegre', 35, 350945, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 6024.0, 72, 14, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Campinas', 35, 350950, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 1204073.0, 26486, 965, 990, 36, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Campo Limpo Paulista', 35, 350960, 35073, 'JUNDIAI', '2020-08-27 00:00:00', 35, 84650.0, 942, 73, 62, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Campos Novos Paulista', 35, 350980, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 4965.0, 41, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Campos do Jordão', 35, 350970, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 52088.0, 549, 40, 9, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cananéia', 35, 350990, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 12540.0, 154, 12, 7, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Canas', 35, 350995, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 5138.0, 30, 4, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Canitar', 35, 351015, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 5216.0, 36, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Capela do Alto', 35, 351030, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 20706.0, 225, 16, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Capivari', 35, 351040, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 55768.0, 744, 56, 9, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Capão Bonito', 35, 351020, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 47138.0, 572, 45, 18, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Caraguatatuba', 35, 351050, 35173, 'LITORAL NORTE', '2020-08-27 00:00:00', 35, 121532.0, 1619, 158, 68, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Carapicuíba', 35, 351060, 35014, 'ROTA DOS BANDEIRANTES', '2020-08-27 00:00:00', 35, 400927.0, 6052, 234, 285, 11, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Cardoso', 35, 351070, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 12326.0, 100, 8, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Casa Branca', 35, 351080, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 30380.0, 273, 27, 6, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Castilho', 35, 351100, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 21006.0, 171, 14, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Catanduva', 35, 351110, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 121862.0, 2865, 185, 91, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Catiguá', 35, 351120, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 7804.0, 117, 15, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Caçapava', 35, 350850, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 94263.0, 1113, 72, 31, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Cedral', 35, 351130, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 9237.0, 159, 12, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cerqueira César', 35, 351140, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 19985.0, 116, 11, 5, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Cerquilho', 35, 351150, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 48949.0, 399, 23, 12, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cesário Lange', 35, 351160, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 18148.0, 109, 7, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Charqueada', 35, 351170, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 17190.0, 262, 18, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Chavantes', 35, 355720, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 12418.0, 63, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Clementina', 35, 351190, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 8617.0, 76, 10, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Colina', 35, 351200, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 18468.0, 183, 13, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Colômbia', 35, 351210, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 6210.0, 60, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Conchal', 35, 351220, 35101, 'ARARAS', '2020-08-27 00:00:00', 35, 28050.0, 296, 61, 10, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Conchas', 35, 351230, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 17896.0, 172, 22, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cordeirópolis', 35, 351240, 35102, 'LIMEIRA', '2020-08-27 00:00:00', 35, 24528.0, 1184, 69, 14, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Coroados', 35, 351250, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 6058.0, 81, 7, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Coronel Macedo', 35, 351260, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 4681.0, 4, 1, 2, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Corumbataí', 35, 351270, 35104, 'RIO CLARO', '2020-08-27 00:00:00', 35, 4055.0, 92, 8, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cosmorama', 35, 351290, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 7307.0, 228, 18, 11, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cosmópolis', 35, 351280, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 72252.0, 1194, 67, 23, 2, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Cotia', 35, 351300, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 249210.0, 3397, 117, 171, 6, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Cravinhos', 35, 351310, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 35292.0, 278, 22, 26, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cristais Paulista', 35, 351320, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 8631.0, 15, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cruzeiro', 35, 351340, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 82238.0, 532, 49, 13, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cruzália', 35, 351330, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 2073.0, 4, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cubatão', 35, 351350, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 130705.0, 5614, 191, 172, 11, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Cunha', 35, 351360, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 21547.0, 71, 7, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cássia dos Coqueiros', 35, 351090, 35133, 'VALE DAS CACHOEIRAS', '2020-08-27 00:00:00', 35, 2523.0, 55, 9, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cândido Mota', 35, 351000, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 31280.0, 211, 14, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Cândido Rodrigues', 35, 351010, 35033, 'NORTE DO DRS III', '2020-08-27 00:00:00', 35, 2793.0, 28, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Descalvado', 35, 351370, 35034, 'CORACAO DO DRS III', '2020-08-27 00:00:00', 35, 33718.0, 244, 38, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Diadema', 35, 351380, 35015, 'GRANDE ABC', '2020-08-27 00:00:00', 35, 423884.0, 7140, 275, 288, 13, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Dirce Reis', 35, 351385, 35153, 'JALES', '2020-08-27 00:00:00', 35, 1793.0, 10, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Divinolândia', 35, 351390, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 11146.0, 72, 7, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Dobrada', 35, 351400, 35033, 'NORTE DO DRS III', '2020-08-27 00:00:00', 35, 8929.0, 53, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Dois Córregos', 35, 351410, 35064, 'JAU', '2020-08-27 00:00:00', 35, 27315.0, 150, 18, 3, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Dolcinópolis', 35, 351420, 35153, 'JALES', '2020-08-27 00:00:00', 35, 2115.0, 65, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Dourado', 35, 351430, 35034, 'CORACAO DO DRS III', '2020-08-27 00:00:00', 35, 8873.0, 57, 5, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Dracena', 35, 351440, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 46793.0, 461, 34, 16, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Duartina', 35, 351450, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 12445.0, 151, 13, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Dumont', 35, 351460, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 9868.0, 272, 19, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Echaporã', 35, 351470, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 6102.0, 17, 4, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Eldorado', 35, 351480, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 15494.0, 247, 26, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Elias Fausto', 35, 351490, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 17772.0, 356, 29, 9, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Elisiário', 35, 351492, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 3651.0, 93, 12, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Embaúba', 35, 351495, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 2452.0, 41, 5, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Embu das Artes', 35, 351500, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 273726.0, 2962, 103, 144, 6, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Embu-Guaçu', 35, 351510, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 69385.0, 998, 57, 31, 3, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Emilianópolis', 35, 351512, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 3214.0, 37, 5, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Engenheiro Coelho', 35, 351515, 35102, 'LIMEIRA', '2020-08-27 00:00:00', 35, 20773.0, 553, 36, 12, 3, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Espírito Santo do Pinhal', 35, 351518, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 44330.0, 522, 41, 11, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Espírito Santo do Turvo', 35, 351519, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 4829.0, 28, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Estiva Gerbi', 35, 355730, 35141, 'BAIXA MOGIANA', '2020-08-27 00:00:00', 35, 11304.0, 135, 9, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Estrela dOeste', 35, 351520, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 8419.0, 321, 37, 9, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Estrela do Norte', 35, 351530, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 2766.0, 21, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Euclides da Cunha Paulista', 35, 351535, 35115, 'PONTAL DO PARANAPANEMA', '2020-08-27 00:00:00', 35, 9371.0, 31, 6, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Fartura', 35, 351540, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 16036.0, 64, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Fernando Prestes', 35, 351560, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 5783.0, 70, 8, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Fernandópolis', 35, 351550, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 69116.0, 1822, 94, 29, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Fernão', 35, 351565, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 1716.0, 5, 3, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Ferraz de Vasconcelos', 35, 351570, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 194276.0, 2393, 127, 111, 8, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Flora Rica', 35, 351580, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 1464.0, 15, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Floreal', 35, 351590, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 2917.0, 33, 4, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Florínea', 35, 351610, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 2676.0, 4, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Flórida Paulista', 35, 351600, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 14640.0, 47, 4, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Franca', 35, 351620, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 353187.0, 2436, 177, 67, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Francisco Morato', 35, 351630, 35012, 'FRANCO DA ROCHA', '2020-08-27 00:00:00', 35, 175844.0, 2364, 86, 97, 18, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Franco da Rocha', 35, 351640, 35012, 'FRANCO DA ROCHA', '2020-08-27 00:00:00', 35, 154489.0, 1869, 85, 94, 7, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Gabriel Monteiro', 35, 351650, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 2776.0, 24, 3, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Garça', 35, 351670, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 44390.0, 465, 40, 12, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Gastão Vidigal', 35, 351680, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 4808.0, 79, 8, 12, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Gavião Peixoto', 35, 351685, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 4789.0, 159, 27, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'General Salgado', 35, 351690, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 10869.0, 171, 11, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Getulina', 35, 351700, 35065, 'LINS', '2020-08-27 00:00:00', 35, 11409.0, 177, 25, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Glicério', 35, 351710, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 4815.0, 46, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guaimbê', 35, 351730, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 5765.0, 41, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guaiçara', 35, 351720, 35065, 'LINS', '2020-08-27 00:00:00', 35, 12168.0, 450, 56, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guapiara', 35, 351760, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 17157.0, 93, 10, 8, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guapiaçu', 35, 351750, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 21454.0, 639, 40, 18, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Guaraci', 35, 351790, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 11188.0, 132, 11, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guarani dOeste', 35, 351800, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 2000.0, 44, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guarantã', 35, 351810, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 6664.0, 82, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guararapes', 35, 351820, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 32939.0, 423, 24, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guararema', 35, 351830, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 29798.0, 364, 25, 21, 3, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Guaratinguetá', 35, 351840, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 121798.0, 905, 49, 42, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guaraçaí', 35, 351780, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 8323.0, 36, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guareí', 35, 351850, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 18520.0, 275, 31, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Guariba', 35, 351860, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 40105.0, 859, 42, 26, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guarujá', 35, 351870, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 320459.0, 6439, 406, 295, 28, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guarulhos', 35, 351880, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 1379182.0, 16590, 530, 1243, 36, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Guará', 35, 351770, 35083, 'ALTA MOGIANA', '2020-08-27 00:00:00', 35, 21220.0, 253, 26, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guatapará', 35, 351885, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 7656.0, 51, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guaíra', 35, 351740, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 40790.0, 740, 40, 15, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Guzolândia', 35, 351890, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 5267.0, 30, 4, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Gália', 35, 351660, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 6548.0, 31, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Herculândia', 35, 351900, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 9526.0, 56, 5, 2, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Holambra', 35, 351905, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 14930.0, 250, 31, 2, 1, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Hortolândia', 35, 351907, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 230851.0, 5238, 874, 111, 8, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Iacanga', 35, 351910, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 11710.0, 192, 23, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Iacri', 35, 351920, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 6321.0, 13, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Iaras', 35, 351925, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 9240.0, 37, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ibaté', 35, 351930, 35034, 'CORACAO DO DRS III', '2020-08-27 00:00:00', 35, 35104.0, 225, 16, 3, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Ibirarema', 35, 351950, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 7753.0, 99, 13, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ibirá', 35, 351940, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 12393.0, 198, 12, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ibitinga', 35, 351960, 35032, 'CENTRO OESTE DO DRS III', '2020-08-27 00:00:00', 35, 60033.0, 1044, 53, 27, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ibiúna', 35, 351970, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 78878.0, 361, 32, 19, 3, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Icém', 35, 351980, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 8243.0, 83, 10, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Iepê', 35, 351990, 35113, 'ALTO CAPIVARI', '2020-08-27 00:00:00', 35, 8159.0, 31, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Igarapava', 35, 352010, 35083, 'ALTA MOGIANA', '2020-08-27 00:00:00', 35, 30432.0, 320, 23, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Igaratá', 35, 352020, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 9534.0, 416, 31, 7, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Igaraçu do Tietê', 35, 352000, 35064, 'JAU', '2020-08-27 00:00:00', 35, 24674.0, 272, 17, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Iguape', 35, 352030, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 30857.0, 422, 30, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ilha Comprida', 35, 352042, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 11166.0, 87, 7, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ilha Solteira', 35, 352044, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 26686.0, 154, 8, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ilhabela', 35, 352040, 35173, 'LITORAL NORTE', '2020-08-27 00:00:00', 35, 34970.0, 1309, 139, 10, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Indaiatuba', 35, 352050, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 251627.0, 2581, 148, 128, 14, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Indiana', 35, 352060, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 4885.0, 78, 15, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Indiaporã', 35, 352070, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 3897.0, 28, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Inúbia Paulista', 35, 352080, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 3991.0, 9, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ipaussu', 35, 352090, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 14971.0, 196, 21, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Iperó', 35, 352100, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 37133.0, 189, 11, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ipeúna', 35, 352110, 35104, 'RIO CLARO', '2020-08-27 00:00:00', 35, 7546.0, 96, 28, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ipiguá', 35, 352115, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 5392.0, 148, 9, 6, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Iporanga', 35, 352120, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 4218.0, 43, 6, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ipuã', 35, 352130, 35082, 'ALTA ANHANGUERA', '2020-08-27 00:00:00', 35, 16409.0, 409, 32, 11, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Iracemápolis', 35, 352140, 35102, 'LIMEIRA', '2020-08-27 00:00:00', 35, 24235.0, 834, 55, 12, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Irapuru', 35, 352160, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 8294.0, 43, 6, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Irapuã', 35, 352150, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 7993.0, 77, 18, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itaberá', 35, 352170, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 17556.0, 104, 9, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itajobi', 35, 352190, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 15262.0, 314, 17, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itaju', 35, 352200, 35064, 'JAU', '2020-08-27 00:00:00', 35, 3835.0, 103, 8, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itanhaém', 35, 352210, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 101816.0, 973, 71, 55, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itaoca', 35, 352215, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 3328.0, 26, 4, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Itapecerica da Serra', 35, 352220, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 175693.0, 2138, 87, 156, 10, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Itapetininga', 35, 352230, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 163901.0, 1091, 78, 39, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itapeva', 35, 352240, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 94354.0, 394, 24, 6, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itapevi', 35, 352250, 35014, 'ROTA DOS BANDEIRANTES', '2020-08-27 00:00:00', 35, 237700.0, 2831, 110, 217, 7, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Itapira', 35, 352260, 35141, 'BAIXA MOGIANA', '2020-08-27 00:00:00', 35, 74773.0, 958, 80, 26, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itapirapuã Paulista', 35, 352265, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 4241.0, 60, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itaporanga', 35, 352280, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 15149.0, 152, 15, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itapura', 35, 352300, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 4906.0, 48, 10, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itapuí', 35, 352290, 35064, 'JAU', '2020-08-27 00:00:00', 35, 13992.0, 229, 17, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itaquaquecetuba', 35, 352310, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 370821.0, 3502, 143, 239, 10, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Itararé', 35, 352320, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 50503.0, 239, 14, 12, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Itariri', 35, 352330, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 17436.0, 191, 25, 4, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itatiba', 35, 352340, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 120858.0, 1090, 76, 18, 4, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Itatinga', 35, 352350, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 20697.0, 271, 22, 5, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itaí', 35, 352180, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 27125.0, 70, 8, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Itirapina', 35, 352360, 35104, 'RIO CLARO', '2020-08-27 00:00:00', 35, 18157.0, 148, 10, 6, 1, ' ', ' ', 0.0],  
['Sudeste', 'SP', 'Itirapuã', 35, 352370, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 6499.0, 8, 2, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itobi', 35, 352380, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 7841.0, 274, 30, 2, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itu', 35, 352390, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 173939.0, 2242, 108, 76, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itupeva', 35, 352400, 35073, 'JUNDIAI', '2020-08-27 00:00:00', 35, 61252.0, 1359, 126, 31, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ituverava', 35, 352410, 35083, 'ALTA MOGIANA', '2020-08-27 00:00:00', 35, 41824.0, 182, 17, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Itápolis', 35, 352270, 35032, 'CENTRO OESTE DO DRS III', '2020-08-27 00:00:00', 35, 43120.0, 326, 27, 8, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jaborandi', 35, 352420, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 6929.0, 82, 10, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jaboticabal', 35, 352430, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 77263.0, 401, 19, 26, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jacareí', 35, 352440, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 233662.0, 2477, 111, 103, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jaci', 35, 352450, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 7067.0, 230, 58, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jacupiranga', 35, 352460, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 17866.0, 341, 30, 9, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jaguariúna', 35, 352470, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 57488.0, 750, 87, 20, 4, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Jales', 35, 352480, 35153, 'JALES', '2020-08-27 00:00:00', 35, 49107.0, 1018, 60, 16, 10, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jambeiro', 35, 352490, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 6602.0, 56, 6, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jandira', 35, 352500, 35014, 'ROTA DOS BANDEIRANTES', '2020-08-27 00:00:00', 35, 124937.0, 1267, 81, 76, 6, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Jardinópolis', 35, 352510, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 44380.0, 400, 15, 33, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jarinu', 35, 352520, 35073, 'JUNDIAI', '2020-08-27 00:00:00', 35, 30044.0, 354, 17, 22, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Jaú', 35, 352530, 35064, 'JAU', '2020-08-27 00:00:00', 35, 150252.0, 1602, 65, 44, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jeriquara', 35, 352540, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 3159.0, 36, 8, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Joanópolis', 35, 352550, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 13220.0, 89, 13, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'José Bonifácio', 35, 352570, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 37015.0, 799, 41, 15, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'João Ramalho', 35, 352560, 35113, 'ALTO CAPIVARI', '2020-08-27 00:00:00', 35, 4523.0, 49, 5, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jumirim', 35, 352585, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 3367.0, 48, 10, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Jundiaí', 35, 352590, 35073, 'JUNDIAI', '2020-08-27 00:00:00', 35, 418962.0, 10017, 464, 358, 13, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Junqueirópolis', 35, 352600, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 20679.0, 116, 13, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Juquitiba', 35, 352620, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 31444.0, 572, 72, 10, 2, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Juquiá', 35, 352610, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 18812.0, 246, 17, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Júlio Mesquita', 35, 352580, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 4776.0, 13, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lagoinha', 35, 352630, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 4896.0, 30, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Laranjal Paulista', 35, 352640, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 28516.0, 455, 33, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lavrinhas', 35, 352660, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 7260.0, 45, 7, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Lavínia', 35, 352650, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 11980.0, 87, 15, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Leme', 35, 352670, 35101, 'ARARAS', '2020-08-27 00:00:00', 35, 103391.0, 1910, 143, 48, 5, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Lençóis Paulista', 35, 352680, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 68432.0, 2283, 152, 41, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Limeira', 35, 352690, 35102, 'LIMEIRA', '2020-08-27 00:00:00', 35, 306114.0, 4077, 158, 202, 17, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Lindóia', 35, 352700, 35074, 'CIRCUITO DAS AGUAS', '2020-08-27 00:00:00', 35, 7980.0, 68, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lins', 35, 352710, 35065, 'LINS', '2020-08-27 00:00:00', 35, 78013.0, 1949, 124, 31, 4, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Lorena', 35, 352720, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 88706.0, 562, 40, 17, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lourdes', 35, 352725, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 2289.0, 12, 2, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Louveira', 35, 352730, 35073, 'JUNDIAI', '2020-08-27 00:00:00', 35, 48885.0, 696, 36, 22, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lucianópolis', 35, 352750, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 2394.0, 12, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lucélia', 35, 352740, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 21747.0, 73, 5, 5, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Luiziânia', 35, 352770, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 5790.0, 75, 16, 3, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lupércio', 35, 352780, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 4584.0, 20, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Lutécia', 35, 352790, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 2649.0, 7, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Luís Antônio', 35, 352760, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 14947.0, 171, 16, 9, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Macatuba', 35, 352800, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 17163.0, 557, 39, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Macaubal', 35, 352810, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 8120.0, 62, 6, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Macedônia', 35, 352820, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 3698.0, 78, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Magda', 35, 352830, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 3119.0, 38, 5, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mairinque', 35, 352840, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 47150.0, 367, 33, 15, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mairiporã', 35, 352850, 35012, 'FRANCO DA ROCHA', '2020-08-27 00:00:00', 35, 100179.0, 896, 53, 49, 3, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Manduri', 35, 352860, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 9846.0, 42, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Marabá Paulista', 35, 352870, 35114, 'EXTREMO OESTE PAULISTA', '2020-08-27 00:00:00', 35, 5853.0, 26, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Maracaí', 35, 352880, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 14002.0, 126, 21, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Marapoama', 35, 352885, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 3031.0, 35, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Marinópolis', 35, 352910, 35153, 'JALES', '2020-08-27 00:00:00', 35, 2112.0, 24, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mariápolis', 35, 352890, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 4084.0, 22, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Martinópolis', 35, 352920, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 26461.0, 185, 16, 10, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Marília', 35, 352900, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 238882.0, 1685, 73, 27, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Matão', 35, 352930, 35033, 'NORTE DO DRS III', '2020-08-27 00:00:00', 35, 83170.0, 413, 20, 11, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Mauá', 35, 352940, 35015, 'GRANDE ABC', '2020-08-27 00:00:00', 35, 472912.0, 5001, 150, 288, 13, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Mendonça', 35, 352950, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 5490.0, 152, 13, 8, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Meridiano', 35, 352960, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 3836.0, 94, 12, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mesópolis', 35, 352965, 35153, 'JALES', '2020-08-27 00:00:00', 35, 1908.0, 21, 7, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Miguelópolis', 35, 352970, 35083, 'ALTA MOGIANA', '2020-08-27 00:00:00', 35, 22226.0, 323, 36, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mineiros do Tietê', 35, 352980, 35064, 'JAU', '2020-08-27 00:00:00', 35, 12908.0, 186, 28, 4, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Mira Estrela', 35, 353000, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 3086.0, 34, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Miracatu', 35, 352990, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 19779.0, 262, 18, 13, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mirandópolis', 35, 353010, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 29564.0, 281, 16, 6, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mirante do Paranapanema', 35, 353020, 35115, 'PONTAL DO PARANAPANEMA', '2020-08-27 00:00:00', 35, 18259.0, 52, 5, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Mirassol', 35, 353030, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 59824.0, 1031, 51, 21, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mirassolândia', 35, 353040, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 4871.0, 125, 15, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mococa', 35, 353050, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 68885.0, 521, 43, 13, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mogi Guaçu', 35, 353070, 35141, 'BAIXA MOGIANA', '2020-08-27 00:00:00', 35, 151888.0, 1941, 96, 61, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mogi Mirim', 35, 353080, 35141, 'BAIXA MOGIANA', '2020-08-27 00:00:00', 35, 93189.0, 1088, 425, 35, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mogi das Cruzes', 35, 353060, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 445842.0, 5978, 180, 317, 9, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Mombuca', 35, 353090, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 3493.0, 33, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Mongaguá', 35, 353110, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 56702.0, 482, 53, 16, 3, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Monte Alegre do Sul', 35, 353120, 35074, 'CIRCUITO DAS AGUAS', '2020-08-27 00:00:00', 35, 8038.0, 41, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Monte Alto', 35, 353130, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 50498.0, 508, 41, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Monte Aprazível', 35, 353140, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 25087.0, 530, 35, 10, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Monte Azul Paulista', 35, 353150, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 19008.0, 139, 10, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Monte Castelo', 35, 353160, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 4166.0, 42, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Monte Mor', 35, 353180, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 59772.0, 1092, 65, 23, 3, ' ', ' ', 1.0],
['Sudeste', 'SP', 'Monteiro Lobato', 35, 353170, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 4653.0, 62, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Monções', 35, 353100, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 2259.0, 41, 4, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Morro Agudo', 35, 353190, 35082, 'ALTA ANHANGUERA', '2020-08-27 00:00:00', 35, 32968.0, 905, 71, 16, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Morungaba', 35, 353200, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 13622.0, 76, 6, 2, 1, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Motuca', 35, 353205, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 4758.0, 47, 7, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Murutinga do Sul', 35, 353210, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 4486.0, 19, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nantes', 35, 353215, 35113, 'ALTO CAPIVARI', '2020-08-27 00:00:00', 35, 3141.0, 13, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Narandiba', 35, 353220, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 4857.0, 47, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Natividade da Serra', 35, 353230, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 6661.0, 25, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nazaré Paulista', 35, 353240, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 18524.0, 201, 17, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Neves Paulista', 35, 353250, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 8930.0, 148, 12, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nhandeara', 35, 353260, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 11478.0, 111, 10, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nipoã', 35, 353270, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 5213.0, 98, 17, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Nova Aliança', 35, 353280, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 6973.0, 140, 9, 2, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Nova Campina', 35, 353282, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 9755.0, 14, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nova Canaã Paulista', 35, 353284, 35152, 'SANTA FE DO SUL', '2020-08-27 00:00:00', 35, 1881.0, 30, 8, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nova Castilho', 35, 353286, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 1267.0, 18, 2, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nova Europa', 35, 353290, 35032, 'CENTRO OESTE DO DRS III', '2020-08-27 00:00:00', 35, 11186.0, 151, 20, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nova Granada', 35, 353300, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 21500.0, 456, 28, 8, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Nova Guataporanga', 35, 353310, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 2316.0, 12, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nova Independência', 35, 353320, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 3969.0, 49, 7, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Nova Luzitânia', 35, 353330, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 4101.0, 72, 8, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nova Odessa', 35, 353340, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 60174.0, 743, 35, 38, 5, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Novais', 35, 353325, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 5830.0, 51, 9, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Novo Horizonte', 35, 353350, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 41052.0, 385, 46, 3, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Nuporanga', 35, 353360, 35082, 'ALTA ANHANGUERA', '2020-08-27 00:00:00', 35, 7432.0, 33, 4, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ocauçu', 35, 353370, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 4289.0, 19, 8, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Olímpia', 35, 353390, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 54772.0, 1616, 115, 30, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Onda Verde', 35, 353400, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 4381.0, 110, 27, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Oriente', 35, 353410, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 6515.0, 58, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Orindiúva', 35, 353420, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 7066.0, 191, 21, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Orlândia', 35, 353430, 35082, 'ALTA ANHANGUERA', '2020-08-27 00:00:00', 35, 44028.0, 649, 43, 21, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Osasco', 35, 353440, 35014, 'ROTA DOS BANDEIRANTES', '2020-08-27 00:00:00', 35, 698418.0, 11867, 504, 719, 18, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Oscar Bressane', 35, 353450, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 2603.0, 10, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Osvaldo Cruz', 35, 353460, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 32879.0, 156, 21, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ourinhos', 35, 353470, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 113542.0, 1463, 117, 17, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ouro Verde', 35, 353480, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 8562.0, 16, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ouroeste', 35, 353475, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 10361.0, 142, 13, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pacaembu', 35, 353490, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 14197.0, 91, 7, 5, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Palestina', 35, 353500, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 12957.0, 101, 13, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Palmares Paulista', 35, 353510, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 13275.0, 253, 19, 10, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Palmeira dOeste', 35, 353520, 35153, 'JALES', '2020-08-27 00:00:00', 35, 9283.0, 98, 10, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Palmital', 35, 353530, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 22221.0, 173, 11, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Panorama', 35, 353540, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 15777.0, 82, 5, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paraguaçu Paulista', 35, 353550, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 45703.0, 275, 17, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paraibuna', 35, 353560, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 18222.0, 116, 10, 8, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Paranapanema', 35, 353580, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 20197.0, 126, 12, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paranapuã', 35, 353590, 35153, 'JALES', '2020-08-27 00:00:00', 35, 4078.0, 52, 6, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Parapuã', 35, 353600, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 10964.0, 43, 8, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paraíso', 35, 353570, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 6454.0, 114, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pardinho', 35, 353610, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 6435.0, 119, 10, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Pariquera-Açu', 35, 353620, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 19648.0, 516, 38, 9, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Parisi', 35, 353625, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 2161.0, 68, 6, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Patrocínio Paulista', 35, 353630, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 14670.0, 66, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paulicéia', 35, 353640, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 7366.0, 25, 4, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paulistânia', 35, 353657, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 1833.0, 7, 1, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paulo de Faria', 35, 353660, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 8945.0, 135, 12, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Paulínia', 35, 353650, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 109424.0, 4333, 153, 66, 5, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Pederneiras', 35, 353670, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 46687.0, 472, 20, 11, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pedra Bela', 35, 353680, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 6093.0, 68, 15, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pedranópolis', 35, 353690, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 2494.0, 29, 4, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pedregulho', 35, 353700, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 16744.0, 55, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pedreira', 35, 353710, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 47919.0, 335, 38, 6, 1, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Pedrinhas Paulista', 35, 353715, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 3093.0, 16, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pedro de Toledo', 35, 353720, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 11331.0, 49, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Penápolis', 35, 353730, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 63407.0, 607, 37, 16, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pereira Barreto', 35, 353740, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 25669.0, 189, 14, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pereiras', 35, 353750, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 8668.0, 38, 5, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Peruíbe', 35, 353760, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 68284.0, 732, 82, 26, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piacatu', 35, 353770, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 5980.0, 76, 60, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piedade', 35, 353780, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 55348.0, 548, 30, 19, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pilar do Sul', 35, 353790, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 29185.0, 179, 16, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pindamonhangaba', 35, 353800, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 168328.0, 1556, 112, 26, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pindorama', 35, 353810, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 17049.0, 279, 18, 9, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pinhalzinho', 35, 353820, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 15207.0, 118, 13, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piquerobi', 35, 353830, 35114, 'EXTREMO OESTE PAULISTA', '2020-08-27 00:00:00', 35, 3692.0, 33, 9, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piquete', 35, 353850, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 13657.0, 108, 12, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piracaia', 35, 353860, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 27303.0, 297, 14, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piracicaba', 35, 353870, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 404142.0, 9856, 340, 275, 11, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piraju', 35, 353880, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 29806.0, 171, 10, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pirajuí', 35, 353890, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 25492.0, 261, 25, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pirangi', 35, 353900, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 11417.0, 293, 20, 10, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pirapora do Bom Jesus', 35, 353910, 35014, 'ROTA DOS BANDEIRANTES', '2020-08-27 00:00:00', 35, 18895.0, 455, 21, 5, 1, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Pirapozinho', 35, 353920, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 27527.0, 260, 29, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pirassununga', 35, 353930, 35101, 'ARARAS', '2020-08-27 00:00:00', 35, 76409.0, 973, 52, 13, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Piratininga', 35, 353940, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 13636.0, 172, 11, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pitangueiras', 35, 353950, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 39719.0, 574, 36, 10, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Planalto', 35, 353960, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 5237.0, 125, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Platina', 35, 353970, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 3550.0, 5, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Poloni', 35, 353990, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 6059.0, 69, 17, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pompéia', 35, 354000, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 22014.0, 83, 13, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pongaí', 35, 354010, 35065, 'LINS', '2020-08-27 00:00:00', 35, 3416.0, 51, 6, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pontal', 35, 354020, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 49961.0, 1233, 64, 38, 4, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Pontalinda', 35, 354025, 35153, 'JALES', '2020-08-27 00:00:00', 35, 4628.0, 50, 5, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pontes Gestal', 35, 354030, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 2577.0, 98, 12, 3, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Populina', 35, 354040, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 4169.0, 44, 4, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Porangaba', 35, 354050, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 9925.0, 29, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Porto Feliz', 35, 354060, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 53098.0, 963, 50, 14, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Porto Ferreira', 35, 354070, 35034, 'CORACAO DO DRS III', '2020-08-27 00:00:00', 35, 56150.0, 941, 110, 22, 4, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Potim', 35, 354075, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 24643.0, 157, 15, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Potirendaba', 35, 354080, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 17361.0, 445, 55, 7, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Poá', 35, 353980, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 117452.0, 1452, 44, 89, 5, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Pracinha', 35, 354085, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 4093.0, 4, 1, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pradópolis', 35, 354090, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 21496.0, 522, 56, 14, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Praia Grande', 35, 354100, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 325073.0, 6264, 221, 182, 32, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Pratânia', 35, 354105, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 5261.0, 44, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Presidente Alves', 35, 354110, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 4094.0, 53, 11, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Presidente Bernardes', 35, 354120, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 13106.0, 152, 10, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Presidente Epitácio', 35, 354130, 35114, 'EXTREMO OESTE PAULISTA', '2020-08-27 00:00:00', 35, 44200.0, 380, 29, 10, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Presidente Prudente', 35, 354140, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 228743.0, 3166, 140, 86, 7, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Presidente Venceslau', 35, 354150, 35114, 'EXTREMO OESTE PAULISTA', '2020-08-27 00:00:00', 35, 39516.0, 350, 28, 12, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Promissão', 35, 354160, 35065, 'LINS', '2020-08-27 00:00:00', 35, 40432.0, 1344, 83, 6, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Quadra', 35, 354165, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 3804.0, 9, 1, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Quatá', 35, 354170, 35113, 'ALTO CAPIVARI', '2020-08-27 00:00:00', 35, 14109.0, 88, 6, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Queiroz', 35, 354180, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 3406.0, 25, 3, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Queluz', 35, 354190, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 13420.0, 224, 23, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Quintana', 35, 354200, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 6638.0, 47, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rafard', 35, 354210, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 9076.0, 134, 11, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rancharia', 35, 354220, 35113, 'ALTO CAPIVARI', '2020-08-27 00:00:00', 35, 29707.0, 493, 59, 11, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Redenção da Serra', 35, 354230, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 3851.0, 15, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Regente Feijó', 35, 354240, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 20261.0, 70, 5, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Reginópolis', 35, 354250, 35062, 'BAURU', '2020-08-27 00:00:00', 35, 9621.0, 25, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Registro', 35, 354260, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 56322.0, 1260, 55, 27, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Restinga', 35, 354270, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 7593.0, 23, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ribeira', 35, 354280, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 3340.0, 34, 5, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ribeirão Bonito', 35, 354290, 35034, 'CORACAO DO DRS III', '2020-08-27 00:00:00', 35, 13219.0, 104, 8, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ribeirão Branco', 35, 354300, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 16444.0, 156, 16, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ribeirão Corrente', 35, 354310, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 4718.0, 6, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ribeirão Grande', 35, 354325, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 7673.0, 72, 10, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ribeirão Pires', 35, 354330, 35015, 'GRANDE ABC', '2020-08-27 00:00:00', 35, 123393.0, 1101, 38, 55, 4, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Ribeirão Preto', 35, 354340, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 703293.0, 16432, 753, 550, 24, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Ribeirão do Sul', 35, 354320, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 4541.0, 24, 4, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Ribeirão dos Índios', 35, 354323, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 2225.0, 13, 10, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rifaina', 35, 354360, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 3629.0, 41, 12, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rincão', 35, 354370, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 10799.0, 88, 12, 4, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rinópolis', 35, 354380, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 9981.0, 39, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rio Claro', 35, 354390, 35104, 'RIO CLARO', '2020-08-27 00:00:00', 35, 206424.0, 3485, 282, 108, 9, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rio Grande da Serra', 35, 354410, 35015, 'GRANDE ABC', '2020-08-27 00:00:00', 35, 50846.0, 552, 36, 20, 2, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Rio das Pedras', 35, 354400, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 35228.0, 552, 25, 23, 2, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Riolândia', 35, 354420, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 12518.0, 257, 23, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Riversul', 35, 354350, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 5524.0, 15, 2, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rosana', 35, 354425, 35115, 'PONTAL DO PARANAPANEMA', '2020-08-27 00:00:00', 35, 16643.0, 91, 8, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Roseira', 35, 354430, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 10712.0, 141, 20, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rubinéia', 35, 354450, 35152, 'SANTA FE DO SUL', '2020-08-27 00:00:00', 35, 3148.0, 54, 13, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Rubiácea', 35, 354440, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 3128.0, 36, 7, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sabino', 35, 354460, 35065, 'LINS', '2020-08-27 00:00:00', 35, 5590.0, 33, 10, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sagres', 35, 354470, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 2432.0, 6, 1, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sales', 35, 354480, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 6331.0, 52, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sales Oliveira', 35, 354490, 35082, 'ALTA ANHANGUERA', '2020-08-27 00:00:00', 35, 11890.0, 247, 19, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Salesópolis', 35, 354500, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 17139.0, 156, 11, 9, 1, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Salmourão', 35, 354510, 35091, 'ADAMANTINA', '2020-08-27 00:00:00', 35, 5300.0, 8, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Saltinho', 35, 354515, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 8286.0, 94, 7, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Salto', 35, 354520, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 118663.0, 1997, 119, 38, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Salto Grande', 35, 354540, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 9331.0, 45, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Salto de Pirapora', 35, 354530, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 45422.0, 718, 55, 16, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sandovalina', 35, 354550, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 4302.0, 23, 7, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Adélia', 35, 354560, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 15480.0, 244, 16, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Albertina', 35, 354570, 35153, 'JALES', '2020-08-27 00:00:00', 35, 6008.0, 100, 8, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Branca', 35, 354600, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 14788.0, 166, 14, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Bárbara dOeste', 35, 354580, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 193475.0, 4013, 187, 112, 11, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Santa Clara dOeste', 35, 354610, 35152, 'SANTA FE DO SUL', '2020-08-27 00:00:00', 35, 2115.0, 34, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Cruz da Conceição', 35, 354620, 35101, 'ARARAS', '2020-08-27 00:00:00', 35, 4503.0, 79, 8, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Cruz da Esperança', 35, 354625, 35133, 'VALE DAS CACHOEIRAS', '2020-08-27 00:00:00', 35, 2139.0, 13, 2, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Santa Cruz das Palmeiras', 35, 354630, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 34361.0, 1306, 155, 14, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Cruz do Rio Pardo', 35, 354640, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 47673.0, 618, 40, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Ernestina', 35, 354650, 35033, 'NORTE DO DRS III', '2020-08-27 00:00:00', 35, 5599.0, 100, 13, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Santa Fé do Sul', 35, 354660, 35152, 'SANTA FE DO SUL', '2020-08-27 00:00:00', 35, 32322.0, 672, 66, 26, 11, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Santa Gertrudes', 35, 354670, 35104, 'RIO CLARO', '2020-08-27 00:00:00', 35, 26898.0, 743, 55, 12, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Isabel', 35, 354680, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 57386.0, 1004, 41, 63, 9, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Santa Lúcia', 35, 354690, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 8817.0, 38, 3, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Maria da Serra', 35, 354700, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 6173.0, 91, 9, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Mercedes', 35, 354710, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 2939.0, 1, 1, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Rita dOeste', 35, 354740, 35152, 'SANTA FE DO SUL', '2020-08-27 00:00:00', 35, 2498.0, 17, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Rita do Passa Quatro', 35, 354750, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 27557.0, 191, 21, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Rosa de Viterbo', 35, 354760, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 26540.0, 158, 11, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santa Salete', 35, 354765, 35153, 'JALES', '2020-08-27 00:00:00', 35, 1545.0, 44, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santana da Ponte Pensa', 35, 354720, 35153, 'JALES', '2020-08-27 00:00:00', 35, 1487.0, 10, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santana de Parnaíba', 35, 354730, 35014, 'ROTA DOS BANDEIRANTES', '2020-08-27 00:00:00', 35, 139447.0, 2557, 64, 87, 4, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Santo Anastácio', 35, 354770, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 20878.0, 128, 10, 8, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santo André', 35, 354780, 35015, 'GRANDE ABC', '2020-08-27 00:00:00', 35, 718773.0, 14202, 376, 497, 14, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Santo Antônio da Alegria', 35, 354790, 35133, 'VALE DAS CACHOEIRAS', '2020-08-27 00:00:00', 35, 6929.0, 27, 5, 2, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Santo Antônio de Posse', 35, 354800, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 23310.0, 386, 43, 4, 1, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Santo Antônio do Aracanguá', 35, 354805, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 8420.0, 142, 12, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santo Antônio do Jardim', 35, 354810, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 5954.0, 58, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santo Antônio do Pinhal', 35, 354820, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 6811.0, 54, 6, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santo Expedito', 35, 354830, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 3111.0, 14, 2, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santos', 35, 354850, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 433311.0, 19298, 620, 561, 25, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Santópolis do Aguapeí', 35, 354840, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 4777.0, 37, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sarapuí', 35, 355110, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 10285.0, 11, 1, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sarutaiá', 35, 355120, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 3638.0, 52, 11, 2, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Sebastianópolis do Sul', 35, 355130, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 3513.0, 41, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Serra Azul', 35, 355140, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 14662.0, 121, 26, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Serra Negra', 35, 355160, 35074, 'CIRCUITO DAS AGUAS', '2020-08-27 00:00:00', 35, 29229.0, 136, 9, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Serrana', 35, 355150, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 45107.0, 754, 51, 34, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sertãozinho', 35, 355170, 35131, 'HORIZONTE VERDE', '2020-08-27 00:00:00', 35, 125815.0, 3267, 171, 79, 8, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sete Barras', 35, 355180, 35121, 'VALE DO RIBEIRA', '2020-08-27 00:00:00', 35, 12832.0, 253, 22, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Severínia', 35, 355190, 35051, 'NORTE - BARRETOS', '2020-08-27 00:00:00', 35, 17496.0, 387, 36, 6, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Silveiras', 35, 355200, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 6302.0, 32, 10, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Socorro', 35, 355210, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 41005.0, 340, 30, 7, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sorocaba', 35, 355220, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 679378.0, 12938, 578, 337, 15, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sud Mennucci', 35, 355230, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 7718.0, 135, 26, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Sumaré', 35, 355240, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 282441.0, 5150, 288, 138, 7, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Suzano', 35, 355250, 35011, 'ALTO DO TIETE', '2020-08-27 00:00:00', 35, 297637.0, 3856, 140, 193, 8, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Suzanápolis', 35, 355255, 35022, 'LAGOS DO DRS II', '2020-08-27 00:00:00', 35, 3963.0, 40, 5, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Bento do Sapucaí', 35, 354860, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 10878.0, 42, 6, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Bernardo do Campo', 35, 354870, 35015, 'GRANDE ABC', '2020-08-27 00:00:00', 35, 838936.0, 21345, 1075, 758, 23, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'São Caetano do Sul', 35, 354880, 35015, 'GRANDE ABC', '2020-08-27 00:00:00', 35, 161127.0, 3745, 152, 168, 11, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'São Carlos', 35, 354890, 35034, 'CORACAO DO DRS III', '2020-08-27 00:00:00', 35, 251983.0, 2093, 97, 32, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Francisco', 35, 354900, 35153, 'JALES', '2020-08-27 00:00:00', 35, 2821.0, 51, 9, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Joaquim da Barra', 35, 354940, 35082, 'ALTA ANHANGUERA', '2020-08-27 00:00:00', 35, 51888.0, 692, 55, 15, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São José da Bela Vista', 35, 354950, 35081, 'TRES COLINAS', '2020-08-27 00:00:00', 35, 8928.0, 35, 13, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São José do Barreiro', 35, 354960, 35172, 'CIRCUITO DA FE E VALE HISTORICO', '2020-08-27 00:00:00', 35, 4147.0, 15, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São José do Rio Pardo', 35, 354970, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 54946.0, 261, 29, 14, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São José do Rio Preto', 35, 354980, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 460671.0, 16223, 683, 402, 19, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São José dos Campos', 35, 354990, 35171, 'ALTO VALE DO PARAIBA', '2020-08-27 00:00:00', 35, 721944.0, 12358, 480, 330, 24, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São João da Boa Vista', 35, 354910, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 91211.0, 382, 42, 11, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São João das Duas Pontes', 35, 354920, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 2568.0, 65, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São João de Iracema', 35, 354925, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 1922.0, 38, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São João do Pau dAlho', 35, 354930, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 2105.0, 2, 1, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Lourenço da Serra', 35, 354995, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 15825.0, 188, 25, 6, 1, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'São Luiz do Paraitinga', 35, 355000, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 10687.0, 16, 6, 5, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Manuel', 35, 355010, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 40954.0, 241, 11, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Miguel Arcanjo', 35, 355020, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 32931.0, 251, 16, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Paulo', 35, 355030, 35016, 'SAO PAULO', '2020-08-27 00:00:00', 35, 12252023.0, 254146, 7063, 11278, 179, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'São Pedro', 35, 355040, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 35653.0, 355, 22, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Pedro do Turvo', 35, 355050, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 7666.0, 143, 24, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Roque', 35, 355060, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 91016.0, 580, 31, 19, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Sebastião', 35, 355070, 35173, 'LITORAL NORTE', '2020-08-27 00:00:00', 35, 88980.0, 1280, 107, 28, 4, ' ', ' ', 0.0],
['Sudeste', 'SP', 'São Sebastião da Grama', 35, 355080, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 12182.0, 120, 27, 4, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Simão', 35, 355090, 35132, 'AQUIFERO GUARANI', '2020-08-27 00:00:00', 35, 15322.0, 126, 10, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'São Vicente', 35, 355100, 35041, 'BAIXADA SANTISTA', '2020-08-27 00:00:00', 35, 365798.0, 5733, 272, 349, 22, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tabapuã', 35, 355260, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 12407.0, 340, 31, 13, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tabatinga', 35, 355270, 35032, 'CENTRO OESTE DO DRS III', '2020-08-27 00:00:00', 35, 16496.0, 160, 11, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taboão da Serra', 35, 355280, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 289664.0, 5737, 282, 249, 12, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Taciba', 35, 355290, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 6285.0, 43, 10, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taguaí', 35, 355300, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 13859.0, 81, 6, 1, 1, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Taiaçu', 35, 355310, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 6295.0, 133, 16, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taiúva', 35, 355320, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 5566.0, 211, 67, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tambaú', 35, 355330, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 23207.0, 307, 24, 8, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tanabi', 35, 355340, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 25967.0, 970, 96, 19, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tapiratiba', 35, 355360, 35143, 'RIO PARDO', '2020-08-27 00:00:00', 35, 12960.0, 107, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tapiraí', 35, 355350, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 7807.0, 108, 15, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taquaral', 35, 355365, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 2811.0, 75, 8, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taquaritinga', 35, 355370, 35033, 'NORTE DO DRS III', '2020-08-27 00:00:00', 35, 57177.0, 394, 30, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taquarituba', 35, 355380, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 23218.0, 84, 10, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taquarivaí', 35, 355385, 35162, 'ITAPEVA', '2020-08-27 00:00:00', 35, 5852.0, 21, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tarabai', 35, 355390, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 7468.0, 63, 5, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tarumã', 35, 355395, 35092, 'ASSIS', '2020-08-27 00:00:00', 35, 15000.0, 89, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tatuí', 35, 355400, 35161, 'ITAPETININGA', '2020-08-27 00:00:00', 35, 121766.0, 1620, 101, 52, 5, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Taubaté', 35, 355410, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 314924.0, 2735, 274, 98, 13, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tejupá', 35, 355420, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 4532.0, 13, 3, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Teodoro Sampaio', 35, 355430, 35115, 'PONTAL DO PARANAPANEMA', '2020-08-27 00:00:00', 35, 23148.0, 190, 16, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Terra Roxa', 35, 355440, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 9370.0, 216, 14, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tietê', 35, 355450, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 42076.0, 486, 49, 9, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Timburi', 35, 355460, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 2658.0, 13, 3, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Torre de Pedra', 35, 355465, 35063, 'POLO CUESTA', '2020-08-27 00:00:00', 35, 2412.0, 14, 2, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Torrinha', 35, 355470, 35064, 'JAU', '2020-08-27 00:00:00', 35, 10010.0, 133, 9, 4, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Trabiju', 35, 355475, 35031, 'CENTRAL DO DRS III', '2020-08-27 00:00:00', 35, 1724.0, 17, 3, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Tremembé', 35, 355480, 35174, 'VALE DO PARAIBA/REGIAO SERRANA', '2020-08-27 00:00:00', 35, 47185.0, 203, 13, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Três Fronteiras', 35, 355490, 35152, 'SANTA FE DO SUL', '2020-08-27 00:00:00', 35, 5807.0, 184, 36, 8, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tuiuti', 35, 355495, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 6894.0, 46, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tupi Paulista', 35, 355510, 35111, 'ALTA PAULISTA', '2020-08-27 00:00:00', 35, 15495.0, 126, 12, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Tupã', 35, 355500, 35095, 'TUPA', '2020-08-27 00:00:00', 35, 65524.0, 553, 30, 28, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Turiúba', 35, 355520, 35023, 'CONSORCIOS DO DRS II', '2020-08-27 00:00:00', 35, 2016.0, 23, 5, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Turmalina', 35, 355530, 35154, 'FERNANDOPOLIS', '2020-08-27 00:00:00', 35, 1727.0, 17, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ubarana', 35, 355535, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 6309.0, 200, 16, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ubatuba', 35, 355540, 35173, 'LITORAL NORTE', '2020-08-27 00:00:00', 35, 90799.0, 1010, 52, 29, 3, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Ubirajara', 35, 355550, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 4780.0, 65, 7, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Uchoa', 35, 355560, 35155, 'SAO JOSE DO RIO PRETO', '2020-08-27 00:00:00', 35, 10110.0, 265, 20, 9, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'União Paulista', 35, 355570, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 1844.0, 45, 9, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Uru', 35, 355590, 35065, 'LINS', '2020-08-27 00:00:00', 35, 1165.0, 28, 5, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Urupês', 35, 355600, 35151, 'CATANDUVA', '2020-08-27 00:00:00', 35, 13809.0, 125, 38, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Urânia', 35, 355580, 35153, 'JALES', '2020-08-27 00:00:00', 35, 9114.0, 248, 16, 9, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Valentim Gentil', 35, 355610, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 13326.0, 492, 38, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Valinhos', 35, 355620, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 129193.0, 2307, 114, 73, 5, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Valparaíso', 35, 355630, 35021, 'CENTRAL DO DRS II', '2020-08-27 00:00:00', 35, 26480.0, 400, 27, 13, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Vargem', 35, 355635, 35071, 'BRAGANCA', '2020-08-27 00:00:00', 35, 10537.0, 44, 4, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Vargem Grande Paulista', 35, 355645, 35013, 'MANANCIAIS', '2020-08-27 00:00:00', 35, 52597.0, 400, 30, 21, 2, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Vargem Grande do Sul', 35, 355640, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 42845.0, 271, 17, 2, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Vera Cruz', 35, 355660, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 10843.0, 52, 18, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Vinhedo', 35, 355670, 35072, 'REGIAO METROPOLITANA DE CAMPINAS', '2020-08-27 00:00:00', 35, 78728.0, 1467, 106, 28, 2, ' ', ' ', 1.0], 
['Sudeste', 'SP', 'Viradouro', 35, 355680, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 18898.0, 245, 18, 7, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Vista Alegre do Alto', 35, 355690, 35052, 'SUL - BARRETOS', '2020-08-27 00:00:00', 35, 8810.0, 148, 13, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Vitória Brasil', 35, 355695, 35153, 'JALES', '2020-08-27 00:00:00', 35, 1840.0, 21, 7, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Votorantim', 35, 355700, 35163, 'SOROCABA', '2020-08-27 00:00:00', 35, 122480.0, 1902, 140, 64, 6, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Votuporanga', 35, 355710, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 94547.0, 3242, 248, 62, 7, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Várzea Paulista', 35, 355650, 35073, 'JUNDIAI', '2020-08-27 00:00:00', 35, 121838.0, 1375, 63, 63, 2, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Zacarias', 35, 355715, 35156, 'JOSE BONIFACIO', '2020-08-27 00:00:00', 35, 2718.0, 66, 15, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Águas da Prata', 35, 350040, 35142, 'MANTIQUEIRA', '2020-08-27 00:00:00', 35, 8180.0, 28, 4, 1, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Águas de Lindóia', 35, 350050, 35074, 'CIRCUITO DAS AGUAS', '2020-08-27 00:00:00', 35, 18705.0, 136, 10, 6, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Águas de Santa Bárbara', 35, 350055, 35061, 'VALE DO JURUMIRIM', '2020-08-27 00:00:00', 35, 6075.0, 19, 4, 0, 0, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Águas de São Pedro', 35, 350060, 35103, 'PIRACICABA', '2020-08-27 00:00:00', 35, 3451.0, 35, 4, 0, 0, ' ', ' ', 0.0],
['Sudeste', 'SP', 'Álvares Florence', 35, 350120, 35157, 'VOTUPORANGA', '2020-08-27 00:00:00', 35, 3679.0, 48, 6, 2, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Álvares Machado', 35, 350130, 35112, 'ALTA SOROCABANA', '2020-08-27 00:00:00', 35, 24915.0, 158, 12, 5, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Álvaro de Carvalho', 35, 350140, 35093, 'MARILIA', '2020-08-27 00:00:00', 35, 5227.0, 10, 2, 3, 1, ' ', ' ', 0.0], 
['Sudeste', 'SP', 'Óleo', 35, 353380, 35094, 'OURINHOS', '2020-08-27 00:00:00', 35, 2496.0, 4, 1, 0, 0, ' ', ' ', 0.0]]

print(')))))))AQUI TODOS OS CASOS DE ÓBITOS dos Municípios do ESTADO dos DE SÃO PAULO(((((((((')
print(lista2[0][12])
print(lista2[1][12])
print(lista2[2][12])
print(lista2[3][12])
print(lista2[4][12])
print(lista2[5][12])
print(lista2[6][12])
print(lista2[7][12])
print(lista2[8][12])
print(lista2[9][12])
print(lista2[10][12])
print(lista2[11][12])
print(lista2[12][12])
print(lista2[13][12])
print(lista2[14][12])
print(lista2[15][12])
print(lista2[16][12])
print(lista2[17][12])
print(lista2[18][12])
print(lista2[19][12])
print(lista2[20][12])
print(lista2[21][12])
print(lista2[22][12])
print(lista2[23][12])
print(lista2[24][12])
print(lista2[25][12])
print(lista2[26][12])
print(lista2[27][12])
print(lista2[28][12])
print(lista2[29][12])
print(lista2[30][12])
print(lista2[31][12])
print(lista2[32][12])
print(lista2[33][12])
print(lista2[34][12])
print(lista2[35][12])
print(lista2[36][12])
print(lista2[37][12])
print(lista2[38][12])
print(lista2[39][12])
print(lista2[40][12])
print(lista2[41][12])
print(lista2[42][12])
print(lista2[43][12])
print(lista2[44][12])
print(lista2[45][12])
print(lista2[46][12])
print(lista2[47][12])
print(lista2[48][12])
print(lista2[49][12])
print(lista2[50][12])
print(lista2[51][12])
print(lista2[52][12])
print(lista2[53][12])
print(lista2[54][12])
print(lista2[55][12])
print(lista2[56][12])
print(lista2[57][12])
print(lista2[58][12])
print(lista2[59][12])
print(lista2[60][12])
print(lista2[61][12])
print(lista2[62][12])
print(lista2[63][12])
print(lista2[64][12])
print(lista2[65][12])
print(lista2[66][12])
print(lista2[67][12])
print(lista2[68][12])
print(lista2[69][12])
print(lista2[70][12])
print(lista2[71][12])
print(lista2[72][12])
print(lista2[73][12])
print(lista2[74][12])
print(lista2[75][12])
print(lista2[76][12])
print(lista2[77][12])
print(lista2[78][12])
print(lista2[79][12])
print(lista2[80][12])
print(lista2[81][12])
print(lista2[82][12])
print(lista2[83][12])
print(lista2[84][12])
print(lista2[85][12])
print(lista2[86][12])
print(lista2[87][12])
print(lista2[88][12])
print(lista2[89][12])
print(lista2[90][12])
print(lista2[91][12])
print(lista2[92][12])
print(lista2[93][12])
print(lista2[94][12])
print(lista2[95][12])
print(lista2[96][12])
print(lista2[97][12])
print(lista2[98][12])
print(lista2[99][12])
print(lista2[100][12])
print(lista2[101][12])
print(lista2[102][12])
print(lista2[103][12])
print(lista2[104][12])
print(lista2[105][12])
print(lista2[106][12])
print(lista2[107][12])
print(lista2[108][12])
print(lista2[109][12])
print(lista2[110][12])
print(lista2[111][12])
print(lista2[112][12])
print(lista2[113][12])
print(lista2[114][12])
print(lista2[115][12])
print(lista2[116][12])
print(lista2[117][12])
print(lista2[118][12])
print(lista2[119][12])
print(lista2[120][12])
print(lista2[121][12])
print(lista2[122][12])
print(lista2[123][12])
print(lista2[124][12])
print(lista2[125][12])
print(lista2[126][12])
print(lista2[127][12])
print(lista2[128][12])
print(lista2[129][12])
print(lista2[130][12])
print(lista2[131][12])
print(lista2[132][12])
print(lista2[133][12])
print(lista2[134][12])
print(lista2[135][12])
print(lista2[136][12])
print(lista2[137][12])
print(lista2[138][12])
print(lista2[139][12])
print(lista2[140][12])
print(lista2[141][12])
print(lista2[142][12])
print(lista2[143][12])
print(lista2[144][12])
print(lista2[145][12])
print(lista2[146][12])
print(lista2[147][12])
print(lista2[148][12])
print(lista2[149][12])
print(lista2[150][12])
print(lista2[151][12])
print(lista2[152][12])
print(lista2[153][12])
print(lista2[154][12])
print(lista2[155][12])
print(lista2[156][12])
print(lista2[157][12])
print(lista2[158][12])
print(lista2[159][12])
print(lista2[160][12])
print(lista2[161][12])
print(lista2[162][12])
print(lista2[163][12])
print(lista2[164][12])
print(lista2[165][12])
print(lista2[166][12])
print(lista2[167][12])
print(lista2[168][12])
print(lista2[169][12])
print(lista2[170][12])
print(lista2[171][12])
print(lista2[172][12])
print(lista2[173][12])
print(lista2[174][12])
print(lista2[175][12])
print(lista2[176][12])
print(lista2[177][12])
print(lista2[178][12])
print(lista2[179][12])
print(lista2[180][12])
print(lista2[181][12])
print(lista2[182][12])
print(lista2[183][12])
print(lista2[184][12])
print(lista2[185][12])
print(lista2[186][12])
print(lista2[187][12])
print(lista2[188][12])
print(lista2[189][12])
print(lista2[190][12])
print(lista2[191][12])
print(lista2[192][12])
print(lista2[193][12])
print(lista2[194][12])
print(lista2[195][12])
print(lista2[196][12])
print(lista2[197][12])
print(lista2[198][12])
print(lista2[199][12])
print(lista2[200][12])
print(lista2[201][12])
print(lista2[202][12])
print(lista2[203][12])
print(lista2[204][12])
print(lista2[205][12])
print(lista2[206][12])
print(lista2[207][12])
print(lista2[208][12])
print(lista2[209][12])
print(lista2[210][12])
print(lista2[211][12])
print(lista2[212][12])
print(lista2[213][12])
print(lista2[214][12])
print(lista2[215][12])
print(lista2[216][12])
print(lista2[217][12])
print(lista2[218][12])
print(lista2[219][12])
print(lista2[220][12])
print(lista2[221][12])
print(lista2[222][12])
print(lista2[223][12])
print(lista2[224][12])
print(lista2[225][12])
print(lista2[226][12])
print(lista2[227][12])
print(lista2[228][12])
print(lista2[229][12])
print(lista2[230][12])
print(lista2[231][12])
print(lista2[232][12])
print(lista2[233][12])
print(lista2[234][12])
print(lista2[235][12])
print(lista2[236][12])
print(lista2[237][12])
print(lista2[238][12])
print(lista2[239][12])
print(lista2[240][12])
print(lista2[241][12])
print(lista2[242][12])
print(lista2[243][12])
print(lista2[244][12])
print(lista2[245][12])
print(lista2[246][12])
print(lista2[247][12])
print(lista2[248][12])
print(lista2[249][12])
print(lista2[250][12])
print(lista2[251][12])
print(lista2[252][12])
print(lista2[253][12])
print(lista2[254][12])
print(lista2[255][12])
print(lista2[256][12])
print(lista2[257][12])
print(lista2[258][12])
print(lista2[259][12])
print(lista2[260][12])
print(lista2[261][12])
print(lista2[262][12])
print(lista2[263][12])
print(lista2[264][12])
print(lista2[265][12])
print(lista2[266][12])
print(lista2[267][12])
print(lista2[268][12])
print(lista2[269][12])
print(lista2[270][12])
print(lista2[271][12])
print(lista2[272][12])
print(lista2[273][12])
print(lista2[274][12])
print(lista2[275][12])
print(lista2[276][12])
print(lista2[277][12])
print(lista2[278][12])
print(lista2[279][12])
print(lista2[280][12])
print(lista2[281][12])
print(lista2[282][12])
print(lista2[283][12])
print(lista2[284][12])
print(lista2[285][12])
print(lista2[286][12])
print(lista2[287][12])
print(lista2[288][12])
print(lista2[289][12])
print(lista2[290][12])
print(lista2[291][12])
print(lista2[292][12])
print(lista2[293][12])
print(lista2[294][12])
print(lista2[295][12])
print(lista2[296][12])
print(lista2[297][12])
print(lista2[298][12])
print(lista2[299][12])
print(lista2[300][12])
print(lista2[301][12])
print(lista2[302][12])
print(lista2[303][12])
print(lista2[304][12])
print(lista2[305][12])
print(lista2[306][12])
print(lista2[307][12])
print(lista2[308][12])
print(lista2[309][12])
print(lista2[310][12])
print(lista2[311][12])
print(lista2[312][12])
print(lista2[313][12])
print(lista2[314][12])
print(lista2[315][12])
print(lista2[316][12])
print(lista2[317][12])
print(lista2[318][12])
print(lista2[319][12])
print(lista2[320][12])
print(lista2[321][12])
print(lista2[322][12])
print(lista2[323][12])
print(lista2[324][12])
print(lista2[325][12])
print(lista2[326][12])
print(lista2[327][12])
print(lista2[328][12])
print(lista2[329][12])
print(lista2[330][12])
print(lista2[331][12])
print(lista2[332][12])
print(lista2[333][12])
print(lista2[334][12])
print(lista2[335][12])
print(lista2[336][12])
print(lista2[337][12])
print(lista2[338][12])
print(lista2[339][12])
print(lista2[340][12])
print(lista2[341][12])
print(lista2[342][12])
print(lista2[343][12])
print(lista2[344][12])
print(lista2[345][12])
print(lista2[346][12])
print(lista2[347][12])
print(lista2[348][12])
print(lista2[349][12])
print(lista2[350][12])
print(lista2[351][12])
print(lista2[352][12])
print(lista2[353][12])
print(lista2[354][12])
print(lista2[355][12])
print(lista2[356][12])
print(lista2[357][12])
print(lista2[358][12])
print(lista2[359][12])
print(lista2[360][12])
print(lista2[361][12])
print(lista2[362][12])
print(lista2[363][12])
print(lista2[364][12])
print(lista2[365][12])
print(lista2[366][12])
print(lista2[367][12])
print(lista2[368][12])
print(lista2[369][12])
print(lista2[370][12])
print(lista2[371][12])
print(lista2[372][12])
print(lista2[373][12])
print(lista2[374][12])
print(lista2[375][12])
print(lista2[376][12])
print(lista2[377][12])
print(lista2[378][12])
print(lista2[379][12])
print(lista2[380][12])
print(lista2[381][12])
print(lista2[382][12])
print(lista2[383][12])
print(lista2[384][12])
print(lista2[385][12])
print(lista2[386][12])
print(lista2[387][12])
print(lista2[388][12])
print(lista2[389][12])
print(lista2[390][12])
print(lista2[391][12])
print(lista2[392][12])
print(lista2[393][12])
print(lista2[394][12])
print(lista2[395][12])
print(lista2[396][12])
print(lista2[397][12])
print(lista2[398][12])
print(lista2[399][12])
print(lista2[400][12])
print(lista2[401][12])
print(lista2[402][12])
print(lista2[403][12])
print(lista2[404][12])
print(lista2[405][12])
print(lista2[406][12])
print(lista2[407][12])
print(lista2[408][12])
print(lista2[409][12])
print(lista2[410][12])
print(lista2[411][12])
print(lista2[412][12])
print(lista2[413][12])
print(lista2[414][12])
print(lista2[415][12])
print(lista2[416][12])
print(lista2[417][12])
print(lista2[418][12])
print(lista2[419][12])
print(lista2[420][12])
print(lista2[421][12])
print(lista2[422][12])
print(lista2[423][12])
print(lista2[424][12])
print(lista2[425][12])
print(lista2[426][12])
print(lista2[427][12])
print(lista2[428][12])
print(lista2[429][12])
print(lista2[430][12])
print(lista2[431][12])
print(lista2[432][12])
print(lista2[433][12])
print(lista2[434][12])
print(lista2[435][12])
print(lista2[436][12])
print(lista2[437][12])
print(lista2[438][12])
print(lista2[439][12])
print(lista2[440][12])
print(lista2[441][12])
print(lista2[442][12])
print(lista2[443][12])
print(lista2[444][12])
print(lista2[445][12])
print(lista2[446][12])
print(lista2[447][12])
print(lista2[448][12])
print(lista2[449][12])
print(lista2[450][12])
print(lista2[451][12])
print(lista2[452][12])
print(lista2[453][12])
print(lista2[454][12])
print(lista2[455][12])
print(lista2[456][12])
print(lista2[457][12])
print(lista2[458][12])
print(lista2[459][12])
print(lista2[460][12])
print(lista2[461][12])
print(lista2[462][12])
print(lista2[463][12])
print(lista2[464][12])
print(lista2[465][12])
print(lista2[466][12])
print(lista2[467][12])
print(lista2[468][12])
print(lista2[469][12])
print(lista2[470][12])
print(lista2[471][12])
print(lista2[472][12])
print(lista2[473][12])
print(lista2[474][12])
print(lista2[475][12])
print(lista2[476][12])
print(lista2[477][12])
print(lista2[478][12])
print(lista2[479][12])
print(lista2[480][12])
print(lista2[481][12])
print(lista2[482][12])
print(lista2[483][12])
print(lista2[484][12])
print(lista2[485][12])
print(lista2[486][12])
print(lista2[487][12])
print(lista2[488][12])
print(lista2[489][12])
print(lista2[490][12])
print(lista2[491][12])
print(lista2[492][12])
print(lista2[493][12])
print(lista2[494][12])
print(lista2[495][12])
print(lista2[496][12])
print(lista2[497][12])
print(lista2[498][12])
print(lista2[499][12])
print(lista2[500][12])
print(lista2[501][12])
print(lista2[502][12])
print(lista2[503][12])
print(lista2[504][12])
print(lista2[505][12])
print(lista2[506][12])
print(lista2[507][12])
print(lista2[508][12])
print(lista2[509][12])
print(lista2[510][12])
print(lista2[511][12])
print(lista2[512][12])
print(lista2[513][12])
print(lista2[514][12])
print(lista2[515][12])
print(lista2[516][12])
print(lista2[517][12])
print(lista2[518][12])
print(lista2[519][12])
print(lista2[520][12])
print(lista2[521][12])
print(lista2[522][12])
print(lista2[523][12])
print(lista2[524][12])
print(lista2[525][12])
print(lista2[526][12])
print(lista2[527][12])
print(lista2[528][12])
print(lista2[529][12])
print(lista2[530][12])
print(lista2[531][12])
print(lista2[532][12])
print(lista2[533][12])
print(lista2[534][12])
print(lista2[535][12])
print(lista2[536][12])
print(lista2[537][12])
print(lista2[538][12])
print(lista2[539][12])
print(lista2[540][12])
print(lista2[541][12])
print(lista2[542][12])
print(lista2[543][12])
print(lista2[544][12])
print(lista2[545][12])
print(lista2[546][12])
print(lista2[547][12])
print(lista2[548][12])
print(lista2[549][12])
print(lista2[550][12])
print(lista2[551][12])
print(lista2[552][12])
print(lista2[553][12])
print(lista2[554][12])
print(lista2[555][12])
print(lista2[556][12])
print(lista2[557][12])
print(lista2[558][12])
print(lista2[559][12])
print(lista2[560][12])
print(lista2[561][12])
print(lista2[562][12])
print(lista2[563][12])
print(lista2[564][12])
print(lista2[565][12])
print(lista2[566][12])
print(lista2[567][12])
print(lista2[568][12])
print(lista2[569][12])
print(lista2[570][12])
print(lista2[571][12])
print(lista2[572][12])
print(lista2[573][12])
print(lista2[574][12])
print(lista2[575][12])
print(lista2[576][12])
print(lista2[577][12])
print(lista2[578][12])
print(lista2[579][12])
print(lista2[580][12])
print(lista2[581][12])
print(lista2[582][12])
print(lista2[583][12])
print(lista2[584][12])
print(lista2[585][12])
print(lista2[586][12])
print(lista2[587][12])
print(lista2[588][12])
print(lista2[589][12])
print(lista2[590][12])
print(lista2[591][12])
print(lista2[592][12])
print(lista2[593][12])
print(lista2[594][12])
print(lista2[595][12])
print(lista2[596][12])
print(lista2[597][12])
print(lista2[598][12])
print(lista2[599][12])
print(lista2[600][12])
print(lista2[601][12])
print(lista2[602][12])
print(lista2[603][12])
print(lista2[604][12])
print(lista2[605][12])
print(lista2[606][12])
print(lista2[607][12])
print(lista2[608][12])
print(lista2[609][12])
print(lista2[610][12])
print(lista2[611][12])
print(lista2[612][12])
print(lista2[613][12])
print(lista2[614][12])
print(lista2[615][12])
print(lista2[616][12])
print(lista2[617][12])
print(lista2[618][12])
print(lista2[619][12])
print(lista2[620][12])
print(lista2[621][12])
print(lista2[622][12])
print(lista2[623][12])
print(lista2[624][12])
print(lista2[625][12])
print(lista2[626][12])
print(lista2[627][12])
print(lista2[628][12])
print(lista2[629][12])
print(lista2[630][12])
print(lista2[631][12])
print(lista2[632][12])
print(lista2[633][12])
print(lista2[634][12])
print(lista2[635][12])
print(lista2[636][12])
print(lista2[637][12])
print(lista2[638][12])
print(lista2[639][12])
print(lista2[640][12])
print(lista2[641][12])
print(lista2[642][12])
print(lista2[643][12])
print('>>>>>>>Total de Óbitos de São Paulo é de: 29432 <<<<<<')
print()
print('Reabertura do comércio em Teresina pode ser congelada; casos recentes de coronavírus voltaram a aumentar. Prefeito avaliou que aumento de cerca de 10 porcento e ainda está dentro da margem de erro da pesquisa, mas próximas fases da reabertura do comércio serão avaliadas na capital.')
print('Teresina realizou o total de 74.665 e já contam como: 25.546 Casos Acumulados')
print()
print()
print()
print('-=-=-=-=-=-=-=- FIQUE EM CASA, SE PROTEJA DO COVID-19 -=-=-=-=-=-=-=--=-=-=-=-')
print()
print()
print()