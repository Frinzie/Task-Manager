"""Module that provides a parser function which takes a string
and returns a dictionary with the note, tags, date, reminders and errors"""
from task import Task


def parser(text: str):
    note = ""
    tags = []
    for word in text.split():
        if word[0] == "#":
            tags.append(word[1:])
            continue
        note += word + " "
    return Task(note=note, tags=tags)


if __name__ == "__main__":
    print(__doc__)
    inp = None
    while 1:
        inp = input()
        if inp == "quit()":
            break
        print(parser(inp))
