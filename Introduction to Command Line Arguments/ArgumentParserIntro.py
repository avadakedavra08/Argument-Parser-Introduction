import argparse
import os

# os.getcwd() -> To get the current working directory.
print(os.getcwd())

# os.listdir() -> To get the list of the files in the current directory as
# the  name of files in the form of strings.
print(os.listdir())

# Instantiating ArgumentParser object as ap.
# So, "ap" is basically the object of ArgumentParser() class in argparse package
ap = argparse.ArgumentParser()

# Versions to be used in command lines.
ap.add_argument("-n","--name",required = True,help="Name of the User")

# -n -> Shorthand versions
# --name -> Longhand versions
# required = True -> This is a compulsory required argument.
# help -> Additional information in the terminal if required.
# Both of these flags can be used in command line.


# This particular line instructs Python and the argparse to
# parse the command line arguments into a Python dictionary where the key
# to the dictionary is the name of the command line argument and
# the value is value of the dictionary supplied for the command line argument.
args = vars(ap.parse_args())
print("Argument Parser Object :",args)

# args["name"] receiving the command line argument as entered by the user.
print("Hello from the other side, {}".format(args["name"]))
