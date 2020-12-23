from datetime import date
import textwrap


working_essay_file = open("working_essay.txt", "r")
lines = filter(None, (line.rstrip() for line in working_essay_file))


def today_to_meta_text():
# Formats date to display on site e.g. 22 Dec 2020

    meta_text = date.today().strftime("%d %B %Y")
    meta_text = meta_text.split()
    meta_text = meta_text[0] + " " + meta_text[1][:3] + " " + meta_text[2]

    return meta_text


def line_to_paragraph(line):
# Takes in raw lines, surrounds them with <p></p> 
# adds <br> at the end of each line and turns
# them into paragraphs so that html looks nice

    # processed_line = line.replace("\n", "")
    # processed_line = textwrap.wrap(processed_line, 70)

    # [wrapped_line + "\n" for wrapped_line in processed_line]
    
    # paragraph_output = "".join(processed_line)
    line = "\t\t<p>\n\t\t\t" + line + "\n\t\t</p>\n"

    return line


def lines_to_formatted(input_lines):
  
    formatted_output = ""

    for line in input_lines:
        
        processed_paragraph = line_to_paragraph(line)
        processed_paragraph = "".join(processed_paragraph)
        formatted_output = formatted_output + processed_paragraph + "\n"

    return formatted_output


def formatted_to_essay(essay_title, essay_address, essay_main_text, essay_meta_text):

    with open("essays/empty.html", "r") as empty_essay_file:
        empty_essay_data = empty_essay_file.read()

    final_essay_data = empty_essay_data.replace("ESSAY_TITLE", essay_title)
    final_essay_data = final_essay_data.replace("ESSAY_MAIN_TEXT", essay_main_text)
    final_essay_data = final_essay_data.replace("ESSAY_META_TEXT", essay_meta_text)

    with open("essays/" + essay_address + ".html", "w") as final_essay_file:
        final_essay_file.write(final_essay_data)


def link_to_essay(essay_title, essay_address):

    line_to_add_new_essay_link = 0
    link_to_essay_html = "\t\t<a href=\"essays/" + \
                          essay_address + \
                          ".html\">" + \
                          essay_title + \
                          "</a><br>\n"

    with open("essays.html", "r") as essay_links_file:
        essay_links_data = essay_links_file.readlines()

    for i, line in enumerate(essay_links_data):
        if "essays_list" in line:
            line_to_add_new_essay_link = i+1
            essay_links_data.insert(line_to_add_new_essay_link, link_to_essay_html)
    
    essay_links_data = "".join(essay_links_data)
    with open("essays.html", "w") as modified_essays_file:
        modified_essays_file.write(essay_links_data)


essay_title = input("What's the essay's title?: ")
essay_address = input("What's the essay's address?: ")

formatted_to_essay(essay_title,
                   essay_address,
                   lines_to_formatted(lines),
                   today_to_meta_text())

link_to_essay(essay_title, essay_address)

print("Done! Your blogpost is available here:\n http://vanjaknezevic.com/essays/" + essay_address + ".html")