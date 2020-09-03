# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# This script describes how to scrape multiple 
#  patents using python's multiprocessing module.
#  The scripts example patents are shown in list_of_patents, and
#  are a subset of patents from Thomas Alva Edison.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~ #
# ~~~ Libraries ~~~ #
# ~~~~~~~~~~~~~~~~~ #

# ~ Script specific ~ #
from functions import *

# ~ Multiprocessing ~ #
from functools import partial
import multiprocessing as mp
import os

list_of_patents = [ 'FR362691A', 'CA130636A']

path_to_data = 'output/'
filename = 'google_patents.csv'

## Create csv file to store the data from the patent runs 
#  (1) Specify column order of patents
#  (2) Create csv if it does not exist in the data path
data_column_order = [
                    'pub_date',
                    'priority_date',
                    'grant_date',
                    'filing_date',
                     'url']
if filename not in os.listdir(path_to_data):
    with open(path_to_data + filename,'w',newline='') as ofile:
        writer = csv.writer(ofile)
        writer.writerow(data_column_order)

########### Run pool process #############
if __name__ == "__main__":

    ## Create lock to prevent collisions when processes try to write on same file 
    l = mp.Lock()    

    ## Use a pool of workers where the number of processes is equal to 
    ##   the number of cpus - 1 
    with poolcontext(processes=mp.cpu_count()-1,initializer=init,initargs=(l,)) as pool:
        pool.map(partial(single_process_scraper,path_to_data_file=path_to_data + filename,
                                                data_column_order=data_column_order),
                                                list_of_patents)
