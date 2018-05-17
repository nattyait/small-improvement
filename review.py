import re, os
print
print ("-- Welcome to Small Improvement Reformat ---")
print ("Below is the list of file in this directory. Please choose the original file.")
print
for item in os.listdir('.'):
	print ("- " + item)

print
print ("Type the filename again:")
filename = raw_input("> ")

txt = open(filename)

txt = txt.read()
txt = re.sub(r"Answered by \d* out of \d*", "", txt)
txt = re.sub(r"No answer provided.", "", txt)
txt = re.sub(r"No one selected this", "", txt)
txt = re.sub(r"\d* people selected this", "", txt)
txt = re.sub(r"1 person selected this", "", txt)
txt = re.sub(r"\nSomewhat committed\n(\d*%)", r"Somewhat committed \1", txt)
txt = re.sub(r"\nGood commitment\n(\d*%)", r"Good commitment \1", txt)
txt = re.sub(r"\nVery committed\n(\d*%)", r"Very committed \1", txt)
txt = re.sub(r"\nCould improve a little\n(\d*%)", r"Could improve a little \1", txt)
txt = re.sub(r"\nA good example\n(\d*%)", r"A good example \1", txt)
txt = re.sub(r"\nAn exceptional example\n(\d*%)", r"An exceptional example \1", txt)
txt = re.sub(r"Additional thoughts or feedback:\n*", r"Additional thoughts or feedback:\n\n", txt)
txt = re.sub(r"Additional thoughts and feedback:\n*", r"Additional thoughts and feedback:\n\n", txt)
txt = re.sub(r"\n*General Feedback", r"\n\nGeneral Feedback", txt)
txt = re.sub(r"\n*Pronto Values - Part (\d*)", r"\n\nPronto Values - Part \1", txt)
txt = re.sub(r"\n\n\n\n", r"\n\n", txt)
text_file = open("new_"+filename, "w")
text_file.write(txt)
text_file.close()
print
print ("Your new file is generated: " + text_file.name)
print
