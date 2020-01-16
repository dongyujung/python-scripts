

expression | matches
---|---
\d | Any digit (0-9)
\D | 
. | Any single character
[abc] | Matching specific characters
[^abc] | Excluding specific characters
[0-6], [^n-p] | Character ranges
\w | Alphanumeric
a{m} | m repetitions
a{m,n} | m to n repetitions
a+ | 1 or more repetitions (Kleene Plus)
a* | 0 or more repetitions (Kleene Star)
a? | Optionality: 0 or 1
' ' | Space
\t | Tab
\n | New line
\s | Any whitespace
\S | Any non-whitespace
^a | Starts with
a$ | Ends with
(a)bc | Extract part: a
(a(bc)) | Capture sub-group: abc, bc
.* | Capture all
pipe | Or 

^... different from [^...]  

Match | Skip | Regex
---|---|---
can, man, fan | dan, ran, pan | [cmf]an
hog, dog | bog | [^b]og
Ana, Bob, Cpc | aaz, bby, ccz | [A-C][n-p][a-c]
wawzzzzzup, wazzzup | wazup | waz{3,5}up
aaaabcc, aabbbbc, aacc | a | a+b*c+
1 file found?, 2 files found?, 24 files found? | No files found. |  \d+ files? found\?
' abc', '  abc', '  abc' | 'abc' | \s+abc   
Mission: successful | Last Mission: unsuccessful, Next Mission: successful upon capture of target | ^Mission
file_record_transcript.pdf, file_07241999.pdf | testfile_fake.pdf.tmp | (^file_.*).pdf$
Jan 1987, May 1969, Aug 2011 | | (\D{3} (\d{4})) gives Jan 1987, 1987
I love cats, I love dogs | I love logs, I love cogs | I love (cats pipe dogs)

