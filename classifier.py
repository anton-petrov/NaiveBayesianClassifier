class Classifier:
    _indices = []
    _classes = []
    _numOfDocs = 0
    _numOfDocsPerClass = []
    _numOfToks = 0
    _numOfToksPerClass = []

    def __init__(self):
        pass

    def train(self, sample, class_name):

        if class_name in self._classes:
            class_index = self._classes.index(class_name)
        else:
            class_index = len(self._classes)
            self._classes.append(class_name)
            self._numOfDocsPerClass.append(0)
            self._numOfToksPerClass.append(0)
            self._indices.append({})
        self._numOfDocs += 1
        self._numOfDocsPerClass[class_index] += 1
        for token in sample.lower().split():
            self._numOfToks += 1
            if token not in self._indices[class_index]:
                self._indices[class_index][token] = 0
            self._indices[class_index][token] += 1
            self._numOfToksPerClass[class_index] += 1

    def get_hypothesis(self, opinion):
        result = []
        for class_index in range(0, len(self._classes)):
            prob = self._numOfDocsPerClass[class_index] / self._numOfDocs
            for token in opinion.lower().split():
                if token not in self._indices[class_index]:
                    counter = 0
                else:
                    counter = self._indices[class_index][token]
                prob *= (counter + 1) / (self._numOfToksPerClass[class_index] + self._numOfToks)
            result.append((self._classes[class_index], prob))
        result.sort(key=lambda element: float(element[1]), reverse=True)
        return result
