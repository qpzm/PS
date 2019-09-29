require_relative '9663_n_queen'
require 'rspec'

describe 'n_queen in size of' do
  it 'trivial numbers' do
    expect(n_queen(1)).to eq(1)
    expect(n_queen(2)).to eq(0)
    expect(n_queen(3)).to eq(0)
    expect(n_queen(4)).to eq(2)
    expect(n_queen(5)).to eq(10)
    expect(n_queen(6)).to eq(4)
    expect(n_queen(8)).to eq(92)
  end

  it '10' do
    expect(n_queen(10)).to eq(724)
  end

  xit '11' do
    expect(n_queen(11)).to eq(2680)
  end

  xit '12' do
    expect(n_queen(12)).to eq(14200)
  end

  xit '13' do
    expect(n_queen(13)).to eq(73_712)
  end

  xit '14' do
    expect(n_queen(14)).to eq(365_596)
  end
end
