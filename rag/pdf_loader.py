from PyPDF2 import PdfReader


class PdfLoader:

    def load_pdf(self, file_path):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text