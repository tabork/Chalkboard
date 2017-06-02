
for PHOTO in guibak/*
do
	BASE=`basename $PHOTO`
	convert -strip "$PHOTO" "gui/$BASE"
done
