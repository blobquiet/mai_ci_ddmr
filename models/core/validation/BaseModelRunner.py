from tensorflow.keras.optimizers import Adam, SGD, RMSprop

from models.core.validation.ModelRunner import ModelRunner


class BaseModelRunner(ModelRunner):
    def __init__(self, model_builder, image_size=(224, 224), batch_size=128, augmentation=None):
        params, model_builders = self._get_model_compile_params_model_builders(model_builder)
        super().__init__(model_builders, params, [image_size] * len(model_builders), batch_size, augmentation)

    @staticmethod
    def _get_model_compile_params_model_builders(model_builder):
        params = [
            {"dropout": .7, "optimizer": Adam(.00001)},
            {"dense": 128, "optimizer": Adam()},
            {"optimizer": SGD(.005)},
            {"dense": 128, "optimizer": RMSprop(.0001)},
            {"dense": 128, "dropout": .1, "optimizer": Adam(.00001)}
        ]
        model_builders = [model_builder] * len(params)
        return params, model_builders
