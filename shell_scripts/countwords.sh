num=`wc -l < /usr/share/dict/words`

echo The number of words in this file is $num

if [ "$num" -gt "10" ]
then 
	echo ; 
	echo "Too many words!"
	echo "Go to sleep"; 
fi
