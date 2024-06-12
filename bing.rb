require 'time'

# 사용자로부터 지정한 날짜와 시간을 입력받습니다.
print "지정한 날짜와 시간을 입력하세요 (예: 2024-06-15 14:30): "
specified_datetime_str = gets.chomp

# 입력받은 문자열을 시간 객체로 변환합니다.
begin
  specified_datetime = Time.parse(specified_datetime_str)
rescue ArgumentError
  puts "잘못된 형식입니다. 날짜와 시간을 'YYYY-MM-DD HH:MM' 형식으로 입력해주세요."
  exit
end

# 현재 시간을 가져옵니다.
current_datetime = Time.now

# 두 시간 사이의 차이를 계산합니다.
time_difference = current_datetime - specified_datetime

# 결과 출력
puts "현재 시간과 #{specified_datetime_str} 사이의 시간 차이는 #{time_difference.abs} 초입니다."
puts "현재 시간과 #{specified_datetime_str} 사이의 시간 차이는 #{time_difference.abs / 60} 분입니다."
puts "현재 시간과 #{specified_datetime_str} 사이의 시간 차이는 #{time_difference.abs / 3600} 시간입니다."