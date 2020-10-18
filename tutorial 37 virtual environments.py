# okay so today we will learn about virtual environments
#
# virtual environment--  a copy or clone of a python compiler which will remain in it's state
#                        till the time we code in ti so when we open a file 50 years later
#                        then we will not face any update problem if we will code in this python
#
# STEPS---
# 1> create a file in which we want the new compiler
#
# 2> press> shift+right click
#
# 3> choose powershell
#  but first go in powershell admin and run the following code
#  """"""set-executionpolicy remotesigned""""""
# after that press Y
#
# 4>install virtual environment by the code
#  pip install virtualenv
#
# 5> now create a compiler like this
#  virtualenv virtualenv_name
#
# 6>then activate it with the code
# .\virtualenv_name\Scripts\activate
#
# 7> we can even uninstall it with the code
# (virtualenv_name) deactivate
#
# 8>go in python with code
#     python
#
# 9>here this new python compiler will have no modules so we will have to  instal them with code
#     pip install 'module name'
#
# 10>we can uninstall  a module with code
#     pip uninstall 'module name'
#
# 11> so suppose we made a app and someone used it after 30 years but then after due to
# some updates in a module maybe 'pandas' then it will not run so we keep a list of all
# modules with version name and module names called requirements so we can paas it to the
# user in a file name requirements and freeze it and create a file named requirements by the
# code--
#       pip freeze>requirements.txt
#
# 12> the user will now able to install python and install all the module names using
# requirements file and install then in it
#
# 13> but suppose there are millions of modules and the new user wants to install all
# the modules so  the user will take a loot of time and trouble so we will use the code
# pip install - r .\requirements.txt
#
#
# ***OKEY SO CONSIDER WE WANT TO CREATE A VIRTUAL ENVIRONMENT WHICH HAVE ALL THE SIDE PACKAGES
# OF THE PYTHON IN THE COMPUTER THEN WE WILL MAKE THE CODE USING CODE
# virtualenv--system-site-packages 'name'
