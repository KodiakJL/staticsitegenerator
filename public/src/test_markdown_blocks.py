import unittest
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        test = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.   

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        blocks = markdown_to_blocks(test)
        self.assertEqual(
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ],
            blocks
        )

    def test_block_to_block_type(self):
        block1 = "### This is a heading"
        block2 = "```\nThis is code\n```"
        block3 = ">This is a quote"
        block4 = "* This is a list\n* Second list item"
        block5 = "1. list\n2. items"
        block6 = "This is a paragraph"

        heading = block_to_block_type(block1)
        self.assertEqual("heading", heading)
        code = block_to_block_type(block2)
        self.assertEqual("code", code)
        quote = block_to_block_type(block3)
        self.assertEqual("quote", quote)
        unordered_list = block_to_block_type(block4)
        self.assertEqual("unordered list", unordered_list)
        ordered_list = block_to_block_type(block5)
        self.assertEqual("ordered list", ordered_list)
        paragraph = block_to_block_type(block6)
        self.assertEqual("paragraph", paragraph)

if __name__ == "__main__":
    unittest.main()