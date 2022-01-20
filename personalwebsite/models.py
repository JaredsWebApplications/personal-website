"""
A module that contains all the
repeatable structures that are rendered on the screen
"""

import typing


class PortfolioItem:
    """
    An item that showcases a particular project
    """

    def __init__(
        self,
        title: typing.Text,
        description: typing.Text,
        image_path: typing.Text,
        doc_link: typing.Text,
        src_link: typing.Text,
        authors: typing.List[typing.Text],
        languages: typing.List[typing.Text],
    ):
        if not (
            isinstance(title, typing.Text)
            or isinstance(description, typing.Text)
            or isinstance(image_path, typing.Text)
            or isinstance(doc_link, typing.Text)
            or isinstance(src_link, typing.Text)
            or isinstance(authors, list)
            or isinstance(languages, list)
        ):
            raise ValueError

        self.authors = authors
        self.description = description
        self.doc_link = doc_link  # should point to an official PDF rendition or article
        self.image_path = image_path
        self.languages = languages
        self.name = title
        self.src_link = src_link


class DemoItem:
    """
    An item that has a web application
    to demonstrate how the project functions
    """

    def __init__(
        self,
        name: typing.Text,
        local_link: typing.Text,
        src_code_link: typing.Text,
        information: typing.Text,
        authors: typing.List[typing.Text],
        languages: typing.List[typing.Text],
    ):
        if not (
            isinstance(name, typing.Text)
            and isinstance(local_link, typing.Text)
            and isinstance(information, typing.Text)
            and isinstance(src_code_link, typing.Text)
            and isinstance(authors, list)
            and isinstance(languages, list)
        ):
            raise ValueError

        self.authors = authors
        self.demo_link = local_link
        self.base_link = "static/demos"
        self.full_link = f"{self.base_link}/{self.demo_link}/runtime/driver.html"
        self.information = information
        self.languages = languages
        self.name = name
        self.src_code_link = src_code_link
