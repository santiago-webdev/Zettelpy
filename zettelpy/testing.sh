#!/usr/bin/env bash

zettelpy
sleep 5
zettelpy Test1.md
sleep 5
zettelpy Testing/Test2.md
sleep 5
zettelpy -i Test1.md  # The "Test1.md" should be ignored when parsed a -i
sleep 5
zettelpy -v Test853.md  # Should fail beacuse it doesn't exists
sleep 5
zettelpy Testing/Test2.md -v
