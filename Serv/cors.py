class CorsMiddleware(object):
    def process_response(self, req, res):
        res["Acces-Controll-Allow-Origin"] = "*"
        return res