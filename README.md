This repository contains a python script designed to interpret a collection of
texts and create an index based on word frequency for subsequent analysis and 
use.

To utilize this script locally, make sure line 8 contains the ip address of
the machine where mongodb has been deployed.

To run locally simply run as follows:

$ python InvIndex.py your_text_file.txt [your_text_file2.txt, ...]

To run on a hadoop cluster, use the following line

$ python InvIndex.py -r hadoop hdfs:///<absolute path to data> --output hdfs:///<absolute path to output>

Additionally under the folder site, you will find a simple web application that'll allow you to visualize
and query a local mongodb database for documents.

To run said website use the following line:

$ python2.7 __init__.py
