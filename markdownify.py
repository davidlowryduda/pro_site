import markdown
import sys


def convert_file(fname):
    md = markdown.Markdown(extensions=['extra'], tab_length=2)
    with open(fname, "r") as f:
        content = ''.join(f.readlines())
    return md.convert(content)


def main():
    output = []
    for fname in sys.argv[1:]:
        output.append(convert_file(fname))
    return '\n'.join(output)


if __name__ == "__main__":
    print(main())
