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


def build_bib(mode='normal'):
    venue_fullname = pd.read_csv('venue_fullname.txt', sep='$', dtype=str)

    """Conference Papers"""
    conference = pd.read_csv('conference.txt', sep='$', dtype=str)
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
        # authors = conference.loc[i, 'author']
        # target = "Ziqing Yang"  # 想要加粗的作者名
        # authors_bib = authors.replace(target, r"\underline{" + target + "}")
        # f.write("author = {" + authors_bib + "},\n")
        f.write("author = {"+conference.loc[i, 'author']+"},")
        f.write('\n')
        # title
        f.write("title = {{"+conference.loc[i, 'title']+"}},")
        f.write('\n')
        # venue
        venue = conference.loc[i, 'venue']
        f.write("abbr = {{"+venue+"}},")
        f.write('\n')

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

        f.write("booktitle = {{"+proceedings+"}},")
        f.write('\n')

        if pd.notna(conference.loc[i, 'pages']):
            f.write("pages = {"+conference.loc[i, 'pages']+"},")
            f.write('\n')
        # publisher
        if pd.notna(conference.loc[i, 'publisher']):
            f.write("publisher = {"+conference.loc[i, 'publisher']+"},")
            f.write('\n')
        if pd.notna(conference.loc[i, 'arxiv']):
            f.write("arxiv = {"+str(conference.loc[i, 'arxiv'])+"},")
            f.write('\n')
        if pd.notna(conference.loc[i, 'pdf']):
            f.write("pdf = {"+conference.loc[i, 'pdf']+"},")
            f.write('\n')
        if pd.notna(conference.loc[i, 'code']):
            f.write("code = {"+conference.loc[i, 'code']+"},")
            f.write('\n')
        if pd.notna(conference.loc[i, 'website']):
            f.write("website = {"+conference.loc[i, 'website']+"},")
            f.write('\n')
        if pd.notna(conference.loc[i, 'slides']):
            f.write("slides = {"+conference.loc[i, 'slides']+"},")
            f.write('\n')

        # year
        f.write("year = {"+str(conference.loc[i, 'year'])+"}")
        f.write('\n')
        f.write("}")
        f.write('\n')
        f.write('\n')
        f.close()

    journal = pd.read_csv('journal.txt', sep='$', dtype=str)
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
        # authors = journal.loc[i, 'author']
        # target = "Ziqing Yang"  # 想要加粗的作者名
        # authors_bib = authors.replace(target, r"\underline{" + target + "}")
        # f.write("author = {" + authors_bib + "},\n")

        f.write("author = {"+journal.loc[i, 'author']+"},")
        f.write('\n')
        # title
        f.write("title = {{"+journal.loc[i, 'title']+"}},")
        f.write('\n')
        # venue
        venue = journal.loc[i, 'venue']
        f.write("abbr = {{"+venue+"}},")
        f.write('\n')
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
        if pd.notna(arxiv.loc[i, 'publisher']):
            f.write("publisher = {"+journal.loc[i, 'publisher']+"},")
            f.write('\n')
        if pd.notna(journal.loc[i, 'arxiv']):
                f.write("arxiv = {"+str(journal.loc[i, 'arxiv'])+"},")
                f.write('\n')
        if pd.notna(arxiv.loc[i, 'pdf']):
            f.write("pdf = {"+journal.loc[i, 'pdf']+"},")
            f.write('\n')
        if pd.notna(arxiv.loc[i, 'code']):
            f.write("code = {"+journal.loc[i, 'code']+"},")
            f.write('\n')
        if pd.notna(arxiv.loc[i, 'website']):
            f.write("website = {"+journal.loc[i, 'website']+"},")
            f.write('\n')
        if pd.notna(journal.loc[i, 'slides']):
            f.write("slides = {"+journal.loc[i, 'slides']+"},")
            f.write('\n')
        # year
        f.write("year = {"+str(journal.loc[i, 'year'])+"}")
        f.write('\n')
        f.write("}")
        f.write('\n')
        f.write('\n')
        f.close()

    arxiv = pd.read_csv('arxiv.txt', sep='$', dtype=str)
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
        # authors = arxiv.loc[i, 'author']
        # target = "Ziqing Yang"  # 想要加粗的作者名
        # authors_bib = authors.replace(target, r"\underline{" + target + "}")
        # f.write("author = {" + authors_bib + "},\n")
        f.write("author = {"+arxiv.loc[i, 'author']+"},")
        f.write('\n')
        # title
        f.write("title = {{"+arxiv.loc[i, 'title']+"}},")
        f.write('\n')
        # journal
        f.write("journal = {{"+arxiv.loc[i, 'venue']+"}},")
        f.write('\n')
        # venue
        f.write("abbr = {{arxiv}},")
        f.write('\n')
        if pd.notna(arxiv.loc[i, 'arxiv']):
                f.write("arxiv = {"+str(arxiv.loc[i, 'arxiv'])+"},")
                f.write('\n')
        if pd.notna(arxiv.loc[i, 'pdf']):
            f.write("pdf = {"+arxiv.loc[i, 'pdf']+"},")
            f.write('\n')
        if pd.notna(arxiv.loc[i, 'code']):
            f.write("code = {"+arxiv.loc[i, 'code']+"},")
            f.write('\n')
        if pd.notna(arxiv.loc[i, 'website']):
            f.write("website = {"+arxiv.loc[i, 'website']+"},")
            f.write('\n')
        if pd.notna(arxiv.loc[i, 'slides']):
            f.write("slides = {"+arxiv.loc[i, 'slides']+"},")
            f.write('\n')
        # year
        f.write("year = {"+str(arxiv.loc[i, 'year'])+"}")
        f.write('\n')
        f.write("}")
        f.write('\n')
        f.write('\n')
        f.close()

    book = pd.read_csv('book.txt', sep='$', dtype=str)
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
        # authors = book.loc[i, 'author']
        # target = "Ziqing Yang"  # 想要加粗的作者名
        # authors_bib = authors.replace(target, r"\underline{" + target + "}")
        # f.write("author = {" + authors_bib + "},\n")
        f.write("author = {"+book.loc[i, 'author']+"},")
        f.write('\n')
        # title
        f.write("title = {{"+book.loc[i, 'title']+"}},")
        f.write('\n')
        # publisher
        f.write("publisher = {"+book.loc[i, 'publisher']+"},")
        f.write('\n')
        # year
        f.write("year = {"+str(book.loc[i, 'year'])+"}")
        f.write('\n')
        f.write("}")
        f.write('\n')
        f.write('\n')
        f.close()
    
    website = pd.read_csv('website.txt', sep='$', dtype=str)

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
            # target = "Ziqing Yang"  # 想要加粗的作者名
            # authors_bib = authors.replace(target, r"\underline{" + target + "}")
            # f.write("author = {" + authors_bib + "},\n")
            f.write("author = {"+authors+"},")
            f.write('\n')
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
        f.write("}")
        f.write('\n')
        f.write('\n')
        f.close()


mode = "homepage_normal"

if os.path.exists(mode+save_suffix):
    os.remove(mode+save_suffix)

build_bib(mode)
