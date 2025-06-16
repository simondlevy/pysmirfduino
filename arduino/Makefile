# Copyright (C) 2025 Simon D. Levy
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, in version 3.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

SKETCH = arduino

BOARD = teensy:avr:teensy40

PORT = /dev/ttyACM0

build: $(SKETCH).ino
	arduino-cli compile --fqbn $(BOARD) $(SKETCH).ino

flash:
	arduino-cli upload -p $(PORT) --fqbn $(BOARD) .

clean:
	rm -rf obj

edit:
	vim $(SKETCH).ino

listen:
	miniterm.py $(PORT) 115200

