import is_empty as lib_is_empty
from typing import Any, Self

class Questionable:
	def __init__(self,most:Any,least:Any) -> Self:
		self._value = self.__setup__(most,least)
	def __setup__(self,most:Any,least:Any):
		answer = [lib_is_empty.not_empty(most),lib_is_empty.not_empty(least)]
		if not True in answer: return None # both false - empty
		if not False in answer: return most # both true - 2 values
		return [most,least][answer.index(True)]
	def value(self) -> Any:
		return self._value
	def __call__(self) -> Any:
		return self.value()
def qq(most:any,least:any):
	return Questionable(most,least)()