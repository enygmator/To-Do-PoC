#!/bin/bash
echo "To Do PoC App Installer"
echo "Do you have python3 and pip3 installed? Y (yes) / N (no)"
read VALID
if [ $VALID == "Y" -o $VALID == "y" ]
then
    echo "What do you want to do?"
    select CHOICE in "install" "uninstall"
    do
    case $CHOICE in
        "install")
            echo "Do you want to install in Development mode? Y (yes) / N (no)"
            read DEV
            if [ $DEV == "Y" -o $DEV == "y" ]
            then    
                pip3 install -e ./todopoc
            else
                pip3 install ./todopoc
            fi
            if [ $? ]
            then
                echo "App has been installed"
            else
                echo "There was some error"
            fi
            break
        ;;
        "uninstall")
            pip3 uninstall todopoc
            if [ $? ]
            then
                echo "App has been uninstalled"
            else
                echo "There was some error"
            fi
            break
        ;;
    esac
    done
else
    echo "Install python and pip and then try again"
fi