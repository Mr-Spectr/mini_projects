#!/bin/sh

f="t.txt"

if [ -r $f ]
then
echo "Read permission"
else
echo "Not have read permission"
fi

if [ -w $f ]
then
echo "Write permission"
else
echo "Not have write permission"
fi

if [ -x $f ]
then
echo "Execute permission"
else
echo "Not have execute permission"
fi

if [ -f $f ]
then
echo "Oedinary file "
else
echo "Not ordinary"
fi

if [ -d $f ]
then
echo " File is a directory"
else
echo "file is not directory"
fi

if [ -b $f ]
then
echo " File is a block"
else
echo "File is not a block"
fi

if [ -e $f ]
then
echo " File exist"
else
echo " File not exixt"
fi

if [ -c $f ]
then
echo " File is a character"
else
echo " File is not a acharacter"
fi

