#!/bin/bash
rm output/google_patents.csv
start_time="$(date -u +%s)"
python multiprocess_scraper.py 
end_time="$(date -u +%s)"

elapsed="$(($end_time-$start_time))"
echo "Total of $elapsed seconds elapsed for process"