from itertools import chain
import re

import html5lib

from pelican import signals
from pelican.settings import DEFAULT_CONFIG

from .settings import RST_FOOTNOTES_TYPE


def _init(pelican):
    print(f"\x1b[31m_init({pelican})\x1b[0m")

    DEFAULT_CONFIG.setdefault("RST_FOOTNOTES_TYPE", RST_FOOTNOTES_TYPE)
    if pelican is not None:
        pelican.settings.setdefault("RST_FOOTNOTES_TYPE", RST_FOOTNOTES_TYPE)


def _prev_non_text_node(node):
    prev = node.previousSibling
    while prev is not None and prev.nodeType == prev.TEXT_NODE:
        prev = prev.previousSibling
    return prev


def _process_footnotes(content, output):
    parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("dom"))
    root = parser.parse(content)

    series = []

    # build lists of tables for the footnotes
    # there can be multiple lists where each lists contains neighouring footnote
    # tables so they can be easily "squashed" into one list

    prev_footnote, this_footnote = None, None
    for table in root.getElementsByTagName("table"):
        _class = table.attributes.get("class")
        if _class is not None and "footnote" in _class.value:
            # this is a footnote table so find the previous first non-text
            # element to check if this is a nth footnote in a series
            prev_non_text = _prev_non_text_node(table)
            if prev_non_text is not None and prev_non_text.isSameNode(prev_footnote):
                # the first non-text element is the same as recorder previous
                # element (which must be a footnote table) so we found
                # neighbouring table that we can squash
                this_footnote.append(table)
            else:
                # this is a first footnote in a series because the previous
                # non-text element is not a footnote table
                this_footnote = [table]
                # insert to head, will make further processing easier
                series.insert(0, this_footnote)
                # series.append(this_footnote)
            prev_footnote = table

    # build new representation of the footnotes

    new_nodes = []
    for footnotes in series:
        if output == "DEFINITION_LIST":
            footnotes_node = root.createElement("dl")
            footnotes_node.setAttribute("class", "footnotes")

            for footnote in footnotes:
                cells = footnote.getElementsByTagName("td")

                footnote_node_number = root.createElement("dt")
                footnote_node_number.setAttribute(
                    "class", footnote.attributes["class"].value
                )
                footnote_node_number.setAttribute("id", footnote.attributes["id"].value)
                footnote_node_number.childNodes = cells[0].childNodes

                footnote_node_content = root.createElement("dd")
                footnote_node_content.childNodes = cells[1].childNodes

                footnotes_node.appendChild(footnote_node_number)
                footnotes_node.appendChild(footnote_node_content)
        elif output == "BULLET_LIST":
            footnotes_node = root.createElement("ul")
            footnotes_node.setAttribute("class", "footnotes")

            for footnote in footnotes:
                cells = footnote.getElementsByTagName("td")

                footnote_node_element = root.createElement("li")

                footnote_node_number = root.createElement("span")
                footnote_node_number.setAttribute(
                    "class", footnote.attributes["class"].value
                )
                footnote_node_number.setAttribute("id", footnote.attributes["id"].value)
                footnote_node_number.childNodes = cells[0].childNodes

                footnote_node_content = root.createElement("span")
                footnote_node_content.childNodes = cells[1].childNodes

                footnote_node_element.appendChild(footnote_node_number)
                footnote_node_element.appendChild(footnote_node_content)
                footnotes_node.appendChild(footnote_node_element)
        else:
            raise RuntimeError("Invalid value for RST_FOOTNOTES_TYPE")

        new_nodes.append(footnotes_node)

    # process in reverse order
    for old_footnote, new_footnote in zip(series, new_nodes):
        start, end = None, None

        # find the starting index of the footnote table serier
        m = re.search(
            rf'<table[^>]*id="{old_footnote[0].attributes["id"].value}".+?\/table>',
            content,
            re.DOTALL,
        )
        start = m.start()

        # find the ending index of the footnote table serier
        m = re.search(
            rf'<table[^>]*id="{old_footnote[-1].attributes["id"].value}".+?\/table>',
            content,
            re.DOTALL,
        )
        end = m.end()

        content = (
            content[:start]
            + new_footnote.toprettyxml(indent="    ")
            + content[end + 1 :]
        )

    return content


def _process_articles_footnotes(article_generator):
    print(f"\x1b[31m_process_articles_footnotes({article_generator})\x1b[0m")

    for article in chain(article_generator.articles, article_generator.drafts):
        article._content = _process_footnotes(
            article._content, article_generator.settings["RST_FOOTNOTES_TYPE"]
        )


def _process_pages_footnotes(page_generator):
    print(f"\x1b[31m_process_pages_footnotes({page_generator})\x1b[0m")

    for page in page_generator.pages:
        page._content = _process_footnotes(
            page._content, page_generator.settings["RST_FOOTNOTES_TYPE"]
        )


def register():
    signals.initialized.connect(_init)
    signals.article_generator_finalized.connect(_process_articles_footnotes)
    signals.page_generator_finalized.connect(_process_pages_footnotes)
