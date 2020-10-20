

# Importando as bibliotecas
import csv
import numpy as np
import pandas as pd
from time import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Afinando as bibliotecas
#Para encontrar bons valores para esses parâmetros, podemos usar ferramentas como grid search  
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

#Importando modelo de aprendizado supervisionado
from sklearn.naive_bayes import GaussianNB  # Importando o classificador Naive Bayes do sklearn
from sklearn import svm     # Importando o SVM do sklearn
from sklearn.linear_model import SGDClassifier  # Importando o classificador de Descida de Gradiente Estocástica do sklearn
from sklearn.ensemble import GradientBoostingClassifier # Importando o Classificador Gradient Boosting do sklearn

#Inicilizando os modelos
clf = GaussianNB() # Classificador Naive Bayes
clf2 = svm.SVC()   # Classificador Support Vector Machine 
clf3 = SGDClassifier(loss = "hinge")   # Classificador de Descida de Gradiente Estocástica
clf4 = GradientBoostingClassifier(n_estimators=100, learning_rate = 1.0, max_depth =1, random_state =0 ) # Classificador Gradient Boosting


#Definindo Funções de Testes e Treinamento

def train_classifier(clf, X_train, y_train):
    ''' Fits a classifier to the training data. '''
    
    start = time()
    clf.fit(X_train, y_train)
    end = time()
    
    print ("Trained model in {:.4f} seconds".format(end - start))

    
def predict_labels(clf, features, target):
    ''' Makes predictions using a fit classifier based on F1 score. '''
    
    start = time()
    y_pred = clf.predict(features)
    end = time()
    
    print ("Made predictions in {:.4f} seconds.".format(end - start))
    return f1_score(target.values, y_pred, pos_label=1)


def train_predict(clf, X_train, y_train, X_test, y_test):
    ''' Train and predict using a classifer based on F1 score. '''
    
    print ("Training a {} using a training set size of {}. . .".format(clf.__class__.__name__, len(X_train)))
    
    train_classifier(clf, X_train, y_train)
    
    print ("F1 score for training set: {:.4f}.".format(predict_labels(clf, X_train, y_train)))
    print ("F1 score for test set: {:.4f}.".format(predict_labels(clf, X_test, y_test)))


# Funções de ajuste / otimização

def performance_metric(y_true, y_predict):
    error = f1_score(y_true, y_predict, pos_label=1)
    return error

def fit_model(X, y):
  
    classifier = svm.SVC()

    parameters = {'kernel':['poly', 'rbf', 'sigmoid'], 'degree':[1, 2, 3], 'C':[0.1, 1, 10]}


    f1_scorer = make_scorer(performance_metric,
                                   greater_is_better=True)

    clf = GridSearchCV(classifier,
                       param_grid=parameters,
                       scoring=f1_scorer)

    clf.fit(X, y)

    return clf


# Lendo os dados
parkinson_data = pd.read_csv(r"C:\Users\Win-7\Documents\Parkinsons-Vocal-Analysis-Model-master\parkinsons.csv")
print ("Student data read successfully!")

#Análise dos dados

#Número de pacientes
n_patients = parkinson_data.shape[0]

#Número de caaracterísticas
n_features = parkinson_data.shape[1]-1

#Pacientes com Parkinson
n_parkinsons = parkinson_data[parkinson_data['status'] == 1].shape[0]     #Retorna as dimensões (quantidades) de linhas (0) com "status" com valor igual a 1

#Pacientes sem Parkinson
n_healthy = parkinson_data[parkinson_data['status'] == 0].shape[0]        #Retorna as dimensões (quantidades) de linhas (0) com "status" com valor igual a 0

#Saída dos resultados
print ("Total number of patients: {}".format(n_patients))
print ("Number of features: {}".format(n_features))
print ("Number of patients with Parkinsons: {}".format(n_parkinsons))
print ("Number of patients without Parkinsons: {}".format(n_healthy))

#Preparando os dados

# Extrair características das colunas
feature_cols = list(parkinson_data.columns[1:16]) + list(parkinson_data.columns[18:])   # Coluna de características
target_col = parkinson_data.columns[17]  # Alvo

# Mostrar  lista das colunas
print ("Feature columns:\n{}".format(feature_cols))
print ("\nTarget column: {}".format(target_col))

# Separe os dados em dados de características e dados de destino (X_all e y_all, respectivamente)
X_all = parkinson_data[feature_cols]      
y_all = parkinson_data[target_col]

# Mostre as informações de características pela impressão das primeiras cinco linhas 
print ("\nFeature values:")
print (X_all.head())   #Função usada para obter as primeiras n linhas (n=5 by default)

# Divisão de dados de treinamento e teste
num_all = parkinson_data.shape[0] 
num_train = 150 # cerca de 75% dos dados
num_test = num_all - num_train

# Seleção dos recursos e rótulos correspondentes para conjuntos de treinamento / teste

X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=num_test,random_state=5)
print ("Shuffling of data into test and training sets complete!")

print ("Training set: {} samples".format(X_train.shape[0]))
print ("Test set: {} samples".format(X_test.shape[0]))

X_train_50 = X_train[:50]
y_train_50 = y_train[:50]

X_train_100 = X_train[:100]
y_train_100 = y_train[:100]

X_train_150 = X_train[:150]
y_train_150 = y_train[:150]

#Treinando os dados

#50 set
print ("Naive Bayes:")
train_predict(clf,X_train_50,y_train_50,X_test,y_test)

print ("Support Vector Machines:")
train_predict(clf2,X_train_50,y_train_50,X_test,y_test)

print ("Stochastic Gradient Descent:")
train_predict(clf3,X_train_50,y_train_50,X_test,y_test)

print ("Gradient Tree Boosting:")
train_predict(clf4,X_train_50,y_train_50,X_test,y_test)

#100 set

print ("Naive Bayes:")
train_predict(clf,X_train_100,y_train_100,X_test,y_test)

print ("Support Vector Machines:")
train_predict(clf2,X_train_100,y_train_100,X_test,y_test)

print ("Stochastic Gradient Descent:")
train_predict(clf3,X_train_100,y_train_100,X_test,y_test)

print ("Gradient Tree Boosting:")
train_predict(clf4,X_train_100,y_train_100,X_test,y_test)

#150 set

print ("Naive Bayes:")
train_predict(clf,X_train_150,y_train_150,X_test,y_test)

print ("Support Vector Machines:")
train_predict(clf2,X_train_150,y_train_150,X_test,y_test)

print ("Stochastic Gradient Descent:")
train_predict(clf3,X_train_150,y_train_150,X_test,y_test)

print ("Gradient Tree Boosting:")
train_predict(clf4,X_train_150,y_train_150,X_test,y_test)

###################

#Ajuste de Modelo (Support Vector Machine)

print ("Tuning the model. This may take a while.....")

clf2 = fit_model(X_train, y_train)
print ("Successfully fit a model!")

print ("The best parameters were: " )

print (clf2.best_params_)

start = time()
    
print ("Tuned model has a training F1 score of {:.4f}.".format(predict_labels(clf2, X_train, y_train)))
print ("Tuned model has a testing F1 score of {:.4f}.".format(predict_labels(clf2, X_test, y_test)))

end = time()
    
print ("Tuned model in {:.4f} seconds.".format(end - start))





