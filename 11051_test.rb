require_relative './11051'
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

  def test_big
    assert_equal 1000, binomial(1000, 999)
  end
end
