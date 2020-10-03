from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
from joblib import dump,load
from sklearn.decomposition import PCA, IncrementalPCA

"""x=[[1,2],[2,4],[4,5],[3,2],[3,1]]
y=[0,0,1,1,2]
classificador=OneVsRestClassifier(estimator=SVC(gamma='scale',random_state=0))
modeloTreinado=classificador.fit(x,y)
print(modeloTreinado.predict(x))

digits=load_digits()
print(digits.data.shape)
plt.gray()
for image in digits.images:
    plt.matshow(image)
    plt.show()

clf=svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1],digits.target[:-1])
predicted=clf.predict(digits.data[-1:])
print(predicted)

images_and_predictions = list(zip(digits.images[-1:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:1]):
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()

clf=SCV(gamma='scale')
iris = load_iris()
clf.fit(iris.data,iris.target)
dump(clf,'modeloTreinado.joblib')
print(iris.target[51])
clf = load('modeloTreinado.joblib')
print(clf.predict([iris.data[51]]))


iris=load_iris()
x=iris.data
y=iris.target
n=2
ipca=IncrementalPCA(n_components=n,batch_size=10)
x_ipca=ipca.fit_transform(x)
pca=PCA(n_components=n)
x_pca=pca.fit_transform(x)
colors=['navy','turquoise','darkorange']

for x_transformed, title in [(x_ipca,'Incremental PCA'),(x_pca,'PCA')]:
    plt.figure(figSize(8,8))
    for color,i,target_name in zip (color,[0,1,2], iris.target_names):
        plt.scatter(x_transformed[y==i,0],x_transformed[y==i,1],color=color, label=target_name)
plt.show()"""