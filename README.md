This repository contains a python script designed to interpret a collection of
texts and create an index based on word frequency for subsequent analysis and 
use.

To utilize this script locally, make sure line 7 contains the ip address of
the machine where mongodb has been deployed.

Warning: This has only been tested with ASCII characters, and will not work with other encodings.

To run locally simply run as follows:

$ python InvIndex.py your_text_file.txt [your_text_file2.txt, ...]
