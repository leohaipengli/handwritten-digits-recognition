import numpy as np
import PIL
import keras.models
import tensorflow as tf

class Recognizer:

    def __init__(self, model_path):
        global graph
        with graph.as_default():
            print("loading model from {}".format(model_path))
            self.model = keras.models.load_model(model_path)
            # (28, 28, 1)
            self.single_img_shape = self.model.get_input_shape_at(0)[1:]
            print("finished loading")

    def _prepare_img(self, pil_img):
        """
        recognize the digit
        :param pil_img: PIL.Image object 
        :return: integer, the result
        """
        h = self.single_img_shape[0]
        w = self.single_img_shape[1]
        c = self.single_img_shape[2]
        image = pil_img.resize((h, w)).convert('L')

        image_array = (np.array(image, dtype=np.float32)).reshape((1, h, w, c)) / 255
        return image_array

    def predict(self, image_array: np.ndarray):
        global graph

        with graph.as_default():
            preds = self.model.predict(image_array)

        return preds.argmax()


    def recognize(self, image):
        """
        recognize the digit
        :param image: PIL.Image object 
        :return: integer, the result
        """

        image_array = self._prepare_img(image)

        return self.predict(image_array)


graph = tf.Graph()
recognizer = Recognizer('handwritten_digits/static/handwritten_digits/CS231N-handwritten-digits.h5')
