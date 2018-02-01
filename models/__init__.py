from flask_sqlalchemy import SQLAlchemy
import time


db = SQLAlchemy()


def timestamp():
    return int(time.time())


class ModelMixin(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        # self.deleted = True
        # self.save()

"""
脚本的例子

apt-get install python3 python3-dev ....
pip3 install flask flask-script flask-migrate ....

import os

os.system('pip3 install flask')

你以后看到的 shell 脚本是不会有函数的
shell 一个失败的功能
要实现什么功能，去查 python 库，然后去实现
shell 一个错误的发明，因为大量历史遗留问题
"""