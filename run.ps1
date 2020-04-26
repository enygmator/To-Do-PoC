#!/bin/bash
Write-Output "To Do PoC App Installer"
Write-Output "Note that this script may be system specific, so verify its contents in case of an error"
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
                Write-Output "App has been installed"
            }
            else
            {
                Write-Output "There was some error"
            }
            break
        }
        "u" {} "U"
        {
            pip3 uninstall todopoc
            if ( $? )
            {
                Write-Output "App has been uninstalled"
            }
            else
            {
                Write-Output "There was some error"
            }
            break
        }
    }
}
else
{
    Write-Output "Install python and pip and then try again"
}