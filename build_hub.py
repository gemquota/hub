import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from hub_builder import build_index, build_project_pages
# Just import and run
sys.path.insert(0, '.')
