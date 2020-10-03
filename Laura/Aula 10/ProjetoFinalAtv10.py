import matplotlib.pyplot as plt
import pandas as pd
import statistics


a = pd.read_excel('Resultados ImageJ.xlsx')
print('Arquivo importado com sucesso.')

print(a.head())
print(a['Area'].value_counts())
fig = a['Area'].hist(bins=25)
plt.show()

print('Media: ',a['Area'].mean())
print('DP: ', statistics.stdev(a['Area']))
print('Mediana: ', statistics.median(a['Area']))
print('Maximo: ', max(a['Area']))
print('Mínimo: ', min(a['Area']))

class Experimento:
  def __init__(self, data):
    self.media = data.mean()
    self.desvpad =  statistics.stdev(data)
    self.mediana = statistics.median(data)
    self.max = max(data)
    self.min = min(data)

  def salvarResultados(self, arquivo, tipo):
    if tipo == 'txt':
      arquivo += '.txt'
      temp = open(arquivo,'w')
      temp.write('Media: '+str(self.media) + '\n')
      temp.write('Mediana: '+str(self.mediana) + '\n')
      temp.write('DP: '+str(self.desvpad) + '\n')
      temp.write('Maximo: '+str(self.max) + '\n')
      temp.write('Minimo: '+str(self.min) + '\n')
      print('Arquivo Salvo com resultados.')
      temp.close()

    elif tipo == 'csv':
      data = dict()
      data['Media'] = [self.media]
      data['Mediana'] = [self.mediana]
      data['DP'] = [self.desvpad]
      data['Maximo'] = [self.max]
      data['Minimo'] = [self.min]
      dataframe = pd.DataFrame(data)
      arquivo += '.csv'
      dataframe.to_csv(arquivo)
      print('Arquivo Salvo com resultados.')
      
    elif tipo == 'excel':
      data = dict()
      data['Media'] = [self.media]
      data['Mediana'] = [self.mediana]
      data['DP'] = [self.desvpad]
      data['Maximo'] = [self.max]
      data['Minimo'] = [self.min]
      dataframe = pd.DataFrame(data)
      arquivo += '.xlsx'
      dataframe.to_excel(arquivo)
      print('Arquivo Salvo com resultados.')
    else: print('Tipo não identificado.')

experimento = Experimento(a['Area'])


escolha = input('Deseja salvar arquivo de saída? ')
if escolha == 'sim':
  nomeArquivo = input('Digite o nome do arquivo de saída: ')
  while True:
    tipoSaida = input('Informe o tipo de arquivo que deseja salvar de saída [txt, csv ou excel]: ')
    if tipoSaida in ['csv','excel','txt']:
      break

  experimento.salvarResultados(nomeArquivo,tipoSaida)


