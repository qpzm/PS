# 시간 제한이 10초
# 아래 코드가 시간초과라서 cpp로 재작성하니 4100ms로 통과

def safe?(arr, row, col)
  arr[0...col].each.with_index do |row2, col2|
    return false if row == row2 || (row - row2).abs == col - col2
  end
  true
end

def n_queen(size)
  $sum = 0
  arr = [-1] * size
  n_queen_iter(arr, 0)
  $sum
end

def n_queen_iter(arr, col)
  (0...arr.size).each do |row|
    if safe?(arr, row, col)
      if col == arr.size - 1
        $sum += 1
      else
        arr[col] = row
        n_queen_iter(arr, col + 1)
        #arr[col] = -1
      end
    end
  end
end

if __FILE__ == $PROGRAM_NAME
  size = gets.to_i
  puts n_queen(size)
end
