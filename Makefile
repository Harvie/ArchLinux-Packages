help:
	#
	#	usage:
	# - make clean
	#
clean:
	rm -rfv */pkg/
	rm -rfv */src/
	find . -regextype egrep -iregex '.*\.(part|tar|gz|xz|bz|bz2|tgz|zip|rar)$$' -print0 | xargs -0 rm -fv
