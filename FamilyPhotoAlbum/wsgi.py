import os
from django.core.wsgi import get_wsgi_application

# 设置Django的配置文件环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FamilyPhotoAlbum.settings')

# 明确定义 application 变量
application = get_wsgi_application()