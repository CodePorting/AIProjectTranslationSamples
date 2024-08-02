from ApplicationContext import ApplicationContext


class SpringBeansApplication:
    @staticmethod
    def main():
        ctx = ApplicationContext()

        hello_beans = [
            ctx.get_bean("componentScanBean"),
            ctx.get_bean("javaConfigBean"),
            ctx.get_bean("xmlBean")
        ]

        for hello_bean in hello_beans:
            hello_bean.say_hello()


if __name__ == '__main__':
    SpringBeansApplication.main()