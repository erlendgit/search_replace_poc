Copyright: Erlend ter Maat 2024 CC0-1.0

# What it is

This is a proof of the concept of transforming a word or pdf file with replacement patterns inside.

The question that is answered here is: **How can we apply structured data to template docx and PDF files with form input fields.**

# What it is not

This is not a production ready tool. It is a proof of concept.

For this reason I did not pay much attention to the 'structured data' part. One may have expected json or csv files to be supported as input for the replacement patterns. I regarded this functionality as out of scope. I mainly focused on the file format of the templates.

# Get started

Run in bash:
```bash
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## File structure

### /engines

Contains the engines for the different file formats. Currently it supports docx and pdf.

### /output

Here one can write the translated files to. Note that you have to enter the full path of the destination file when you run the script.

### /templates

Here one can put the templates files. Include the full path to the file whene you run the script.

### /venv

Python virtual environment. will be automatically generated upon project setup (see above).

### /master.py

The main script. Run this to translate a file.

## How can it be done

### Docx

To convert *.docx files the `docxtpl` library can be used. This library is strict in its conditions to convert tokens to text because it acts on a (under the hood) text based file format. It demands the tokens to be wrapped in curly braces like the following example:

```
{{ Key-name }}
```

It offers the possibility to inspect a template file to lookup all available replacement patterns. A caveat is that you have to put the patterns with curly braces in the template, but when you apply the patterns you have to use the key-name without the curly braces.

### PDF

For replacing patterns in PDF files the `PyMuPDF` library can be used. For PDF conversion we make use of the PDF feature for form fields.

A template PDF file has form fiels with tokens filled in. To fill in a form field with a replacement pattern you fill in the key in the form field. After processing the key is 1 to 1 replaced by the intended value.

Because there is no guessing of keys - form fields have special "handle-bars" on their own, it is managed in the protocol - the conditions for the replacement pattern are less demanding. One can use text as pattern. For consistency it is still recomended to use curly braces.