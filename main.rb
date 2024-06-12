current_time = Time.now
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
puts formatted_time

formatted_times = date_formats.map { |format| Time.now.strftime(format) }

# 저장된 형식들을 출력
formatted_times.each do |formatted_time|
  puts formatted_time


#nowtime = [_nowtime.slice(5, 6)]
#puts nowtime
# _wanttime = "2024-06-14 09:00:00 +0900"
class Time
  attr_accessor :month, :date, :hour, :minute, :second

  def initialize(month, date, hour, minute, second)
    @month = month
    @date = date
    @hour = hour
    @minute = minute
    @second = second
  end


end

wantTime = Time.new(6, 14, 9, 0, 0)

#puts nowtime

