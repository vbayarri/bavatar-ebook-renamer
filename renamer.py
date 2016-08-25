import isbnlib
import os
import sys

from shutil import copyfile

print('Bavatar eBook Renamer')

# Checking program invocation
if len(sys.argv) !=3:
    print("Commandline: python rename.py ISBN Filename")
else:
    # Recovering arguments
    isbn = sys.argv[1]
    book_filename = sys.argv[2]

    # Checking arguments
    isbn = isbnlib.to_isbn13(isbnlib.clean(isbn))
    if isbn is None:
        print("ISBN is not a valid code. Please check the argument")
    else:
        if not os.path.isfile(book_filename):
            print("Filename is not a valid file. Please check the argument")
        else:
            # Get ISBN info from code
            meta = isbnlib.meta(isbn)
            print(meta)

            # Format new filename
            filename, file_extension = os.path.splitext(book_filename)
            
            title = meta['Title']
            year = meta['Year']
            book_new_filename = isbn + ' - ' + title + ' (' + year + ')' + file_extension
            print(book_new_filename)

            # Rename file
            copyfile(book_filename, book_new_filename)
