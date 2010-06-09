help:
	#
	#	usage:
	# - make clean
	#
clean:
	rm -rf */pkg/
	rm -rf */src/
	find . -regextype egrep -iregex '.*\.(part|gz|xz|bz|bz2|zip|rar)$$' -print0 | xargs -0 rm -f
