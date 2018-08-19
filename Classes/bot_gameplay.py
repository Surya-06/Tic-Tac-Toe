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
        if not self.prev_model_exists:
            self.prev_model_exists = self.build_classifier()

    def check_model_valid(self):
        if self.model is not None:
            return True
        else:
            return self.build_classifier()

    def build_classifier(self):
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
        x = 1
        o = 0

        for i in range(len(x_values)):
            for j in range(len(x_values[i])):
                if x_values[i][j] == 'x':
                    x_values[i][j] = x
                elif x_values[i][j] == 'o':
                    x_values[i][j] = o
                elif x_values[i][j] is None:
                    # print(x_values[i][j])
                    x_values[i][j] = -1

        for j in range(len(y_values)):
            # print(y_values[j])
            if y_values[j] == 'x':
                y_values[j] = x
            elif y_values[j] == 'o':
                y_values[j] = o

        x_values = np.array(x_values)
        y_values = np.array(y_values)
        class_labels = set(y_values)
        class_labels = np.array(list(class_labels))

        classifier = linear_model.SGDClassifier()
        classifier.partial_fit(x_values, y_values, class_labels)

        self.model = classifier
        return True

    def update_model(self, example, outcome):
        self.check_model_valid()
        example = [example]
        self.model.partial_fit(example, outcome)
        return True

    def convert_input(self, value):
        for i in range(len(value)):
            if value[i] == 'x':
                value[i] = self.x
            if value[i] == 'o':
                value[i] = self.o
        return value

    def return_prediction(self, value):
        self.check_model_valid()
        print("bot_gameplay.py - input value before conversion is " , value )
        value = self.convert_input(value)
        print("bot_gameplay.py - Given input value : " , value)
        temp_array = [value]
        temp_array = np.array(temp_array)
        prediction = self.model.predict(temp_array)
        print("bot_gameplay.py - Prediction : " , prediction)
        if prediction[0] == self.x:
            return 'x'
        elif prediction[0] == self.o:
            return 'o'
        else:
            print("NOTHING PREDICTED")
            return 'o'

    def load_model(self):
        if self.prev_model_exists:
            self.model = pickle.load(open(constants.MODEL_FILENAME, 'rb'))
        else:
            self.build_classifier()

    def save_model(self):
        pickle.dump(self.model, constants.MODEL_FILENAME, 'wb')
