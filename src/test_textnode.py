import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text_to_html_plain(self):
        node = TextNode("This is a plain text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a plain text node")

    def test_text_to_html_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_to_html_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_text_to_html_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_text_to_html_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})

    def test_text_to_html_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "https://www.example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://www.example.com/image.png", "alt": "This is an image text node"})


if __name__ == "__main__":
    unittest.main()
