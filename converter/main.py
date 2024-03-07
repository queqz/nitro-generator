with open("in.txt", "r") as input_file:
    with open("out.txt", "w") as output_file:
        for line in input_file:
            modified_line = "https://" + line.strip()
            output_file.write(modified_line + "\n")
