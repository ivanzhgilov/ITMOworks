mkdir lab0
cd lab0
mkdir caterpie5
cd caterpie5
echo -e "Ходы\tBlock Drain Punch Fire Punch Helping Hand Ice Punch\nKnock Off Low Kick Sleep Talk Snore Superpower\nThunderpunch" >> gurdurr
mkdir meganium
echo -e "Ходы\tDark Pulse Dragon Pulse Drain Punch Dual\nChop Fire Punch Foul Play Ice Punch Iron Defense Iron Head Iron Tail\nKnock Off Low Kick Outrage Sleep Talk Snatch Snore Spite Super Fang\nThunderpunch Zen Headbutt" >> scrafty
mkdir pupitar
cd ..
mkdir manectric0
cd manectric0
echo -e "weigth=59.5 height=67.0 atk=10\ndef=11" >> huntail
echo -e "Тип покемона\tSTEEL GROUND" >> steelix
mkdir vileplume numel mankey
echo -e "Тип покемона\nWater Ground" >> seismitoad
cd ..
echo -e "Ходы\tBug Bite Electroweb Iron Defense String\nShot" >> silcoon2
mkdir torterra6
cd torterra6
mkdir seedot guagsire ekans
cd ..
echo -e "Тип покемона\tGROUND NONE" >> trapinch1
echo -e "Способности\nPetal Dance Solarbeam" >> vileplume0
cd caterpie5
chmod 400 gurdurr
chmod u=rwx,g=rw,o=r meganium
chmod 664 scrafty
chmod 771 pupitar
cd ..
cd manectric0
chmod 644 huntail
chmod u=r,go=- steelix
chmod u=rw,g=w,o=- seismitoad
chmod ug=wx,o=rx vileplume
chmod a=wx mankey
chmod u=rx,g=rwx,o=rw numel
cd ..
cd torterra6
chmod u=rx,g=rwx,o=wx seedot
chmod u=wx,g=wx,o=rx guagsire
chmod 750 ekans
cd ..
chmod 551 caterpie5
chmod u=rx,g=x,o=wx manectric0
chmod 361 torterra6
chmod 640 silcoon2
chmod 666 trapinch1
chmod 644 vileplume0
chmod 713 manectric0
cp trapinch1 ./manectric0/seismitoadtrapinch
ln /lab0/silcoon2 ./manectric0/huntailsilcoon
chmod u=rx,g=x,o=wx manectric0
ln -s ./caterpie5 ./Copy_52
cat ./manectric0/steelix ./caterpie5/gurdurr > ./vileplume0_80
chmod 751 caterpie5
cp -r caterpie5 ./caterpie5/meganium
ln -s ../silcoon2 ./caterpie5/scraftysilcoon
chmod 551 caterpie5
cp trapinch1 ./manectric0/vileplume
wc -m * */* */*/* */*/*/* | grep "e$" | sort -nr
grep -rl "man" 2>/tmp/a | xargs ls -ltr 2>/tmp/a | head -3 
cat -n t* */t* */*/t* */*/*/t* | sort -r -k 2
ls -lR | grep "^-" | grep -v ":$" | grep ' s.* s.* s' | sort -k5 -nr | tail -4
ls -luR 2>/tmp/a | grep "^-" | grep -v ":$" | grep "0$"
grep -rl "me" 2>/tmp/a | xargs ls -lt 2>/tmp/a | tail -2 
rm trapinch1
chmod 777 ./caterpie5
rm ./caterpie5/scrafty
rm ./caterpie5/scraftysilco*
rmdir ./caterpie5/pupitar/
chmod 777 ./caterpie5/gurdurr ./caterpie5/meganium/caterpie5/gurdurr
rm -r caterpie5/
chmod 777 manectric0/
rm ./manectric0/huntailsilco*
chmod u=rx,g=x,o=wx manectric0