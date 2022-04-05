class BuildResponse:

    def __init__(self, data, meta=None, http_status_code=None, page_info=None):
        self._data = data
        self._meta = meta
        self._http_status_code = http_status_code
        self._page_info = page_info

    @property
    def data(self):
        return self._data

    @property
    def meta(self):
        if self._page_info:
            self._meta['page_info'] = self._page_info
        return self._meta

    @property
    def status(self):
        return self._http_status_code

    @property
    def page_info(self):
        return self._page_info

    def __dict__(self):
        result = dict()
        result['data'] = self._data
        result['meta'] = self._meta
        result['success'] = True
        result['status'] = self._http_status_code
        return result
