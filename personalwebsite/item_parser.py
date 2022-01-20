#!/usr/bin/env python

import json
import pathlib
import typing

from models import DemoItem, PortfolioItem


class ItemParsingException(Exception):
    """
    An exception if an item cannot be parsed
    """

    def __init__(self, message: typing.Text):
        if not isinstance(message, typing.Text):
            raise ValueError("[ERROR] Failed to create an Exception")
        self.message = message


def parse_contents(
    json_path: pathlib.Path,
) -> typing.List[typing.Union[DemoItem, PortfolioItem]]:

    """
    Given a JSON file, parse the contents to
    obtain either a list of DemoItems or PortfolioItem

    Returns:
        typing.List[typing.Union[DemoItem, PortfolioItem]]: a container of parsed objects
    """

    if not json_path.is_file():
        raise FileNotFoundError(f"cannot load {json_path}, it does not exist")

    container: typing.List[typing.Union[DemoItem, PortfolioItem]] = []

    with open(json_path, "r", encoding="utf-8") as file_pointer:
        contents = json.load(file_pointer)

    for item in contents["items"]:
        match item:
            case {
                "authors": authors,
                "demo_link": demo_link,
                "information": information,
                "languages": languages,
                "name": name,
                "source_code_link": source_code_link,
            }:
                container.append(
                    DemoItem(
                        name,
                        demo_link,
                        source_code_link,
                        information,
                        authors,
                        languages,
                    )
                )
            case {
                "authors": authors,
                "description": description,
                "documenation_link": doc_link,
                "image_path": path,
                "languages": languages,
                "name": name,
                "source_code_link": source_code_link,
            }:
                container.append(
                    PortfolioItem(
                        name,
                        description,
                        path,
                        doc_link,
                        source_code_link,
                        authors,
                        languages,
                    )
                )
            case _:
                raise ItemParsingException(f"Failed to parse {item}")
    return container
