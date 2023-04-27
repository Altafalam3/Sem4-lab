#using grep 

echo -n "No of lines: "
echo `grep -c "" $filepath`

echo -n "No of words: "
echo `grep -o '\w*' $filepath | wc -w`

echo -n "No of Characters: "
echo `grep -o . $filepath | wc -l`
