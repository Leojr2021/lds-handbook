import os

def join_markdown_files(input_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(input_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(input_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n\n')  # Add a newline between files

input_directory = './handbook'  # Replace with your directory path
output_filename = 'combined_output.md'  # Replace with your desired output file name

join_markdown_files(input_directory, output_filename)