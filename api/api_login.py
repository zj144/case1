class ApiLogin:

    # 初始化获取url,session
    def __init__(self,session):
        self.session = session
        self.code_url = 'http://localhost/index.php?m=Home&c=User&a=verify'
        self.login_url = 'http://localhost/index.php?m=Home&c=User&a=do_login'
    # 获取验证码
    def api_verify_code(self):
        self.session.get(self.code_url)
    # 登录(post)
    def api_login(self,username,password,verify_code):
        data = {"username":username,'password':password,'verify_code':verify_code}
        self.session.post(self.login_url,data=data)