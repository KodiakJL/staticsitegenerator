import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_to_html(self):
        test1_atr = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        test2_atr = {
            "href": "http://www.gmail.com",
            "muted": "audio",
            "name": "button"
        }
        test3_atr = {
            "muted": "video"
        }
        test1 = HTMLNode(props=test1_atr)
        test2 = HTMLNode(props=test2_atr)
        test3 = HTMLNode(props=test3_atr)
        test4 = HTMLNode()

        self.assertEqual(test1.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(test2.props_to_html(), ' href="http://www.gmail.com" muted="audio" name="button"')
        self.assertEqual(test3.props_to_html(), ' muted="video"')
        self.assertEqual(test4.props_to_html(), "")

    def test_values(self):
        test1 = HTMLNode("div", "I wish I could read")

        self.assertEqual(test1.tag, "div")
        self.assertEqual(test1.value, "I wish I could read")
        self.assertEqual(test1.children, None)
        self.assertEqual(test1.props, None)

    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(Tag: p, Value: What a strange world, Children: None, Props: {'class': 'primary'})")

    def test_to_html(self):
        node = LeafNode("p", "This is a test", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "This is the second test.")
        node4 = LeafNode(None, "This should be raw text")

        self.assertEqual(node.to_html(), '<p href="https://www.google.com">This is a test</p>')
        self.assertEqual(node2.to_html(), '<a>This is the second test.</a>')
        self.assertEqual(node4.to_html(), "This should be raw text")

    def test_parentnodes(self):
        node = ParentNode("p", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                ParentNode("h", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    ],
                ),
                ParentNode("f", [
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                )
            ]
        )
        node3 = ParentNode("p", None)
        node4 = ParentNode(None, [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        self.assertEqual(node2.to_html(), "<p><h><b>Bold text</b>Normal text</h><f><i>italic text</i>Normal text</f></p>")
        with self.assertRaises(ValueError):
            node3.to_html()
        with self.assertRaises(ValueError):
            node4.to_html()

if __name__ == "__main__":
    unittest.main()