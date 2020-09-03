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

list_of_patents = [ 'US3478381A',
'US4077087A',
'US4309791A',
'US5203149A',
'US6163903A',
'US6240579B1',
'US6286165B1',
'EP681799A1',
'WO2003072373A1',
'US4095532A',
'US4723808A',
'US5279010A',
'US5330064A',
'US6000076A',
'US6315319B1',
'US6321878B1',
'US6446283B1',
'US7302717B2',
'FR2780638A1',
'US2738539A',
'US3304116A',
'US4677706A',
'US4788741A',
'US5303450A',
'US5348326A',
'US5996149A',
'US6282738B1',
'US6421854B1',
'US6691346B2',
'US7882580B2',
'CH570802A5',
'US4414702A',
'US4439879A',
'US5139116A',
'US5184373A',
'US5450639A',
'US5806111A',
'US6076208A',
'US6820294B2',
'US20040139545A1',
'US3452386A',
'US3479681A',
'US3487495A',
'US4175783A',
'US5377372A',
'US5503416A',
'US5991947A',
'US6658680B2',
'FR2783463A1',
'FR2836375A1',
'WO2000051541A2',
'US3493085A',
'US3635491A',
'US3705438A',
'US4385414A',
'US4815161A',
'US4922574A',
'US5242035A',
'US5987671A',
'US6314597B2',
'US6330926B1',
'US6460205B1',
'US6598247B1',
'US6865775B2',
'US7644457B2',
'WO2002076266A1',
'US7200894B2',
'US2096229A',
'US3879796A',
'US4190002A',
'US4526253A',
'US5014391A',
'US5634532A',
'US5774936A',
'US6182310B1',
'US6264006B1',
'US6453508B1',
'US6473921B2',
'US6505359B2',
'US8122535B2',
'EP1243241A2',
'WO2002032271A1',
'US2572548A',
'US3988800A',
'US4276962A',
'US4722114A',
'US5129218A',
'US5497856A',
'US5737801A',
'US20030131413A1',
'EP1985275A2',
'US7350248B2',
'US20010044970A1',
'US20020170113A1',
'FR1450817A',
'WO1999015126A2',
'US2564083A',
'US2817855A',
'US2979738A',
]

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
