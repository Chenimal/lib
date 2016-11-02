# encoding: utf-8
import os
import sys
import time

# notify function


def notify(title='', message='', url='', group='', execute=''):
    t = '-title "%s"' % (title)
    m = '-message "%s"' % (message)
    u = '-open "%s"' % (url)
    g = '-group "%s"' % (group)
    e = '-execute "%s"' % (execute)
    print ' '.join([m, t, u, g, e])
    os.system(
        '/usr/local/bin/terminal-notifier %s' % (' '.join([m, t, u, g, e])))

# if unicode char is chinese


def isChinese(uchar):
    return True if uchar >= u'\u4e00' and uchar <= u'\u9fa5' else False

# log


def logger(name=__name__, msg='', print_out=True):
    if print_out:
        print(msg)
    path = sys.path[0] + '/log/' + name + '.log'
    f = open(path, 'a')
    f.write(msg + '\n')
    f.close()

# testA => test_a


def camelToUnderline(string):
    result = ''
    for char in string:
        result += char if char.islower() else '_' + char.lower()
    return result

# test_a => testA


def underlineToCamel(string):
    result = ''
    for substr in string.split('_'):
        result += substr if result == '' else substr.capitalize()
    return result

# in-class decorator
# it calculate total time cost by the function().
# need to specify a class attribute(accum)


def timerAccumulate(accum):
    def timer(f):
        def _func(*args, **kw):
            s = time.time()
            r = f(*args, **kw)
            # arg[0] is self (instance)
            t = getattr(args[0], accum) + time.time() - s
            setattr(args[0], accum, t)
            return r
        return _func
    return timer
