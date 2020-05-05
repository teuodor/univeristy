from Lab6.MLEval import MLEval
import matplotlib.pyplot as plot


def run():
    real_labels = ['spam', 'spam', 'ham', 'ham', 'spam', 'ham']
    computed_outputs = [[0.7, 0.3], [0.2, 0.8], [0.4, 0.6], [0.9, 0.1], [0.7, 0.3], [0.4, 0.6]]
    #spam ham ham spam spam ham
    ml_eval = MLEval()

    print(ml_eval.prediction_error(real_labels, computed_outputs))
    print(ml_eval.loss(real_labels, computed_outputs))
    print(ml_eval.eval_classification(real_labels, computed_outputs))
    print()

    real_labels = ['gaina', 'bunica', 'bunic', 'cocos', 'bunic', 'bunica', 'bunic']

    computed_outputs = [[0.4, 0.3, 0.2, 0.1], [0.35, 0.3, 0.31, 0.04], [0.12, 0.6, 0.01, 0.27], [0.2, 0.1, 0.1, 0.6], [0.2, 0.3, 0.3, 0.2], [0.2, 0.2, 0.4, 0.2], [0.1, 0.3, 0.3, 0.3]]
    print(ml_eval.prediction_error(real_labels, computed_outputs))
    print(ml_eval.loss(real_labels, computed_outputs))
    print(ml_eval.eval_classification(real_labels, computed_outputs))

    plot.plot(real_labels)
    plot.plot(computed_outputs)
    plot.show()


run()
