# NewsAPI
This is a project served to learn about API and the use case for them. In this project, I am getting the news from newsapi.com. 


To run the scrip collector:
python -m newscover.collector -k <api_key> [-b <# days to lookback>] -i <input_file> -o <output_dir>

the input file has to look like this : 
{ 
  “trump_fiasco”: [“trump”, “trial”],
  “swift”: [“taylor”, “swift”, “movie”] 
}

