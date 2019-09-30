require_relative '1992'

def with_stdin
  stdin = $stdin             # remember $stdin
  $stdin, write = IO.pipe    # create pipe assigning its "read end" to $stdin
  yield write                # pass pipe's "write end" to block
ensure
  write.close                # close pipe
  $stdin = stdin             # restore $stdin
end

describe 'quadtree' do
  # parsing from stdin does not work
  xit 'parses input' do
    input = <<~EOF
      2
      12
      34
    EOF

    with_stdin do |user|
      user.puts input
      size, arr = parse
      expect(size).to eq(2)
      expect(arr).to eq([[1, 2], [3, 4]])
    end
  end

  it '' do
    input = <<~EOF.chomp!.split(/\s+/).map(&:chars)
      11110000
      11110000
      00011100
      00011100
      11110000
      11110000
      11110011
      11110011
    EOF

    answer = '((110(0101))(0010)1(0001))'
    expect(quadtree(8, input, 0, 0)).to eq(answer)
  end

  it '' do
    arr = [%w(0 1 0 1) * 16] * 64
    quadtree(64, arr, 0, 0)
  end

  it '' do
    arr = [['0'] * 64] * 64
    expect(quadtree(64, arr, 0, 0)).to eq('0')
  end

  it '' do
    arr = [['1'] * 64] * 64
    expect(quadtree(64, arr, 0, 0)).to eq('1')
  end
end
