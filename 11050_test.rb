require_relative './11050'
require 'test/unit'

class TestCheckedAttribute < Test::Unit::TestCase
  def test_zero
    assert_equal 1, binomial(3, 0)
  end

  def test_1
    assert_equal 10, binomial(5, 2)
  end

  def test_n
    assert_equal 1, binomial(5, 5)
  end
end
