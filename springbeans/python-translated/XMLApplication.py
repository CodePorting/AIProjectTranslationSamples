from ApplicationContext import ApplicationContext


class XmlApplication:
    @staticmethod
    def main():
        ctx = ApplicationContext()
        bean = ctx.get_bean("xmlBean")
        bean.say_hello()