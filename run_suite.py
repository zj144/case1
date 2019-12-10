'''

'''

# 导包


# 定义测试套件
import unittest

from HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('./scripts')

with open('./report/report.html','wb') as f:
    HTMLTestRunner(stream=f).run(suite)

