# STA9760_bigdata
Analyzing millions of NYC Parking Violations


Inputs/Outputs

Here are all the command line arguments your script must support:
$ docker run -e APP_KEY={YOUR_APP_KEY} -t bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=results.json
Some key arguments here:
●	 APP_KEY: This is how a user can pass along an APP_KEY for the api in a safe manner. DO NOT COMMIT YOUR (actual) APP KEY to Github! Also, APP_KEY should not be “hardcoded” anywhere in your source code.
●	bigdata1: This is the name of your docker image. We want the output for Part 1 to be version 1.
●	--page_size: This command line argument is required. It will ask for how many records to request from the API per call.
●	--num_pages: This command line argument is optional. If not provided, your script should continue requesting data until the entirety of the content has been exhausted. If this argument is provided, continue querying for data num_pages times.
●	--output: This command line argument is optional. If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).
It is expected that stdout or results.json will contain the API response, which is simply rows and rows of data from the API within the confines of the parameters provided to the script.


Solutions in Windows Powershell

docker build -t bigdat1:1.0 .

docker run -e APP_KEY=%APP_KEY% -v C:\project1\bigdata1:/app/foo -it bigdata1:1.0 python main.py --page_size=1000 --num_pages=4 --output=foo/results.json


