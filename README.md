# Meeting Notes to Action Items

A small Python tool that turns messy meeting notes into a clean list of tasks and owners.

## What it does
Reads meeting notes from a text file, asks the AI to find the action items, and prints them as a numbered list with who is responsible.

## How it works
1. Reads the notes from `notes.txt`
2. Sends them to the Gemini API with a request for a JSON list
3. Converts the JSON reply into a Python list
4. Prints each task and its owner

## How to run it
1. Install the library: `pip install requests`
2. Get a free API key from Google AI Studio
3. Create a file called `key.txt` and paste your key in it (one line, nothing else)
4. Put your meeting notes in `notes.txt`
5. Run `actions.py`

Your API key stays in `key.txt` and is never written in the code.

## Tools used
Python, JSON, Gemini API, file handling

## Example output
1 Create a new logo by Friday - Ali
2 Contact the client about payment - Sara
3 Decide on the budget - unknown# meeting-notes-actions
