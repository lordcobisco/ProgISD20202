'''
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import label_binarize

X = [[1,2],[2,4],[4,5],[3,2],[3,1]]
Y = [0, 0, 1, 1, 2]

classif = OneVsRestClassifier(estimator= SVC(gamma='scale',random_state=0))
modeloTreinado = classif.fit(X,Y)
print(modeloTreinado.predict(X))

X = [[1,3],[1,4],[3,5],[2,2],[4,1]]
print(modeloTreinado.predict(X))
'''

from sklearn.svm import SVC
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
#from sklearn.preprocessing import label_binarize

digits = load_digits()
print(digits.data.shape)

plt.gray()
for image in digits.images:
  plt.matshow(image)
  plt.show()