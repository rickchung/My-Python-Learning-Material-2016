class AbstractClassifier(object):
    """ 
    This is the AbstractClassifier used to be derived
    """
    def __init__(self, name):
        self.name = name
        self.model = None
    def predict(self, instance):
        # predict the instance
        pass
    def trainClassifier(self, data):
        # do something to train the classifier
        pass
    def getName(self):
        return self.name

class NaiveBayesClassifier(AbstractClassifier):
    """
    NaiveBayesClassifier implements the Bayes theorem
    """
    def __init__(self):
        super(NaiveBayesClassifier, self).__init__('NaiveBayesClassifier')

class SMOClassifier(AbstractClassifier):
    """
    Kind of SVM classifier
    """
    def __init__(self):
        super(SMOClassifier, self).__init__('SMOClassifier')

if __name__ == '__main__':
    classifiers = [NaiveBayesClassifier(), SMOClassifier()]
    for c in classifiers:
        print(c.getName())