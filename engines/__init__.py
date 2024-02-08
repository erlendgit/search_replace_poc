from pathlib import Path


class SearchReplace:
    def __init__(self, template_path):
        self.template_path = Path(template_path)

    @classmethod
    def select_engine(cls, template_path, engines):
        for enigine_class in engines:
            if enigine_class.supports(template_path):
                return enigine_class(template_path)
        raise ValueError("Unsupported file type")

    @classmethod
    def supports(cls, template_path):
        raise NotImplementedError()

    def get_replacement_tokens(self):
        raise NotImplementedError()

    def search_replace(self, context, output_path):
        raise NotImplementedError()
