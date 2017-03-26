# Final Project

Final project for PIC 10C

Author: Jiwei Zhang

UID: 304184466

Organization: UCLA

## Background

Since 1973, the Ellis Island Oral History project has been dedicated to preserving the first-hand recollections
of immigrants who passed through the Ellis Island immigration station between 1892 and 1954 and the employees
who worked there.

Over the years, the project has grown to include approximately 1900 interviews. The interviews include people
from dozens of countries, former Immigration and Public Health Service employees, military personnel stationed
at Ellis Island and the Statue of Liberty as well as people detained at Ellis Island during World War II until
it closed in 1954.

Each interview includes an examination of everyday life in the country of origin, family history, reasons for
coming to the United States, the journey to the existing port, experiences or the ship, arrival and processing
at the Ellis Island facility and an in-depth look at the adjustment to living in the United States.
Approximately fifteen interviews are added yearly by full time and volunteer staff members.

[More Information](http://www.libertyellisfoundation.org/oral-histories)

## Project Description 

Language: Python _**(all codes were written in Ipython Notebook)**_

I chose python for this project for its convenient libraries that are used for text analysis.

Utilizing the 960 transcripts that are available on the Ellis Island Foundation website, this project charaterizes the common experiences of immigrants who came to the United States between 1892 and 1954. Specifically, this project generates the 1000 most common meaningful singletons (single words), bigrams (two adjacent words), and trigrams (three adjacent words) from the transcripts available. The function written can also be used to generate and analyze n-grams (n>=1).

### Preparation for Coding
Firstly, all 960 transcripts were downloaded from the Ellis Island Foundation Website. As the website does not provide an option to download all transcripts at once, all transcripts were copied and pasted by hand then saved into a .txt file. They are stored in the folder "Transcript."

To distinguish interviewees, I generated a .xls file (**keys.xls**) which contains interviewees' lastnames and their corresponding identifier numbers. Transcript text files are named the same as the identifier number.

### Algorithm
**cleanfile.py** takes two string variables, first of which being the raw trascript and second of which being the lastname of interviewee. This function filters out content that is not from the interviewee, takes out numbers, punctuations, and expands contractions (e.g. "it's"). Before returning, the function stems every word using the Porter Stemmer. So words of the same root would be counted as the same "word" in analysis. Then the function returns a cleaned transcript as a string variable.

**genngram** is a generic function that takes two arguments, one string variable and one integer n, and generates a list of n-grams from the text passed in.

**ngramanalysis** takes one integer n and produces a list of 1000 most common n-grams stored in text files under folder "results." First, the function reads in "keys.xls" and stores in a list. Then the function opens the folder "Transcripts" and read all file names (and hence identifier numbers). One by one, all transcripts are cleaned by calling the cleanfile function. Then n-grams are generated by calling the genngram function.

**finalstep_analysis.ipynb** calls ngramanalysis three times to generate most common singletons/bigrams/trigrams. (Higher grams can be generated as well using the same function call).

## Project and PIC 10C

Python and C++ are different in many ways. I connect my project to our class in following ways:

* Unlike C++, Python has a build-in "garbage cleaning" mechanism that abides by RAII and frees up memory automatically. In other words, when I write in Python, memory that requires management is already handled as if it was acquired upon construction. Specifically, variables in Python are like pointers in C++ (or shared pointers). When reference count of an object goes to zero, delete is called and the corresponding memory is freed.

* "Try catch" (try/except in python)" was implemented in **ngramanalysis.py** not to manage memory but to catch ill-formed transcripts. Many immigrants are registered twice on the Ellis Island Foundation website (most commonly an immigrant is registered one time with her lastname and then a second time with her maiden name). Try catch throws an error message to alert me which transcripts are not compatible with algorithm written in **cleanfile.py**. I was able to fix these errors by going to these transcripts and identify what crashed my program.

* Originally I was planning on write separate n-gram generating algorithms and analysis algorithms for singletons/bigrams/trigrams. Eventually, I genericized both algorithms to take an arbituary integer and generate results, which proved to be much more efficient.

