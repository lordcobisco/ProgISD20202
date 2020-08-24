#Pais
#Estados Total

centroOeste=["Distrito Federal","Goiás","Mato Grosso","Mato Grosso do Sul"]
Norte=["Acre ","Amapá","Amazonas","Rondônia","Roraima","Tocantins","Pará"]
Noedeste=["Alagoas ","Bahia","Ceará ","Maranhão","Paraíba","Pernambuco","Piauí","Rio Grande do Norte","Sergipe"]
sul=["Rio Grande do Sul","Santa Catarina","Paraná"]
Sudeste=["Rio de Janeiro","São Paulo ","Espírito Santo","Minas Gerais"]
estados=[Norte]
populacao=[881935,845731,4144597,605761,1777225,1572866,8602865]
CasosAcumulado=[22605,39703,112263,39665,48232,37856,178375]
casosnovos=[57,185,351,42,365,867,406]
obitosAcumulados=[582,617,3505,568,1017,516,5945]
NovosObitos=[6,4,22,0,4,5,5]

print("############################################################")
print("1-Acre\n2-Amapá\n3-Amazonas\n4-Rondônia\n5-Rondônia\n6-Roraima\n7-Tocantins\n8-Pará")
opc=int(input("Selecione o número do estado escolhido: "))
print(estados[0][opc],"\nPopulação:",populacao[opc],"\n",CasosAcumulado[opc],casosnovos[opc],obitosAcumulados[opc],NovosObitos[opc])
"""MunicipiosNO=[["Alta Floresta D OESTE"]]
RegioesNO=[["Zona da mata"]]
PopulacaoNO=[[22945]]
CasosAcumuladoNO=[[415]]
ObitosAcumuladosNO=[[4]]
CasosNovosNO=[[6]]
ObitosNovosNO=[[0]]"""
