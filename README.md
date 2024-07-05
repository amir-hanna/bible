# bible
Display a verse(s) from multiple bible versions

First install required modules, which are glob and tinydb

The script will load and display any version of the bible as long as it is saved as a tinydb json database with the same structure and has a valid hash.

It uses the following translations from the public domain:

Berean study bible (BSB)
King James version (KJV)
World English bible (WEB)
Young's literal translation (YLT)

Each version is stored in a separate tinydb json file

The structure of the records in all databases is:
    book, chapter, verse, text
All fields are stored as text

You can download any version which is in the public domain in your country.

Usage:

python bible.py book chapter:verse
or: python bible.py book chapter:verse-verse
Example: python bible.py Proverbs 2:4
Example: python bible.py Proverbs 2:4-6

