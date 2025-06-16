/*
Copyright (C) 2025 Simon D. Levy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, in version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
*/

void serialEvent1()
{
    if (Serial1.available()) {       
        Serial.write(Serial1.read()); 
    }
}

void setup() 
{
    Serial.begin(115200);
    Serial1.begin(115200);
}

void loop() 
{
    static uint8_t k;

    Serial1.write(97+k);
    k = (k + 1) % 26;
}
