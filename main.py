from ubidots import ApiClient

api = ApiClient(token='BBFF-uiHDZ3oCZ7DAUMcuvpiFawSga4keUW')
my_variable = api.get_variable('62672f2dc2c55c000c247107')
print("encendiendo el foco...")


new_value = my_variable.save_value({'value': 1})