__author__ = 'felixgao'
#Code stolen from Bruce Eckel's pycon presentation
class ResultError(Exception): pass

class Result(object):
    def __init__(self, result, failed=False):
        self.__result = result
        self.failed = failed
    @property
    def result(self):
        if not self.failed:
            return self.__result
        else:
            raise ResultError(self.failed)

    def __str__(self):
        return "Type: Result\nValue:%s"%self.__result.__str__()

class Fail(Result):
    def __init__(self, reason=True, exception=ResultError(True)):
        Result.__init__(self, None, reason)
        self.exception = exception
    def __str__(self):
        return "Type: Fail\nReason:%s\nException:%s"%(self.reason, self.exception)