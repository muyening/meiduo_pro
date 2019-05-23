from django.shortcuts import render

# Create your views here.
from meiduo_mall.settings.dev import logger

# 创建日志记录器
# logger = logging.getLogger('django')
# 输出日志
logger.debug('测试logging模块debug')
logger.info('测试logging模块info')
logger.error('测试logging模块error')