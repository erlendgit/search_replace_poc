from . import SearchReplace
from docxtpl import DocxTemplate
from pathlib import Path
import os

class SearchReplaceDocx(SearchReplace):

    def __init__(self, template_path):
        super().__init__(template_path)
        self.template = DocxTemplate(self.template_path)

    @classmethod
    def supports(cls, template_path):
        return template_path.endswith(".docx")

    def get_replacement_tokens(self):
        print(self.template.get_undeclared_template_variables())

    def search_replace(self, context, output_path):
        if os.path.exists(Path(output_path)):
            os.unlink(Path(output_path))

        self.template.render(context)
        self.template.save(Path(output_path))

