#!/bin/bash
echo "To Do PoC App Installer"
$VALID = read-host "Do you have python3 and pip3 installed? Y (yes) / N (no)"
if ($VALID -eq "Y" -OR $VALID -eq "y")
{
    $CHOICE = read-host "What do you want to do? install [I] / uninstall [U]"
    switch ($CHOICE) {
        "I" {} "i"
        {
            $DEV = read-host "Do you want to install in Development mode? Y (yes) / N (no)"
            if ( $DEV -eq "Y" -OR $DEV -eq "y" )
            {
                pip3 install -e ./todopoc
            }
            else
            {
                pip3 install ./todopoc
            }
            if ( $? )
            {
                echo "App has been installed"
            }
            else
            {
                echo "There was some error"
            }
            break
        }
        "u" {} "U"
        {
            pip3 uninstall todopoc
            if ( $? )
            {
                echo "App has been uninstalled"
            }
            else
            {
                echo "There was some error"
            }
            break
        }
    }
}
else
{
    echo "Install python and pip and then try again"
}