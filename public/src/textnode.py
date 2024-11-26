from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"


class TextNode:
    def __init__(self, node_content, type_of_text, link=None):
        self.text = node_content
        self.text_type = type_of_text
        self.url = link

    def __eq__(self, comparison_textnode):
        return (
            self.text == comparison_textnode.text
            and self.text_type == comparison_textnode.text_type
            and self.url == comparison_textnode.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
