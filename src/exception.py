import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    message = "Error found in Python script name [{0}], line no [{1}], error [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__()
        self.error = error
        self.error_detail = error_detail
        self.error_details = error_message_detail(self.error, self.error_detail)

    def __str__(self):
        return self.error_details

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)