#! /bin/sh
#
#
# exercise 2a
MASTER=MasterList

# exercise 5a
GENMASTER="no"

# exercise 5d
DELMASTER="no"

NAMMASTER="no"

# exercise 3a
TMP=/tmp/$$
> $TMP

# exercise 5b
for i in $@
do
	case "$i" in
	-m*)	TEMPNAME=`expr "$i" : '-m\(.*\)'`
		if [ -z "$TEMPNAME" ]
		then
			 NAMMASTER=yes
		else
			MASTER="$TEMPNAME"
		fi		;;
	-g)	GENMASTER=yes	;;
	# next two lines are for exercise 5e
	-d)	DELMASTER=yes	;;
	*)	if [ "$NAMMASTER" = yes ]
		then
			MASTER="$i"
			NAMMASTER=no
		else
			echo "Unknown option $i" 1>&2
			exit 1
		fi		;;
	esac
done

if [ "$NAMMASTER" = yes ]
then
	echo "You gave the -m option but no file name" 1>&2
	exit 1
fi

#
# sanity check: only one of -d, -g
# exercise 5g
if [ "$DELMASTER" = 'yes' -a "$GENMASTER" = 'yes' ]
then
        echo "Only one of -d, -g allowed" 1>&2
        exit 1
fi


#
# if delete master, do so and exit
# exercise 5f
if [ "$DELMASTER" = 'yes' ]
then
        if [ -e "$MASTER" ]
        then
                rm "$MASTER"
                exit 0
        else
                echo "Master file does not xist; please generate it" 1>&2
                exit 1
        fi
fi

if [ "$GENMASTER"x = yesx ]
then
	if [ -e "$MASTER" ]
	then
        	echo "$MASTER exists; please delete it" 1>&2
        	exit 1
	else
        	> "$MASTER"
	fi
	#
	for i in *
	do
        	if [ ! -f "$i" -o "$i"x = "$MASTER"x ]
        	then
                	continue
        	fi
        	echo `ls -sail "$i"` `shasum "$i"` >> "$MASTER"
	done
	exit 0
fi

# exercise 3e
if [ ! -f "$MASTER" ]
then
	echo "Master file does not exist; please generate it" 1>&2
	exit 1
fi

for i in *
do
	# exercise 3b
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
