#!/usr/bin/awk -f
BEGIN {
	RS="\r\n" 
	LIGNE=1
	getline entete
	where = match(entete, /^WEBVTT$/)
	if (where) {
		# sauter la ligne suivante également
		getline
	} else {
		print FILENAME, "mauvaise entête WEBVTT" > "/dev/stderr"
		exit 1
	}
}
/^[0-9][0-9]:[0-9][0-9]:/ {
	gsub(/\./, ",", $0)
	print LIGNE 
	LIGNE++ 
}
{
	print $0
}
