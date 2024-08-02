from ComponentScanBean import ComponentScanBean
from JavaConfigBean import JavaConfigBean
from XMLBean import XmlBean


class ApplicationContext:
    def __init__(self):
        self.beans = {
            "componentScanBean": ComponentScanBean(),
            "javaConfigBean": JavaConfigBean(),
            "xmlBean": XmlBean()
        }

    def get_bean(self, name):
        return self.beans.get(name)