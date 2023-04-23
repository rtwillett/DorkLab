# DorkLab

Web app tool for helping compose advance search operators (aka Google dorking AKA boolean searches) for a variety of search engines

## Team Members

* Ryan Willett
* Ally Petitt
This section is a list of team members, and possibly links to GitHub/GitLab/LinkedIn/personal blog pages for members.

## Tool Description

Web app tool for helping compose advance search operators (aka Google dorking AKA boolean searches) for a variety of search engines

### Use Cases

This application can be used for:
* Introduction to use of advance search operators
* Base for cheat cheats and references around such operators
* Simplicity of construction of operators with numerous terms

## Installation

This section includes detailed instructions for installing the tool, including any terminal commands that need to be executed and dependencies that need to be installed. Instructions should be understandable by non-technical users (e.g. someone who knows how to open a terminal and run commands, but isn't necessarily a programmer), for example:


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
This sections includes detailed instructions for using the tool. If the tool has a command-line interface, include common commands and arguments, and some examples of commands and a description of the expected output. If the tool has a graphical user interface or a browser interface, include screenshots and describe a common workflow.

## Additional Information


### Future Steps

* Part of speech (POS) tagging to detect nouns in the quicksearch queries to build that into the additional filter words
* Better detection of lookback and lookforward when one date is given in quicksearch
* More search engines:
    * Brave
    * DuckDuckGo