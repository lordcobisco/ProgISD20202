import plotly.graph_objects as go
import pandas as pd
from scipy.signal import find_peaks

#### INFORMAÇÕES DO PACIENTE ####
print("Este programa tem o objetivo de encontrar as ondas geradas através do potencial evocado auditivo de tronco encefálico.\nPara iniciar, insira os parâmetros de avaliação\n")
nome=input("Insira o nome do paciente: ")
idade = int(input("O paciente é criança ou adulto? Digite '0' para bebê e '1' para adulto: "))
if (idade==0):
    meses=int(input("Insira a idade do bebê em meses: "))
    if (meses<=8):
        print("Esses são os valores normativos das latências para esta idade:\n\n|Onda I: 1.81|\n|Onda III: 4.70|\n|Onda V: 7.14|\n")
    else:
        print("Esses são os valores normativos das latências para esta idade:\n\n|Onda I: 1.70|\n|Onda III: 4.37|\n|Onda V: 6.50|\n")
else:
    print("Esses são os valores normativos das latências para esta idade:\n\n|Onda I: 1.50|\n|Onda III: 3.57|\n|Onda V: 5.53|\n")


data = pd.read_csv("C:\\Users\\carol\\Desktop\\programacao20202\\isdprog2020\\projetoCarol\\dadosFormatados.csv")
time_series = data['Average']/10**4

#### ENCONTRANDO OS PICOS #####
indices = find_peaks(time_series, prominence=1, width=6)[0]
temposPico = (data['Pnt']).loc[indices]
print("Essas são as latências dos picos I, III, V do/a paciente", nome)
print(temposPico[5:8]) #tiro os 5 primeiros pois sao tempos negativos antes do estimulo e os outros picos também não sao importantes

##### PLOTANDO O GRÁFICO ####
fig = go.Figure()
fig.add_trace(go.Scatter(y=time_series, mode='lines+markers', name='PEATE'))
fig.update_layout(title='Potencial Evocado Auditivo de Tronco Encefálico',
                   xaxis_title='Tempo',
                   yaxis_title='Amplitude')


fig.add_trace(go.Scatter(x=indices, y=[time_series[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='red',
        symbol='cross'),
    name='Ondas'))

fig.show()
