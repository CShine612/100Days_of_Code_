def decorator(function):
    def wrapper():
        function()
        function()

    return wrapper


@decorator
def hello():
    print("Hello!")


hello()

# Create the logging_decorator() function 👇

def logging_decorator(function):
  def wrapper(*args, **kwargs):
    function_name = function.__name__
    function_inputs = []
    for item in args:
      function_inputs.append(item)
    for key, value in kwargs.items():
      function_inputs.append(value)
    function_output = function(*args, **kwargs)
    return {"name": function_name,
            "inputs": function_inputs,
            "output": function_output}
  return wrapper

# Use the decorator 👇

@logging_decorator
def multiply(x, y):
  return x*y

print(multiply(3, 5))

