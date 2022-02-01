from ..rstfootnotes import _process_footnotes
from .fixtures import *  # NOQA


class TestDefinitionListOutput:
    def test_footnotes_in_the_middle_of_element(
        self, html_with_footnotes_in_the_middle_of_element
    ):
        html = _process_footnotes(
            html_with_footnotes_in_the_middle_of_element, "DEFINITION_LIST"
        )

        assert (
            html
            == """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Test article</title>
        </head>
        <body>

        <p>Sentence with footnote <a class="footnote-reference" href="#id10" id="id1">[1]</a>\
 and <a class="footnote-reference" href="#id11" id="id2">[2]</a>.</p>
        <p>Another sentence with a footnote <a class="footnote-reference" href="#id12" id="id3">[3]</a>\
 and the second one <a class="footnote-reference" href="#id13" id="id4">[4]</a>.</p>

        <table><tr><td>Ordinary table</td></tr></table>

        <dl class="footnotes">
    <dt class="docutils footnote" id="id10">
        <a class="fn-backref" href="#id1">[1]</a>
    </dt>
    <dd>footnote 1</dd>
    <dt class="docutils footnote" id="id11">
        <a class="fn-backref" href="#id2">[2]</a>
    </dt>
    <dd>footnote 2</dd>
</dl>

        <p>Paragraph separating two tables.</p>

        <dl class="footnotes">
    <dt class="docutils footnote" id="id12">
        <a class="fn-backref" href="#id3">[3]</a>
    </dt>
    <dd>footnote 3</dd>
    <dt class="docutils footnote" id="id13">
        <a class="fn-backref" href="#id4">[4]</a>
    </dt>
    <dd>footnote 4</dd>
</dl>

        </body>
        </html>
    """
        )

    def test_footnotes_at_the_beginning_and_and_of_element(
        self, html_with_footnotes_at_the_beginning_and_and_of_element
    ):
        html = _process_footnotes(
            html_with_footnotes_at_the_beginning_and_and_of_element, "DEFINITION_LIST"
        )

        assert (
            html
            == """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Test article</title>
        </head>
        <body>

        <p>Sentence with footnote <a class="footnote-reference" href="#id10" id="id1">[1]</a>\
 and <a class="footnote-reference" href="#id11" id="id2">[2]</a>.</p>
        <p>Another sentence with a footnote <a class="footnote-reference" href="#id12" id="id3">[3]</a>\
 and the second one <a class="footnote-reference" href="#id13" id="id4">[4]</a>.</p>

        <table><tr><td>Ordinary table</td></tr></table>

        <div>
        <dl class="footnotes">
    <dt class="docutils footnote" id="id10">
        <a class="fn-backref" href="#id1">[1]</a>
    </dt>
    <dd>footnote 1</dd>
    <dt class="docutils footnote" id="id11">
        <a class="fn-backref" href="#id2">[2]</a>
    </dt>
    <dd>footnote 2</dd>
</dl>

        <p>Paragraph separating two tables.</p>

        <dl class="footnotes">
    <dt class="docutils footnote" id="id12">
        <a class="fn-backref" href="#id3">[3]</a>
    </dt>
    <dd>footnote 3</dd>
    <dt class="docutils footnote" id="id13">
        <a class="fn-backref" href="#id4">[4]</a>
    </dt>
    <dd>footnote 4</dd>
</dl>
        </div>

        </body>
        </html>
    """
        )


class TestBulletListOutput:
    def test_footnotes_in_the_middle_of_element(
        self, html_with_footnotes_in_the_middle_of_element
    ):
        html = _process_footnotes(
            html_with_footnotes_in_the_middle_of_element, "BULLET_LIST"
        )

        assert (
            html
            == """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Test article</title>
        </head>
        <body>

        <p>Sentence with footnote <a class="footnote-reference" href="#id10" id="id1">[1]</a>\
 and <a class="footnote-reference" href="#id11" id="id2">[2]</a>.</p>
        <p>Another sentence with a footnote <a class="footnote-reference" href="#id12" id="id3">[3]</a>\
 and the second one <a class="footnote-reference" href="#id13" id="id4">[4]</a>.</p>

        <table><tr><td>Ordinary table</td></tr></table>

        <ul class="footnotes">
    <li>
        <span class="docutils footnote" id="id10">
            <a class="fn-backref" href="#id1">[1]</a>
        </span>
        <span>footnote 1</span>
    </li>
    <li>
        <span class="docutils footnote" id="id11">
            <a class="fn-backref" href="#id2">[2]</a>
        </span>
        <span>footnote 2</span>
    </li>
</ul>

        <p>Paragraph separating two tables.</p>

        <ul class="footnotes">
    <li>
        <span class="docutils footnote" id="id12">
            <a class="fn-backref" href="#id3">[3]</a>
        </span>
        <span>footnote 3</span>
    </li>
    <li>
        <span class="docutils footnote" id="id13">
            <a class="fn-backref" href="#id4">[4]</a>
        </span>
        <span>footnote 4</span>
    </li>
</ul>

        </body>
        </html>
    """
        )

    def test_footnotes_at_the_beginning_and_and_of_element(
        self, html_with_footnotes_at_the_beginning_and_and_of_element
    ):
        html = _process_footnotes(
            html_with_footnotes_at_the_beginning_and_and_of_element, "BULLET_LIST"
        )

        assert (
            html
            == """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Test article</title>
        </head>
        <body>

        <p>Sentence with footnote <a class="footnote-reference" href="#id10" id="id1">[1]</a>\
 and <a class="footnote-reference" href="#id11" id="id2">[2]</a>.</p>
        <p>Another sentence with a footnote <a class="footnote-reference" href="#id12" id="id3">[3]</a>\
 and the second one <a class="footnote-reference" href="#id13" id="id4">[4]</a>.</p>

        <table><tr><td>Ordinary table</td></tr></table>

        <div>
        <ul class="footnotes">
    <li>
        <span class="docutils footnote" id="id10">
            <a class="fn-backref" href="#id1">[1]</a>
        </span>
        <span>footnote 1</span>
    </li>
    <li>
        <span class="docutils footnote" id="id11">
            <a class="fn-backref" href="#id2">[2]</a>
        </span>
        <span>footnote 2</span>
    </li>
</ul>

        <p>Paragraph separating two tables.</p>

        <ul class="footnotes">
    <li>
        <span class="docutils footnote" id="id12">
            <a class="fn-backref" href="#id3">[3]</a>
        </span>
        <span>footnote 3</span>
    </li>
    <li>
        <span class="docutils footnote" id="id13">
            <a class="fn-backref" href="#id4">[4]</a>
        </span>
        <span>footnote 4</span>
    </li>
</ul>
        </div>

        </body>
        </html>
    """
        )
