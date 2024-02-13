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
    parser.add_argument("-t", "--template", dest="template", help="Template file", required=True)
    parser.add_argument("-o", "--output", dest="output", help="Output file")
    parser.add_argument("-l", "--list", dest="list", help="List replacement tokens", action="store_true", default=False)

    args = parser.parse_args()

    engine = SearchReplace.select_engine(args.template, [SearchReplaceDocx, SearchReplacePdf])

    context = {
        "Bedrijfsnaam": "Bedrijfsnaam zonder haakjes",
        "Voornaam": "Heel",
        "Achternaam": "Erg",
        "antwoord_vraag_3_cliëntprofiel": "Dit is het antwoord vraag 3 cliëntprofiel",
        "antwoord_vraag_6_cliëntprofiel": "Dit is het antwoord vraag 6 cliëntprofiel",
        "antwoord_vraag_19_cliëntprofiel": "Dit is het antwoord vraag 19 cliëntprofiel",
        "antwoord_vraag_13_cliëntprofiel": "Dit is het antwoord vraag 13 cliëntprofiel",
        "antwoord_vraag_17_cliëntprofiel": "Dit is het antwoord vraag 17 cliëntprofiel",
        "antwoord_vraag_16_cliëntprofiel": "Dit is het antwoord vraag 16 cliëntprofiel",
    }

    if args.output:
        engine.search_replace(context, args.output)
        print("Migration complete. {} is ready.".format(args.output))
    elif args.list:
        print(engine.get_replacement_tokens())
    else:
        raise Exception("No output path or method specified")
