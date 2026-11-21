import sys
import os
import pandas as pd

save_suffix = '_generated_py3.bib'

def build_ref_key(bib_item):
    # generate ref key
    author_list = bib_item['author'].split(' and ')
    ref_key = ''
    for a in author_list:
        name_part = a.split(' ')
        ref_key += name_part[-1][0]
    ref_key += str(bib_item['year'])[2:]

    return ref_key

def process_title(df):
    df['title'] = df['title'].str.replace("<dollar-inline>", "$")


def opt(df, i, col):
    """Value of an optional column, or None if the column is missing or the cell is empty."""
    if col not in df.columns:
        return None
    v = df.loc[i, col]
    if pd.isna(v) or str(v).strip() == '':
        return None
    return str(v).strip().replace("<dollar-inline>", "$")


def write_tail(f, df, i):
    """Write usera (CCF rank, from the 'ccf' column), year and note, then close the entry."""
    ccf = opt(df, i, 'ccf')
    if ccf:
        f.write("usera = {" + ccf + "},\n")
    f.write("year = {" + str(df.loc[i, 'year']) + "}")
    note = opt(df, i, 'note')
    if note:
        f.write(",\nnote = {" + note + "}")
    f.write("\n}\n\n")


def build_bib(mode='normal'):
    venue_fullname = pd.read_csv('venue_fullname.txt', sep='$')

    conference = pd.read_csv('conference.txt', sep='$')
    process_title(conference)


    ref_key_dict = {}
    for i in range(conference.shape[0]):
        print(i)

        ref_key = build_ref_key(conference.loc[i])
        if ref_key in ref_key_dict:
            ref_key_dict[ref_key] += 1
            ref_key += str(ref_key_dict[ref_key])
        else:
            ref_key_dict[ref_key] = 1

        f = open(mode + save_suffix, 'a')

        # type of bib
        f.write("@inproceedings{"+ref_key+',')
        f.write('\n')
        # author
        authors = conference.loc[i, 'author']
        target = "Ziqing Yang"  # 想要加粗的作者名
        authors_bib = authors.replace(target, r"\textbf{" + target + "}")
        f.write("author = {" + authors_bib + "},\n")
        # f.write("author = {"+conference.loc[i, 'author']+"},")
        # f.write('\n')
        # title
        f.write("title = {{"+conference.loc[i, 'title']+"}},")
        f.write('\n')
        # venue
        venue = conference.loc[i, 'venue']
        if mode == 'normal':
            if venue == 'WWW_old':
#                proceedings = 'Proceedings of the '+ str(conference.loc[i, 'year']) + ' ' +\
#                            venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0] + ' (WWW)'
                proceedings = venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0] + ' (WWW)'
            elif venue == 'KDD_old':
                proceedings = venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0] + ' (KDD)'
            elif venue == 'ICWSM_old':
                proceedings = venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0] + ' (ICWSM)'
            elif venue == 'NeurIPSCT':
                proceedings = venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0]
            else:
#                proceedings = 'Proceedings of the '+ str(conference.loc[i, 'year']) + ' ' +\
#                            venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0] + ' (' + venue + ')'
                proceedings = venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0] + ' (' + venue + ')'
        elif mode == 'simple':
            if venue == 'WWW_old':
#                proceedings = "Proc.\ "+'WWW'
                proceedings = 'WWW'
            else:
#                proceedings = "Proc.\ "+venue
                proceedings = venue

        f.write("booktitle = {{"+proceedings+"}},")
        f.write('\n')

        if type(conference.loc[i, 'pages'])!=float:
            f.write("pages = {"+conference.loc[i, 'pages']+"},")
            f.write('\n')
        if mode == 'normal':
            # publisher
            if type(conference.loc[i, 'publisher'])!=float:
                f.write("publisher = {"+conference.loc[i, 'publisher']+"},")
                f.write('\n')
        elif mode == 'simple':
            # publisher
            f.write("publisher = {},")
            f.write('\n')
        # usera (CCF rank), year, note
        write_tail(f, conference, i)
        f.close()

    journal = pd.read_csv('journal.txt', sep='$')
    process_title(journal)
    
    for i in range(journal.shape[0]):
        print(i)

        ref_key = build_ref_key(journal.loc[i])
        if ref_key in ref_key_dict:
            ref_key_dict[ref_key] += 1
            ref_key += str(ref_key_dict[ref_key])
        else:
            ref_key_dict[ref_key] = 1

        f = open(mode+save_suffix, 'a')

        # type of bib
        f.write("@article{"+ref_key+',')
        f.write('\n')
        # author
        authors = journal.loc[i, 'author']
        target = "Ziqing Yang"  # 想要加粗的作者名
        authors_bib = authors.replace(target, r"\textbf{" + target + "}")
        f.write("author = {" + authors_bib + "},\n")

        # f.write("author = {"+journal.loc[i, 'author']+"},")
        # f.write('\n')
        # title
        f.write("title = {{"+journal.loc[i, 'title']+"}},")
        f.write('\n')
        venue = journal.loc[i, 'venue']
        # journal
        proceedings = venue_fullname.loc[venue_fullname.venue==venue, 'fullname'].values[0]
        f.write("journal = {{"+proceedings+"}},")
        f.write('\n')
#        # volume
#        if type(journal.loc[i, 'volume'])!=float:
#            f.write("volume = {"+str(journal.loc[i, 'volume'])+"},")
#            f.write('\n')
#        # number
#        if type(journal.loc[i, 'number'])!=float:
#            f.write("number = {"+str(journal.loc[i, 'number'])+"},")
#            f.write('\n')
#        # pages
#        if type(journal.loc[i, 'pages'])!=float:
#            f.write("pages = {"+journal.loc[i, 'pages']+"},")
#            f.write('\n')
        # publisher
        if type(journal.loc[i, 'publisher'])!=float:
            f.write("publisher = {"+journal.loc[i, 'publisher']+"},")
            f.write('\n')
        # usera (CCF rank), year, note
        write_tail(f, journal, i)
        f.close()

    arxiv = pd.read_csv('arxiv.txt', sep='$')
    process_title(arxiv)
    
    for i in range(arxiv.shape[0]):
        print(i)

        ref_key = build_ref_key(arxiv.loc[i])
        if ref_key in ref_key_dict:
            ref_key_dict[ref_key] += 1
            ref_key += str(ref_key_dict[ref_key])
        else:
            ref_key_dict[ref_key] = 1

        f = open(mode+save_suffix, 'a')

        # type of bib
        f.write("@article{"+ref_key+',')
        f.write('\n')
        # author
        authors = arxiv.loc[i, 'author']
        target = "Ziqing Yang"  # 想要加粗的作者名
        authors_bib = authors.replace(target, r"\textbf{" + target + "}")
        f.write("author = {" + authors_bib + "},\n")
        # f.write("author = {"+arxiv.loc[i, 'author']+"},")
        # f.write('\n')
        # title
        f.write("title = {{"+arxiv.loc[i, 'title']+"}},")
        f.write('\n')
        # journal
        f.write("journal = {{"+arxiv.loc[i, 'venue']+"}},")
        f.write('\n')
        # usera (CCF rank), year, note
        write_tail(f, arxiv, i)
        f.close()

    """Unpublished manuscripts (e.g., under review): columns author$title$year$note"""
    if os.path.exists('unpublished.txt'):
        unpublished = pd.read_csv('unpublished.txt', sep='$')
        process_title(unpublished)

        for i in range(unpublished.shape[0]):
            print(i)

            ref_key = build_ref_key(unpublished.loc[i])
            if ref_key in ref_key_dict:
                ref_key_dict[ref_key] += 1
                ref_key += str(ref_key_dict[ref_key])
            else:
                ref_key_dict[ref_key] = 1

            f = open(mode+save_suffix, 'a')

            f.write("@unpublished{"+ref_key+',')
            f.write('\n')
            authors = unpublished.loc[i, 'author']
            target = "Ziqing Yang"
            authors_bib = authors.replace(target, r"\textbf{" + target + "}")
            f.write("author = {" + authors_bib + "},\n")
            f.write("title = {{"+unpublished.loc[i, 'title']+"}},")
            f.write('\n')
            write_tail(f, unpublished, i)
            f.close()

    book = pd.read_csv('book.txt', sep='$')
    process_title(book)
    
    for i in range(book.shape[0]):
        print(i)

        ref_key = build_ref_key(book.loc[i])
        if ref_key in ref_key_dict:
            ref_key_dict[ref_key] += 1
            ref_key += str(ref_key_dict[ref_key])
        else:
            ref_key_dict[ref_key] = 1

        f = open(mode+save_suffix, 'a')

        # type of bib
        f.write("@book{"+ref_key+',')
        f.write('\n')
        # author
        authors = book.loc[i, 'author']
        target = "Ziqing Yang"  # 想要加粗的作者名
        authors_bib = authors.replace(target, r"\textbf{" + target + "}")
        f.write("author = {" + authors_bib + "},\n")
        # f.write("author = {"+book.loc[i, 'author']+"},")
        # f.write('\n')
        # title
        f.write("title = {{"+book.loc[i, 'title']+"}},")
        f.write('\n')
        # publisher
        f.write("publisher = {"+book.loc[i, 'publisher']+"},")
        f.write('\n')
        # usera (CCF rank), year, note
        write_tail(f, book, i)
        f.close()
    
    website = pd.read_csv('website.txt', sep='$')

    for i in range(website.shape[0]):

        print(i)
        ref_key = website.loc[i, 'key']

        f = open(mode+save_suffix, 'a')

        f.write("@misc{"+ref_key+',')
        f.write('\n')

        title = website.loc[i, 'title']
        if title is not None and title == title:
            f.write("title = {{"+title+"}},")
            f.write('\n')

        authors = website.loc[i, 'author']
        if authors:
            target = "Ziqing Yang"  # 想要加粗的作者名
            authors_bib = authors.replace(target, r"\textbf{" + target + "}")
            f.write("author = {" + authors_bib + "},\n")
        # author = website.loc[i, 'author']
        # if author is not None and author == author:
        #     f.write("author = {"+author+"},")
        #     f.write('\n')
            
        year = website.loc[i, 'year']
        if year is not None and year == year:
            f.write("year = {"+str(int(year))+"},")
            f.write('\n')

        f.write(r"howpublished = {\url{"+website.loc[i, 'url']+"}},")
        f.write('\n')
        note = opt(website, i, 'note')
        if note:
            f.write("note = {" + note + "},")
            f.write('\n')
        f.write("}")
        f.write('\n')
        f.write('\n')
        f.close()


mode = sys.argv[1] # "normal"

if os.path.exists(mode+save_suffix):
    os.remove(mode+save_suffix)

build_bib(mode)
