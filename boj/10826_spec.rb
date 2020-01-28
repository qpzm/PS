require_relative '10826'

describe MyNum do
  it '+' do
    expect(MyNum.new(2, 3) + MyNum.new(3, 4)).to eq(MyNum.new(5, 7))
  end

  it '*' do
    expect(MyNum.new(2, 3) * MyNum.new(3, 4)).to eq(MyNum.new(66, 17))
  end

  it '**' do
    expect(MyNum.new(3, 1) ** 2).to eq(MyNum.new(14, 6))
  end
end

describe 'fibonacci' do
  it '0' do
    expect(fibo(0)).to eq(0)
  end

  it '1..2' do
    expect(fibo(1)).to eq(1)
    expect(fibo(2)).to eq(1)
  end

  it '3' do
    expect(fibo(3)).to eq(2)
  end

  it '10' do
    expect(fibo(10)).to eq(55)
  end

  it '1000' do
    expect(fibo(10000)).to eq(55)
  end
end
