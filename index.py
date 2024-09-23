from fasthtml.common import *
from fastcore.foundation import *
from pathlib import Path

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )

app, rt = fast_app(hdrs=hdrs)

from mone27.home import *
from mone27.core import *


@rt('/')
def get(req):
    blogs = get_blogs()
    return Titled("Mone's Blog",
        H2("Welcome to my blog!"),
        P("This is the first draft of my blog project implemented using FastHTML."),
        Div(*[blog_box(title, content) for title, content in blogs],
            style = "display: flex; gap: 1em; flex-wrap: wrap;"    
        )
    )

@rt('/{blog_slug}')
def get(blog_slug: str):
    blog = get_blogs().filter(lambda x: x[0] == blog_slug)
    if blog:
        title, content = blog[0]
        return Title(title), Container(Markdown(content))
    else:
        return Titled("Not Found", P(blog_slug))


serve()