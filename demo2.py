from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166,65, 40], [190, 90, 47], [175, 64, 39], [159, 55, 37], [171, 75, 42], [189, 80, 45], [152, 42, 40], [191, 76, 46]]

Y = ['male', 'female', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([[192, 70, 54], [189, 65, 44], [185, 35, 60]])


print(prediction)

