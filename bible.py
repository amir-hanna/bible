import glob
import sys
import os
from tinydb import TinyDB, Query
import sha_hash

def get_verses(db_path, book, chapter, verse_start, verse_end):
    db = TinyDB(db_path)
    Verse = Query()
    verses = db.search((Verse.book.test(lambda v: v.lower() == book.lower())) & 
                       (Verse.chapter == chapter) & 
                       (Verse.verse.test(lambda v: int(verse_start) <= int(v) <= int(verse_end))))
    return [verse['text'] for verse in verses]

def print_usage():
    print("Usage: python script_name.py book chapter:verse")
    print("or: python script_name.py book chapter:verse-verse")
    print("Example: python script_name.py Proverbs 2:4")
    print("Example: python script_name.py Proverbs 2:4-6")

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print_usage()
        return

    # Parse command line arguments
    book = sys.argv[1]
    chapter_verse = sys.argv[2]
    chapter, verse = chapter_verse.split(':')
    if '-' in verse:
        verse_start, verse_end = verse.split('-')
    else:
        verse_start = verse_end = verse

    # Find all .json files in the current directory
    db_files = glob.glob('./*.json')

    hashes = {'bsb.json':'94f78faff6b8d43966a39badcbbd7c27937ce0e517c7f9c71540ac672d6fc1d05c6134262e5fd27ed37f45894953125293d112ffdceac0b7851221742cdb8ff3', 
              'kjv.json':'2076e4cfde8e9a610e0afc43daacee2ef531649d26affa3f1a0b08c8d0f4a1458c22dc4690bb69df1e205990bb078cc0ed7aecb2e16e88d5bf39d5b9775d01b6', 
              'web.json':'d29f567ea53cac413ec27934a19bad6cd200c8ddd6e190d772cb46f570b9d56ee86a73d79f644b14d81e5ad6bfda946f81dad36d767df9eeba9abc998c8d3656', 
              'ylt.json':'005a09761b494712453a566b6ca8ea41912b3bd08b03a1907b036923b01002e29a5917d5126b9b2a8ea13af7b2e4fe2dcd2e2cb9cde34452588571f2cad2940b'}

    for db_file in db_files:
        file_name = os.path.basename(db_file)

        if not sha_hash.sha512_ok(db_file, hashes.get(file_name)):
            print(f'Hash file error for: {file_name}')
            if db_file != db_files[-1]:  # Only print dashes if it's not the last file
                print('-' * 20)
            continue

        verses = get_verses(db_file, book, chapter, verse_start, verse_end)
        print(file_name.upper().replace('.JSON', '') + ':\n')
        for verse in verses:
            print(verse)
        if db_file != db_files[-1]:  # Only print dashes if it's not the last file
            print('-' * 20)

if __name__ == "__main__":
    main()
