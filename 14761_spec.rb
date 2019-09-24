require_relative '14761'

describe 'FizzBuzz' do
  context '' do
    it '2 3 7' do
      expect(fizzbuzz_string(2, 3, 7)).to eq \
        <<~EOF.chomp
          1
          Fizz
          Buzz
          Fizz
          5
          FizzBuzz
          7
        EOF
    end

    it '2 4 7' do
      expect(fizzbuzz_string(2, 4, 7)).to eq \
        <<~EOF.chomp
          1
          Fizz
          3
          FizzBuzz
          5
          Fizz
          7
        EOF
    end

    it '3 5 7' do
      expect(fizzbuzz_string(3, 5, 7)).to eq \
        <<~EOF.chomp
          1
          2
          Fizz
          4
          Buzz
          Fizz
          7
        EOF
    end
  end
end
