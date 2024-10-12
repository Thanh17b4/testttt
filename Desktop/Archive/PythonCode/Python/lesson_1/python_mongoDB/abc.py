from collections.abc import Mapping

from python_mongoDB.general_func.model import myfunc

if __name__ == '__main__':
   x = myfunc().get_collection("customers").estimated_document_count()
   print(x)