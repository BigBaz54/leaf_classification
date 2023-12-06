import warnings

from sklearn.exceptions import UndefinedMetricWarning

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UndefinedMetricWarning)


class Metrics:
    """ Class containing the metrics of a classifier.

    Attributes:
        classifier_name (str): the name of the classifier.
        metrics (list): a list of Metrics.Metric objects.
    """

    class Metric:
        """ Class containing the name and the score of a metric.

        Attributes:
            name (str): the name of the metric.
            score (float): the score of the metric.
        """

        def __init__(self, name: str, score: float):
            self.name = name
            self.score = score

    def __init__(self, classifier_name):
        """ Constructor for the Metrics object.

        :param classifier (sklearn classifier): the classifier to evaluate.
        :param data (Data): the data to use for the evaluation.
        """

        self.classifier_name = classifier_name
        self.metrics = []

    def __str__(self):
        """ String representation of the Metrics object.

        :return: the string representation of the Metrics object.
        """

        value: str = 'Metric scores of classifier ' + self.classifier_name + ' : '
        for metric in self.metrics:
            value += f'\n\t{metric.name} : {metric.score}'

        return value
