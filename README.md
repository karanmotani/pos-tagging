File to run: 
--> posTagging.py

Minimum Python version to run the file: 3.5


--------------------------------------------------------------------------------------


HOW TO RUN:

--> On the command line interface, type the file name along with the python extension, 
	followed by just one argument which contains the input string with Gold Tags.
	Example: posTagging.py "Input Test String with Gold Tags"

--> The program takes approximately 3 mintues (180 seconds) to run

--> Number of iteration (training rules) are set at default to 10, i.e. 
	# of best transformation rules that will be trained are 10


--------------------------------------------------------------------------------------


OUTPUT:

--> The command line will display the error rate of Most Probable Tags and Brills Tags


--> 2 files will be generated upon running the program.
	4 outputs file
	

	=>  The output file is:
		
		mostProbableTags.txt - contains the words and their corresponding most probable tags

		brillsTags.txt - contains the Brills rules

		mostProbable-OUTPUT.txt - contains the word and its most probable tag on the 
								input sentence along with the error rate

		brillsTagging-OUTPUT.txt - contains the word and its Brill tag on the 
								input sentence along with the error rate