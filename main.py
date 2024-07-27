import clickhouse_connect


client = clickhouse_connect.get_client(host="localhost", username="", password="")
query = """
  select
    if(number % 15 = 0, 'FizzBuzz',
    if(number % 5 = 0, 'Buzz',
    if(number % 3 = 0, 'Fizz',
    toString(number))))
    as FizzBuzz
  from system.numbers
  where number >= 1
  limit 100
  """

print(client.command(query))
