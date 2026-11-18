import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode(tag="div", value="Hello", props={"class": "my-class"})
        self.assertEqual(str(node), "LeafNode(tag=div, value=Hello, props={'class': 'my-class'})")

    def test_leaf_to_html(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_value(self):
        node = LeafNode(tag="p", value=None)
        self.assertEqual(node.to_html(), ValueError)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(tag=None, value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
