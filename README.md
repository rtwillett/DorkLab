# DorkLab

Web app tool for helping compose advance search operators (aka Google dorking AKA boolean searches) for a variety of search engines

## Team Members

* Ryan Willett
* Ally Petitt

## Tool Description

Web app tool for helping compose advance search operators (aka Google dorking AKA boolean searches) for a variety of search engines

### Use Cases

This application can be used for:
* Introduction to use of advance search operators
* Base for cheat cheats and references around such operators
* Simplicity of construction of operators with numerous terms

## Installation
Make sure you have Python version 3.8 or greater installed


Download the tool's repository using the command:

```
 git clone https://github.com/rtwillett/DorkLab.git
```

Move to the tool's directory and install the tool

```
 cd Dorklab
 pip install -r requirements.txt
 python -m spacy download en_core_web_lg
```

Run the application
```
# method 1
python app.py

# method 2
gunicorn app:app
```


## Usage
The tool can be used by navigating to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in the browser


### Future Steps

* Part of speech (POS) tagging to detect nouns in the quicksearch queries to build that into the additional filter words
* Better detection of lookback and lookforward when one date is given in quicksearch
* More search engines:
    * Brave
    * DuckDuckGo