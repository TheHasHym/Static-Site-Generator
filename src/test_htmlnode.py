import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "my-class"})
        self.assertEqual(str(node), "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'my-class'})")

    def test_props_to_html(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), ' class="my-class" id="my-id"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={})
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
