class PDFDocument:
    def create(self):
        return "PDF Document"

class WordDocument:
    def create(self):
        return "Word Document"

class ExcelDocument:
    def create(self):
        return "Excel Document"

class DocumentFactory:
    @staticmethod
    def get_document(doc_type):
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "excel":
            return ExcelDocument()
        return None

# Usage
factory = DocumentFactory()

pdf = factory.get_document("pdf")
print(pdf.create())  # Output: PDF Document

word = factory.get_document("word")
print(word.create())  # Output: Word Document
