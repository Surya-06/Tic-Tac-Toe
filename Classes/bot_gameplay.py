from sklearn import linear_model
import pickle
import numpy as np
from Resources import constants
import os


class bot:
    prev_model_exists = False
    model = None
    x = 1
    o = 0

    def __init__(self):
        if os.path.isfile(constants.MODEL_FILENAME):
            self.prev_model_exists = True
            self.load_model()
        if not self.prev_model_exists:
            self.prev_model_exists = self.build_classifier()

    def build_classifier(self):
        print("bot_gameplay.py - Building classifier from scratch")
        data = open(constants.MODEL_RAW_DATA)
        data_values = data.readlines()
        x_values = []
        y_values = []
        for i in range(len(data_values)):
            data_values[i] = data_values[i].split(',')
        for i in data_values:
            x_values.append(i[:9])
            y_values.append(i[9])
        for i in range(len(y_values)):
            if y_values[i] == 'positive\n':
                y_values[i] = 'x'
            else:
                y_values[i] = 'o'
            for j in range(len(x_values[i])):
                if x_values[i][j] == 'b':
                    x_values[i][j] = None
        for i in range(len(x_values)):
            for j in range(len(x_values[i])):
                if x_values[i][j] == 'x':
                    x_values[i][j] = self.x
                elif x_values[i][j] == 'o':
                    x_values[i][j] = self.o
                elif x_values[i][j] is None:
                    # print(x_values[i][j])
                    x_values[i][j] = -1

        for j in range(len(y_values)):
            # print(y_values[j])
            if y_values[j] == 'x':
                y_values[j] = self.x
            elif y_values[j] == 'o':
                y_values[j] = self.o

        x_values = np.array(x_values)
        y_values = np.array(y_values)
        class_labels = set(y_values)
        class_labels = np.array(list(class_labels))

        classifier = linear_model.SGDClassifier()
        classifier.partial_fit(x_values, y_values, class_labels)

        self.model = classifier
        return True

    def update_model(self, example, outcome):
        if outcome == 'x':
            outcome = self.x
        elif outcome == 'y':
            outcome = self.o
        else:
            outcome = self.x
        outcome = [outcome]
        example = self.convert_input(example)
        example = np.array([example])
        self.model.partial_fit(example, outcome)
        return True

    def convert_input(self, value):
        for i in range(len(value)):
            if value[i] == 'x':
                value[i] = self.x
            if value[i] == 'o':
                value[i] = self.o
        return value

    def return_prediction(self, init_input):
        value = [x for x in init_input]
        value = self.convert_input(value)
        temp_array = [value]
        temp_array = np.array(temp_array)
        prediction = self.model.predict(temp_array)
        if prediction[0] == self.x:
            return 'x'
        elif prediction[0] == self.o:
            return 'o'
        else:
            return 'o'

    def load_model(self):
        if self.prev_model_exists:
            print("bot_gameplay.py - loaded previous model from file")
            self.model = pickle.load(open(constants.MODEL_FILENAME, 'rb'))
        else:
            self.build_classifier()

    def save_model(self):
        pickle.dump(self.model, open (constants.MODEL_FILENAME, 'wb'))
