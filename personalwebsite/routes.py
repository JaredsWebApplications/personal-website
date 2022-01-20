from flask import (
    Flask,
    render_template,
    url_for,
    flash,
    redirect,
    request,
    session,
    send_file,
    send_from_directory,
)

from personalwebsite import app
from personalwebsite.models import (
    PortfolioItem,
    DemoItem,
)

@app.route("/")
@app.route("/home")
def home():
    """
    Landing page for the website
    """

    return render_template("index.html")


@app.route("/about")
def about():
    """
    About me page that needs to be changed
    """

    return render_template("about.html", title="About")


@app.route("/demos")
def demos():
    """
    A area where all my demo applications are running
    These should be containerized instances running concurrently
    """

    # 335 Siska Projects

    cella_ant = DemoItem(
        "Cella Ant 0x15",
        "Cella-Ant",
        "https://github.com/JaredDyreson/Cella-Ant-x15",
        "A cellular automaton variant of Langton's Ant",
        ["Jared Dyreson", "Mason Godfrey"],
        ["CSS", "HTML", "Javascript"],
    )

    sorting_olympics = DemoItem(
        "Sorting Olympics",
        "Sorting-Olympics",
        "https://github.com/JaredDyreson/Sorting-Olympics",
        "Sorting algorithm comparision program",
        ["Jared Dyreson", "Mason Godfrey"],
        ["CSS", "HTML", "Javascript"],
    )

    balloon_juice = DemoItem(
        "Balloon Juice",
        "Balloon-Juice",
        "https://github.com/JaredDyreson/Ballon-Juice/",
        "Mission reconnaissance visualizer, showing a bot retrieve a balloon in a deeply nested balloon field",
        ["Jared Dyreson", "Mason Godfrey"],
        ["CSS", "HTML", "Javascript"],
    )

    items = [
        cella_ant,
        sorting_olympics,
        # balloon_juice
    ]

    return render_template("demos.html", Demos=items)


@app.route("/projects")
def projects():
    """
    Items to show case but cannot be demonstrated using a
    web application, such as schedulers and algorithms
    """

    tuffix = PortfolioItem(
        "Tuffix",
        "Official Linux development environment for CSUF",
        "/static/assets/portfolio_items/tuffix.png",
        "https://github.com/mshafae/tuffix",
        "https://github.com/mshafae/tuffix/wiki",
        ["Michael Shafae", "Kevin Wortman", "Paul Inventado", "Jared Dyreson"],
        ["Python 3.8"],
    )

    starbucks_automa = PortfolioItem(
        "Starbucks Automa",
        "Auto work scheduler for the Starbucks Partner Portal",
        "/static/assets/portfolio_items/starbucks_coffee_robot_wallpaper-t2.jpg",
        "https://jareddyreson.github.io/posts/starbucks_automa_documentation.html",
        "https://github.com/JaredDyreson/starbucks_automa_production",
        ["Jared Dyreson"],
        ["Python 3.8", "HTML", "CSS"],
    )

    funnel_cake = PortfolioItem(
        "Funnel Cake",
        "Utility for managing Spotify playlists",
        "/static/assets/portfolio_items/funnel_cake.jpg",
        # "#", # TODO : demo link for Funnel Cake
        "https://github.com/JaredDyreson/Spoterm/blob/master/flask_stuff/DOCUMENTATION.md",  # TODO : more readable documentation
        "https://github.com/jareddyreson/funnel-cake",
        ["Jared Dyreson"],
        ["Python 3.8"],
    )

    website = PortfolioItem(
        "Personal Website",
        "A place to host portfolio items and show a little about me",
        "/static/assets/portfolio_items/python-bottle-aws-1.width-808.jpg",
        # "https://www.jareddyreson.xyz",
        "#",  # TODO: documentation about the site?
        "https://github.com/JaredDyreson/personal-website",
        ["Jared Dyreson"],
        ["Python 3.8", "HTML", "CSS"],
    )

    bauer = PortfolioItem(
        "Bauer",
        "Reverse Polish Notation Calculator",
        "/static/assets/portfolio_items/bauer.jpg",
        # "#", # TODO : demo of Bauer
        "https://github.com/JaredDyreson/RPN-Calculator/blob/master/README.md",
        "https://github.com/JaredDyreson/RPN-Calculator",
        ["Jared Dyreson", "Sergio Herrera"],
        ["Python 3.8", "Javascript", "HTML", "CSS"],
    )
    items = [tuffix, bauer, starbucks_automa, funnel_cake, website]
    return render_template("portfolio.html", PortfolioItems=items)
