<<<<<<< HEAD
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jobbole"])

# sys.path.append()
=======
import os
import sys
from scrapy.cmdline import execute

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))

#把工程目录添加到sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#执行scrapy中的execute()命令,传进去参数列表
execute(["scrapy","crawl","jobbole"])
>>>>>>> aeb36332caf00ea2afb1f7877770e48b9e05056c
