#!/usr/bin/env python
import argparse

from engines import SearchReplace
from engines.docx import SearchReplaceDocx
from engines.pdf import SearchReplacePdf

"""
Hoe gaat het werken?

1. Aangeleverd wordt een word document met tokens in de stijl {{key-naam}}
2. op onderstaande manier wordt een bestand (dus) geconverteerd

"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template", dest="template", help="Template file")
    parser.add_argument("-o", "--output", dest="output", help="Output file")
    parser.add_argument("-l", "--list", dest="list", help="List replacement tokens", action="store_true", default=False)

    args = parser.parse_args()

    engine = SearchReplace.select_engine(args.template, [SearchReplaceDocx, SearchReplacePdf])

    context = {
        "Bedrijfsnaam": "Bedrijfsnaam zonder haakjes",
        "Voornaam": "Heel",
        "Achternaam": "Erg",
    }

    if args.output:
        engine.search_replace(context, args.output)
        print("Migration complete. {} is ready.".format(args.output))
    elif args.list:
        print(engine.get_replacement_tokens())
