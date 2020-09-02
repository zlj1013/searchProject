
from search.models import Text
## 存储到数据库功能的文件
def addText(text):
    text1 = Text(text=text)
    text1.save()