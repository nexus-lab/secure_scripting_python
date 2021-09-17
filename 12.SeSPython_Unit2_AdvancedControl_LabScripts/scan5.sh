#! /bin/sh
#
# -m<name>: master file is named <name>
# -g: generate master list of files in this directory
# -d: delete existing master
# no option: do comparison if master exists, otherwise generate it
#
MASTER=MasterList
DELMASTER=no
GENMASTER=no
#
# process argument list
#
for i in "$@":
do
	case "$i" in
	-d)	DELMASTER=yes	;;
	-g)	GENMASTER=yes	;;
	*)	echo "Unknown option $i" 1>&2
		exit 1
				;;
	esac
done
#
# sanity check: only one of -d, -g
#
if [ "$DELMASTER" = 'yes' -a "$GENMASTER" = 'yes' ]
then
	echo "Only one of -d, -g allowed" 1>&2
	exit 1
fi
#
# if delete master, do so and exit
#
if [ "$DELMASTER" = 'yes' ]
then
	rm "$MASTER"
	exit 0
fi
#
# if generating master, do so
#
if [ "$GENMASTER" = 'yes' ]
then
	if [ -e $"$MASTER" ]
	then
		echo "$MASTER exists; please delete it"
		exit 1
	else
		>$MASTER
		for i in *
		do
			if [ "$i" = "$MASTER" -o ! -f "$i" ]
			then
				continue
			fi
			echo `ls -sail "$i"` `shasum $i` >> $MASTER
		done
		exit 0
	fi
fi
#
# okay, it's just a check
#
TMP=/tmp/$$
#
>$TMP
for i in *
do
	if [ "$i" = "$MASTER" -o ! -f "$i" ]
	then
		continue
	fi
	echo `ls -sail "$i"` `shasum $i` >> $TMP
done
diff "$MASTER" $TMP | grep '^\(<\|>\)' | awk '{ print "\t", $NF }' | sort | uniq
rm $TMP
