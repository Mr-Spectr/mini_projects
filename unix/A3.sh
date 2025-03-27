#!/bin/sh

ps
echo "ps : process status"

ps -f
echo "ps -f : full listing process status"

ps -l
echo "ps -l : long listing process status with memory related info"

ps -u
echo "ps -u :  user process stauts"

ps -e
echo "ps :  all process status including user and system"

ps -a
echo "ps : process of all user including thone not listed"

ps -t
echo "ps : process running on terminal -l along memory related"


