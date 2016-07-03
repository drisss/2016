#!/usr/bin/env lua

local JSON  = require "JSON"
local utils = require "toolbox"
local date  = require "date"

local GMT = 2

local counter = 1
for line in io.stdin:lines() do
--  io.stderr:write(counter.."\n")
  counter = counter + 1
  local plain = JSON:decode(line)
  if plain.text then
    local processed_text = plain.text:gsub("\n", "  ")
    assert(not processed_text:match("\t"))
    assert(not processed_text:match("\n"))
    -- id time text retweet_count lang
    local processed_time = date.gmtime(tonumber(plain.timestamp_ms:sub(1,-4))+(GMT * 3600))
    print(string.format("%s\t%s\t%s\t%s\t%s", plain.id_str, processed_time, processed_text, plain.retweet_count, plain.lang))
  end
end
