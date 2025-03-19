import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nnimpit/ros2_tutorial/install/bumperbot_py_examples'
