#!/usr/bin/env python

import json
import pathlib
import typing

with open("demos.json", "r", encoding="utf-8") as file_pointer:
    contents = json.load(file_pointer)


def parse_contents(json_path: pathlib.Path) -> typing.Union[]

for item in contents["items"]:
    match item:
        case {'authors': authors, "demo_link": demo_link, "information": information, "languages": languages, "name": name, "source_code_link": source_code_link}:
            print(authors, demo_link, information, languages, name, source_code_link)
        case {'authors': authors, "description": description, "image_path": path, "languages": languages, "name": name, "source_code_link": source_code_link}:
            print("ye[]")
        case _:
            print(item)

