# easy-bib

This is a python script to generate nice bibtex file for latex.

## Usage

For homepage update:
- run `python3 py3-easy-bib-homepage.py`
- the resulting .bib is ../_bibliography/normal_generated_py3.bib

For CV:
- run `python3 py3-easy-bib.py normal`
- the resulting .bib is normal_generated_py3.bib

For other files, you can:
- add the bib item you want into conference.txt, journal.txt, arxiv.txt or book.txt
- `python easy-bib.py normal`
- the resulting .bib is normal_generated.bib

You can use `diff normal_generated.bib normal_generated_py3.bib` to check the difference between two files.

## Results

> @inproceedings{P18,  
> author = {Chinese Panda},  
> title = {{An Efficient Algorithm for Finding Bamboos in the Wild}},  
> booktitle = {{Proceedings of the 2018 Conference on Pandas (CP)}},  
> pages = {1-20},  
> publisher = {XXX},  
> year = {2018}  
> }
