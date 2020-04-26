#!/bin/bash
Write-Output "To Do PoC App Release"
Write-Output "Note that this script may be system specific, so verify its contents in case of an error"
$VALID = read-host "Do you have latest version of setuptools, wheel and twine installed? Y (yes) / N (no)"
if ($VALID -eq "Y" -OR $VALID -eq "y")
{
    Set-Location .\todopoc
    $CLEAN = read-host "Do you want to clean the directories ('build' and 'dist') before installation? Y (yes) / N (no)"
    if ($CLEAN -eq "Y" -OR $CLEAN -eq "y")
    {
        Remove-Item .\build -Force -Recurse
        Remove-Item .\dist -Force -Recurse
    }
    Write-Output "Starting the packaging"
    python setup.py sdist bdist_wheel
    if ($?)
    {
        $UPLOAD = read-host "Do you want to upload the build? Y (yes) / N (no)"
        if ($UPLOAD -eq "Y" -OR $UPLOAD -eq "y")
        {
            twine upload dist/*
            if ($?)
            {
                Write-Output "Package seems to have successfully uploaded"
            }
            else
            {
                Write-Output "There might have been an error. Did you check the version numbering?"
            }
        }
    }
    else
    {
        Write-Output "There might have been an error"
    }
    Set-Location ..
}
else
{
    Write-Output "run 'python3 -m pip install --user --upgrade setuptools wheel' and then try again"
}