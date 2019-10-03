require_relative '14003'

describe 'lis_len' do
  it '' do
    arr = [10, 20, 10, 30, 20, 50]
    len_arr = lis_len(arr, arr.size)
    expect(format_result(arr, len_arr)).to eq([4, "10 20 30 50"])
  end

  it '' do
    arr = [10, 20, 10, 30, 20, 50, 40, 30]
    len_arr = lis_len(arr, arr.size)
    expect(format_result(arr, len_arr)).to eq([4, "10 20 30 50"])
  end

  it '' do
    arr = [-10, 20, 10, -30, 20, 50, 40, 30]
    len_arr = lis_len(arr, arr.size)
    expect(len_arr.max).to eq(4)
    expect(format_result(arr, len_arr)).to eq([4, "-10 10 20 50"])
  end
end
