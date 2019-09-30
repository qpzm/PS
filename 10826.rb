class MyNum
  attr_accessor :n, :m
  # n + m * sqrt(5)
  def initialize(n, m)
    @n = n
    @m = m
  end

  def +(num)
    MyNum.new(n + num.n, m + num.m)
  end

  def *(num)
    MyNum.new(n * num.n + 5 * m * num.m, m * num.n + n * num.m)
  end

  def ==(num)
    n == num.n && m == num.m
  end

  def **(exp)
    raise StandardError if exp < 0
    exp == 0 ? MyNum.new(1, 0) : self * (self ** (exp - 1))
  end
end

def fibo(n)
  case n
  when 0
    0
  when 1..2
    1
  else
    m = n - 2
    (MyNum.new(3, 1) * (MyNum.new(1, 1) ** m) + MyNum.new(-3, 1) * (MyNum.new(1, -1) ** m)).m / (2 ** (m + 1))
  end
end

if __FILE__ == $0
  puts fibo(gets.to_i)
end
