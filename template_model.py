from common.ModelAPI import ModelHandler, ModelType, Predict, ModelInfo

class TemplateModel(ModelHandler):
    def invoke(self, request: Predict.Request):
        return Predict.Response([])

    def model_info(self) -> ModelInfo.Response:
        return ModelInfo.Response("Template", "xiaoxigua", "1.0", ModelType.Predict)


def setup() -> ModelHandler:
    return TemplateModel()
