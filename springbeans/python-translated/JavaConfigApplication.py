from ApplicationContext import ApplicationContext


class JavaConfigApplication:
    @staticmethod
    def main():
        ctx = ApplicationContext()
        bean = ctx.get_bean("javaConfigBean")
        bean.say_hello()