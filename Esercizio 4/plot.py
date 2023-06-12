colori = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]

#foreach classe in classi assign a color
colors_list = {}
i = 0
for classe in classi:
    if classe not in colors_list.keys():
        colors_list[classe] = colori[i]
        i += 1 

print(colors_list['economia'])

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#get all document term vectors and assign a color to each class
X = []
color_classes = []
for doc in documents:
    X.append(list(doc.term_vector.values()))
    color_classes.append(colors_list[doc.classe])

#convert to numpy array
X = np.array(X)

#apply PCA
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

#plot
plt.scatter(X_r[:, 0], X_r[:, 1], c=color_classes)
plt.show()



#
# ALTRA VISUALIZZAZIONE GRAFICA
#

prototipi = {}
for classe in classi:
    prototipi[classe] = prototipo_rocchio(classe, documents, 4, 16)

    colori = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]

#foreach classe in classi assign a color
colors_list_pr = {}
i = 0
for classe in classi:
    if classe not in colors_list_pr.keys():
        colors_list_pr[classe] = colori[i]
        i += 1 


        import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

X = []
color_classes_pr = []
for classe in classi:
    X.append(list(prototipi[classe].profile_vector.values()))
    color_classes_pr.append(colors_list_pr[classe])

#convert to numpy array
X = np.array(X)

#apply PCA
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

#plot
plt.scatter(X_r[:, 0], X_r[:, 1], c=color_classes_pr)
plt.show()