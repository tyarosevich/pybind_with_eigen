So this is the template I've found to be the most useful, since it has a basic project structure and bundles the python extension up in an importable library. The build is handled by the setup.py file and pybind, though I can't recall if it's using Cmake under the hood, but it did build just fine on this system. 

##### 4/4/24 #####
 - Adjusted to split functionality into multiple source cpp files. Interestingly, pybind handles inclusion no problem, just have to declare the functions appropriately.

 - Still unclear to me how to specify a particular build process using setup.py. Presumably there is a way to do it with a makefile somewhere, but right now it just searches
 - for the highest VC standard available.