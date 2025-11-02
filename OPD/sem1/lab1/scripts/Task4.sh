cd lab0
wc -m * */* */*/* */*/*/* | grep "e$" | sort -nr
grep -rl "man" 2>/tmp/a | xargs ls -ltr 2>/tmp/a | head -3 
cat -n t* */t* */*/t* */*/*/t* | sort -r -k 2
ls -lR | grep "^-" | grep -v ":$" | grep ' s.* s.* s' | sort -k5 -nr | tail -4
ls -luR 2>/tmp/a | grep "^-" | grep -v ":$" | grep "0$"
grep -rl "me" 2>/tmp/a | xargs ls -lt 2>/tmp/a | tail -2 
