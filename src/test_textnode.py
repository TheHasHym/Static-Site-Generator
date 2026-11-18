import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.example.com")
        self.assertEqual(node, node2)

    def test_eq_fail(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.example.com")
        self.assertNotEqual(node, node2)

    def test_repr_with_url(self):
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(str(node), "TextNode(This is some anchor text, link, https://www.boot.dev)")

    def test_repr_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), "TextNode(This is a text node, bold, None)")


if __name__ == "__main__":
    unittest.main()
