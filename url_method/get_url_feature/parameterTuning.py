import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import accuracy_score

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import pandas as pd

maxd, gini, entropy = [], [], []
for i in range(1,50):
    ###
    dtree = tree.DecisionTreeClassifier(criterion='gini', max_depth=i)
    dtree.fit(X_train, y_train)
    pred = dtree.predict(X_test)
    gini.append(accuracy_score(y_test, pred))
    
    ####
    dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=i)
    dtree.fit(X_train, y_train)
    pred = dtree.predict(X_test)
    entropy.append(accuracy_score(y_test, pred))
    
    ####
    maxd.append(i)
    
####
d = pd.DataFrame({'gini':pd.Series(gini), 'entropy':pd.Series(entropy), 'max_depth':pd.Series(maxd)})
# visualizing changes in parameters
plt.plot('max_depth','gini', data=d, label='Gini Index')
plt.plot('max_depth','entropy', data=d, label='Entropy')
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.legend()