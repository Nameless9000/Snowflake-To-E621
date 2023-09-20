# Snowflake-To-E621
Why did I make this...

## How to install:
1. Download python https://www.python.org/
2. Check that it's inside your "PATH" (open command prompt and run "python" to check if it's correctly installed)
3. Run these commands to install the dependencies:
```bash
pip install requests
pip install argparse
pip install base64
```
4. Download the "e621.py" file to somewhere safe

## How to set it up
1. Create an e621 account (my biggest regret) https://e621.net
2. Edit the file and enter your username and api key e.g.
```py
### Get an API key from https://e621.net/users/home
username = "notafurry123"
api_key = "ABCDEF1234567890"
###
```

## How to use the tool
1. Open command prompt
2. Run the command `cd` followed by the location of the folder the .py file is in e.g. `cd C:/Users/human123/Downloads`
3. Run the program `python e621.py <SNOWFLAKE> <AMOUNT/LIMIT>` (the "snowflake" can be anything e.g. for discord id the first few results will be more unique)
4. Profit??
