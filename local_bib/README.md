# easy-bib

This is a python script to generate nice bibtex file for latex.

## Usage

For homepage update:

- run `python3 py3-easy-bib-homepage.py`
- the resulting .bib is ../\_bibliography/normal_generated_py3.bib

For CV:

- run `python3 py3-easy-bib.py normal`
- the resulting .bib is normal_generated_py3.bib

For other files, you can:

- add the bib item you want into conference.txt, journal.txt, arxiv.txt or book.txt
- `python easy-bib.py normal`
- the resulting .bib is normal_generated.bib

You can use `diff normal_generated.bib normal_generated_py3.bib` to check the difference between two files.

## Optional columns

- `note`: in every .txt file. Written as `note = {...}` after `year`. LaTeX is kept as is, e.g. `\textit{\textbf{Best Paper Nomination}}`.
- `ccf`: in conference.txt, journal.txt and arxiv.txt. The CCF rank (A / B / C / N), written as `usera = {...}`.
- `award_name`: in conference.txt, only used by `py3-easy-bib-homepage.py` (award badge on the homepage).
- `unpublished.txt` (columns `author$title$year$note`): manuscripts without a venue, e.g. under review. Written as `@unpublished` entries by `py3-easy-bib.py`; the homepage script ignores it.

Empty cells are skipped. A missing column is treated as empty.

## Results

> @inproceedings{P18,  
> author = {Chinese Panda},  
> title = {{An Efficient Algorithm for Finding Bamboos in the Wild}},  
> booktitle = {{Proceedings of the 2018 Conference on Pandas (CP)}},  
> pages = {1-20},  
> publisher = {XXX},  
> year = {2018}  
> }
