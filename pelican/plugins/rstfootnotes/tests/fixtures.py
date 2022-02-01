import pytest


@pytest.fixture
def html_with_footnotes_in_the_middle_of_element():
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Test article</title>
        </head>
        <body>

        <p>Sentence with footnote <a class="footnote-reference" href="#id10" id="id1">[1]</a> and <a class="footnote-reference" href="#id11" id="id2">[2]</a>.</p>
        <p>Another sentence with a footnote <a class="footnote-reference" href="#id12" id="id3">[3]</a> and the second one <a class="footnote-reference" href="#id13" id="id4">[4]</a>.</p>

        <table><tr><td>Ordinary table</td></tr></table>

        <table class="docutils footnote" frame="void" id="id10" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>footnote 1</td></tr>
        </tbody>
        </table>
        <table class="docutils footnote" frame="void" id="id11" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>footnote 2</td></tr>
        </tbody>
        </table>

        <p>Paragraph separating two tables.</p>

        <table class="docutils footnote" frame="void" id="id12" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id3">[3]</a></td><td>footnote 3</td></tr>
        </tbody>
        </table>
        <table class="docutils footnote" frame="void" id="id13" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id4">[4]</a></td><td>footnote 4</td></tr>
        </tbody>
        </table>

        </body>
        </html>
    """


@pytest.fixture
def html_with_footnotes_at_the_beginning_and_and_of_element():
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Test article</title>
        </head>
        <body>

        <p>Sentence with footnote <a class="footnote-reference" href="#id10" id="id1">[1]</a> and <a class="footnote-reference" href="#id11" id="id2">[2]</a>.</p>
        <p>Another sentence with a footnote <a class="footnote-reference" href="#id12" id="id3">[3]</a> and the second one <a class="footnote-reference" href="#id13" id="id4">[4]</a>.</p>

        <table><tr><td>Ordinary table</td></tr></table>

        <div>
        <table class="docutils footnote" frame="void" id="id10" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id1">[1]</a></td><td>footnote 1</td></tr>
        </tbody>
        </table>
        <table class="docutils footnote" frame="void" id="id11" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id2">[2]</a></td><td>footnote 2</td></tr>
        </tbody>
        </table>

        <p>Paragraph separating two tables.</p>

        <table class="docutils footnote" frame="void" id="id12" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id3">[3]</a></td><td>footnote 3</td></tr>
        </tbody>
        </table>
        <table class="docutils footnote" frame="void" id="id13" rules="none">
        <colgroup><col class="label" /><col /></colgroup>
        <tbody valign="top">
        <tr><td class="label"><a class="fn-backref" href="#id4">[4]</a></td><td>footnote 4</td></tr>
        </tbody>
        </table>
        </div>

        </body>
        </html>
    """
