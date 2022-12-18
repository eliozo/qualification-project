# from mistletoe import Document, HTMLRenderer
import mistletoe
import mistletoe.ast_renderer

file_path = "out.json"

with open('content.md', 'r', encoding='utf-8') as fin:
    with mistletoe.ast_renderer.ASTRenderer() as renderer:     # or: `with HTMLRenderer(AnotherToken1, AnotherToken2) as renderer:`
        doc = mistletoe.Document(fin)              # parse the lines into AST
        rendered = renderer.render(doc)  # render the AST
        # internal lists of tokens to be parsed are automatically reset when exiting this `with` block
        out_file = open(file_path, "w", encoding='utf-8')
        out_file.write(rendered)
        out_file.close()