"""Module that provides a parser function which takes a string
and returns a dictionary with the note, tags, date, reminders and errors"""
from task import Task
import datetime as dt
from dateutil.rrule import *

abbreviations = {
    "monday": MO, "mon": MO, "mo": MO,
    "tuesday": TU, "tue": TU, "tu": MO,
    "wednesday": WE, "wed": WE, "we": WE,
    "thursday": TH, "thu": TH, "th": TH,
    "friday": FR, "fri": FR, "fr": FR,
    "saturday": SA, "sat": SA, "sa": SA,
    "sunday": SU, "sun": SU, "su": SU
}

error_messages = {"!!ERROR": "Incorrect format; consult the docs"}


def parser(text: str):
    note = ""
    tags = set()
    date = None
    errors = []
    for word in text.split():
        if word[0] == "#":
            tags.add(word[1:])
            continue
        elif word[0:2] == "!!":
            if word[2:] in abbreviations:
                date = rrule(DAILY, dtstart=dt.date.today() +
                             dt.timedelta(days=1),
                             byweekday=abbreviations[word[2:]])[0]
                continue
            errors.append((word, error_messages["!!ERROR"]))
        note += word + " "
    return Task(note=note.strip(), tags=tags, date=date, errors=errors)


if __name__ == "__main__":
    print(__doc__)
    inp = None
    while 1:
        inp = input()
        if inp == "quit()":
            break
        x = parser(inp)
        print(x, x.tags, x.date, x.errors)
