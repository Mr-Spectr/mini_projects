#!/bin/sh

a=2
b=4
c=19

val=`expr $a + $b`
echo "Sum = $val"

val=`expr $a - $b`
echo "Diff = $val"

val=`expr $a \* $b`
echo "Mul = $val"

val=`expr $a / $b`
echo "Quotient = $val"

val=`expr $a % $b`
echo "Mod = $val"

if [ $a -eq $b ]
then
echo "a is equal to b"
else
echo "a is not equa to b"
fi

if [ $a -ne $c ]
then
echo "a is not equal to c"
else
echo "a is equal to c"
fi

if [ $a -gt 1 -o $b -lt 5 ]
then
echo "True"
else
echo "False"
fi

if [ $b -lt 5 -a $c -gt 5 ]
then 
echo "True"
else
echo "False"
fi 
