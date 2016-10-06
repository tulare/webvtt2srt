# setup.py
from distutils.core import setup
import py2exe

setup(
	console=["conv2srt.py"],
	zipfile=None,
	options={
		"py2exe":{
			"bundle_files": 1,
			"compressed": True
		}
	}
)