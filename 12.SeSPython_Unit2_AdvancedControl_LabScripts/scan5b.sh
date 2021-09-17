#! /bin/sh
#
#
# exercise 2a
MASTER=MasterList

# exercise 5a
GENMASTER="no"

# exercise 3a
TMP=/tmp/$$
> $TMP

# exercise 3e
if [ ! -f "$MASTER" ]
then
	echo "Master file does not exist; please generate it" 1>&2
	exit 1
fi

# exercise 5b
for i in "$@"
do
	case "$i" in
	-g)	GENMASTER=yes	;;
	esac
done

for i in *
do
	# exercise 3c
	if [ "$i" = "$TMP" ]
	then
		continue
	fi
	# exercise 2c
	if [ "$i" = "$MASTER" -o ! -f "$i" ]
	then
		continue
	fi
	# exercise 3c
	echo `ls -sail "$i"` `shasum "$i"` >> $TMP
done

# exercise 3d, with the modification given in exercise 4
echo "Changed files:"
diff "$MASTER" "$TMP" | grep '^\(<\|>\)' | awk '{ print $NF }' | sort | uniq
# exercise 3f
rm $TMP
exit 0
