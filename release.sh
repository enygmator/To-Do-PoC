#!/bin/bash
echo "To Do PoC App Release"
echo "Note that this script may be system specific, so verify its contents in case of an error"
echo "Do you have latest version of setuptools, wheel and twine installed? Y (yes) / N (no)"
read VALID
if [ $VALID == "Y" -o $VALID == "y" ]
then
    cd todopoc
    echo "Do you want to clean the directories ('build' and 'dist') before installation? Y (yes) / N (no)"
    read CLEAN
    if [ $CLEAN == "Y" -o $CLEAN == "y" ]
    then
        rm -rf build
        rm -rf dist
    fi
    echo "Starting the packaging"
    python3 setup.py sdist bdist_wheel
    if [ $? ]
    then
        echo "Do you want to upload the build? Y (yes) / N (no)"
        read UPLOAD
        if [ $UPLOAD == "Y" -o $UPLOAD == "y" ]
        then
            python3 -m twine upload dist/*
            if [ $? ]
            then
                echo "Package seems to have successfully uploaded"
            else
                echo "There might have been an error. Did you check the version numbering?"
            fi
        fi
    else
        echo "There might have been an error"
    fi
    cd ..
else
    echo "run 'python3 -m pip install --user --upgrade setuptools wheel' and then try again"
fi