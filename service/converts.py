class CheckParam:

    regex = '[0-9]{2}'

    def to_python(self, val):
        return int(val)

    def to_url(self, val):
        return '%02d' % val