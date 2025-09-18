import sys
# import src
# from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    # exc.infor() returns three information, out of which only the last one is important
    # exc_tb = which tells that in which file, on which line, where the error occurred.

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

# For just checking if the code is working properly or not
# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e, sys)