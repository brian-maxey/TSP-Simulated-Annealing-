Date:
April 17, 2020

Authors:
Bryan Cook
bcook75@gatech.edu

Brian Maxey
bmaxey3@gatech.edu

Files:
tsp-3510.py: 
Primary python file containing the algorithm and all of the code required to execute it.

Output_tour.txt:
A sample output from one run of tsp-3510. Though different runs may have different outputs due to the random nature of Simulated Annealing, each run will have an output of  the style:
Total Cost: <tour cost>
Tour:
<tour ids in order of the found tour>

Algorithm.pdf:
PDF file explaining our process for choosing the Simulated Annealing algorithm as well as accompanying pseudocode and ten sample output tour results from running the program the provided mat-test.txt coordinates including their average and standard deviation. 

Command line to run: 
Python tsp-3510.py <input-coordinates.txt> <output-tour.txt> <time>

Known bugs/limits:
	-Inputting a non-existing file name will cause the program to crash.
-Due to the random nature of the Simulated Annealing algorithm, no two runs of the same input are guaranteed to produce the same output; it may take several runs to produce a more-optimal tour or a tour more indicative of the average that our program is capable of producing.
