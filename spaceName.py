def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
inner_function() # Выдает ошибку так как не будит известна в глобальной области видимости