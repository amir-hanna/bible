# bible
Display a verse from multiple bible versions

First install required modules, which are glob and tinydb

The script will load and display any version of the bible as long as it is saved as a tinydb json database in the same format and has a valid hash.

It use the following translations from the public domain:

Berean study bible (BSB)
King James version (KJV)
World English bible (WEB)
Young's literal translation (YLT)

You can download any version which is in the public domain in your country.

Usage:

python bible.py book chapter:verse
or: python bible.py book chapter:verse-verse
Example: python bible.py Proverbs 2:4
Example: python bible.py Proverbs 2:4-6

