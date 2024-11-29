

def markdown_to_blocks(markdown_string):
    block_markdown = markdown_string.split("\n\n")
    final_blocks = []
    for i in range(len(block_markdown)):
        if block_markdown[i] == "":
            continue
        final_blocks.append(block_markdown[i].strip(" "))
    return final_blocks
    
def block_to_block_type(block):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    elif len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    elif block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    elif block.startswith(("* ", "- ")):
        for line in lines:
            if not line.startswith(("* ", "- ")):
                return "paragraph"
        return "unordered list"
    elif block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered list"
    else:
        return "paragraph"
