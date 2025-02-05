class WritingUtils:
    def __init__(self, string):
        self.string = string

    @staticmethod
    def countOccurrence(self):
        occurrences = {}
        sentence = (self.string).split()
        for word in sentence: 
            occurrences[word] += 1