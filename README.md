# testpl
test parity


### steps to run and info

/p3 --> this is python3 stuff. This folder would be used when you set up a virtual environment (venv) in python (just in case if you still have p2 and p3 on the same pc)

to run, first you would get the google sheet document and its ID. Put it in the retrieve_stats.py file (p2). For p3, use the quickstart.py file in the p3 folder

this will generate the stats/rawdata/*.json file that's needed (outputs the spreadsheet in arrays)

exeucte transform2.py to transform the array into the json output and it will output the data to transformedata/*.json