#!/usr/bin/env ruby

# This script is from http://stackoverflow.com/a/22131019

File.open("module2_reading.md", 'r') do |f|
  f.each_line do |line|
    forbidden_words = ['Table of contents', 'define', 'pragma']
    next if !line.start_with?("#") || forbidden_words.any? { |w| line =~ /#{w}/ }

    title = line.gsub("#", "").strip
    href = title.gsub(" ", "-").downcase
    puts "  " * (line.count("#")-1) + "* [#{title}](\##{href})"
  end
end