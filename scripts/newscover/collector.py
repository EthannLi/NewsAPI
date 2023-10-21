from pathlib import Path
import json
import argparse
import os
from newscover.newsapi import fetch_latest_news

def getPath(file):
    path = Path(__file__).parent / file
    return path

def argumentParser():
    global args
    parse = argparse.ArgumentParser()
    parse.add_argument("-k", "--api_key", required=True,help="API key for newsapi.org")
    parse.add_argument("-b","--days",required=False,help="The number of days of news that has been published within the last lookback_days")
    parse.add_argument("-i","--input",required=True,help="The input file containing the news keywords")
    parse.add_argument("-o","--output",required=True,help="The output directory where the news articles will be stored")    
    return parse.parse_args()

def dump_json(output_dir,key,value):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    fname = os.path.join(output_dir, key+".json")

    news = fetch_latest_news(args.api_key,value,args.days)

    with open(fname, "w") as file:
        json.dump(news, file, indent=4)

def main():
    global args
    # parse arguments
    args = argumentParser()
    # input json file looks like 
    # { “trump_fiasco”: [“trump”, “trial”], “swift”: [“taylor”, “swift”, “movie”] ]

    # read the json file
    fpath = getPath("test.json")
    print(fpath)
    with open(fpath) as f:
        data = json.load(f)
    # for each keyword name N and keyword list X, do a query for X and output the results to <output_dir>/N/.json

    for key,values in data.items():
        for value in values :
            dump_json(args.output,key,value)

if __name__ == "__main__":
    main()