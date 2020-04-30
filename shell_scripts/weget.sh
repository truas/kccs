#WGET
#get mensa page
wget https://www.seezeit.com/essen/speiseplaene/menseria-giessberg/?no_cache=1 -O index


#get the current and next day:
# the $() are important to run the command and save the result in the variable.
day=$(date +"%u")
    #Alternative
    day=`date +"%u"`
    
day2=`expr $day + 1`
    #Alternative
    day2=$(expr $day + 1)
echo "Current day: "$day
echo "Next day: " $day2

#filter for the correct page
sed -n "/id=\"tab$day\"/,/id=\"tab$day2\"/p" index |
sed -rn 's/((.*\"category\">)(.*)(<.*))|(.*class=\"title\">)(.*)(<\/div>)/\3-\6-/gpi'|
sed 's/<sup[^ ]*sup>//g'