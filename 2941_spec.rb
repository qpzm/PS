require_relative '2941'

describe 'Croatian.count' do
  it '' do
    expect(Croatian.count('ljes=njak')).to eq(6)
  end

  it '' do
    expect(Croatian.count('ddz=z=')).to eq(3)
  end

  it '' do
    expect(Croatian.count('nljj')).to eq(3)
  end
end
