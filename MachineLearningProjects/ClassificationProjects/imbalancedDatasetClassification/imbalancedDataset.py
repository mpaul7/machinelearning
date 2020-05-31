from numpy import mean
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot
from numpy import where


def imbalanceClassification():
	print('hello')
	X, y = make_classification(n_samples=10000,
	                           n_features=2,
	                           n_redundant=0,
	                           n_clusters_per_class=1,
	                           weights=[0.99],
	                           flip_y=0,
	                           random_state=3)

	model = DecisionTreeClassifier(class_weight='balanced')
	# define evaluation procedure
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
	# evaluate model
	scores = cross_val_score(model, X, y, scoring='roc_auc', cv=cv, n_jobs=-1)
	# summarize performance
	print('Mean ROC AUC: %.3f' % mean(scores))


if __name__ == '__main__':
	imbalanceClassification()