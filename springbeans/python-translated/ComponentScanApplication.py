from ApplicationContext import ApplicationContext


class ComponentScanApplication:
    @staticmethod
    def main():
        ctx = ApplicationContext()
        bean = ctx.get_bean("componentScanBean")
        bean.say_hello()