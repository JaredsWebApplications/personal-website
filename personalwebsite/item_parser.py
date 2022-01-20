#!/usr/bin/env python

import json
import pathlib
import typing

from models import DemoItem, PortfolioItem



def parse_contents(json_path: pathlib.Path) -> typing.List[typing.Union[DemoItem, PortfolioItem]]:
    if not json_path.is_file():
        raise FileNotFoundError(f'cannot load {json_path}, it does not exist')

    container: typing.List[typing.Union[DemoItem, PortfolioItem]] = []

    with open(json_path, "r", encoding="utf-8") as file_pointer:
        contents = json.load(file_pointer)

    for item in contents["items"]:
        match item:
            case {'authors': authors, "demo_link": demo_link, "information": information, "languages": languages, "name": name, "source_code_link": source_code_link}:
                container.append(DemoItem(name, demo_link, source_code_link, information, authors, languages))
            case {'authors': authors, "description": description,"documenation_link": doc_link , "image_path": path, "languages": languages, "name": name, "source_code_link": source_code_link}:
                container.append(PortfolioItem(name, description, path, doc_link, source_code_link, authors, languages))
            case _:
                raise ValueError(f'failed to parse {item}')
    return container

contents = parse_contents(pathlib.Path("static/models_json/demos.json"))
print(contents)
