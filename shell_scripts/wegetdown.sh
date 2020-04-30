wget -p http://pudim.com.br/
wget -o download.log http://pudim.com.br/
# The -p or --page-requisite option causes wget to fetch all files
#+ required to display the specified page.

wget -r https://news.google.com/?hl=en-US&gl=US&ceid=US:en -O $SAVEFILE
# The -r option recursively follows and retrieves all links
#+ on the specified site.

wget -c ftp://ftp.xyz25.net/bozofiles/filename.tar.bz2
# The -c option lets wget resume an interrupted download.
# This works with ftp servers and many HTTP sites.
