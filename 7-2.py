# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating
# point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
count = 0
count = int(count)
total = 0.0
total = float(total)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
 #   print line
    total = total + float(line[line.find(' '):])
    count = count + 1

print("Average spam confidence:", total/count)
