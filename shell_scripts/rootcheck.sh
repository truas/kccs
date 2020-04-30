if [ "$(whoami)" != 'root' ]; then
printf "You are not the root \n"$0" is not for you.\n"
exit 1;
fi
