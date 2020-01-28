def fizzbuzz(a, b, num)
  if (num % a).zero?
    return 'FizzBuzz' if (num % b).zero?
    'Fizz'
  elsif (num % b).zero?
    'Buzz'
  else
    num.to_s
  end
end

def fizzbuzz_string(a, b, n)
  (1..n).map { |m| fizzbuzz(a, b, m) }
        .reduce { |sum, elem| sum + "\n" + elem }
end

if __FILE__ == $0
  puts fizzbuzz_string(*gets.split.map(&:to_i))
end
