import os
import imp

util = imp.load_source("_util", os.path.realpath(os.path.join(__file__, "..", "..", "_util.py")))
util.wrap_module(__name__)