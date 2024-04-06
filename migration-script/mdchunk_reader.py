import re
import markdown


def extract_problem(text):
    problem_text = []
    lines = text.split('\n')
    for line in lines:
        if line.startswith('# '):
            continue
        elif re.fullmatch(r'^\s*<small>\s*', line) or re.fullmatch(r'## .*', line):
            break
        else:
            problem_text.append(line)
    return '\n'.join(problem_text)

def extract_metadata(text):
    metadata = dict()
    lines = text.split('\n')
    meta_opened = False
    for line in lines:
        if re.fullmatch(r'\s*<small>\s*'):
            meta_opened = True






# Read problems one by one from Markdown file "filepath"
def extract_sections_from_md(filepath):
    section_titles = []
    current_section = None
    sections = []
    title = "NA"

    heading_re = re.compile(r'^#\s+<lo-sample/>\s+(.*)')

    with open(filepath, 'r') as file:
        for line in file:
            m = heading_re.match(line)
            if m:
                new_title = m.group(1)
                # append the previous (title, current_section)
                if current_section is not None:
                    sections.append((title, current_section))
                    # print(f"Appending {title}")
                title = new_title
                current_section = line
            elif current_section is not None:
                # before seeing the first title, we do not append anything
                current_section += line
    # Append the last (title, current_section)
    if current_section:
        sections.append((title, current_section))
        # print(f"Appending last {title}")
    return sections


def main():
    file_path = 'resources/LV-AMO-lv-amo-2023.md'
    sections = extract_sections_from_md(file_path)

    for i, (title,section) in enumerate(sections):
        the_html = markdown.markdown(extract_problem(section))
        print(f"Section {i + 1}:{title}:\n{the_html}\n{'=' * 50}\n")


if __name__ == '__main__':
    main()

