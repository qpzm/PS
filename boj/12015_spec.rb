require_relative '12015'

describe 'lis_len' do
  it '' do
    arr = [10, 20, 10, 30, 20, 50]
    expect(lis_len(arr, arr.size)).to eq(4)
  end

  it '' do
    arr = [10, 20, 10, 30, 20, 50, 40, 30]
    expect(lis_len(arr, arr.size)).to eq(4)
  end
end
