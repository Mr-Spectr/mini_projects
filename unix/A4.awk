#!/bin/awk -f

BEGIN{print "START"}
{print $1, "\t", $2}
END{print "END"}
