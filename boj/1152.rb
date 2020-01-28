def count_words(str)
  str.scan(/\w+/).size
end

if __FILE__ == $0
  puts count_words(gets)
end
