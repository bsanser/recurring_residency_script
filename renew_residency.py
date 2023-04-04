from datetime import date
import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder

current_date = date.today().strftime("%d/%m/%Y")

# Fill the writer with the pages you want
pdf_path = "solicitud_certificado_residencia_sf.pdf"
reader = PdfReader(pdf_path)
second_page = reader.pages[1]
writer = PdfWriter()
writer.add_page(second_page)

# Create the annotation and add it
annotation = AnnotationBuilder.free_text(
    current_date,
    rect=(50, 150, 200, 180),
    font="Arial",
    bold=True,
    italic=True,
    font_size="100pt",
    font_color="272822",
    border_color="0000ff",
    background_color="fcfcfc",
)
writer.add_annotation(page_number=0, annotation=annotation)

# Add first page of the original document to the beginning of the annotated second page
original_document = open(pdf_path, "rb")
writer.merge(position=0, fileobj=original_document, pages=(0, 1)) 

# Write the annotated file to disk
with open("solicitud_certificado_residencia.pdf", "wb") as fp:
    writer.write(fp)


