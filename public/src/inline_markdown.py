import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_node_list = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            if node.text_type == TextType.TEXT:
                string_list = list(enumerate(node.text.split(delimiter)))
                if len(string_list) % 2 != 1:
                    raise Exception(f"Unmatched delimeter in {node}")
                for string in string_list:
                    if string[1] == "":
                        continue
                    if string[0] % 2 == 0:
                        final_node_list.append(TextNode(string[1], TextType.TEXT))
                    elif string[0] % 2 != 0:
                        final_node_list.append(TextNode(string[1], text_type))
            else:
                final_node_list.append(node)
    return final_node_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    final_node_list = []
    for node in old_nodes:
        remaining_text = node.text
        image_alt_url = extract_markdown_images(remaining_text)
        if len(image_alt_url) == 0:
            final_node_list.append(node)
            continue
        for i in range(len(image_alt_url)):
            sections = list(remaining_text.split(f"![{image_alt_url[i][0]}]({image_alt_url[i][1]})", 1))
            if sections[0] != "":
                final_node_list.append(TextNode(sections[0], TextType.TEXT))
            final_node_list.append(TextNode(image_alt_url[i][0], TextType.IMAGE, image_alt_url[i][1]))
            remaining_text = sections[1]
        if remaining_text != "":
            final_node_list.append(TextNode(remaining_text, TextType.TEXT))
    return final_node_list

def split_nodes_link(old_nodes):
    final_node_list = []
    for node in old_nodes:
        remaining_text = node.text
        link_label_url = extract_markdown_links(remaining_text)
        if len(link_label_url) == 0:
            final_node_list.append(node)
            continue
        for i in range(len(link_label_url)):
            sections = list(remaining_text.split(f"[{link_label_url[i][0]}]({link_label_url[i][1]})", 1))
            if sections[0] != "":
                final_node_list.append(TextNode(sections[0], TextType.TEXT))
            final_node_list.append(TextNode(link_label_url[i][0], TextType.LINK, link_label_url[i][1]))
            remaining_text = sections[1]
        if remaining_text != "":
            final_node_list.append(TextNode(remaining_text, TextType.TEXT))
    return final_node_list


def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    bold_list = split_nodes_delimiter(node, "**", TextType.BOLD)
    italic_list = split_nodes_delimiter(bold_list, "*", TextType.ITALIC)
    code_list = split_nodes_delimiter(italic_list, "`", TextType.CODE)
    images_list = split_nodes_image(code_list)
    final_node_list = split_nodes_link(images_list)
    return final_node_list
      