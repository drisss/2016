#!/usr/bin/env lua

local utils = require "toolbox"

local time_shift = tonumber(arg[1]) or 5
local annotation_fd = io.open(arg[2])
if not annotation_fd then
  error(arg[2])
end

local tweets = {}
do
  for tweet in io.stdin:lines() do
    local time = tweet:match("^[^\t]+\t([^\t]+)\t")
    local h, m, s = time:match("^(%d%d):(%d%d):(%d%d)$")
    time = (h * 60 + m) * 60 + s
    assert(time)
    table.insert(tweets, { text = tweet, time = time })
  end
end

annotation_fd:read()

local dir = arg[2]:sub(1, -5).."_per_event"

for line in annotation_fd:lines() do
  if line:match("%d") then
    local time, event, parameter = line:match("^([^\t]*)\t([^\t]*)\t([^\t]*)")
    if not time then
      time, event = line:match("^(%S*)\t(%S*)")
    end
    local h, m, s = time:match("(%d%d):(%d%d):(%d%d)")
    time = (h * 60 + m) * 60 + s
    local parameters = {}
    for p in (parameter or ""):gmatch("(%S+)") do
      if p ~= ";" then
        table.insert(parameters, p)
      end
    end
    assert(time)
    assert(event)

    local output_fd = io.open(dir.."/"..event.."_"..time..".txt", "w")
    output_fd:write(line.."\n")
    for _, tweet in ipairs(tweets) do
      if tweet.time > time + (time_shift * 60) then
        output_fd:write(tweet.text.."\n")
      end
    end
    output_fd:close()
  end
end
