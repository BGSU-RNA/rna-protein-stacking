#!/usr/bin/env python

from jinja2 import Template


def get_stacking(filename):
    """Load the stacking interactions from a file.

    :filename: The filename to read.
    :returns: A list of the stacking interactions.
    """
    return [{'nt': '3V2F|1|A|A|6 ', 'aa': '3V2F|1|A|U|2897'}]


def main(input_file, output_file, template_file='templates/interactions.html'):
    """The main entry point for this script.

    :input_file: The input filename for the interactions.
    :output_file: The filename to write the interactions HTML to.
    """

    interactions = get_stacking(input_file)

    with open(template_file, 'rb') as raw:
        template = Template(raw.read())

    with open(output_file, 'wb') as out:
        out.write(template.render(interactions=interactions))


if __name__ == '__main__':
    input_file = None
    output_file = 'interactions.html'
    main(input_file, output_file)
