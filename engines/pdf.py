from pathlib import Path

from . import SearchReplace
import fitz


class SearchReplacePdf(SearchReplace):
    @classmethod
    def supports(cls, template_path):
        return template_path.endswith(".pdf")

    def get_replacement_tokens(self):
        return [*self._yield_replacement_tokens()]

    def _yield_replacement_tokens(self):
        doc = fitz.open(self.template_path)
        for page in doc:
            for widget in page.widgets():
                if widget.field_value.startswith("{{"):
                    yield widget.field_value

    def search_replace(self, context, output_path):
        doc = fitz.open(self.template_path)
        for page in doc:
            for widget in page.widgets():
                if self._update_widget(widget, context):
                    widget.update()

        doc.save(output_path)

    @staticmethod
    def _update_widget(widget, context):
        for field, new_value in context.items():
            key = "{{" + field + "}}"
            if widget.field_value == key:
                widget.field_value = new_value
                return True
        return False
