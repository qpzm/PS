# frozen_string_literal: true

# O(nlogk) where k is the length of lis
INT_MAX = 1_000_001

def lis_len(arr, size)
  len_arr = [1] * size
  candidate = [0] + [INT_MAX] * size
  arr.each_with_index do |elem, i|
    # bsearch_index는 해당 block이 true를 return하는 가장 작은 인덱스를 반환
    # strictly increasing 이므로 같은 것이 있으면 그 오른쪽에 놓으면 안 됨
    j = candidate.bsearch_index { |x| elem <= x }
    candidate[j] = elem if candidate[j] > elem
    len_arr[i] = j
  end
  len_arr.max
end

if __FILE__ == $0
  n = gets.to_i
  arr = gets.split.map(&:to_i)
  puts lis_len(arr, n)
end
