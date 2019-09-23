import distutils.dir_util			# for copying trees
import os											# for env vars
import stat										# for file stats
import subprocess							# do stuff at the shell level
from resources.ci.common import common
from shutil import copy, make_archive, move, rmtree	# file manipulation

env = common.prepare_env()

# make dir to put the binary in
if not os.path.isdir("../artifact"):
	os.mkdir("../artifact")

BUILD_FILENAME = ""

# list executables
BUILD_FILENAME = common.find_binary('.')

DEST_FILENAME = common.prepare_filename(BUILD_FILENAME)

print("OS Name:        " + env["OS_NAME"])
print("OS Version:     " + env["OS_VERSION"])
print("Build Filename: " + BUILD_FILENAME)
print("Dest Filename:  " + DEST_FILENAME)
if not BUILD_FILENAME == "":
	print("Build Filesize: " + common.file_size(BUILD_FILENAME))

if not BUILD_FILENAME == "":
	move(
		BUILD_FILENAME,
		"../artifact/" + BUILD_FILENAME
	)
