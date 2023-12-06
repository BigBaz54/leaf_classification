class Metrics:

    class Metric:

        def __init__(self, name: str, score: float):
            self.name = name
            self.score = score

    def __init__(self, classifier_name):

        self.classifier_name = classifier_name
        self.metrics = []

    def __str__(self):
        value: str = 'Metric scores of classifier ' + self.classifier_name + ' : '
        for metric in self.metrics:
            value += f'\n\t{metric.name} : {metric.score}'

        return value
