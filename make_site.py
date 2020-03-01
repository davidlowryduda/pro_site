import jinja2
import markdown


def convert_file(fname):
    """
    Convert markdown file `fname` to html. Returns html string.
    """
    md = markdown.Markdown(extensions=['extra'], tab_length=2)
    with open(fname, "r") as f:
        content = ''.join(f.readlines())
    return md.convert(content)

INDEX_FILES = [
    'personal.markdown',
    'travel.markdown',
    'education.markdown',
    'publications.markdown',
    'teaching-classes.markdown',
    'teaching-students.markdown',
    'programming-projects.markdown',
    'talks.markdown',
    'service.markdown',
    'programming-service.markdown',
]
INDEX_TITLE = ""

def make_index():
    env = jinja2.Environment(loader=jinja2.loaders.FileSystemLoader('templates/'))
    template = env.get_template("index.html.jinja")

    content=[]
    for sourcefile in INDEX_FILES:
        fname = "markdown/" + sourcefile
        content.append(convert_file(fname))
    content_string = '\n'.join(content)

    with open("index.html", "w") as indexfile:
        indexfile.write(template.render(title=INDEX_TITLE, stuff=content_string))


def make_main_pages():
    make_index()
    #make_research
    #make_teaching
    #make_programming


def main():
    make_main_pages()


if __name__ == "__main__":
    main()
